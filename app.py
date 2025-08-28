import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="రసభారత్", layout="wide")

# 🌸 Gradient background
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: white;'>✨ తెలంగాణ ప్రసిద్ధ వంటకాలు ✨</h1>", unsafe_allow_html=True)

# 📂 Images folder
img_folder = "images"
images = [img for img in os.listdir(img_folder) if img.endswith(("png", "jpg", "jpeg"))]

# Show recipes in grid (3 per row)
st.subheader("🥘 ప్రసిద్ధ వంటకాలు")
cols = st.columns(3)
for i, img in enumerate(images):
    with cols[i % 3]:
        st.image(os.path.join(img_folder, img), caption=img.split(".")[0], use_container_width=True)

# 📋 Community Recipes Section
st.subheader("👩‍🍳 కమ్యూనిటీ వంటకాలు")
recipes_file = "recipes.csv"

# Load existing recipes
if os.path.exists(recipes_file):
    df = pd.read_csv(recipes_file)
else:
    df = pd.DataFrame(columns=["Name", "Recipe", "Language", "Image"])

# Recipe submission form
with st.form("recipe_form"):
    name = st.text_input("మీ పేరు")
    recipe = st.text_area("మీ వంటకం")
    lang = st.selectbox("భాష", ["తెలుగు", "English", "हिन्दी", "தமிழ்"])
    img_url = st.text_input("వంటకం చిత్రం URL (ఐచ్చికం)")
    submitted = st.form_submit_button("వంటకం పంపించండి")

    if submitted and name and recipe:
        new_entry = pd.DataFrame([[name, recipe, lang, img_url]], columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(recipes_file, index=False)
        st.success("✅ మీ వంటకం విజయవంతంగా జోడించబడింది!")

# Show submitted recipes
if not df.empty:
    for i, row in df.iterrows():
        st.write(f"🍴 **{row['Recipe']}** (✍ {row['Name']} - {row['Language']})")
        if row["Image"]:
            st.image(row["Image"], width=250)
else:
    st.info("ఇప్పటివరకు ఎవరూ వంటకం జోడించలేదు. మీరు మొదటివారు అవ్వండి! 🎉")
