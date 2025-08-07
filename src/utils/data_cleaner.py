import string

import  pandas as pd

class DataCleaner:


        def clean_data(self, df):
            df = df.copy()
            df = self.saving_the_relevant_columns_from_the_data_file(df)
            df = self.removing_punctuation_marks(df)
            df = self.convert_to_lowercase(df)
            df = self.removing_uncategorized_tweets(df)
            return df

        def saving_the_relevant_columns_from_the_data_file(self, df):
            return df[['Text', 'Biased']]

        def removing_punctuation_marks(self, df):
            df['Text'] = df['Text'].apply(
                lambda x: x.translate(str.maketrans('', '', string.punctuation))
                if isinstance(x, str) else x
            )
            return df

        def convert_to_lowercase(self, df):
            df['Text'] = df['Text'].apply(
                lambda x: x.lower() if isinstance(x, str) else x
            )
            return df

        def removing_uncategorized_tweets(self, df):
            return df[df['Biased'].isin([0, 1])]
