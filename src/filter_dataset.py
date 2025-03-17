import pandas as pd

# Load the dataset
df = pd.read_csv("data/universal_top_spotify_songs.csv")

# Convert album_release_date to datetime
df["album_release_date"] = pd.to_datetime(df["album_release_date"], errors="coerce")

# Step 1: Remove all songs released in 2025
df = df[df["album_release_date"].dt.year < 2025]

# Step 2: Toggle country filter
FILTER_COUNTRY_ISO = True  # Set to False to disable country-based filtering
EXPANDED_WESTERN_ISO = True  # Set to False to use only strictly English-speaking countries

if FILTER_COUNTRY_ISO:
    if EXPANDED_WESTERN_ISO:
        # Expanded list including culturally aligned Western nations
        country_list = ["US", "CA", "GB", "AU", "IE", "NZ",  # English-speaking
                        "SE", "NO", "DK", "NL", "DE", "FR"]  # Western European nations with strong English-language music consumption
    else:
        # Strictly English-speaking countries only
        country_list = ["US", "CA", "GB", "AU", "IE", "NZ"]

    df = df[df["country"].isin(country_list)]

# Step 3: Sort values (popularity first, then album release date)
df = df.sort_values(by=["popularity", "album_release_date"], ascending=[False, False])

# Step 4: Remove duplicate songs based on song name, artist, and duration
df_cleaned = df.drop_duplicates(subset=["name", "artists", "duration_ms"], keep="first")

# Step 5: Shuffle the dataset before saving
df_cleaned = df_cleaned.sample(frac=1, random_state=42).reset_index(drop=True)

# Step 6: Save the cleaned dataset
output_filename = "data/filtered_songs_EXPANDED.csv" if FILTER_COUNTRY_ISO else "data/filtered_songs_GLOBAL.csv"
df_cleaned.to_csv(output_filename, index=False)

# Summary of cleaning
print(f"Original dataset size: {len(df)} rows")
print(f"Filtered dataset size: {len(df_cleaned)} rows")
print(f"Dataset saved as: {output_filename}")