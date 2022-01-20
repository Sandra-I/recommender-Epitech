import pandas as pd
from itertools import permutations
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
from google_api.get_file_from_google import GetFileFromGoogleDrive
class ItemRecommender:
    
    df = pd.DataFrame()
    df_best_item_by_cli = pd.DataFrame()
    df_unique_item = pd.DataFrame()
    pair_counts_df_sorted = pd.DataFrame()
    rfm_cli_article_df = pd.DataFrame()
    df_reset_freq = pd.DataFrame()
    get_file_from_google = GetFileFromGoogleDrive()

    most_buyed_articles = {}
    most_buyed_articles_among_users = {}
    unpersonnalized_recommended_items = []

    def __init__(self):
        self.df = self.get_file_from_google.get_clean_dataframe() 
        self.df_best_item_by_cli = self.get_file_from_google.get_best_item_by_cli_dataframe()
        self.pair_counts_df_sorted = self.get_file_from_google.get_paired_item_dataframe()
        self.df_reset_freq = self.get_file_from_google.get_frequence_item_dataframe()
        self.rfm_cli_article_df = self.get_file_from_google.get_rfm_cli_article_dataframe()
        self.df.head()
    
    def create_unique_item_df(self):
        self.df_unique_item = self.df.drop_duplicates(subset=["LIBELLE"], keep='first')

    def get_most_buyed_articles(self, limitValue):
        most_buyed_articles_df = self.df["LIBELLE"].value_counts().head(3)
        self.most_buyed_articles = most_buyed_articles_df.to_json(orient="index")
        return self.most_buyed_articles

    def get_article_buyed_by_most_users(self, limitValue):
        self.most_buyed_articles_among_users = self.df_best_item_by_cli['Most_Buyed_Article'].value_counts()[:3].to_json(orient="index")
        return self.most_buyed_articles_among_users

    def get_unpersonalized_recommendation(self, limitValue):
        most_buyed_articles = self.get_most_buyed_articles(self)
        most_buyed_articles_among_users = self.get_article_buyed_by_most_users(self)
        self.unpersonnalized_recommended_items.append(most_buyed_articles)
        self.unpersonnalized_recommended_items.append(most_buyed_articles_among_users)
        return self.unpersonnalized_recommended_items

    def get_often_buy_together_articles(self, customerId):
        customer_best_article = self.get_user_most_buyed_articles(customerId)
        customer_best_article_libelle = customer_best_article["LIBELLE"].values[0]
        paired_article = self.pair_counts_df_sorted[self.pair_counts_df_sorted["item_a"] == customer_best_article_libelle][:3]["item_b"].tolist()
        return paired_article

    def get_user_most_buyed_articles(self, customerId):
        return self.df[self.df["LIBELLE"] == self.df_best_item_by_cli[self.df_best_item_by_cli["CLI_ID"] == int(customerId)]["Most_Buyed_Article"].values[0]][:1]

    def get_closest_product_by_customer(self, customerId):

        df_best_item_cli = self.get_user_most_buyed_articles(customerId)
        i = 0.1
        df_close_item = None
        myValue = None
        while(myValue == None):
            df_close_item = self.df_unique_item[(self.df_unique_item["FAMILLE"] == df_best_item_cli["FAMILLE"].values[0]) & (self.df_unique_item["UNIVERS"] == df_best_item_cli["UNIVERS"].values[0]) & (self.df_unique_item["MAILLE"] == df_best_item_cli["MAILLE"].values[0]) & (self.df_unique_item["LIBELLE"] != df_best_item_cli["LIBELLE"].values[0]) & (self.df_unique_item["PRIX_NET"] >= df_best_item_cli["PRIX_NET"].values[0] - i) & (self.df_unique_item["PRIX_NET"] <= df_best_item_cli["PRIX_NET"].values[0] +i)]
            i = i+0.25
            if ( not df_close_item.empty):
                myValue = 1
        closest_product = []
        index = df_close_item.index
        number_of_rows = len(index)
        for j in range (1,number_of_rows):
            if j in df_close_item[:4]["LIBELLE"].values.index:
                closest_product.append(df_close_item[:4]["LIBELLE"].values[j])
        return closest_product

    def get_article_from_similar_client(self, customerId):
        user = self.rfm_cli_article_df[self.rfm_cli_article_df["CLI_ID"] == int(customerId)]
        similar_users = self.rfm_cli_article_df[(self.rfm_cli_article_df["RFM_SEGMENT"] == user["RFM_SEGMENT"].values[0]) & (self.rfm_cli_article_df["Most_Buyed_Article"] == user["Most_Buyed_Article"].values[0])][:3]
        closest_product = []
        for i in range(1,3):
            if i in similar_users.index:
                product_index = self.df_reset_freq[self.df_reset_freq["CLI_ID"] == similar_users.iloc[[i]]["CLI_ID"].values[0]]["Frequence"].nlargest(3).index.values[1]
                closest_product.append(self.df_reset_freq.loc[[product_index]]["Item"].values[0])
        return closest_product
    
    def get_personnalized_recommendation_for_a_user(self, customerId):
        data = {}
        mb = self.get_user_most_buyed_articles(customerId)
        data["most_buyed_article"] = mb["LIBELLE"].values[0]
        of = self.get_often_buy_together_articles(customerId)
        data["paired_articles"] = of
        cl = self.get_closest_product_by_customer(customerId)
        data["similar_product"] = cl
        sm = self.get_article_from_similar_client(customerId)
        data["similar_user_product"] = sm
        return data
