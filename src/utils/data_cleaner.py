import string
import pandas as pd


class DataCleaner:
    """Simple cleaner. Expects columns 'Text' and 'Biased'."""

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run the cleaning steps and return a NEW DataFrame.
        Raises on bad input.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("DataCleaner.clean_data expects a pandas DataFrame")
        missing = [c for c in ("Text", "Biased") if c not in df.columns]
        if missing:
            raise ValueError(f"DataCleaner: missing required columns: {missing}")
        df = df.copy()
        df = self.saving_the_relevant_columns_from_the_data_file(df)
        df = self.removing_punctuation_marks(df)
        df = self.convert_to_lowercase(df)
        df = self.removing_uncategorized_tweets(df)
        return df

    def saving_the_relevant_columns_from_the_data_file(self, df: pd.DataFrame) -> pd.DataFrame:
        """Keep only the columns we actually use."""
        return df[["Text", "Biased"]]

    def removing_punctuation_marks(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove basic punctuation from Text."""
        df = df.copy()
        df["Text"] = df["Text"].apply(
            lambda x: x.translate(str.maketrans('', '', string.punctuation)) if isinstance(x, str) else x
        )
        return df

    def convert_to_lowercase(self, df: pd.DataFrame) -> pd.DataFrame:
        """Lowercase for consistency."""
        df = df.copy()
        df["Text"] = df["Text"].apply(lambda x: x.lower() if isinstance(x, str) else x)
        return df

    def removing_uncategorized_tweets(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter rows to where Biased is 0/1 only."""
        df = df.copy()
        return df[df["Biased"].isin([0, 1])]
