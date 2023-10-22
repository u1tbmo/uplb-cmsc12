# tabamo_ex6.py

## Global Variables

Keeps track of the current cash, stocks, and history of transactions.

```python
stock_dict = {
    "CASH" : ["Cash", 10000.00, 1.00],
}

history = [
    ["CASH", "Initial cash", 10000.00, 1.00],
]
```

## Helper Functions

### Clean Dict

```python
def clean_dict(s_dict: dict[str, list]) -> dict:
    for key, val in s_dict.items():
        if val[1] == 0 and key != "CASH":
            s_dict[key] = [val[0], val[1], 0]
    return s_dict
```

1. Iterate through the dictionary of stocks.
2. If the number of stocks is zero and the key is not `CASH`, set the price to zero.
3. Return the updated dictionary.

### Calculate Total Value

```python
def calc_total_value(s_dict: dict[str, list]) -> float:
    total_value = 0
    for val in s_dict.values():
        total_value += val[1]*val[2]
    return total_value
```

1. Initialize the total value to zero.
2. Iterate through the dictionary of stocks.
3. Add the total value of each stock to the total value.
4. Return the total value.

### Check for Stocks

```python
def check_for_stocks(s_dict: dict[str, list]) -> bool:
    no_stocks_exist = True
    for key, val in s_dict.items():
        if val[1] != 0 and key != "CASH":
            no_stocks_exist = False
            break
    return no_stocks_exist
```

1. Create a flag `no_stocks_exist` and set it to `True`.
2. Iterate through the dictionary of stocks.
3. If there exists at least one stock with a quantity greater than zero, set `no_stocks_exist` to `False` and break out of the loop.
4. Return the flag.

### Print History

```python
def print_history(history: list[list]) -> None:
    print("=============================== HISTORY ===============================")
    print("Symbol      Description            Quantity    Price        Value      ")
    print("::::::::::: :::::::::::::::::::::: ::::::::::: :::::::::::: :::::::::::")
    for entry in history:
        print(f"{entry[0]:11} {entry[1]:22} {entry[2]:11.2f} {entry[3]:12.2f} {(entry[2]*entry[3]):11.2f}")
    print("=======================================================================")
```

- For every entry in the history, print the stock symbol, description, quantity, price, and value with formatting.

> NOTE: While this function is not necessary, it is useful for debugging purposes.

## Main Functions

NOTE: In the following functions, history is being updated globally without being passed as a parameter and being returned. If we want to remove the history functionality, we must comment out ALL lines that have `# ! Add the transaction to the history`, the option in the main program, and the `print_history()` function or else the program will crash.

### Menu

```python
def menu() -> str:
    print(
        "                          \n"
        "========== Menu ==========\n",
        "[1] View Portfolio        \n",
        "[2] Buy Stock             \n",
        "[3] Sell Stock            \n",
        "[4] Change Stock Price    \n",
        "[5] Liquidate all Stocks  \n",
        "[6] Exit                  \n",
        sep="", end=""
    )

    return input("Choice: ")
```

1. Print the menu.
2. Return the user's choice.

### View Portfolio

```python
    for key, val in s_dict.items():
        if val[1] != 0:
            print(f"{key:11} {(val[0]):22} {(val[1]):11.2f} {(val[2]):12.2f} {(val[1]*val[2]):11.2f}")
```

1. Iterates through the dictionary of stocks.
2. Since `s_dict.items()` returns a tuple of key and value, we can assign them to `key` and `val` respectively using multiple assignment.
3. If the number of stocks is not zero, print the stock symbol, name, number of stocks, price, and total value with formatting.

What happens to stocks with zero quantity?

> They are not displayed, but they are still in the dictionary.
> This is useful so that stock symbols are cached and therefore, you will no longer have to type their names again when buying stocks.

### Buy Stock

```python
    # Ask for stock symbol
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    if s_symb == "CASH":
        print("ERROR: You cannot buy cash.")
        return s_dict

    new_entry = True
    if s_symb in s_dict:
        print(f"INFO: Adding shares of {s_symb}\n")
        s_desc = s_dict[s_symb][0]
        new_entry = False
    else:
        print(f"INFO: Initial entry of {s_symb}\n")
        s_desc = input("Enter Company Name: ").strip()
```

