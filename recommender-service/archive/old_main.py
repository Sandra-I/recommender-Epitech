from pydantic.main import BaseModel
from customer_segmenter import CustomerSegmenter
from item_recommender import ItemRecommender
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",
    "http://localhost:8080"
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

@app.get("/customers", tags=["RFM"])
def get_customer_segmentation():
    return { "data": customer_segmenter.get_customer_RFM() }

@app.get("/unrecommendedArticles")
def get_most_buyed_articles():
    return { "data": item_recommender.get_unpersonalized_recommendation(10)}

@app.get("/pairedArticles/{id}")
def get_paired_articles(id):
    return {"data": item_recommender.get_often_buy_together_articles(id)}

@app.get("/closestArticle/{id}")
def get_closest_article(id):
    return {"data": item_recommender.get_closest_product_by_customer(id)}

@app.get("/neighborMostBuyedArticle/{id}")
def get_article_from_closest_customer(id):
    return {"data": item_recommender.get_article_from_similar_client(id)}

@app.get("/most_buyed_product_of_an_user/{id}", tags=["RECOMMENDER"])
def get_most_buyed_product_of_an_user(id):
    return {"data": item_recommender.get_user_most_buyed_articles(id)}

# to keep
@app.get("/all/{id}", tags=["RECOMMENDER"])
def get_all_personalized_recommendation_for_a_user(id):
    return {"data": item_recommender.get_personnalized_recommendation_for_a_user(id)}

@app.get("/counts/{cat}", tags=["RFM"])
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_by_category(cat) }

@app.get("/counts_by_customer/{cat}", tags=["RFM"])
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_category_by_customer(cat) }

@app.get("/average_basket", tags=["RFM"])
def get_average_basket():
    return { "data": customer_segmenter.get_average_basket() }
    
@app.get("/average_basket/{id}", tags=["RFM"])
def get_average_basket_by_client(id):
    return { "data": customer_segmenter.get_average_basket_by_client(id) }

@app.get("/recency_group", tags=["RFM"])
def get_recency_group():
    return { "data": customer_segmenter.get_recency_group() }

@app.get("/recency_group/{id}", tags=["RFM"])
def get_recency_group_by_customer(id):
    return { "data": customer_segmenter.get_recency_group_by_customer(id) }

@app.get("/frequency_group", tags=["RFM"])
def get_frequency_group_repartition():
    return { "data": customer_segmenter.get_frequency_group_repartition() }

@app.get("/frequency_group/{id}", tags=["RFM"])
def get_frequency_group_by_customer(id):
    return { "data": customer_segmenter.get_frequency_group_by_customer(id) }

@app.get("/frequency", tags=["RFM"])
def get_mean_frequency():
    return { "data": customer_segmenter.get_mean_frequency() }

@app.get("/recency/{id}", tags=["RFM"])
def get_recency_by_customer(id):
    return { "data": customer_segmenter.get_recency_by_customer(id) }

@app.get("/frequency/{id}", tags=["RFM"])
def get_frequency_by_customer(id):
    return { "data": customer_segmenter.get_frequency_by_customer(id) }

# to keep
@app.get("/all_customers/{search}", tags=["RFM"])
def get_all_customers(search):
    return { "data": customer_segmenter.get_all_customers(search) }

# @app.get("/customers_details/{id}", tags=["RFM"])
# def get_details_by_customer(id):
#     return { "data": customer_segmenter.get_details_by_customer(id) }

# to keep
@app.get("/last_order/{id}", tags=["RFM"])
def get_last_order(id):
    return { "data": customer_segmenter.get_last_order(id) }

# to keep
@app.get("/customers_details/{id}", tags=["RFM"])
def get_customer_details_in_csv(id):
    return { "data": customer_segmenter.get_customer_details_in_csv(id) }

@app.get("/generate_csv_customer_details", tags=["RFM"])
def generate_csv_details():
    return { "data": customer_segmenter.generate_csv_details() }

# to keep
@app.get("/get_top_categories/{cat}/{num}", tags=["CATEGORY"])
def get_top_categories(cat, num):
    return { "data": customer_segmenter.get_top_categories(cat, num) }