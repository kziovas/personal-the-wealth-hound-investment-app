from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    base_currency = Column(String, default="USD")

    # Required investment preferences
    target_return_pct = Column(Float, nullable=False)  # desired annual return %
    risk_tolerance = Column(String, nullable=False)  # low, medium, high

    # Optional investment preferences for AI assistant
    segments_of_interest = Column(Text, nullable=True)  # e.g., 'crypto, stocks'
    investing_comments = Column(Text, nullable=True)  # other notes by user
    investment_horizon_years = Column(
        Integer, nullable=True
    )  # optional: investment duration
    liquidity_preference = Column(String, nullable=True)  # low, medium, high
    ethics_preferences = Column(Text, nullable=True)  # e.g., ESG, green investments

    portfolios = relationship("Portfolio", back_populates="owner")


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="portfolios")
    assets = relationship("Asset", back_populates="portfolio")


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    content = Column(String, nullable=False)

    asset = relationship("Asset", back_populates="news_items")


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    name = Column(String, nullable=False)
    invested_amount = Column(Float, nullable=False)
    invested_currency = Column(String, nullable=False)
    invested_price = Column(Float, nullable=False)
    date_bought = Column(DateTime, default=datetime.utcnow)
    note = Column(Text, nullable=True)  # optional notes about this asset

    news_items = relationship(
        "News", back_populates="asset", cascade="all, delete-orphan"
    )
    portfolio = relationship("Portfolio", back_populates="assets")
