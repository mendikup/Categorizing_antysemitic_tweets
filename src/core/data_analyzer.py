import pandas as pd

class DataAnalyzer:

    def analyze(self, df):
        statistics = {
            "total_tweets": self.count_tweets_per_category(df),
            "average_words_in_tweet": self.average_words_per_tweet(df),
            "longest_3_tweets": self.find_the_3_longest_tweets_per_category(df),
            "common_words": self.find_the_10_most_common_words_in_all_categories(df),
            "uppercase_words": self.find_the_number_of_words_in_uppercase(df)
        }

        return statistics

    def count_tweets_per_category(self, df):
        total = len(df)
        value_counts = df["Biased"].value_counts().to_list()
        return {
            "total": total,
            "not_antisemitic": value_counts[0],
            "antisemitic": value_counts[1]
        }

    def average_words_per_tweet(self, df):
        not_antisemitic_mask = df["Biased"] == 0
        antisemitic_mask = df["Biased"] == 1

        not_antisemitic_avg = df[not_antisemitic_mask]["Text"].apply(lambda x: len(str(x).split())).mean()
        antisemitic_avg = df[antisemitic_mask]["Text"].apply(lambda x: len(str(x).split())).mean()

        return {
            "not_antisemitic": round(not_antisemitic_avg, 2) if not_antisemitic_avg is not None else 0,
            "antisemitic": round(antisemitic_avg, 2) if antisemitic_avg is not None else 0
        }


    def find_the_3_longest_tweets_per_category(self, df):
        longest_3_tweets_per_category = {"antisemitic":[],"not_antisemitic":[]}
        not_antisemitic_mask = df["Biased"] == 0
        antisemitic_mask = df["Biased"] == 1

        # Calculate word lengths and sort per not_antisemitic tweets
        df["word_length"] = df[not_antisemitic_mask]["Text"].str.len()
        sorted_df = df.sort_values(by=["word_length"], ascending=False)
        the_longest_3_words = sorted_df["Text"].head(3).to_string(index=False)
        longest_3_tweets_per_category["antisemitic"].append(the_longest_3_words)

        # Calculate word lengths and sort per antisemitic tweets
        df["word_length"] = df[antisemitic_mask]["Text"].str.len()
        sorted_df = df.sort_values(by=["word_length"], ascending=False)
        the_longest_3_words = sorted_df["Text"].head(3).to_string(index=False)
        longest_3_tweets_per_category["not_antisemitic"].append(the_longest_3_words)
        return longest_3_tweets_per_category


    def find_the_10_most_common_words_in_all_categories(self, df):
        seperate_words = df["Text"].sum().split()
        seperate_words = pd.Series(seperate_words)
        count_words = seperate_words.value_counts()
        common_words = count_words.head(10).index.to_list()
        return common_words

    def find_the_number_of_words_in_uppercase(self ,df: pd.DataFrame):
        number_of_words_in_uppercase = {}
        total = 0
        not_antisemitic_mask = df["Biased"] == 0
        df = df[not_antisemitic_mask]
        sum_of_uppercase =df["Text"].apply(lambda x:sum(1 for word in x.split() if word.isupper())).sum()
        total +=sum_of_uppercase
        number_of_words_in_uppercase ["nut_antisemitic"] = sum_of_uppercase


        #count for antisemitic
        antisemitic_mask = df["Biased"] == 1
        df =df[antisemitic_mask]
        sum_of_uppercase = df["Text"].apply(lambda x: sum(1 for word in x.split() if word.isupper())).sum()
        number_of_words_in_uppercase["antisemitic"] = sum_of_uppercase
        total += sum_of_uppercase

        number_of_words_in_uppercase["total"] = total



        return number_of_words_in_uppercase




