import streamlit as st

# Page Config
st.set_page_config(page_title="RasaBharath - Telangana Food", layout="wide")

# --- Custom CSS for Beautiful UI ---
st.markdown("""
    <style>
    .title {
        font-size: 40px; 
        font-weight: bold; 
        color: #a83232;
        text-align: center;
    }
    .subtitle {
        font-size: 24px; 
        color: #444; 
        margin-top: 20px;
    }
    .card {
        background-color: #fff3e6;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🍲 రసభారత్ - తెలంగాణ వంటకాలు 🍲</div>', unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="card">
    <h3>🌟 తెలంగాణ ఆహార సంస్కృతి 🌟</h3>
    తెలంగాణ వంటకాలు మసాలా రుచులతో ప్రసిద్ధి చెందాయి.  
    ఇక్కడి వంటల్లో **మిర్చి, పులుపు, రాగులు, జొన్నలు** ముఖ్యపాత్ర పోషిస్తాయి.  
</div>
""", unsafe_allow_html=True)

# Popular foods
st.markdown('<div class="subtitle">🍛 ప్రసిద్ధ వంటకాలు</div>', unsafe_allow_html=True)

foods = {
    "జొన్న రొట్టె": {
        "desc": "జొన్న పిండి తో చేసే రొట్టె – గోంగూర పచ్చడి తో తింటారు.",
        "img": "images/jonna_roti.jpg"   # keep this image in images/ folder
    },
    "రాగి జావ": {
        "desc": "ఆరోగ్యకరమైన పానీయం, వేసవిలో శరీరాన్ని చల్లగా ఉంచుతుంది.",
        "img": "images/ragi_java.jpg"
    },
    "సరపప్పు పప్పు": {
        "desc": "సరపప్పుతో చేసే పప్పు – రోటీ లేదా అన్నంతో రుచిగా ఉంటుంది.",
        "img": "images/sarapappu.jpg"
    },
    "బజ్జీలు": {
        "desc": "ఉల్లిపాయ, మిరపకాయ లేదా అరటికాయతో వేసే బజ్జీలు.",
        "img": "images/bajji.jpg"
    },
    "సాకినేలు": {
        "desc": "పండుగల సమయంలో చేసే ప్రత్యేక వంటకం.",
        "img": "images/sakinalu.jpg"
    }
}

for food, details in foods.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image(details["img"], caption=food, width=200)
        except:
            st.warning(f"⚠️ చిత్రం {food} కి కనబడలేదు. దయచేసి 'images/' ఫోల్డర్ చెక్ చేయండి.")
    with col2:
        st.markdown(f"<div class='card'><h4>🍴 {food}</h4><p>{details['desc']}</p></div>", unsafe_allow_html=True)

# Add Recipe Section
st.markdown('<div class="subtitle">👩‍🍳 మీ వంటకం జోడించండి</div>', unsafe_allow_html=True)

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

if st.session_state["recipes"]:
    for r_name, r_desc in st.session_state["recipes"]:
        st.markdown(f"<div class='card'><b>🍴 {r_name}</b><br>{r_desc}</div>", unsafe_allow_html=True)

# Extra Info
st.markdown('<div class="subtitle">🎉 ఆహార సంస్కృతి & పండుగలు</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
- **బతుకమ్మ** సమయంలో ప్రత్యేక వంటకాలు చేస్తారు.  
- **సంక్రాంతి** సందర్భంగా అరిసెలు, సాకినేలు చేస్తారు.  
- గోంగూర పచ్చడి, మిరపకాయ పచ్చడి రోజువారీ ఆహారంలో భాగం.  
- **మజ్జిగ, రాగి జావ** వేసవిలో చల్లగా ఉంచే పానీయాలు.  
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2025 రసభారత్ | తెలంగాణ ఆహార సంస్కృతి")
