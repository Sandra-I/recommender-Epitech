
import pandas as pd

class GetFileFromUrl:

    df = pd.DataFrame()
    best_item_by_cli_df = pd.DataFrame()
    frequence_item_df = pd.DataFrame()
    paired_item_df = pd.DataFrame()
    cli_article_rfm_segment = pd.DataFrame()

    def __init__(self):
        url = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/clean_dataset.csv'
        #url1 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/best_item_by_cli.csv'
        #url2 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/frequence_item.csv'
        #url3 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/paired_item.csv'
        #url4 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/cli_article_rfm_segment.csv'


        self.df = pd.read_csv(url, parse_dates=True)
        #self.best_item_by_cli_df = pd.read_csv(url1, parse_dates=True)
        #self.frequence_item_df = pd.read_csv(url2, parse_dates=True)
        #self.paired_item_df = pd.read_csv(url3, parse_dates=True)
        #self.cli_article_rfm_segment = pd.read_csv(url4, parse_dates=True)


    def get_clean_dataframe(self):
        return self.df

    def get_best_item_by_cli_dataframe(self):
        return self.best_item_by_cli_df

    def get_frequence_item_dataframe(self):
        return self.frequence_item_df
    
    def get_paired_item_dataframe(self):
        return self.paired_item_df

    def get_rfm_cli_article_dataframe(self):
        return self.cli_article_rfm_segment