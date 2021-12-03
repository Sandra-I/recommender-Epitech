import pandas as pd

class CustomerSegmenter:

    customer_cluster_result = 0
    df = pd.DataFrame()
    customer_rfm = {}
    customer_family = {}

    def __init__(self):
        self.df = pd.read_csv('..\clean_dataset.csv', parse_dates=True)
        self.df.head()

    def create_customer_clusters(self):
        
        rfm_df = self.get_RFM()
        self.customer_rfm = rfm_df.to_json(orient="index")

    def get_customer_family(self):
        print('Retourne dataframe customer avec famille')
    
    def get_RFM(self):
        monetary_series = self.calculate_monetary()
        recency_series = self.calculate_recency()
        frequency_series = self.calculate_frequency()
        data = {'recency': recency_series, 'frequency': frequency_series, 'monetary': monetary_series }
        return pd.DataFrame(data=data, index = recency_series.index )

    def get_customer_RFM(self):
        return self.customer_rfm

    def calculate_monetary(self):
        return self.df[['CLI_ID', 'PRIX_NET']].groupby('CLI_ID').agg(sum).squeeze()

    def calculate_recency(self):
        return self.df[['CLI_ID', 'MOIS_VENTE']].groupby('CLI_ID').agg('max').squeeze()

    def calculate_frequency(self):
        return self.df[['CLI_ID', 'TICKET_ID']].groupby('CLI_ID').agg(pd.Series.nunique).squeeze()