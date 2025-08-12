from src.dal.dal import Dal
from src.utils.data_cleaner import DataCleaner
from src.core.data_analyzer import DataAnalyzer
from src.utils.convert_numpy_objects import convert_numpy_types


class Manager:
    """Orchestrates the flow. Catches errors and reports them nicely."""

    def __init__(self):
        self.dal = Dal()
        self.data_cleaner = DataCleaner()
        self.data_analyzer = DataAnalyzer()
        self.statistic = None
        self.cleaned_data = None

    def run(self) -> bool:
        """Run the pipeline. Returns True on success, False on failure.
        Prints short messages.
        """
        try:
            data = self.dal.load_data()
            self.statistic = self.data_analyzer.analyze(data)
            self.cleaned_data = self.data_cleaner.clean_data(data)
            safe_stats = convert_numpy_types(self.statistic)
            self.dal.dump_json(safe_stats)
            self.dal.dump_cleaned_csv(self.cleaned_data)
            print("✔ Done. Wrote results.json and cleaned_dataset_tweets.csv under results/.")
            return True
        except FileNotFoundError as e:
            print(f"✖ File not found: {e}")
        except ValueError as e:
            print(f"✖ Bad data: {e}")
        except RuntimeError as e:
            print(f"✖ Runtime error: {e}")
        except Exception as e:
            # last resort
            print(f"✖ Unexpected error: {e}")
        return False
