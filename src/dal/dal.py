import pandas as pd
import json

class Dal:

    def __init__(self):
        self._rwa_data = pd.read_csv("data/tweets_dataset.csv")
        self.json_path = "results/results.json"


    def load_data(self):
        return self._rwa_data


    def dump_json(self, data):
        with open(self.json_path ,"w" ,encoding="utf-8") as file:
            json.dump(file,data)
