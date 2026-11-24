"""Download the Criteo Uplift v2.1 dataset (~311 MB) from Hugging Face into data/raw/."""

from pathlib import Path

from huggingface_hub import hf_hub_download

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = hf_hub_download(
        repo_id="criteo/criteo-uplift",
        filename="criteo-research-uplift-v2.1.csv.gz",
        repo_type="dataset",
        local_dir=RAW_DIR,
    )
    print(f"Downloaded to {path}")


if __name__ == "__main__":
    main()
