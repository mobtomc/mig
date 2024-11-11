import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def clean_text(text):
    stop_words = set(stopwords.words("english"))
    stemmer = SnowballStemmer("english")

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Tokenize and clean
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)
