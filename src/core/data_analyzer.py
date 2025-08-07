from collections import Counter

import pandas as pd

class DataAnalyzer:

    def analyze(self, df):
        antisemitic_mask = df["Biased"] == 1
        non_antisemitic_mask = df["Biased"] == 0

        statistics = {
            "total_tweets": self.count_tweets_per_category(df),
            "average_words_in_tweet": self.average_words_per_tweet(df,antisemitic_mask, non_antisemitic_mask),
            "3 longest_tweets": self.find_3_longest_tweets(df, antisemitic_mask, non_antisemitic_mask),
            "common_words": self.find_most_common_words(df),
            "uppercase_words": self.count_uppercase_words(df,antisemitic_mask, non_antisemitic_mask)
        }

        return statistics

    def count_tweets_per_category(self, df: pd.DataFrame):
        counts = df["Biased"].value_counts()
        return {
            "antisemitic": int(counts.get(1, 0)),
            "non_antisemitic": int(counts.get(0, 0)),
            "total": len(df),
        }

    def average_words_per_tweet(self, df: pd.DataFrame, antisemitic_mask, non_antisemitic_mask):
        return {
            "antisemitic": self._average_words(df[antisemitic_mask]),
            "non_antisemitic": self._average_words(df[non_antisemitic_mask]),
            "total": self._average_words(df)
        }


    def _average_words(self, df: pd.DataFrame):
        return round(df["Text"].apply(lambda x: len(str(x).split())).mean() or 0, 2)

    def find_3_longest_tweets(self, df: pd.DataFrame, antisemitic_mask, non_antisemitic_mask):
        return {
            "antisemitic": self._top_n_longest_tweets(df[antisemitic_mask], n=3),
            "non_antisemitic": self._top_n_longest_tweets(df[non_antisemitic_mask], n=3)
        }

    def _top_n_longest_tweets(self, df: pd.DataFrame, n=3):
        df = df.copy()
        df["text_length"] = df["Text"].astype(str).str.len()
        return df.sort_values(by="text_length", ascending=False)["Text"].head(n).tolist()

    def find_most_common_words(self, df: pd.DataFrame, n=10):
        words = " ".join(df["Text"].astype(str)).split()
        most_common = Counter(words).most_common(n)
        return [word for word, _ in most_common]

    def count_uppercase_words(self, df: pd.DataFrame, antisemitic_mask, non_antisemitic_mask):
        return {
            "antisemitic": self._uppercase_word_count(df[antisemitic_mask]),
            "non_antisemitic": self._uppercase_word_count(df[non_antisemitic_mask]),
            "total": self._uppercase_word_count(df)
        }

    def _uppercase_word_count(self, df: pd.DataFrame):
        return int(df["Text"].apply(lambda x: sum(1 for word in str(x).split() if word.isupper())).sum())



