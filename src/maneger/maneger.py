import pandas as pd
from src.dal.dal import Dal
from src.utils.data_cleaner import DataCleaner
from src.core.data_analyzer import DataAnalyzer
from src.utils.convert_numpy_objects import convert_numpy_types

class Manager:
    dal =Dal()
    data_cleaner = DataCleaner()
    data_analyzer = DataAnalyzer()


    def __init__(self):
        self.cleaned_data = None
        self.statistic = None


    def run(self):
        data = self.dal.load_data()
        self.cleaned_data = self.data_cleaner.clean_data(data)
        self.statistic = self.data_analyzer.analyze(data)
        self.dal.dump_json(convert_numpy_types(self.statistic))
        self.dal.dump_cleaned_csv(self.cleaned_data)







