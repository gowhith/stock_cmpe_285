
# Assignment 1: Stock Profit Calculator
# Name: Gowhith Kanisetty
# SJSU ID: 017515641

def calculate_stock_profit(ticker, allotment, final_price, sell_commission, initial_price, 
                           buy_commission, tax_rate):
    # Calculate proceeds
    proceeds = allotment * final_price

    # Calculate cost breakdown
    total_purchase_price = allotment * initial_price
    capital_gain = proceeds - total_purchase_price - buy_commission - sell_commission
    tax_on_capital_gain = (tax_rate / 100) * capital_gain if capital_gain > 0 else 0

    # Total cost
    total_cost = total_purchase_price + buy_commission + sell_commission + tax_on_capital_gain

    # Net profit
    net_profit = proceeds - total_cost

    # Return on investment (ROI)
    roi = (net_profit / total_cost) * 100 if total_cost > 0 else 0

    # Break-even price per share
    break_even_price = (total_cost - tax_on_capital_gain) / allotment

    # Output results
    print("\nPROFIT REPORT:")
    print(f"Ticker Symbol: {ticker}")
    print(f"Proceeds: ${proceeds:,.2f}")
    print(f"Cost: ${total_cost:,.2f}")
    print("\nCost details:")
    print(f"Total Purchase Price: {allotment} × ${initial_price:.2f} = ${total_purchase_price:,.2f}")
    print(f"Buy Commission: ${buy_commission:.2f}")
    print(f"Sell Commission: ${sell_commission:.2f}")
    print(f"Tax on Capital Gain: {tax_rate}% of ${capital_gain:,.2f} = ${tax_on_capital_gain:,.2f}")
    print(f"\nNet Profit: ${net_profit:,.2f}")
    print(f"Return on Investment: {roi:.2f}%")
    print(f"To break even, you should have a final share price of: ${break_even_price:.2f}\n")

def main():
    print("Compute Your Profit:\n")
    ticker = input("Ticker Symbol: ")
    allotment = int(input("Allotment (number of shares): "))
    final_price = float(input("Final Share Price: "))
    sell_commission = float(input("Sell Commission: "))
    initial_price = float(input("Initial Share Price: "))
    buy_commission = float(input("Buy Commission: "))
    tax_rate = float(input("Capital Gain Tax Rate (%): "))

    calculate_stock_profit(ticker, allotment, final_price, sell_commission,
                           initial_price, buy_commission, tax_rate)

if __name__ == "__main__":
    main()
