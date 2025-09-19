import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
YAHOO_API_KEY = os.getenv("YAHOO_API_KEY")
CACHE_EXPIRATION = 30  # seconds
