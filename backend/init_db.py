# backend/init_db.py
import os

from backend.db import Base, engine
from backend.models import *

# Ensure data folder exists (for SQLite)
os.makedirs("data", exist_ok=True)

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")
