from pydantic.main import BaseModel
from customer_segmenter import CustomerSegmenter
from item_recommender import ItemRecommender
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000"
]

app = FastAPI()

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
    #item_recommender.create_customer_preferences_df()
    #item_recommender.create_unique_item_df()
    #item_recommender.create_pairs_df()
    #item_recommender.create_frequence_df()

@app.get("/customers")
def get_customer_segmentation():
    return { "data": customer_segmenter.get_customer_RFM()}

@app.get("/unrecommendedArticles")
def get_most_buyed_articles():
    return { "data": item_recommender.get_unpersonalized_recommendation(10)}

@app.get("/pairedArticles")
def get_paired_articles():
    return {"data": item_recommender.get_often_buy_together_articles(1490281)}

@app.get("/closestArticle")
def get_closest_article():
    return {"data": item_recommender.get_closest_product_by_customer(1490281)}

@app.get("/neighborMostBuyedArticle")
def get_article_from_closest_customer():
    return {"data": item_recommender.get_article_from_similar_client(1490281)}

@app.get("/all")
def get_all():
    return {"data": item_recommender.get_personnalized_recommendation_for_a_user(1490281)}

@app.get("/{cat}")
def get_customers_data_by_category(cat):
    return { "data": customer_segmenter.get_customers_by_category(cat)}

@app.get("/counts/{cat}")
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_by_category(cat)}

@app.get("/counts_by_customer/{cat}")
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_category_by_customer(cat)}
