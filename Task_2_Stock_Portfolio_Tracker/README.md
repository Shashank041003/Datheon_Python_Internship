Stock Portfolio Performance Tracker
Project Overview
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
Stock_Portfolio_Tracker/
├── portfolio_summary.csv
├── protfolio.py
├── README.md
└── S&P 500 TICKER DATASETS.csv
```

## How to Run

### Step 1: Install Python
Make sure Python 3 is installed on your system.

### Step 2: Download the Project
Download or clone this repository to your computer.

### Step 3: Run the Program
Open the project folder in VS Code and run:

```bash
python portfolio.py
```

### Step 4: Enter Stock Details
Enter the stock ticker symbol, purchase price, number of shares, and current stock price.

To finish entering stocks, type:

```text
DONE
```

## Sample Output
```text
Total Investment: $1,500.00
Current Portfolio Value: $1,800.00
Total Profit/Loss: $300.00
Overall Gain/Loss: 20.00%
```

## CSV Output
The program automatically generates a `portfolio_summary.csv` file containing:
- Date and time
- Stock ticker symbol
- Company name
- Purchase price
- Quantity
- Current price
- Investment amount
- Market value
- Profit or loss
- Gain or loss percentage

## Author
Shashank Tiwari
