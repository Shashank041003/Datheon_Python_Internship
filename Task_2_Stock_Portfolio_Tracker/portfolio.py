import csv
import os
from datetime import datetime

DATASET_FILE = "S&P 500 TICKER DATASETS.csv"
SUMMARY_FILE = "portfolio_summary.csv"


# Load valid stock ticker symbols
def load_tickers():
    tickers = {}

    try:
        with open(DATASET_FILE, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row["Symbol"].strip().upper()
                company = row["Security"].strip()
                tickers[symbol] = company

    except FileNotFoundError:
        print("Dataset file not found!")

    return tickers


# Get valid positive number
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Get valid share quantity
def get_quantity(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")


# Save portfolio data to CSV
def save_to_csv(records):
    file_exists = os.path.isfile(SUMMARY_FILE)

    fields = [
        "Date",
        "Symbol",
        "Company",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Investment",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss Percent"
    ]

    with open(SUMMARY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerows(records)


# Main program
def main():
    print("\n===================================")
    print(" STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("===================================")

    tickers = load_tickers()

    if not tickers:
        print("Unable to load stock dataset.")
        return

    portfolio = []

    while True:
        symbol = input(
            "\nEnter stock ticker (or DONE to finish): "
        ).strip().upper()

        if symbol == "DONE":
            break

        if symbol not in tickers:
            print("Invalid ticker. Please enter a valid S&P 500 ticker.")
            continue

        company = tickers[symbol]

        print("Company:", company)

        buy_price = get_number("Enter purchase price per share: ")
        quantity = get_quantity("Enter number of shares: ")
        current_price = get_number("Enter current stock price: ")

        investment = buy_price * quantity
        market_value = current_price * quantity

        profit_loss = market_value - investment
        percentage = (profit_loss / investment) * 100

        stock = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Symbol": symbol,
            "Company": company,
            "Buy Price": buy_price,
            "Quantity": quantity,
            "Current Price": current_price,
            "Investment": investment,
            "Market Value": market_value,
            "Profit/Loss": profit_loss,
            "Gain/Loss Percent": percentage
        }

        portfolio.append(stock)

        print("\nStock added successfully!")
        print(f"Investment: ${investment:,.2f}")
        print(f"Market Value: ${market_value:,.2f}")
        print(f"Profit/Loss: ${profit_loss:,.2f}")
        print(f"Gain/Loss: {percentage:.2f}%")

    if not portfolio:
        print("\nNo stocks added.")
        return

    # Calculate overall portfolio performance
    total_investment = sum(
        stock["Investment"] for stock in portfolio
    )

    total_value = sum(
        stock["Market Value"] for stock in portfolio
    )

    total_profit = total_value - total_investment

    total_percentage = (
        total_profit / total_investment
    ) * 100

    # Display portfolio summary
    print("\n===================================")
    print("       PORTFOLIO SUMMARY")
    print("===================================")

    print(f"Total Investment: ${total_investment:,.2f}")
    print(f"Current Portfolio Value: ${total_value:,.2f}")
    print(f"Total Profit/Loss: ${total_profit:,.2f}")
    print(f"Overall Gain/Loss: {total_percentage:.2f}%")

    print("\nIndividual Stock Performance:")

    for stock in portfolio:
        print(
            f"{stock['Symbol']} | "
            f"P/L: ${stock['Profit/Loss']:,.2f} | "
            f"{stock['Gain/Loss Percent']:.2f}%"
        )

    # Log results to CSV
    save_to_csv(portfolio)

    print("\nPortfolio summary saved to portfolio_summary.csv")
    print("Thank you for using the tracker!")


if __name__ == "__main__":
    main()