from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def calculate_cagr(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="max", interval="1mo")
        
        if hist.empty:
            search_results = yf.Search(ticker_symbol, news_count=0).quotes
            if search_results:
                first_result = search_results[0]
                ticker_symbol = first_result['symbol']
                ticker = yf.Ticker(ticker_symbol)
                hist = ticker.history(period="max", interval="1mo")
            
            if hist.empty:
                return {"ticker": ticker_symbol, "error": "No data found"}

        start_date = hist.index[0]
        end_date = hist.index[-1]
        
        n_years = (end_date - start_date).days / 365.25
        
        if n_years <= 0:
             return {"ticker": ticker_symbol, "error": "Insufficient data duration"}

        
        price_col = 'Close'
        if 'Adj Close' in hist.columns:
            price_col = 'Adj Close'

        starting_value = hist.iloc[0][price_col]
        final_value = hist.iloc[-1][price_col]
        
        if starting_value == 0:
            return {"ticker": ticker_symbol, "error": "Starting value is 0"}

        # CAGR formula: (Final Value / Starting Value) ^ (1/N) - 1
        cagr = (final_value / starting_value) ** (1 / n_years) - 1
        
        return {
            "ticker": ticker_symbol,
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "starting_value": round(starting_value, 2),
            "final_value": round(final_value, 2),
            "years": round(n_years, 2),
            "cagr": round(cagr * 100, 2) # %
        }
        
    except Exception as e:
        return {"ticker": ticker_symbol, "error": str(e)}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_text = request.form.get('tickers')
    if not input_text:
         return render_template('index.html', error="Please enter tickers")
    
    tickers = [t.strip() for t in input_text.replace('\n', ',').split(',') if t.strip()]
    
    results = []
    for t in tickers:
        results.append(calculate_cagr(t))
        
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
