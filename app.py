import streamlit as st

# App Config
st.set_page_config(page_title="RasaBharath - Telangana Food", layout="centered")

st.title("🍲 రసభారత్ - తెలంగాణ వంటకాలు 🍲")

# --- Intro Section ---
st.markdown("""
### 🌟 తెలంగాణ ఆహార సంస్కృతి 🌟
తెలంగాణ వంటకాలు మసాలా రుచులతో ప్రసిద్ధి చెందాయి.  
ఇక్కడి వంటల్లో **మిర్చి, పులుపు, రాగులు, జొన్నలు** ముఖ్యపాత్ర పోషిస్తాయి.  
""")

# --- Popular Foods with Images ---
st.header("🍛 ప్రసిద్ధ వంటకాలు")

foods = {
    "జొన్న రొట్టె": {
        "desc": "జొన్న పిండి తో చేసే రొట్టె – గోంగూర పచ్చడి తో తింటారు.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Jowar_Roti.jpg/320px-Jowar_Roti.jpg"
    },
    "రాగి జావ": {
        "desc": "ఆరోగ్యకరమైన పానీయం, వేసవిలో శరీరాన్ని చల్లగా ఉంచుతుంది.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Ragi_Porridge.jpg/320px-Ragi_Porridge.jpg"
    },
    "సరపప్పు పప్పు": {
        "desc": "సరపప్పుతో చేసే పప్పు – రోటీ లేదా అన్నంతో రుచిగా ఉంటుంది.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Dal_Tadka.jpg/320px-Dal_Tadka.jpg"
    },
    "బజ్జీలు": {
        "desc": "ఉల్లిపాయ, మిరపకాయ లేదా అరటికాయతో వేసే బజ్జీలు.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mirchi_Bajji.jpg/320px-Mirchi_Bajji.jpg"
    },
    "సాకినేలు": {
        "desc": "పండుగల సమయంలో చేసే ప్రత్యేక వంటకం.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Sakinalu.jpg/320px-Sakinalu.jpg"
    }
}

for food, details in foods.items():
    st.subheader(f"🍴 {food}")
    st.image(details["img"], caption=food, width=300)
    st.write(details["desc"])

# --- Add Your Recipe ---
st.header("👩‍🍳 మీ వంటకం జోడించండి")

if "recipes" not in st.session_state:
    st.session_state["recipes"] = []

new_recipe = st.text_input("వంటకం పేరు:")
new_desc = st.text_area("వంటకం వివరణ:")

if st.button("వంటకం జోడించండి"):
    if new_recipe and new_desc:
        st.session_state["recipes"].append((new_recipe, new_desc))
        st.success(f"✅ {new_recipe} జోడించబడింది!")
    else:
        st.error("దయచేసి వంటకం పేరు మరియు వివరణ ఇవ్వండి.")

# Show added recipes
if st.session_state["recipes"]:
    st.subheader("📖 వినియోగదారుల వంటకాలు")
    for r_name, r_desc in st.session_state["recipes"]:
        st.markdown(f"**🍴 {r_name}** - {r_desc}")

# --- Extra Info ---
st.header("🎉 ఆహార సంస్కృతి & పండుగలు")
st.markdown("""
- **బతుకమ్మ** సమయంలో ప్రత్యేక వంటకాలు చేస్తారు.  
- **సంక్రాంతి** సందర్భంగా అరిసెలు, సాకినేలు చేస్తారు.  
- గోంగూర పచ్చడి, మిరపకాయ పచ్చడి రోజువారీ ఆహారంలో భాగం.  
- **మజ్జిగ, రాగి జావ** వేసవిలో చల్లగా ఉంచే పానీయాలు.  
""")

# Footer
st.markdown("---")
st.caption("© 2025 రసభారత్ | తెలంగాణ ఆహార సంస్కృతి")
