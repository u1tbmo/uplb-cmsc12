"""
This program is a stock portfolio tracking system.
"""

# Global Variable
stock_dict = {
    "CASH" : ["Cash", 10000.00, 1.00],
}

# Helper Functions

def clean_dict(s_dict: dict[str, list]) -> dict:
    """Removes stocks with 0 quantity from the portfolio except for cash.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    for key, val in s_dict.items():
        if val[1] == 0 and key != "CASH":
            # Remove price if quantity is 0
            s_dict[key] = [val[0], val[1], 0]
    return s_dict


# Main Functions

def menu() -> str:
    """Prints a menu and asks the user for a choice.

    Returns:
        int: the choice of the user
    """    
    print(
        "                          \n"
        "========== Menu ==========\n",
        "[1] View Portfolio        \n",
        "[2] Buy Stock             \n",
        "[3] Sell Stock            \n",
        "[4] Change Stock Price    \n",
        "[5] Liquidate all Stocks  \n",
        "[6] Exit",
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
        print(f"{key:11} {(val[0]):22} {(val[1]):11.2f} {(val[2]):12.2f} {(val[1]*val[2]):11.2f}")
    total_value = 0
    for val in s_dict.values():
        total_value += val[1]*val[2]
    print(f"{' '*54}TOTAL {total_value:11.2f}")
    print("=======================================================================")


def buyStock(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to buy stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Buy Stock =====\n")

    # Ask for stock symbol
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    # Check if stock symbol is in portfolio
    new_entry = True
    # If there is an entry, get the description of the company
    if s_symb in s_dict:
        print(f"INFO: Adding more shares of {s_symb}\n")
        s_desc = s_dict[s_symb][0]
        new_entry = False
    # If there is no entry, ask for description of the company
    else:
        print(f"INFO: Initial entry of {s_symb}\n")
        s_desc = input("Enter Company Name: ")

    # Ask for quantity and price
    s_quantity = float(input("Enter Number of Shares to Buy: "))
    s_price = float(input("Enter Current Price per Share: "))

    # Check if there is enough cash
    if s_dict["CASH"][1] < (s_quantity * s_price):
        print(f"\nERROR: Not enough cash.")
    # If there is enough cash, add the stock to the portfolio
    else:
        print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")
        # If this is not a new entry, add the previous quantity to the new quantity
        if not new_entry:
            s_quantity += s_dict[s_symb][1]
        
        # Subtract the total price from the cash and update the stock details
        s_dict["CASH"][1] = s_dict["CASH"][1] - (s_quantity * s_price)
        s_dict[s_symb] = [s_desc, s_quantity, s_price]

    # Return the updated portfolio
    return s_dict


def sellStock(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to sell stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Sell Stock =====\n")

    # Check if all stocks have 0 quantity
    all_zero = True
    for key, val in s_dict.items():
        if val[1] != 0 and key != "CASH":
            all_zero = False
            break

    # Check if there are stocks to liquidate
    if len(s_dict) == 1 or all_zero:
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
        s_quantity = float(input("Enter Number of Shares to Sell: "))
        # If there is not enough shares, you cannot sell
        if s_quantity > s_dict[s_symb][1]:
            print(f"\nERROR: Not enough shares")
        else:
            # Ask for price
            s_price = float(input("Enter Current Price per Share: "))
            print(f"\nINFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

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
        dict: the updated portfolio of stocks
    """    
    print("===== Change Stock Price =====\n")
    
    # Check if all stocks have 0 quantity
    all_zero = True
    for key, val in s_dict.items():
        if val[1] != 0 and key != "CASH":
            all_zero = False
            break

    # Check if there are stocks to liquidate
    if len(s_dict) == 1 or all_zero:
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
        s_price = float(input("Enter New Price per Share: "))
        print(f"\nINFO: {s_symb} price changed to {s_price:.2f}")

        # Update the stock details
        s_dict[s_symb] = [s_dict[s_symb][0], s_dict[s_symb][1], s_price]

    # Return the updated portfolio
    return s_dict


def sellAll(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to liquidate all stocks.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Liquidate All Stocks =====\n")
    
    # Check if all stocks have 0 quantity
    all_zero = True
    for key, val in s_dict.items():
        if val[1] != 0 and key != "CASH":
            all_zero = False
            break

    # Check if there are stocks to liquidate
    if len(s_dict) == 1 or all_zero:
        print("ERROR: No stock assets to liquidate")
        # Return the portfolio as is
        return s_dict


    # Ask for confirmation
    confirmation = input("Are you sure you want to sell all your stocks? [Y] to confirm.\n > ")
    if confirmation == "Y":
        # for every key, val tuple in the portfolio that is not cash
        for key, val in s_dict.items():
            if key != "CASH":
                print(f"INFO: Sold {val[1]} shares of {key} for total of {val[1] * val[2]:.2f}")
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

    # Display menu and ask for choice
    c = menu()

    # Check choice
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
        stock_dict = print("See you next time!")
        break
    else:
        print("Invalid choice.")