1. Ask the user for the stock symbol.
2. Convert the input to uppercase and remove leading and trailing spaces.
3. If the stock symbol is "CASH" print an error message and return the dictionary as is.
4. Create a flag `new_entry` and set it to `True`.
5. Check if the stock symbol is in the dictionary.
   - If it is, set `new_entry` to `False` then get the description of the stock from the dictionary.
   - If it is not, ask for the company name to be added to the dictionary.

```python
    while True:
        s_quantity = float(input("Enter Number of Shares to Buy: "))
        s_price = float(input("Enter Current Price per Share: "))
        if s_quantity > 0 and s_price > 0:
            break
        elif s_quantity <= 0:
            print("\nERROR: Quantity must be positive.")
        elif s_price <= 0:
            print("\nERROR: Price must be positive.")
```

1. Ask the user for the number of shares to buy.
2. Ask the user for the current price per share.
3. Check if the quantity and price are positive.
   - If they are, break out of the infinite loop.
   - If they are not, print an error message.

```python
    if s_dict["CASH"][1] < (s_quantity * s_price):
        print(f"\nERROR: Not enough cash.")

    else:
        print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

        # ! Add the transaction to the history
        history.append([s_symb, f"Bought {s_symb}", s_quantity, s_price])
        history.append(["CASH", f"Bought {s_symb}", -1 * (s_quantity * s_price), 1.00])

        s_dict["CASH"][1] = s_dict["CASH"][1] - (s_quantity * s_price)

        if not new_entry:
            s_quantity += s_dict[s_symb][1]

        s_dict[s_symb] = [s_desc, s_quantity, s_price]
```

1. Check if the cash is enough to buy the stock.
   - If it is not, print an error message.
   - If it is, continue.
2. Print the number of shares and the total price.
3. Add the transaction to the history.
4. Subtract the total price from the cash.
5. Check if this is a new entry.
   - If it is not, add the previous quantity to the new quantity.
6. Add or override the stock in the dictionary depending on whether it is a new entry or not.

```python
    return s_dict
```

- Return the updated portfolio.

### Sell Stock

```python
    no_stocks_exist = check_for_stocks(s_dict)
```

- Check if there are stocks in the portfolio.

```python
    if no_stocks_exist:
        print("\nERROR: No stock assets to sell")
        return s_dict
```

- If there are none, print an error message and return the portfolio as is.

```python
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    if s_symb == "CASH":
        print("\nERROR: Cannot sell cash")
    elif s_symb not in s_dict:
        print(f"\nERROR: {s_symb} not in portfolio")
    elif s_dict[s_symb][1] == 0:
        print(f"\nERROR: {s_symb} has no shares")
    else:
        while True:
            s_quantity = float(input("Enter Number of Shares to Sell: "))

            if s_quantity > 0:
                break
            else:
                print("\nERROR: Quantity must be positive.")
        if s_quantity > s_dict[s_symb][1]:
            print(f"\nERROR: Not enough shares")
        else:
            while True:
                s_price = float(input("Enter Current Price per Share: "))
                if s_price > 0:
                    break
                else:
                    print("\nERROR: Price must be positive.")

            print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

            # ! Add the transaction to the history
            history.append([s_symb, f"Sold {s_symb}", -1 * s_quantity, s_price])
            history.append(["CASH", f"Sold {s_symb}", s_quantity * s_price, 1.00])

            s_dict["CASH"][1] += s_quantity * s_price
            s_dict[s_symb] = [s_dict[s_symb][0], s_dict[s_symb][1] - s_quantity, s_price]
```

1. Ask for the stock symbol.
2. Check the stock symbol.
   - If it is `CASH`, print an error message.
   - If it is not in the dictionary, print an error message.
   - If it is in the dictionary but has zero quantity, print an error message.
3. Ask the user for the number of shares to sell.
   - If it is positive, break out of the infinite loop.
   - If it is not, print an error message.
4. Check if the quantity to sell is greater than the quantity in the portfolio.
   - If it is, print an error message.
   - If it is not, continue.
5. Ask the user for the current price per share.
   - If it is positve, break out of the infinite loop.
   - If it is not, print an error message.
6. Print the number of shares and the total price.
7. Add the transaction to the history.
8. Add the total price to the cash.
9. Subtract the quantity to sell from the quantity in the portfolio.

