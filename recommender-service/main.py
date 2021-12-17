from pydantic.main import BaseModel
from customer_segmenter import CustomerSegmenter
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


@app.on_event("startup")
async def startup_event():
    customer_segmenter.create_customer_clusters()

@app.get("/customers")
def get_customer_segmentation():
    return { "data": customer_segmenter.get_customer_RFM() }

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
