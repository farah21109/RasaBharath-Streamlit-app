import streamlit as st
import pandas as pd
import os

# పేజీ సెట్టింగ్స్
st.set_page_config(page_title="రసభారత్ – తెలంగాణ వంటకాలు", layout="wide")

# కస్టమ్ CSS (గ్రేడియెంట్ బ్యాక్‌గ్రౌండ్)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    color: white;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# శీర్షిక
st.title("🌾 రసభారత్ – తెలంగాణ ఆహార సంస్కృతి")

# --- మీ ఫోల్డర్‌లో ఉన్న ప్రసిద్ధ వంటకాలు ---
famous_recipes = [
    {
        "name": "గరెల పులుసు",
        "desc": "చేపట్టిన గరెలతో చేసిన రుచికరమైన పులుసు వంటకం.",
        "img": "images/Garela-Pulusu.jpg"
    },
    {
        "name": "కుడుములు",
        "desc": "వినాయక చవితి సందర్భంగా తయారు చేసే ప్రసిద్ధ నైవేద్యం.",
        "img": "images/Kudumulu.jpg"
    },
    {
        "name": "మెంతి ఆకులు పెసర పప్పు కూర",
        "desc": "ఆరోగ్యకరమైన మరియు రుచికరమైన ఆకుకూర వంటకం.",
        "img": "images/Menthi-Aaku-Pesaru-Pappu-Koora.jpg"
    }
]

# ప్రసిద్ధ వంటకాలు విభాగం
st.subheader("✨ తెలంగాణ ప్రసిద్ధ వంటకాలు")
cols = st.columns(len(famous_recipes))
for col, recipe in zip(cols, famous_recipes):
    with col:
        if os.path.exists(recipe["img"]):
            st.image(recipe["img"], caption=recipe["name"], use_column_width=True)
        else:
            st.warning(f"ఫైల్ కనిపించలేదు: {recipe['img']}")
        st.markdown(f"**{recipe['name']}**")
        st.caption(recipe["desc"])

# --- కమ్యూనిటీ వంటకాలు ---
st.subheader("👩‍🍳 కమ్యూనిటీ వంటకాలు")
recipes_file = "recipes.csv"

# ఉన్న డేటా లోడ్ చేయడం
if os.path.exists(recipes_file):
    df = pd.read_csv(recipes_file)
else:
    df = pd.DataFrame(columns=["పేరు", "వంటకం", "భాష", "చిత్రం"])

# వంటకం జోడించడానికి ఫారం
with st.form("recipe_form"):
    name = st.text_input("మీ పేరు")
    recipe = st.text_area("మీ వంటకం వివరాలు రాయండి")
    lang = st.selectbox("భాష", ["తెలుగు", "English", "हिन्दी", "தமிழ்"])
    img_url = st.text_input("వంటకం చిత్రం లింక్ (ఐచ్చికం)")
    submitted = st.form_submit_button("వంటకం జోడించండి")

    if submitted and name and recipe:
        new_entry = pd.DataFrame([[name, recipe, lang, img_url]], columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(recipes_file, index=False)
        st.success("✅ మీ వంటకం విజయవంతంగా జోడించబడింది!")

# వంటకాలను చూపించడం
if not df.empty:
    for i, row in df.iterrows():
        st.write(f"🍴 **{row['వంటకం']}** (✍ {row['పేరు']} | 🌐 {row['భాష']})")
        if row["చిత్రం"]:
            st.image(row["చిత్రం"], width=250)
else:
    st.info("మొదట మీ వంటకం జోడించండి! 🎉")
