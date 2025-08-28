import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="RasaBharat", layout="wide")

# Famous Telangana recipes
famous_recipes = [
    {
        "name_en": "Hyderabadi Biryani",
        "name_te": "హైదరాబాది బిర్యాని",
        "desc": "The world-famous biryani with rich spices and basmati rice.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/6/62/Hyderabadi_Biryani.jpg"
    },
    {
        "name_en": "Sarva Pindi",
        "name_te": "సర్వ పిండి",
        "desc": "A traditional savory pancake made with rice flour and spices.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Sarva_Pindi.jpg"
    },
    {
        "name_en": "Sakinalu",
        "name_te": "సాకినాలు",
        "desc": "A crunchy snack prepared during Sankranti festival.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Sakinalu.jpg"
    }
]

st.title("🌾 RasaBharat – Telangana Food Culture")

# Showcase Telangana recipes
st.subheader("✨ Famous Telangana Recipes")
cols = st.columns(len(famous_recipes))
for col, recipe in zip(cols, famous_recipes):
    with col:
        st.image(recipe["img"], caption=recipe["name_en"], use_column_width=True)
        st.markdown(f"**{recipe['name_en']} ({recipe['name_te']})**")
        st.caption(recipe["desc"])

# Community Recipes Section
st.subheader("👩‍🍳 Community Recipes")
recipes_file = "recipes.csv"

# Load existing recipes
if os.path.exists(recipes_file):
    df = pd.read_csv(recipes_file)
else:
    df = pd.DataFrame(columns=["Name", "Recipe", "Language", "Image"])

# Recipe submission form
with st.form("recipe_form"):
    name = st.text_input("Your Name")
    recipe = st.text_area("Enter your recipe")
    lang = st.selectbox("Language", ["English", "తెలుగు", "हिन्दी", "தமிழ்"])
    img_url = st.text_input("Recipe Image URL (optional)")
    submitted = st.form_submit_button("Submit Recipe")

    if submitted and name and recipe:
        new_entry = pd.DataFrame([[name, recipe, lang, img_url]], columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(recipes_file, index=False)
        st.success("✅ Recipe submitted successfully!")

# Show submitted recipes with images
if not df.empty:
    for i, row in df.iterrows():
        st.write(f"🍴 **{row['Recipe']}** (by {row['Name']} in {row['Language']})")
        if row["Image"]:
            st.image(row["Image"], width=250)
else:
    st.info("No community recipes yet. Be the first to add one! 🎉")
