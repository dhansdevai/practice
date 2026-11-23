"""
The backend: a small FastAPI service that analyzes ONE customer review.

Run it with:
    uv run fastapi dev api.py

Then the Streamlit app (app.py) will call this service for every review.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

app = FastAPI()


# What the caller must SEND us
class Review(BaseModel):
    text: str


# What Gemini gives back, and what we SEND to the caller.
# We keep it small on purpose -> fewer tokens used.
class Analysis(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)
    theme: str   # one word: what the review is mainly about (e.g. "delivery")


@app.post("/analyze")
def analyze(review: Review):
    response = model.with_structured_output(Analysis).invoke(
        f"Analyze this customer review. "
        f"label must be 'positive', 'negative', or 'neutral'. "
        f"score must be a number from 1 (very bad) to 5 (very good). "
        f"theme must be ONE lowercase word for the main topic "
        f"(for example: delivery, taste, price, service, quality). "
        f"Review: {review.text}"
    )
    return response
