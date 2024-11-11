from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    try:
        # Check if the input is a string, as required by the pipeline
        if isinstance(text, str):
            # Ensure the input text is not too long for the model
            result = sentiment_pipeline(text, truncation=True)
            
            # Extract the label and score
            sentiment = result[0]["label"]  # "POSITIVE" or "NEGATIVE"
            score = result[0]["score"]      # Confidence score

            return {"sentiment": sentiment, "confidence": score}
        else:
            raise ValueError("Input must be a string.")
    
    except Exception as e:
        return {"error": f"An error occurred during sentiment analysis: {str(e)}"}
