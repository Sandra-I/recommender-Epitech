import pandas as pd
# from get_file_from_url import GetFileFromUrl
# from google_api.get_file_from_google import GetFileFromGoogleDrive

class CustomerSegmenter:

    # get_file_from_url = GetFileFromUrl()
    # get_file_from_google = GetFileFromGoogleDrive()
    customer_cluster_result = 0
    df = pd.DataFrame()
    customer_rfm = {}
    customer_family = {}
    data_by_cat = {}
    counts_by_cat = {}
    counts_cat_by_cust = {}

    def __init__(self):
        # self.df = self.get_file_from_url.get_clean_dataframe()
        # self.df = self.get_file_from_google.get_clean_dataframe()
        self.df = pd.read_csv('../clean_dataset.csv', parse_dates=True)
        # self.df = self.df.tail(n = 50)
        print(self.df.head())

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

    def get_customers_by_category(self, cat):
        cat = cat.upper()
        cat_data_df = self.df[["CLI_ID", cat]]
        self.data_by_cat = cat_data_df.to_json(orient="index")
        return self.data_by_cat

    def get_counts_by_category(self, cat):
        cat = cat.upper()
        counts = self.df[cat].value_counts(dropna=False)
        self.counts_by_cat = counts.to_json(orient="index")
        return self.counts_by_cat

    def get_counts_category_by_customer(self, cat):
        cat = cat.upper()
        counts = self.df.groupby("CLI_ID")[cat].value_counts()
        self.counts_cat_by_cust = counts.to_json(orient="index")
        return self.counts_cat_by_cust
    
    def division_for_average_basket(x, y):
        return y['monetary'] / y['frequency']

    def calculate_average_basket(self):
        data = { 'monetary': self.calculate_monetary(), 'frequency': self.calculate_frequency() }
        data_frame = pd.DataFrame(data=data, index=data['frequency'].index)
        return data_frame.apply(self.division_for_average_basket, axis=1)
    
    def get_average_basket(self):
        average = self.calculate_average_basket()
        mean_average = average.mean()
        return mean_average

    def get_average_basket_by_client(self, id):
        all_average = self.calculate_average_basket()
        client_average = all_average.loc[int(id)]
        return client_average

    def calculate_frequency_group(self):
        data_frame = self.df[['CLI_ID', 'TICKET_ID']].groupby('CLI_ID').agg(pd.Series.nunique)
        return pd.qcut(data_frame['TICKET_ID'], q=2, labels=['OCCASIONNEL','REGULIER'])

    def get_frequency_group_repartition(self):
        freq_group_series = self.calculate_frequency_group()
        freq_counts = freq_group_series.value_counts()
        freq_percent_counts = freq_group_series.value_counts(normalize=True)
        data = { 'recency_counts': freq_counts, 'recency_percent_counts': freq_percent_counts }
        data_frame = pd.DataFrame(data=data, index=data['recency_counts'].index)
        return data_frame.to_json(orient="index")

    def get_frequency_group_by_customer(self, id):
        freq_group_series = self.calculate_frequency_group()
        freq_group = freq_group_series.loc[int(id)]
        return { 'frequency_group': freq_group }
