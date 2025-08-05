import pandas as pd
import json

class Dal:

    def __init__(self):
        self._rwa_data = pd.read_csv("data/tweets_dataset.csv")
        self.json_path = "results/results.json"
        self.cleaned_csv_path = "results/cleaned_dataset_tweets.csv"




    def load_data(self):
        return self._rwa_data


    def dump_json(self, data):
        with open(self.json_path ,"w" ,encoding="utf-8") as file:
            json.dump(data,file, indent= 4)

    def dump_cleaned_csv(self, df):
        df.to_csv(self.cleaned_csv_path, index=False, encoding="utf-8")
