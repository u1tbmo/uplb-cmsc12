"""
This program is a stock portfolio tracking system.
"""

# Global Variable
stock_dict = {
    "CASH" : ["Cash", 10000.00, 1.00]
}


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


def menu() -> int:
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

    return int(input("Choice: "))


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
    print("===== Buy Stock =====")
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    new_entry = True

    if s_symb in s_dict:
        print(f"INFO: Adding more shares of {s_symb}\n")
        s_desc = s_dict[s_symb][0]
        new_entry = False
    else:
        print(f"INFO: Initial entry of {s_symb}\n")
        s_desc = input("Enter Company Name: ")

    s_quantity = float(input("Enter Number of Shares to Buy: "))
    s_price = float(input("Enter Current Price per Share: "))

    if s_dict["CASH"][1] < (s_quantity * s_price):
        print("ERROR: Not enough cash.")
    else:
        print(f"INFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")
        if not new_entry:
            s_quantity += s_dict[s_symb][1]
        
        s_dict["CASH"][1] = s_dict["CASH"][1] - (s_quantity * s_price)
        s_dict[s_symb] = [s_desc, s_quantity, s_price]

    return s_dict


def sellStock(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to sell stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Sell Stock =====")

    if len(s_dict) == 1:
        print("ERROR: No stock assets to sell")
        return s_dict

    s_symb = input("Enter Stock Symbol: ").upper().strip()

    if s_symb == "CASH":
        print("ERROR: Cannot sell cash")
    elif s_symb not in s_dict:
        print(f"ERROR: {s_symb} not in portfolio")
    else:
        s_quantity = float(input("Enter Number of Shares to Sell: "))
        if s_quantity > s_dict[s_symb][1]:
            print(f"ERROR: Not enough shares")
        else:
            s_price = float(input("Enter Current Price per Share: "))
            print(f"INFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")

            s_dict["CASH"][1] += s_quantity * s_price
            s_dict[s_symb] = [
                s_dict[s_symb][0],
                s_dict[s_symb][1] - s_quantity,
                s_price
            ]
    
    return s_dict


def changePrice(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to change the price of a stock.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Change Stock Price =====")

    if len(s_dict) == 1:
        print("ERROR: No stock assets to change")
        return s_dict
    
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    if s_symb == "CASH":
        print("ERROR: Cannot change price of cash")
    elif s_symb not in s_dict:
        print(f"ERROR: {s_symb} not in portfolio")
    else:
        if s_dict[s_symb][1] == 0:
            print(f"ERROR: {s_symb} has no shares")
        else:
            s_price = float(input("Enter New Price per Share: "))
            print(f"INFO: {s_symb} price changed to {s_price:.2f}")

            s_dict[s_symb] = [
                s_dict[s_symb][0],
                s_dict[s_symb][1],
                s_price
            ]

    return s_dict


def sellAll(s_dict: dict[str, list]) -> dict[str, list]:
    """Allows the user to liquidate all stocks.

    Args:
        s_dict (dict): the portfolio of stocks

    Returns:
        dict: the updated portfolio of stocks
    """    
    print("===== Liquidate All Stocks =====")

    if len(s_dict) == 1:
        print("ERROR: No stock assets to liquidate")
        return s_dict

    confirmed = input("Are you sure you want to sell all your stocks? [Y] to confirm.\n > ").upper()
    if confirmed == "Y":
        for key, val in s_dict.items():
            if key != "CASH":
                print(f"INFO: Sold {val[1]} shares of {key} for total of {val[1] * val[2]:.2f}")
                s_dict["CASH"][1] += val[1] * val[2]
                s_dict[key] = [val[0], 0, val[2]]

        print("INFO: All stocks have been liquidated.")
    else:
        print("INFO: No action taken.")

    return s_dict

while True:
    stock_dict = clean_dict(stock_dict)
    c = menu()
    if c == 1:
        viewPortfolio(stock_dict)
    elif c == 2:
        stock_dict = buyStock(stock_dict)
    elif c == 3:
        stock_dict = sellStock(stock_dict)
    elif c == 4:
        stock_dict = changePrice(stock_dict)
    elif c == 5:
        stock_dict = sellAll(stock_dict)
    elif c == 6:
        stock_dict = print("See you next time!")
        break
    else:
        print("Invalid choice.")
