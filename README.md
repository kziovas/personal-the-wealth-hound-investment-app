# The Wealth Hound 🐶💰  

**The Wealth Hound** is your loyal AI-powered portfolio companion, helping you track stocks and ETFs across currencies.  
Stay on top of performance, news, and new opportunities with smart agents that work for you around the clock.  

---

## ✨ Features  

- **User Accounts**  
  Create an account with your name, email, and base currency (e.g., EUR, USD, GBP).  

- **Portfolio Management**  
  Add stocks, ETFs, or other assets with their ticker, quantity, currency, and invested amount.  
  The app automatically calculates average purchase prices (if not entered) and tracks profit/loss.  

- **Multi-Currency Support**  
  Assets can be in different currencies — the app shows returns both in the asset’s own currency and your chosen base currency using live FX rates.  

- **News Agent** 📰  
  Runs three times daily (morning, midday, evening) and collects the latest news and analyst updates for your portfolio holdings. News is stored so you can review past updates per asset.  

- **Discovery Agent** 🔎  
  Suggests similar, fundamentally solid companies (not hype stocks) from different market segments, tailored to your portfolio.  

- **Persistent Storage**  
  Uses SQLite for a lightweight, self-contained database to ensure your data and news aren’t lost when the app closes.  

- **Modern UI**  
  Clean and simple Streamlit interface for an easy and intuitive experience.  

- **Custom Icon** 🐕💼  
  A minimalist beagle with sunglasses and a dollar-sign tie represents your financial hound.  

---

## 🚀 Getting Started  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-username/the-wealth-hound.git
   cd the-wealth-hound
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run beagle_investor_streamlit.py
   ```

4. Open your browser at `http://localhost:8501`

 ---

## 🐾 Deployment  

Deployment is designed to be simple and portable.  
We will provide a **Docker Compose setup** so you can spin up the entire app (Streamlit + database) in one command.  

*(Docker instructions will be added soon!)*  

---

## 📌 Roadmap  

- [ ] Add real news API integration (e.g., NewsAPI)  
- [ ] Improve similarity agent with fundamentals analysis  
- [ ] Docker Compose deployment scripts  
- [ ] Optional charts and analytics dashboard  

---

## 📄 License  

MIT License – free to use and modify. 
