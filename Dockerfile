FROM python:3.11-slim

WORKDIR /app

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Add cron job (runs 3x/day)
RUN echo "0 8,13,19 * * * cd /app && /usr/bin/python3 backend/run_scheduled_tasks.py >> /app/cron.log 2>&1" > /etc/cron.d/news_cron
RUN chmod 0644 /etc/cron.d/news_cron
RUN crontab /etc/cron.d/news_cron

# Ensure data folder exists (for SQLite)
RUN mkdir -p /app/data

# Entrypoint
CMD python backend/init_db.py && cron && streamlit run app.py --server.port 8501 --server.address 0.0.0.0
