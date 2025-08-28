import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="RasaBharat", layout="wide")

st.title("🌾 RasaBharat – Telangana Food Culture")

# --- Load images from your repo folder ---
famous_recipes = [
    {
        "name_en": "Garela Pulusu",
        "name_te": "గరెల పులుసు",
        "desc": "చేపట్టిన గరెలతో చేసిన రుచికరమైన పులుసు వంటకం.",
        "img": "images/Garela-Pulusu.jpg"
    },
    {
        "name_en": "Kudumulu",
        "name_te": "కుడుములు",
        "desc": "వినాయక చవితి సందర్భంగా తయారు చేసే ప్రసిద్ధ నైవేద్యం.",
        "img": "images/Kudumulu.jpg"
    },
    {
        "name_en": "Menthi Aaku Pesaru Pappu Koora",
        "name_te": "మెంతి ఆకులు పెసర పప్పు కూర",
        "desc": "ఆరోగ్యకరమైన మరియు రుచికరమైన ఆకుకూర వంటకం.",
        "img": "images/Menthi-Aaku-Pesaru-Pappu-Koora.jpg"
    }
]

# --- Famous Recipes Section ---
st.subheader("✨ Telangana Traditional Recipes")
cols = st.columns(len(famous_recipes))
for col, recipe in zip(cols, famous_recipes):
    with col:
        if os.path.exists(recipe["img"]):
            st.image(recipe["img"], caption=recipe["name_en"], use_column_width=True)
        else:
            st.warning(f"Image not found: {recipe['img']}")
        st.markdown(f"**{recipe['name_en']} ({recipe['name_te']})**")
        st.caption(recipe["desc"])

# --- Community Recipes Section ---
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
