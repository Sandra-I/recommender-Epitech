
import pandas as pd

class GetFileFromUrl:

    df = pd.DataFrame()

    def __init__(self):
        url = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/clean_dataset.csv'
        self.df = pd.read_csv(url, parse_dates=True)

    def get_clean_dataframe(self):
        return self.df