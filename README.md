# 🎵 The Sound of Union 🎵  
### Quantifying Union College’s Music Preferences with Logistic Regression  

**Author:** Conor Fryer  
**Course:** STA 264 – Hoerl – Winter 2025  

## Overview  
This project explores whether Union College students have distinct musical preferences that can be quantified using logistic regression. Built on **Union Rewind**, an annual WRUC initiative, the study compares students' most-played songs to a dataset of globally popular tracks to determine if certain song characteristics influence inclusion in a Union student’s top five.  

Using **Spotify’s audio features**, a logistic regression model was developed to assess measurable predictors like **danceability, energy, acousticness, and instrumentalness**. The results revealed significant trends—most notably, highly danceable music, despite being dominant in social settings, was *less* likely to appear in students' personal top five lists.  

---

### 🔍 Key Features:
- **Data Collection:** Union Rewind survey data (students' self-reported top five songs) vs. a dataset of globally popular songs.
- **Statistical Analysis:** Logistic regression applied to **Spotify audio features**.
- **Insights:** Identifying measurable trends in Union students' music preferences.
- **Tech Stack:** JMP, Python (for data processing), Spotify API (for feature extraction).

---

## 📂 Repository Structure
```
unionrewindregressionanalysisproject/
│-- data/               # Contains raw and processed datasets
│-- jmp/                # JMP analysis files
│-- src/                # Python scripts (Spotify API extraction, data preprocessing)
│-- LICENSE             # MIT License
│-- README.md           # Project documentation
│-- .gitignore          # Specifies ignored files (e.g., .env)
```

---

## ⚙️ Configuration
This project requires **Spotify API credentials** for extracting song features. You must create a `.env` file in the **root directory** with the following:

```ini
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=your_redirect_uri_here
```

### 🔧 Steps to Set Up:
1. **Register your application** on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to obtain API credentials.
2. **Set the redirect URI** in your Spotify Developer settings.
3. **Create a `.env` file** in the project root and add the credentials.

🔹 **Pro Tip:** To prevent accidental commits, the `.env` file is ignored by Git. Instead, you can use the provided `.env.example` template:

```ini
# Rename this file to .env and fill in your credentials
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=your_redirect_uri_here
```

---

## Data Collection
- **Included Dataset:** Collected through Union Rewind, where Union College students reported their top five songs via an in-person survey.
- **Non-Included Dataset:** Drawn from Kaggle's "Top Spotify Songs in 73 Countries" dataset, representing globally popular music.

---

## Methodology
- **Logistic Regression Analysis:** 
  - Predicts whether a song was included in a Union student's top five based on Spotify audio features.
  - Key predictors analyzed: danceability, energy, acousticness, instrumentalness, speechiness, valence, and live elements.
  - Popularity and loudness were removed due to their overwhelming influence and redundancy.
- **Model Validation:** 
  - Alternative datasets were tested to confirm consistency.
  - Statistical tests ensured robustness.

---

## Key Findings
- **Distinct Preferences:** Union students’ musical choices differed from global streaming trends.
- **Danceability:** Strong negative effect—highly danceable songs were less likely to appear in personal top-five selections.
- **Instrumentalness:** Only feature with a positive effect—songs with instrumental elements had a slightly higher chance of inclusion.
- **Energy & Speechiness:** Moderately negative effects, indicating a preference for structured, polished music over raw or spoken-word-heavy tracks.
- **Model Limitations:** Music preference remains highly subjective, making it difficult to fully capture personal taste with statistical modeling.

---

## Tools & Technologies
- **Spotify API & Chosic Playlist Analyzer** (for extracting audio features)
- **JMP Statistical Software** (for logistic regression analysis)
- **Python & Pandas** (for data processing and structuring)

---

## 🚀 Future Improvements
- Expanding analysis to **multi-year trends** in Union College’s music preferences.
- Exploring **additional Spotify metadata** (e.g., genre classifications) to refine preference modeling.
- Implementing **interactive visualizations** to display trends dynamically.

---

## 📜 License
This project is licensed under the **MIT License**, allowing free use, modification, and distribution with attribution.

**Important:** If you intend to redistribute **Spotify data**, please review [Spotify’s Developer Terms](https://developer.spotify.com/terms) to ensure compliance.

---

## 🏆 Acknowledgments
- **Union Rewind participants** for contributing their top songs.
- **WRUC (Union College Radio Club)** for facilitating data collection.
- **Spotify API** for providing structured audio feature data.
