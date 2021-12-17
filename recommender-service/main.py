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
    item_recommender.create_unique_item_df()

@app.get("/customers")
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

@app.get("/all/{id}")
def get_all(id):
    return {"data": item_recommender.get_personnalized_recommendation_for_a_user(id)}

@app.get("/{cat}")
def get_customers_data_by_category(cat):
    return { "data": customer_segmenter.get_customers_by_category(cat) }

@app.get("/counts/{cat}")
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_by_category(cat) }

@app.get("/counts_by_customer/{cat}")
def get_counts_by_category(cat):
    return { "data": customer_segmenter.get_counts_category_by_customer(cat) }

@app.get("/average_basket")
def get_average_basket():
    return { "data": customer_segmenter.get_average_basket() }
    
@app.get("/average_basket/{id}")
def get_average_basket_by_client(id):
    return { "data": customer_segmenter.get_average_basket_by_client(id) }
