# CAGR Scraper Walkthrough

## Application Overview
This application calculates the Compound Annual Growth Rate (CAGR) for stocks and currencies using a Dollar Cost Averaging (DCA) strategy simulation. It fetches historical data from Yahoo Finance and computes the return as if you invested a fixed amount every month.

## How to Run it
1.  **Dependencies**: Ensure you have Python installed. You can install the required libraries with:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Start the Server**: Open a terminal in the project directory and run:
    ```bash
    python app.py
    ```
3.  **Access the App**: Open your web browser and navigate to `http://localhost:3000`.

## How to Stop it
1.  Go back to the terminal where the app is running.
2.  Press `Ctrl + C` on your keyboard. This will terminate the server.


## User Interface
### Input Page
- Enter tickers (e.g., `AAPL`, `FUTU`, `GOOG`) or company names in the text area.
- Separate multiple entries with commas or new lines.
- Click "Calculate CAGR".

### Results Page
- Displays a table with:
    - **Ticker**: The symbol used.
    - **Start Date**: The date of the first available data point.
    - **End Date**: The date of the most recent data point.
    - **Start Value**: Adjusted Close price on the start date (for reference).
    - **Final Value**: Adjusted Close price on the end date (for reference).
    - **Years (N)**: Duration in years.
    - **CAGR**: The calculated growth rate percentage.
- Positive CAGR is shown in green, negative in red.

## Technical Details: DCA Calculation
The app simulates a monthly investment strategy:
1.  **Data Source**: Fetches "Max" available history with "1mo" (monthly) intervals using `yfinance`.
2.  **Price**: Uses `Adj Close` (Adjusted Close) price.
3.  **Simulation**:
    - Assumes a fixed investment (e.g., 1 unit) is made every month.
    - **PV (Total Invested)**: Total number of months * 1.
    - **Shares Accumulated (sh)**: Sum of `(1 / Price_i)` for all months `i`.
    - **FV (Final Value)**: Total Shares Accumulated * Final Price.
4.  **Formula**:
    - `CAGR = ((FV / PV)^(1/N) - 1) * 100%`
    - where `N` is the number of years.
