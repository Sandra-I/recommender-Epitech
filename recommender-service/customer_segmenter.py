import pandas as pd
# PROD to uncomment for production
from google_api.get_file_from_google import GetFileFromGoogleDrive

class CustomerSegmenter:
    # PROD to uncomment for production
    get_file_from_google = GetFileFromGoogleDrive()
    customer_cluster_result = 0
    df = pd.DataFrame()
    df_customer_details = pd.DataFrame()
    customer_rfm = {}
    customer_family = {}
    data_by_cat = {}
    counts_by_cat = {}
    counts_cat_by_cust = {}
    top_categories = {}

    def __init__(self):
        # DEV to delete or comment for prod
        # self.df = pd.read_csv('../clean_dataset.csv', parse_dates=True)
        # self.df_customer_details = pd.read_csv('../csv_details_by_customer.csv')

        # PROD to uncomment for production
        self.df = self.get_file_from_google.get_clean_dataframe()
        self.df_customer_details = self.get_file_from_google.get_csv_details_by_customer()

        self.customers_id = self.get_customers_id()
        print(self.df.head())

    def create_customer_clusters(self):
        rfm_df = self.get_RFM()
        self.customer_rfm = rfm_df.to_json(orient="index")

    def get_customers_id(self):
        return self.df_customer_details['CLI_ID'].tolist()
    
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
        data = { 'frequency_counts': freq_counts, 'frequency_percent_counts': freq_percent_counts }
        data_frame = pd.DataFrame(data=data, index=data['frequency_counts'].index)
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

    def generate_csv_global(self):
        global_basket = pd.Series(self.get_average_basket())
        global_recency = pd.Series(self.get_recency_group())
        global_freq_group = pd.Series(self.get_frequency_group_repartition())
        global_mean_freq = pd.Series(self.get_mean_frequency())
        df_stitched = pd.concat([global_basket, global_recency, global_freq_group, global_mean_freq], axis=1)
        df_stitched.columns = ['basket', 'recency', 'freq_group', 'mean_freq']
        df_stitched.to_csv('csv_global_metrics.csv')
        print(df_stitched)
        return { 'global_metrics': df_stitched }

    def get_customer_details_in_csv(self, id):
        df = self.df_customer_details
        customer = df[df['CLI_ID'] == int(id)]
        return customer.to_json(orient="records")

    def get_last_order(self, id):
        # Get lasts order for one user
        max = self.df.groupby(['CLI_ID'], sort=False)['MOIS_VENTE'].transform('max')
        df_purchases = self.df[(self.df['MOIS_VENTE'] == max)]

        # If multiple columns on month, get the order with max ticket_id
        max = df_purchases.groupby(['TICKET_ID'], sort=False)['TICKET_ID'].transform('max')
        df_purchases = df_purchases[(df_purchases['TICKET_ID'] == max)]
        df_purchases = df_purchases[['TICKET_ID','MOIS_VENTE','PRIX_NET','FAMILLE','UNIVERS','MAILLE','LIBELLE','CLI_ID']]

        return df_purchases[df_purchases['CLI_ID'] == int(id)].to_json(orient="index")

    def get_all_customers(self, search):
        return [customer_id for customer_id in self.customers_id if search in str(customer_id)][:5]
      
    def get_top_categories(self, cat, num):
        cat = cat.upper()
        num = int(num)
        top_cat = self.df[cat].value_counts(dropna=False)[:num]
        self.top_categories = top_cat.to_json(orient="index")
        print(top_cat)
        return self.top_categories
      
    def get_customer_evolution(self):
        return self.df[['MOIS_VENTE','CLI_ID']].groupby(['MOIS_VENTE'])['CLI_ID'].nunique().to_json(orient="records")

    def get_ca_evolution(self):
        return self.df[['MOIS_VENTE','PRIX_NET']].groupby(['MOIS_VENTE']).sum()['PRIX_NET'].to_json(orient="records")
