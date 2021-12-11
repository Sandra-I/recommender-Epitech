import pandas as pd
from itertools import permutations
from sklearn.metrics.pairwise import cosine_similarity

class ItemRecommender:
    
    df = pd.DataFrame()
    small_df = pd.DataFrame()
    df_best_item_by_cli = pd.DataFrame()
    df_unique_item = pd.DataFrame()
    pair_counts_df_sorted = pd.DataFrame()
    user_cosine_similarity_df = pd.DataFrame()
    df_reset_freq = pd.DataFrame()

    most_buyed_articles = {}
    most_buyed_articles_among_users = {}
    unpersonnalized_recommended_items = []

    def __init__(self):
        self.df = pd.read_csv("../clean_dataset.csv", parse_dates=True)
        self.small_df = self.df
        self.df.head()

    def create_customer_preferences_df(self):
        self.small_df["Most_Buyed_Article"] = self.small_df.groupby("CLI_ID")['LIBELLE'].transform(lambda x: x.value_counts().idxmax())
        self.df_best_item_by_cli =pd.DataFrame({'Count' : self.small_df.groupby(["CLI_ID"])["Most_Buyed_Article"].value_counts()})
        self.df_best_item_by_cli = self.df_best_item_by_cli.reset_index()
        self.df_best_item_by_cli = self.df_best_item_by_cli[["CLI_ID", "Most_Buyed_Article"]]
    
    def create_unique_item_df(self):
        self.df_unique_item = self.small_df.drop_duplicates(subset=["LIBELLE"], keep='first')

    def create_pairs_df(self):
        def create_pairs(x):
            pairs = pd.DataFrame(list(permutations(x.values,2)), columns=["item_a", "item_b"])
            return pairs    
        df_pairs = self.df_unique_item.groupby("CLI_ID")["LIBELLE"].apply(create_pairs)
        df_pairs = df_pairs.reset_index(drop=True)
        pair_counts = df_pairs.groupby(["item_a",'item_b']).size()
        pair_counts_df = pair_counts.to_frame(name = "size").reset_index()
        self.pair_counts_df_sorted = pair_counts_df.sort_values('size', ascending=False)
        self.pair_counts_df_sorted.to_csv('PairedItem.csv', index=False)
    
    def create_frequence_df(self):
        def frequence_item(x):
            total_achat = x["TICKET_ID"].count()
            freq = x["LIBELLE"].value_counts() / total_achat 
            return freq

        df_freq = self.small_df.groupby("CLI_ID").apply(frequence_item)
        df_freq = df_freq.reset_index()
        df_freq = df_freq.set_index("CLI_ID")
        df_freq = df_freq.rename(columns={"level_1": "Item", "LIBELLE": "Frequence"})
        self.df_reset_freq = df_freq.reset_index()
        user_item_frequence_pivot = df_freq.pivot_table(index="CLI_ID",columns="Item", values="Frequence")
        avg_user_item_freq = user_item_frequence_pivot.mean(axis=1)
        user_item_frequence_pivot = user_item_frequence_pivot.sub(avg_user_item_freq, axis=0)
        user_item_frequence_pivot = user_item_frequence_pivot.fillna(0)
        user_similarities = cosine_similarity(user_item_frequence_pivot)
        self.user_cosine_similarity_df = pd.DataFrame(user_similarities, index=user_item_frequence_pivot.index,columns=user_item_frequence_pivot.index)

    def get_most_buyed_articles(self, limitValue):
        most_buyed_articles_df = self.small_df["LIBELLE"].value_counts().head(3)
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
        customer_best_article_libelle = customer_best_article["Most_Buyed_Article"].values[0]
        paired_article = self.pair_counts_df_sorted[self.pair_counts_df_sorted["item_a"] == customer_best_article_libelle][:3]["item_b"].tolist()
        return paired_article

    def get_user_most_buyed_articles(self, customerId):
        return self.small_df[self.small_df["LIBELLE"] == self.df_best_item_by_cli[self.df_best_item_by_cli["CLI_ID"] == customerId]["Most_Buyed_Article"].values[0]][:1]

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

            closest_product.append(df_close_item[:4]["LIBELLE"].values[j])
        return closest_product

    def get_article_from_similar_client(self, customerId):
        user_cosine_similarity_series = self.user_cosine_similarity_df.loc[customerId]
        user_ordered_similarities = user_cosine_similarity_series.sort_values(ascending=False)
        similar_customer_id = user_ordered_similarities[:2].index[1]
        similar_user_product=  self.get_user_most_buyed_articles(similar_customer_id)
        if (similar_user_product["LIBELLE"].values[0] == self.get_user_most_buyed_articles(similar_customer_id)["LIBELLE"].values[0]):
            similar_user_product = self.df_reset_freq[self.df_reset_freq["CLI_ID"] == similar_customer_id][:2].values[1][1]
            return similar_user_product
        return similar_user_product["LIBELLE"].values[0]

    
    def get_personnalized_recommendation_for_a_user(self, customerId):
        zeub = {}
        of = self.get_often_buy_together_articles(customerId)
        zeub["Acheté fréquemment ensemble :"] = of
        
      
        cl = self.get_closest_product_by_customer(customerId)
        zeub["Produits similaires :"] = cl
        sm = self.get_article_from_similar_client(customerId)
        zeub["des utilisateurs similaires ont également acheté :"] = sm
        
        return zeub
