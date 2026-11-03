# Stock Portfolio Performance Tracker

## Project Overview

The Stock Portfolio Performance Tracker is a Python-based application that helps users track their stock investments and calculate portfolio performance.

Users can enter stock ticker symbols, purchase prices, share quantities, and current stock prices. The program calculates total investment, current portfolio value, profit or loss, and percentage gain or loss.

The transaction summary is automatically saved to a CSV file for future reference.

## Features

- Stock ticker validation using an S&P 500 dataset
- Input of stock purchase price and share quantity
- Calculation of total investment
- Calculation of current portfolio value
- Calculation of individual stock profit or loss
- Calculation of overall portfolio performance
- Automatic CSV logging of portfolio data
- Input validation for numeric values

## Technologies Used

- Python 3
- CSV Module
- File Handling
- Datetime Module

## Project Structure

```text
Task_2_Stock_Portfolio_Tracker/
├── portfolio.py
├── S&P 500 TICKER DATASETS.csv
├── portfolio_summary.csv
└── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the Task_2_Stock_Portfolio_Tracker folder in a terminal.
4. Run the following command:

```bash
python portfolio.py
```

5. Enter the requested stock ticker, purchase price, quantity, and current price.

## Sample Calculation

- Stock Symbol: AAPL
- Purchase Price: $150
- Shares: 10
- Current Price: $180
- Total Investment: $1,500
- Current Portfolio Value: $1,800
- Profit: $300
- Gain: 20%

## Output

The portfolio summary is saved automatically in `portfolio_summary.csv`.

## Author

Shashank Tiwari

