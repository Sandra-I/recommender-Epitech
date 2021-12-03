import pandas as pd

class CustomerSegmenter:

    customer_cluster_result = 0
    dataframe = pd.DataFrame()
    result = {}

    def __init__(self):
        self.dataframe = pd.read_csv('..\clean_dataset.csv', parse_dates=True)
        self.dataframe.head()

    def create_customer_clusters(self):
        
        print('')

    
    def get_RFM(self):
        monetary_series = self.calculate_monetary()

    def calculate_monetary(self):
        client_total_spent = self.dataframe.groupby('CLI_ID').agg(sum)['PRIX_NET']
        return pd.qcut(client_total_spent, q=4, labels=range(1,5))

    def calculate_recency(self):
        print('')

    def segment_customers(self):
        # print(self.dataframe.head())
        # print(self.dataframe.info())
        # print('Customer segmented')
        return {"123": {"RECENCE": 2, "FREQUENCE": 5}}