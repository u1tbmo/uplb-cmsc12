stock = {
    "ABS": ["ABS-CBN Corp.", 20.2, 20.9],
    "AC": ["Ayala Corp.", 910.5, 930],
    "CEB": ["Cebu Air Inc.", 67.4, 67.45],
    "JFC": ["Jollibee Foods Corp.", 252.8, 243],
}

# Change Jollibee's price to 260
stock["JFC"][1] = 260
# Print all the stock details of "CEB"
print(stock["CEB"])
# Print all the stock symbols with their prices
for k, v in stock.items():
    print(f"{k}: {v[1]}")
