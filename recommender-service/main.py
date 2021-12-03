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
    return { "data": customer_segmenter.get_customer_RFM()}
