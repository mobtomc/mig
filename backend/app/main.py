from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.core.scraping import scrape_site
from app.core.sentiment_analysis import analyze_sentiment
from app.core.suggestions import get_improvement_suggestions

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Site Scribe"}

@app.post("/scrape/")
async def scrape(request: Request):
    try:
        body = await request.json()
        url = body.get("url")
        
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")
        
        data = scrape_site(url)
        
        if not data or (not data.get("headlines") and not data.get("paragraphs")):
            raise HTTPException(status_code=404, detail="No content found for the provided URL")
        
        # Combine headlines and paragraphs into a single text
        headlines_text = " ".join(data.get("headlines", []))
        paragraphs_text = " ".join(data.get("paragraphs", []))
        full_text = f"{headlines_text} {paragraphs_text}".strip()
        
        if not full_text:
            raise HTTPException(status_code=404, detail="No text content found for the provided URL")
        
        return {"data": full_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while scraping: {str(e)}")

@app.post("/analyze/")
async def analyze(request: Request):
    try:
        body = await request.json()
        data = body.get("data")
        
        if not data or not isinstance(data, str):
            raise HTTPException(status_code=400, detail="Text data is required and must be a string")
        
        sentiment_results = analyze_sentiment(data)
        
        return sentiment_results
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during sentiment analysis: {str(e)}")

@app.post("/suggestions/")
async def suggestions(request: Request):
    try:
        body = await request.json()
        data = body.get("data")
        
        if not data:
            raise HTTPException(status_code=400, detail="Text data is required")
        
        improvements = get_improvement_suggestions(data)
        
        return improvements
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while getting suggestions: {str(e)}")
