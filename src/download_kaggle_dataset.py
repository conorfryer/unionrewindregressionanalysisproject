import kaggle
import os

# Define dataset directory
DATA_DIR = "./data"

def download_dataset():
    """Downloads the Kaggle dataset and extracts it to the data directory."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    kaggle.api.dataset_download_files(
        "asaniczka/top-spotify-songs-in-73-countries-daily-updated",
        path=DATA_DIR,
        unzip=True
    )
    print(f"Dataset downloaded and extracted to {DATA_DIR}")

if __name__ == "__main__":
    download_dataset()