```python
    return s_dict
```

- Return the updated portfolio.

### Change Price

```python
    no_stocks_exist = check_for_stocks(s_dict)
```

- Check if there are stocks in the portfolio.

```python
    if no_stocks_exist:
        print("\nERROR: No stock assets to change")
        return s_dict
```

- If there are none, print an error message and return the portfolio as is.

```python
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    if s_symb == "CASH":
        print("\nERROR: Cannot change price of cash")
    elif s_symb not in s_dict:
        print(f"\nERROR: {s_symb} not in portfolio")
    elif s_dict[s_symb][1] == 0:
        print(f"ERROR: {s_symb} has no shares")
    else:
        while True:
            s_price = float(input("Enter New Price per Share: "))
            if s_price > 0:
                break
            else:
                print("\nERROR: Price must be positive.")

        print(f"\nINFO: {s_symb} price changed to {s_price:.2f}")

        # ! Add the transaction to the history
        history.append([s_symb, f"Changed price of {s_symb}", s_dict[s_symb][1], s_price])

        s_dict[s_symb] = [s_dict[s_symb][0], s_dict[s_symb][1], s_price]
```

1. Ask for the stock symbol.
2. Check the stock symbol.
   - If it is `CASH`, print an error message.
   - If it is not in the dictionary, print an error message.
   - If it is in the dictionary but has zero quantity, print an error message.
3. Ask the user for the new price per share.
   - If it is positive, break out of the infinite loop.
   - If it is not, print an error message.
4. Print the stock symbol and the new price.
5. Add the transaction to the history.
6. Change the price of the stock in the dictionary.

```python
    return s_dict
```

- Return the updated portfolio.

### Sell All Stocks

```python
    no_stocks_exist = check_for_stocks(s_dict)
```

- Check if there are stocks in the portfolio.

```python
    if no_stocks_exist:
        print("ERROR: No stock assets to liquidate")
        return s_dict
```

- If there are none, print an error message and return the stock portfolio as is.

```python
    confirmation = input("Are you sure you want to sell all your stocks? [Y] to confirm.\n > ")
    if confirmation == "Y":
        for key, val in s_dict.items():
            if key != "CASH" and val[1] != 0:
                print(f"INFO: Sold {val[1]} shares of {key} for total of {val[1] * val[2]:.2f}")

                # ! Add the transaction to the history
                history.append([key, f"Sold {key}", -1 * val[1], val[2]])
                history.append(["CASH", f"Sold {key}", val[1] * val[2], 1.00])

                s_dict["CASH"][1] += val[1] * val[2]
                s_dict[key] = [val[0], 0, val[2]]

        print("\nINFO: All stocks have been liquidated.")
    else:
        print(f"\nINFO: '{confirmation}' does not match 'Y'. Cannot confirm liquidation.")
```

1. Ask for confirmation.
   - If the confirmation is exactly `Y`, continue.
   - If the confirmation is not exactly `Y`, print an error message and return the stock portfolio as is.
2. Iterate through the dictionary of stocks.
3. If the key is not `CASH` and the number of stocks is not zero, continue.
4. Print a message about the number of stocks and the total price.
5. Add the transaction to the history.
6. Add the total price to the cash.
7. Set the number of stocks to zero.
8. Print a message that all stocks have been liquidated.

```python
    return s_dict
```

- Return the updated portfolio.

## Main Program

```python
while True:
    stock_dict = clean_dict(stock_dict)
    c = menu()
    if c == "1":
        viewPortfolio(stock_dict)
    elif c == "2":
        stock_dict = buyStock(stock_dict)
    elif c == "3":
        stock_dict = sellStock(stock_dict)
    elif c == "4":
        stock_dict = changePrice(stock_dict)
    elif c == "5":
        stock_dict = sellAll(stock_dict)
    elif c == "6":
        print("See you next time!")
        break
    elif c.upper() == "H":
        print_history(history)
    else:
        print("Invalid choice.")
```

1. Clean the dictionary of stocks.
2. Ask the user for a choice by calling the `menu()` function.
3. Proceed to the corresponding function depending on the choice.
4. If the choice is `6`, print a message and break out of the infinite loop.
5. If the choice is `H`, print the history.
6. If the choice is not valid, print an error message.
