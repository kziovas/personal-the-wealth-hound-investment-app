#!/usr/bin/env python3
"""
Runner script to execute scheduled tasks like fetching news.
This script can be called by cron or a scheduler.
"""

import logging
from datetime import datetime

from backend.news_logic import save_news_for_all_assets

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info(f"Scheduled task started at {datetime.now()}")
    save_news_for_all_assets()
    logging.info(f"Scheduled task finished at {datetime.now()}")
