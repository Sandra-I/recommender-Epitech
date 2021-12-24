import pandas as pd
# from get_file_from_url import GetFileFromUrl
# from google_api.get_file_from_google import GetFileFromGoogleDrive

class CustomerSegmenter:

    # get_file_from_url = GetFileFromUrl()
    # get_file_from_google = GetFileFromGoogleDrive()
    customer_cluster_result = 0
    df = pd.DataFrame()
    df_cutomer_details = pd.DataFrame()
    customer_rfm = {}
    customer_family = {}
    data_by_cat = {}
    counts_by_cat = {}
    counts_cat_by_cust = {}

    def __init__(self):
        # self.df = self.get_file_from_url.get_clean_dataframe()
        # self.df = self.get_file_from_google.get_clean_dataframe()
        # self.df_customer_details = self.get_file_from_google.get_csv_details_by_customer()
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
        return { 'average_basket': client_average }

    def calculate_recency_group(self):
        cli_last_purchase = self.df[['CLI_ID', 'MOIS_VENTE']].groupby('CLI_ID').agg('max')
        cli_recency = 13 - cli_last_purchase
        return pd.qcut(cli_recency['MOIS_VENTE'], q=3, labels=['ACTIVE','OCCASIONNEL','INACTIVE'])

    def get_recency_group(self):
        recency_group_series = self.calculate_recency_group()
        recency_counts = recency_group_series.value_counts()
        recency_percent_counts = recency_group_series.value_counts(normalize=True)
        data = { 'recency_counts': recency_counts, 'recency_percent_counts': recency_percent_counts }
        data_frame = pd.DataFrame(data=data, index=data['recency_counts'].index)
        return data_frame.to_json(orient="index")

    def get_recency_group_by_customer(self, id):
        recency_group_series = self.calculate_recency_group()
        customer_group = recency_group_series.loc[int(id)]
        return { 'recency_group': customer_group }
    
    def get_recency_by_customer(self, id):
        data = { 'recency': self.calculate_recency() }
        recency_dataframe = pd.DataFrame(data=data, index=data['recency'].index)
        customer_recency = recency_dataframe.loc[int(id)]
        return customer_recency.to_json()
    
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

    def frequency_to_dataframe(self):
        data = { 'frequency': self.calculate_frequency() }
        return pd.DataFrame(data=data, index=data['frequency'].index)
    
    def get_mean_frequency(self):
        data_frame = self.frequency_to_dataframe()
        mean_frequency = data_frame.mean()
        return mean_frequency.to_json(orient="index")

    def get_frequency_by_customer(self, id):
        data_frame = self.frequency_to_dataframe()
        client_frequency = data_frame.loc[int(id)]
        return client_frequency.to_json(orient="index")

    def get_details_by_customer(self, id):
        avg = self.get_average_basket_by_client(id)
        rec_grp = self.get_recency_group_by_customer(id)
        rec =  self.get_recency_by_customer(id)
        freq_grp = self.get_frequency_group_by_customer(id)
        freq = self.get_frequency_by_customer(id)
        return id, avg, rec_grp, rec, freq_grp, freq

    def generate_csv_details(self):
        all_average_series = self.calculate_average_basket()
        all_frequencies_series = self.calculate_frequency()
        all_freq_group_series = self.calculate_frequency_group()
        all_recency_series = self.calculate_recency()
        all_recency_group_series = self.calculate_recency_group()   
        df_stitched = pd.concat([all_average_series, all_frequencies_series, all_freq_group_series, all_recency_series, all_recency_group_series], axis=1)
        df_stitched.columns = ['average', 'frequency', 'frequency_group', 'recency', 'recency_group']
        df_stitched.to_csv('csv_details_by_customer.csv')
        return { 'average_basket': 'client_average' }
    
    def get_customer_details_in_csv(self, id):
        # df = self.df_customer_details
        df = pd.read_csv('csv_details_by_customer.csv')
        customer = df[df['CLI_ID'] == int(id)]
        return customer.to_json(orient="index")