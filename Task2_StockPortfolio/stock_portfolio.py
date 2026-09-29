# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

total_investment = 0

# Ask the user how many different stocks they own
number_of_stocks = int(input("How many different stocks do you own? "))

for i in range(number_of_stocks):

    stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock:", stock_name)
        print("Price:", stock_prices[stock_name])
        print("Quantity:", quantity)
        print("Investment:", investment)
        print()

    else:
        print("Stock not available in our price list.")
        print()

print("================================")
print("Total Investment:", total_investment)
print("================================")