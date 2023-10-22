"""
This program is a stock portfolio tracking system.
"""

# Global Variable
stock_dict = {
    "CASH" : ["Cash", 10000.00, 1.00],
}

# Helper List

history = [
    ["CASH", "Initial cash", 10000.00, 1.00],
]

# Helper Functions

def clean_dict(s_dict: dict[str, list]) -> dict:
    """Removes the price of stocks with 0 quantity from the portfolio except for cash.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks where the price of stocks with 0 quantity is removed
    """    
    for key, val in s_dict.items():
        if val[1] == 0 and key != "CASH":
            # Remove price if quantity is 0
            s_dict[key] = [val[0], val[1], 0]
    return s_dict


def calc_total_value(s_dict: dict[str, list]) -> float:
    """Calculates the total value of the portfolio.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        float: the total value of the portfolio
    """    
    total_value = 0
    for val in s_dict.values():
        total_value += val[1]*val[2]
    return total_value


def check_for_stocks(s_dict: dict[str, list]) -> bool:
    """Checks for at least 1 stock with a quantity greater than 0.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        bool: True if all stocks (except cash) have 0 quantity, otherwise returns False
    """    
    # Check if all stocks have 0 quantity
    no_stocks_exist = True
    for key, val in s_dict.items():
        if val[1] != 0 and key != "CASH":
            no_stocks_exist = False
            break
    return no_stocks_exist


def print_history(history: list[list]) -> None:
    """Prints the history of transactions.

    Args:
        history (list): the history of transactions
    """    
    print("=============================== HISTORY ===============================")
    print("Symbol      Description            Quantity    Price        Value      ")
    print("::::::::::: :::::::::::::::::::::: ::::::::::: :::::::::::: :::::::::::")
    for entry in history:
        print(f"{entry[0]:11} {entry[1]:22} {entry[2]:11.2f} {entry[3]:12.2f} {(entry[2]*entry[3]):11.2f}")
    print("=======================================================================")


# Main Functions

def menu() -> str:
    """Prints a menu and asks the user for a choice.

    Returns:
        str: the choice of the user
    """    
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


def viewPortfolio(s_dict: dict[str, list]) -> None:
    """Displays a report of cash and stock assets along with their information
    and current value per line item.

    Args:
        s_dict (dict): the portfolio of stocks
    """
    print("============================== PORTFOLIO ==============================")
    print("Symbol      Description            Quantity    Price        Value      ")
    print("::::::::::: :::::::::::::::::::::: ::::::::::: :::::::::::: :::::::::::")
    for key, val in s_dict.items():
        if val[1] != 0:
            print(f"{key:11} {(val[0]):22} {(val[1]):11.2f} {(val[2]):12.2f} {(val[1]*val[2]):11.2f}")

    total_value = calc_total_value(s_dict)
    
    print(f"{' '*54}TOTAL {total_value:11.2f}")
    print("=======================================================================")


