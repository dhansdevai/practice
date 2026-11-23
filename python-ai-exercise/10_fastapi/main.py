from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the GOOGLE_API_KEY from the .env file so we can call Gemini.
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# This one line creates our web app. We will hang all our endpoints on it.
app = FastAPI()


# -------------------------------------------------------------------
# Part 3: our first endpoint (a simple GET)
# Open http://127.0.0.1:8000/ in the browser to see this.
# -------------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Welcome, Kaise ho aap?"}


# -------------------------------------------------------------------
# Part 4: an endpoint with inputs (query parameters)
# Try: http://127.0.0.1:8000/margin?revenue=5000&expenses=3000
# Notice the type hints (revenue: float). FastAPI uses them to read the
# inputs from the URL and turn the text into numbers for us.
# -------------------------------------------------------------------
@app.get("/margin")
def margin(revenue: float, expenses: float):
    profit = revenue - expenses
    margin_percent = (profit / revenue) * 100
    return {"profit": profit, "margin_percent": margin_percent}


# -------------------------------------------------------------------
# Part 5 + 6: a POST endpoint that calls the AI
# The user sends a review, we ask Gemini for the sentiment, and we send
# back a small, clean result. Low output = few tokens used.
# -------------------------------------------------------------------

# What the user must SEND us (the request body)
class Review(BaseModel):
    text: str


# What Gemini must give back, and what we SEND to the user (the response)
class Sentiment(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)


@app.post("/sentiment")
def analyze_sentiment(review: Review):
    response = model.with_structured_output(Sentiment).invoke(
        f"Find the sentiment of this customer review. "
        f"label must be 'positive', 'negative', or 'neutral'. "
        f"score must be a number from 1 (very bad) to 5 (very good). "
        f"Review: {review.text}"
    )
   
    return response
