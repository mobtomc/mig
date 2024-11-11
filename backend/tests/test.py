import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

# Initialize TestClient
client = TestClient(app)

# Test 1: Check if the root endpoint is working
def test_root():
    response = client.get("/")
    assert response.status_code == 200  # Expect a 200 OK response
    assert response.json() == {"message": "Hello World"}  # Assuming this is what your root returns

# Test 2: Check if the scrape endpoint is working
def test_scrape():
    # Replace with a valid URL for testing
    url = "https://www.example.com"
    response = client.post("/scrape/", json={"url": url})  # Assuming the endpoint is POST /scrape/
    
    # Check the response status code
    assert response.status_code == 200

    # Ensure response contains expected fields (adjust this to your actual response structure)
    data = response.json()
    assert "title" in data
    assert "content" in data
    assert "summary" in data

# Test 3: Test sentiment analysis
def test_sentiment_analysis():
    # Assuming you are passing a text for sentiment analysis
    text_data = {
        "text": "I love programming, it's so fun!"
    }
    
    response = client.post("/analyze/", json=text_data)  # Assuming this is the sentiment analysis endpoint

    assert response.status_code == 200
    assert "sentiment" in response.json()  # Ensure that the response includes sentiment

# Test 4: Test if suggestions are working
def test_suggestions():
    # Test for site improvement suggestions
    url = "https://www.example.com"
    response = client.post("/suggestions/", json={"url": url})  # Assuming the endpoint is POST /suggestions/
    
    assert response.status_code == 200
    suggestions = response.json()
    assert isinstance(suggestions, list)  # Assuming the suggestions are returned as a list
    assert len(suggestions) > 0  # Check if there are any suggestions

# Test 5: Check if SEO suggestions are returned correctly
def test_seo_suggestions():
    url = "https://www.bbc.com"
    response = client.post("/seo/", json={"url": url})  # Assuming this is the SEO suggestions endpoint
    
    assert response.status_code == 200
    seo_suggestions = response.json()
    assert isinstance(seo_suggestions, list)
    assert len(seo_suggestions) > 0  # Check if suggestions exist