def buyStock(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to buy stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks where cash is subtracted and a new stock is added
    """    
    print("===== Buy Stock =====\n")

    # Ask for stock symbol
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    # You cannot buy cash
    if s_symb == "CASH":
        print("ERROR: You cannot buy cash.")
        return s_dict

    # Check if stock symbol is in portfolio
    new_entry = True
    # If there is an entry, get the description of the company
    if s_symb in s_dict:
        print(f"INFO: Adding shares of {s_symb}\n")
        s_desc = s_dict[s_symb][0]
        new_entry = False
    # If there is no entry, ask for description of the company
    else:
        print(f"INFO: Initial entry of {s_symb}\n")
        s_desc = input("Enter Company Name: ").strip()

    # Ask for quantity and price
    while True:
        s_quantity = float(input("Enter Number of Shares to Buy: "))
        s_price = float(input("Enter Current Price per Share: "))
        # Check if quantity and price are positive
        if s_quantity > 0 and s_price > 0:
            break
        elif s_quantity <= 0:
            print("\nERROR: Quantity must be positive.")
        elif s_price <= 0:
            print("\nERROR: Price must be positive.")

    # Check if there is enough cash
    if s_dict["CASH"][1] < (s_quantity * s_price):
        print(f"\nERROR: Not enough cash.")
    # If there is enough cash, add the stock to the portfolio
    else:
        print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

        # ! Add the transaction to the history
        # Add bought stock to history
        history.append([s_symb, f"Bought {s_symb}", s_quantity, s_price])
        # Subtract the total price from the cash
        history.append(["CASH", f"Bought {s_symb}", -1 * (s_quantity * s_price), 1.00])
        
        # Subtract the total price from the cash
        s_dict["CASH"][1] = s_dict["CASH"][1] - (s_quantity * s_price)

        # If this is not a new entry, add the previous quantity to the new quantity before updating the dictionary
        if not new_entry:
            s_quantity += s_dict[s_symb][1]

        # Update the stock details
        s_dict[s_symb] = [s_desc, s_quantity, s_price]

    # Return the updated portfolio
    return s_dict


def sellStock(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to sell stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks where cash is added, stock quantity is subtracted, and stock price is updated
    """    
    print("===== Sell Stock =====\n")

    # Check if all stocks have 0 quantity
    no_stocks_exist = check_for_stocks(s_dict)

    # Check if there are stocks to liquidate
    if no_stocks_exist:
        print("\nERROR: No stock assets to sell")
        # Return the portfolio as is
        return s_dict

    # Ask for stock symbol
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    # You cannot sell cash
    if s_symb == "CASH":
        print("\nERROR: Cannot sell cash")
    # Check if stock symbol is in portfolio
    elif s_symb not in s_dict:
        print(f"\nERROR: {s_symb} not in portfolio")
    # Check if there are shares for the stock
    elif s_dict[s_symb][1] == 0:
        print(f"\nERROR: {s_symb} has no shares")
    else:
        # Ask for quantity
        while True:
            s_quantity = float(input("Enter Number of Shares to Sell: "))
            # Check if quantity is positive
            if s_quantity > 0:
                break
            else:
                print("\nERROR: Quantity must be positive.")

        # If there is not enough shares, you cannot sell
        if s_quantity > s_dict[s_symb][1]:
            print(f"\nERROR: Not enough shares")
        else:
            # Ask for price
            while True:
                s_price = float(input("Enter Current Price per Share: "))
                # Check if price is positive
                if s_price > 0:
                    break
                else:
                    print("\nERROR: Price must be positive.")
            
            print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

            # ! Add the transaction to the history
            # Subtract sold stock from history
            history.append([s_symb, f"Sold {s_symb}", -1 * s_quantity, s_price])
            # Add the total price to the cash
            history.append(["CASH", f"Sold {s_symb}", s_quantity * s_price, 1.00])

            # Add the total price to the cash and update the stock details
            s_dict["CASH"][1] += s_quantity * s_price
            s_dict[s_symb] = [s_dict[s_symb][0], s_dict[s_symb][1] - s_quantity, s_price]
    
    # Return the updated portfolio
    return s_dict


def changePrice(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to change the price of a stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks where the price of a stock is updated
    """    
    print("===== Change Stock Price =====\n")
    
    # Check if all stocks have 0 quantity
    no_stocks_exist = check_for_stocks(s_dict)

    # Check if there are stocks to liquidate
    if no_stocks_exist:
        print("\nERROR: No stock assets to change")
        # Return the portfolio as is
        return s_dict
    
    # Ask for stock symbol
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    # You cannot change the price of cash
    if s_symb == "CASH":
        print("\nERROR: Cannot change price of cash")
    # Check if stock symbol is in portfolio
    elif s_symb not in s_dict:
        print(f"\nERROR: {s_symb} not in portfolio")
    # Check if there are shares for the stock
    elif s_dict[s_symb][1] == 0:
        print(f"ERROR: {s_symb} has no shares")
    else:
        # Ask for price
        while True:
            s_price = float(input("Enter New Price per Share: "))
            # Check if price is positive
            if s_price > 0:
                break
            else:
                print("\nERROR: Price must be positive.")
                
        print(f"\nINFO: {s_symb} price changed to {s_price:.2f}")

        # ! Add the transaction to the history
        # Add the new price to the history
        history.append([s_symb, f"Changed price of {s_symb}", s_dict[s_symb][1], s_price])

        # Update the stock details
        s_dict[s_symb] = [s_dict[s_symb][0], s_dict[s_symb][1], s_price]

    # Return the updated portfolio
    return s_dict


def sellAll(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to liquidate all stocks.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks where cash is added and all stock quantities are set to 0
    """    
    print("===== Liquidate All Stocks =====\n")
    
    # Check if all stocks have 0 quantity
    no_stocks_exist = check_for_stocks(s_dict)

    # Check if there are stocks to liquidate
    if no_stocks_exist:
        print("ERROR: No stock assets to liquidate")
        # Return the portfolio as is
        return s_dict


    # Ask for confirmation
    confirmation = input("Are you sure you want to sell all your stocks? [Y] to confirm.\n > ")
    if confirmation == "Y":
        # for every key, val tuple in the portfolio that is not cash
        for key, val in s_dict.items():
            if key != "CASH" and val[1] != 0:
                print(f"INFO: Sold {val[1]} shares of {key} for total of {val[1] * val[2]:.2f}")

                # ! Add the transaction to the history
                # Add sold stock to history
                history.append([key, f"Sold {key}", -1 * val[1], val[2]])
                # Add the total price to the cash
                history.append(["CASH", f"Sold {key}", val[1] * val[2], 1.00])

                # Add the total price to the cash and update the stock details
                s_dict["CASH"][1] += val[1] * val[2]
                s_dict[key] = [val[0], 0, val[2]]

        print("\nINFO: All stocks have been liquidated.")
    else:
        print(f"\nINFO: '{confirmation}' does not match 'Y'. Cannot confirm liquidation.")

    # Return the updated portfolio
    return s_dict

# Main Program Loop
while True:
    # Remove stock prices for stocks with 0 quantity
    stock_dict = clean_dict(stock_dict)

    # Display menu and ask for choice to assign to c
    c = menu()

    # Check choice
    # The decision to check for string values instead of ints is to prevent base 10 errors when converting to int
    # This makes the program more forgiving to user input
    if c == "1":
        # viewPortfolio() returns None, so we do not need to assign it to a variable
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
    # Just a helper function to see the history of transactions
    elif c.upper() == "H":
        print_history(history)
    else:
        print("Invalid choice.")
