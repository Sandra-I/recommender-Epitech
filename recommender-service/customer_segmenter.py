import pandas as pd

class CustomerSegmenter:

    customer_cluster_result = 0
    df = pd.DataFrame()
    result = {}

    def __init__(self):
        self.df = pd.read_csv('..\clean_dataset.csv', parse_dates=True)
        self.df.head()

    def create_customer_clusters(self):
        
        self.get_RFM()

    
    def get_RFM(self):
        monetary_series = self.calculate_monetary()
        recency_series = self.calculate_recency()
        frequency_series = self.calculate_frequency()
        print(monetary_series.head())
        # data = {'RECENCE': cli_recency['MOIS_VENTE'], 'FREQUENCE': cli_frequency['TICKET_ID'], 'MONTANT': cli_total_spent }
        # rfm_df = pd.DataFrame(data=data, index = recency_series.index )


    def calculate_monetary(self):
        client_total_spent = self.df.groupby('CLI_ID').agg(sum)['PRIX_NET']
        return pd.qcut(client_total_spent, q=4, labels=range(1,5))

    def calculate_recency(self):
        client_last_purchase = self.df[['CLI_ID', 'MOIS_VENTE']].groupby('CLI_ID').agg('max')
        client_recency = 13 - client_last_purchase
        return pd.qcut(client_recency['MOIS_VENTE'], q=3, labels=['ACTIVE','OCCASIONNEL','INACTIVE'])

    def calculate_frequency(self):
        client_frequency = self.df[['CLI_ID', 'TICKET_ID']].groupby('CLI_ID').agg(pd.Series.nunique)
        return pd.qcut(client_frequency['TICKET_ID'], q=2, labels=['OCCASIONNEL','REGULIER'])

    def segment_customers(self):
        # print(self.dataframe.head())
        # print(self.dataframe.info())
        # print('Customer segmented')
        return {"123": {"RECENCE": 2, "FREQUENCE": 5}}