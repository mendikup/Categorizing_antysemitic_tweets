import pandas as pd
import json
from pathlib import Path


class Dal:
    """Tiny data-access layer. Reads CSV, writes results."""

    def __init__(self, csv_path: str = "data/tweets_dataset.csv"):
        self.csv_path = Path(csv_path)
        self.json_path = Path("results/results.json")
        self.cleaned_csv_path = Path("results/cleaned_dataset_tweets.csv")
        self._raw_data = self._safe_read_csv(self.csv_path)

    def _safe_read_csv(self, path: Path) -> pd.DataFrame:
        if not path.exists():
            raise FileNotFoundError(f"CSV not found at {path.resolve()}")
        try:
            return pd.read_csv(path)
        except Exception as exc:
            raise RuntimeError(f"Couldn't read CSV: {exc}") from exc

    def load_data(self) -> pd.DataFrame:
        """Return the raw DataFrame read at init."""
        return self._raw_data

    def dump_json(self, data: dict) -> None:
        """Write JSON with UTF-8 + indentation."""
        try:
            with self.json_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as exc:
            raise RuntimeError(f"Failed writing {self.json_path}: {exc}") from exc

    def dump_cleaned_csv(self, df: pd.DataFrame) -> None:
        """Write the cleaned dataset to CSV."""
        try:
            df.to_csv(self.cleaned_csv_path, index=False, encoding="utf-8")
        except Exception as exc:
            raise RuntimeError(f"Failed writing {self.cleaned_csv_path}: {exc}") from exc
