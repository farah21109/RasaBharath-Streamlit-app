
# REPORT.md – Food App: RasaBharat

## 1.1 Team Information

- **Team Name**: RasaBuilders
- **Project Title**: RasaBharat – Preserving Indian Recipes
- **Team Members**:  
  - Shivani Medamoni – Frontend & Testing  
  - Member 2 – Backend & Deployment  
  - Member 3 – AI Integration  
  - Member 4 – Corpus Strategy & Community Outreach  
  - Member 5 – Project Management & Documentation  
- **Organization**: Swecha  
- **Duration**: 4 Weeks  
- **Platform**: https://code.swecha.org/your-team/rasabharat

## 1.2 Application Overview

### Objective  
Our project aims to preserve and digitize traditional Indian recipes in native languages. Many unique family recipes are undocumented and risk being forgotten, especially in rural areas. This app provides a space for users to share their cooking knowledge in their local dialects while contributing to India's AI corpus.

### MVP Features (Built in 1 Week)
- Multilingual recipe submission form (Title, Ingredients, Steps)
- Optional audio/image upload (lightweight only)
- Offline-first functionality with local caching
- AI-suggested ingredient substitutions
- Recipe browser with filters (language, category)

## 1.3 AI Integration Details

We integrated an open-source NLP model to:
- Suggest ingredient substitutions based on regional availability
- Categorize recipes into vegetarian/non-vegetarian/snack/main dish based on keywords

We used:
- `IndicNLP` for language support
- `transformers` library (offline GPT-2 small) for text enhancement
- Custom rule-based logic for local substitutions (e.g., “Use tamarind instead of tomato”)

## 1.4 Technical Architecture & Development

### Stack:
- **Frontend**: Streamlit (with multilingual input and local file handling)
- **Backend**: JSON-based storage (initial), plan to scale to DB
- **AI Models**: Hugging Face transformers (offline), Indic NLP
- **Deployment**: Hugging Face Spaces
- **Caching/Offline Support**: Streamlit + browser-based caching (IndexedDB/SessionState fallback)

### Folder Structure:
```
├── app.py
├── utils/
│   └── ai_utils.py
├── data/
│   └── recipes.json
├── assets/
├── requirements.txt
├── REPORT.md
├── README.md
└── LICENSE
```

### Development Progress (Week 1)
- Day 1: Set up layout + language toggle
- Day 2: Built recipe form + local preview
- Day 3: Added offline caching
- Day 4: Integrated AI substitution engine
- Day 5: Created recipe browser
- Day 6-7: Testing + Deployment to Hugging Face

## 1.5 User Testing & Feedback

### Methodology
- We recruited testers from:
  - WhatsApp groups (relatives, rural volunteers)
  - Telegram food communities
  - College peers across states

- **Test Setup:**
  - Mobile-first testing
  - Shared sample tasks: “Submit a family recipe in your language,” “Try with poor internet,” “Use Telugu script”
  - Collected feedback via Google Form & phone calls

### Feedback Received:
- “App is easy but submitting in native language is hard without keyboard”
- “Would love to record voice and upload”
- “Works even with slow 2G signal, which is great!”

### Iterations Done:
- Added Hindi/Telugu/English input keyboard guide
- Added offline text save + retry sync
- Compressed image uploads to <100KB
