import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="RasaBharat", page_icon="🍲", layout="wide")

st.title("🍲 RasaBharat – భారతీయ వంటకాల వారసత్వం")

# Recipe submission form
with st.form("recipe_form"):
    name = st.text_input("వంటకం పేరు (Dish Name)")
    ingredients = st.text_area("పదార్థాలు (Ingredients)")
    steps = st.text_area("తయారీ విధానం (Preparation Steps)")
    language = st.selectbox("భాష (Language)", ["Telugu", "Hindi", "English", "Other"])
    contributor = st.text_input("మీ పేరు (Your Name)")
    submitted = st.form_submit_button("సమర్పించండి (Submit Recipe)")

if submitted:
    df = pd.DataFrame([[name, ingredients, steps, language, contributor]], 
                      columns=["Name", "Ingredients", "Steps", "Language", "Contributor"])
    if os.path.exists("recipes.csv"):
        df.to_csv("recipes.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("recipes.csv", index=False)
    st.success("✅ వంటకం విజయవంతంగా జోడించబడింది!")

# Browse recipes
if os.path.exists("recipes.csv"):
    st.subheader("📖 Recipes Collection")
    recipes = pd.read_csv("recipes.csv")
    for _, row in recipes.iterrows():
        with st.container():
            st.markdown(f"### {row['Name']} ({row['Language']})")
            st.markdown(f"**Ingredients:** {row['Ingredients']}")
            st.markdown(f"**Steps:** {row['Steps']}")
            st.caption(f"👤 Contributed by {row['Contributor']}")
            st.divider()
