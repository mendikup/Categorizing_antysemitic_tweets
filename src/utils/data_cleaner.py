import  pandas as pd

class DataCleaner:


    def clean_data(self,df):
        relevant_columns = self.saving_the_relevant_columns_from_the_data_file(df)
        df = self.removing_punctuation_marks(df)
        df = self.convert_to_lowercase(df)
        df = self.removing_uncategorized_tweets(df)
        return df ,relevant_columns





    def saving_the_relevant_columns_from_the_data_file(self, df):
        return

    def removing_punctuation_marks(self, df):
        pass

    def convert_to_lowercase(self,df):
        pass

    def removing_uncategorized_tweets(self, df):
        pass