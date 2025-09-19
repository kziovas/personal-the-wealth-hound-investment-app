import logging
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend.models import Asset, News


def fetch_news_for_asset(asset: Asset) -> List[str]:
    """
    Fetch news for a given asset.
    CURRENTLY: Returns a fixed placeholder string.
    FUTURE: Replace this with real news fetching / AI aggregation.

    Parameters:
    - asset: Asset ORM object

    Returns:
    - List of news strings
    """
    # Placeholder for now
    return [f"All is good for {asset.name}"]


def save_news_for_all_assets():
    """
    Scheduled task: fetch news for all assets and store in DB.
    Runs three times a day (hardcoded).
    """
    db: Session = SessionLocal()
    try:
        assets = db.query(Asset).all()
        for asset in assets:
            news_items = fetch_news_for_asset(asset)
            for news_text in news_items:
                news_entry = News(
                    asset_id=asset.id, timestamp=datetime.now(), content=news_text
                )
                db.add(news_entry)
        db.commit()
        logging.info(f"Saved news for {len(assets)} assets.")
    finally:
        db.close()


def get_latest_news(asset_id: int) -> str:
    """
    Retrieve the most recent news for a given asset from the DB.

    Parameters:
    - asset_id: int

    Returns:
    - str: Latest news content or placeholder if none exists
    """
    db: Session = SessionLocal()
    try:
        news_entry = (
            db.query(News)
            .filter(News.asset_id == asset_id)
            .order_by(News.timestamp.desc())
            .first()
        )
        if news_entry:
            return news_entry.content
        else:
            return "No news available yet."
    finally:
        db.close()
