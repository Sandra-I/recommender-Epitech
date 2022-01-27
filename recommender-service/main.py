from pydantic.main import BaseModel
from customer_segmenter import CustomerSegmenter
from item_recommender import ItemRecommender
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://recommender-31.herokuapp.com"
]

tags_metadata = [
    {
        "name": "RFM",
        "description": "Calcul la récence, fréquence et le montant des achats des clients. Permet de calculer le taux de rétention",
    },
    {
        "name": "RECOMMENDER",
        "description": "Permet d'obtenir quatre types de recommandations, en fonction de l'id du client. Les types de reco : 1. Achetés fréquemment ensemble. 2. Produits similaires. 3. Produits d'utilisateurs similaires. 4. Articles les plus achetés sur le site."
    },
{
        "name": "CATEGORY",
        "description": "Permet d'obtenir le top souhaité dans la catégorie donnée."
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


customer_segmenter = CustomerSegmenter()
item_recommender = ItemRecommender()

@app.on_event("startup")
async def startup_event():
    customer_segmenter.create_customer_clusters()
    item_recommender.create_unique_item_df()

@app.get("/")
def welcome():
    return { "data": "Welcome in our system! What do you want?" }

@app.get("/all_customers/{search}", tags=["RFM"])
def get_all_customers(search):
    return { "data": customer_segmenter.get_all_customers(search) }

@app.get("/last_order/{id}", tags=["RFM"])
def get_last_order(id):
    return { "data": customer_segmenter.get_last_order(id) }

@app.get("/customers_details/{id}", tags=["RFM"])
def get_customer_details_in_csv(id):
    return { "data": customer_segmenter.get_customer_details_in_csv(id) }

@app.get("/get_top_categories/{cat}/{num}", tags=["CATEGORY"])
def get_top_categories(cat, num):
    return { "data": customer_segmenter.get_top_categories(cat, num) }

@app.get("/all/{id}", tags=["RECOMMENDER"])
def get_all_personalized_recommendation_for_a_user(id):
    return {"data": item_recommender.get_personnalized_recommendation_for_a_user(id)}

# TO HIDE
# include_in_schema=False : permets de spécifier de ne pas prendre en compte l'endpoint pour la doc
@app.get("/customers", tags=["RFM"], include_in_schema=False)
def get_customer_segmentation():
    return { "data": customer_segmenter.get_customer_RFM() }
  
@app.get("/counts/{cat}", tags=["RFM"])
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_by_category(cat) }

@app.get("/customers_details_too_long/{id}", include_in_schema=False)
def get_details_by_customer(id):
    return { "data": customer_segmenter.get_details_by_customer(id) }

@app.get("/average_basket/{id}", include_in_schema=False)
def get_average_basket_by_client(id):
    return { "data": customer_segmenter.get_average_basket_by_client(id) }

@app.get("/recency/{id}", include_in_schema=False)
def get_recency_by_customer(id):
    return { "data": customer_segmenter.get_recency_by_customer(id) }

@app.get("/recency_group/{id}", tags=["RFM"], include_in_schema=False)
def get_recency_group_by_customer(id):
    return { "data": customer_segmenter.get_recency_group_by_customer(id) }

@app.get("/frequency/{id}", include_in_schema=False)
def get_frequency_by_customer(id):
    return { "data": customer_segmenter.get_frequency_by_customer(id) }

@app.get("/frequency_group/{id}", tags=["RFM"], include_in_schema=False)
def get_frequency_group_by_customer(id):
    return { "data": customer_segmenter.get_frequency_group_by_customer(id) }

@app.get("/generate_csv_customer_details", include_in_schema=False)
def generate_csv_details():
    return { "data": customer_segmenter.generate_csv_details() }

@app.get("/average_basket", tags=["RFM"], include_in_schema=False)
def get_average_basket():
    return { "data": customer_segmenter.get_average_basket() }  

@app.get("/recency_group", tags=["RFM"], include_in_schema=False)
def get_recency_group():
    return { "data": customer_segmenter.get_recency_group() }

@app.get("/frequency_group", tags=["RFM"], include_in_schema=False)
def get_frequency_group_repartition():
    return { "data": customer_segmenter.get_frequency_group_repartition() }

@app.get("/frequency", tags=["RFM"], include_in_schema=False)
def get_mean_frequency():
    return { "data": customer_segmenter.get_mean_frequency() }

@app.get("/counts/{cat}", tags=["RFM"], include_in_schema=False)
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_by_category(cat) }

@app.get("/counts_by_customer/{cat}", tags=["RFM"], include_in_schema=False)
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_category_by_customer(cat) }

@app.get("/unrecommendedArticles", tags=["RECOMMENDER"])
def get_most_buyed_articles():
    return { "data": item_recommender.get_unpersonalized_recommendation(10)}

@app.get("/pairedArticles/{id}", include_in_schema=False)
def get_paired_articles(id):
    return {"data": item_recommender.get_often_buy_together_articles(id)}

@app.get("/closestArticle/{id}", include_in_schema=False)
def get_closest_article(id):
    return {"data": item_recommender.get_closest_product_by_customer(id)}

@app.get("/neighborMostBuyedArticle/{id}", include_in_schema=False)
def get_article_from_closest_customer(id):
    return {"data": item_recommender.get_article_from_similar_client(id)}

@app.get("/most_buyed_product_of_an_user/{id}", tags=["RECOMMENDER"], include_in_schema=False)
def get_most_buyed_product_of_an_user(id):
    return {"data": item_recommender.get_user_most_buyed_articles(id)}

@app.get("/generate_csv_global", tags=["RFM"])
def generate_csv_global():
    return { "data": customer_segmenter.generate_csv_global() }

@app.get("/global_metrics", tags=["RFM"])
def get_global_metrics():
    return { "data": customer_segmenter.get_global_metrics_csv() }

@app.get("/get_top_categories/{cat}/{num}", tags=["CATEGORY"])
def get_top_categories(cat, num):
    return { "data": customer_segmenter.get_top_categories(cat, num) }

@app.get("/last_order/{id}", tags=["SALE"])
def get_last_order(id):
    return { "data": customer_segmenter.get_last_order(id) }

@app.get("/customer_evolution", tags=["SALE"])
def get_customer_evolution():
    return { "data": customer_segmenter.get_customer_evolution() }

@app.get("/ca_evolution", tags=["SALE"])
def get_ca_evolution():
    return { "data": customer_segmenter.get_ca_evolution() }
