import pandas as pd

class Dal:

    def __init__(self):
        self._rwa_data = pd.read_csv("data/tweets_dataset.csv")


    def load_data(self):
        return self._rwa_data
