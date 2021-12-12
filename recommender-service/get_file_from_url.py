
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

class GetFileFromUrl:

    df = pd.DataFrame()
    best_item_by_cli_df = pd.DataFrame()
    frequence_item_df = pd.DataFrame()
    paired_item_df = pd.DataFrame()
    cli_article_rfm_segment = pd.DataFrame()

    def __init__(self):
        # url = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/clean_dataset.csv'
        #url1 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/best_item_by_cli.csv'
        #url2 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/frequence_item.csv'
        #url3 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/paired_item.csv'
        #url4 = 'http://recommender31.s3-website.eu-west-3.amazonaws.com/cli_article_rfm_segment.csv'

        # url_kado = 'https://drive.google.com/file/d/1uHl2YzpgNUOdXgW_3EtX4_5KYNY2Yu4q/view?usp=sharing'
        url_clean_dataset = 'https://drive.google.com/file/d/1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ/view?usp=sharing'
        url_best_item = 'https://drive.google.com/file/d/1WM9kvmlOhzuyepk77R7k0UM2-PAngkQ0/view?usp=sharing'
        url_freq_item = 'https://drive.google.com/file/d/1J1zoy6uPfCciaQH0WLMhMeC-b3SDV80m/view?usp=sharing'
        url_paired_item = 'https://drive.google.com/file/d/1PAy6z1PHJMCaAmWGmQXqf25epPAdplgn/view?usp=sharing'
        url_rfm_cli_art = 'https://drive.google.com/file/d/1UP8JwG0v9Nv6nUAYfc4kowbHeJ861lA0/view?usp=sharing'


        self.df = pd.read_csv(url_clean_dataset, parse_dates=True)
        #self.best_item_by_cli_df = pd.read_csv(url_best_item, parse_dates=True)
        #self.frequence_item_df = pd.read_csv(url_freq_item, parse_dates=True)
        #self.paired_item_df = pd.read_csv(url_paired_item, parse_dates=True)
        #self.cli_article_rfm_segment = pd.read_csv(url_rfm_cli_art, parse_dates=True)


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