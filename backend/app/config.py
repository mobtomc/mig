import os

class Config:
    API_KEY = os.getenv("COHERE_API_KEY", "XeZs7zzD4D2pwTNGuwO6sVn2l3OzttLqiWrVGdMu")

config = Config()
