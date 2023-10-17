"""
This program keeps track of the the stock symbols, stock descriptions,
stock quantity, and stock price for the company's stock.
"""

stock_dict = {
    # stock_symbol : [stock_desc, stock_quantity, stock_price]
    "CASH" : ["Cash", 10000.00, 1.00],
}

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

def viewPortfolio(s_dict: dict) -> None:
    """Displays a report of cash and stock assets along with their information
    and current value per line item.

    Args:
        s_dict (dict): the dictionary of cash and stocks
    """
    print("============================ PORTFOLIO ============================")
    print("Symbol     |Description           |Quantity   |Price     |Value    ")
    print(":::::::::::|::::::::::::::::::::::|:::::::::::|::::::::::|:::::::::")
    for key, val in s_dict.items():
        print(
            f"{key:11}|{(val[0]):22}|{(val[1]):11.2f}|{(val[2]):10.2f}|{(val[1]*val[2]):9.2f}  \n",
            end=""
        )
    total_value = 0
    for val in s_dict.values():
        total_value += val[1]*val[2]
    print(f"{' '*52}TOTAL {total_value:9.2f}")

def buyStock(s_dict: dict) -> dict:
    print("===== Buy Stock =====")
    s_symb = input("Enter Stock Symbol: ").upper().strip()

    new_entry = True

    # Check if stock symbol exists
    if s_symb in s_dict:
        print(f"INFO: Adding more shares of {s_symb}\n")
        s_desc = s_dict[s_symb][0]
        new_entry = False
    else:
        print(f"INFO: Initial entry of {s_symb}\n")
        s_desc = input("Enter Company Name: ")

    # Ask for stock quantity and price
    s_quantity = float(input("Enter Number of Shares to Buy: "))
    s_price = float(input("Enter Current Price per Share: "))

    # Check if there is enough cash to buy the stock
    if s_dict["CASH"][1] < (s_quantity * s_price):
        print("ERROR: Not enough cash.")
    else:
        print(f"INFO: {s_quantity} shares of {s_symb} sold for total of {s_price * s_quantity:.2f}")
        if not new_entry:
            s_quantity += s_dict[s_symb][1]
        
        s_dict["CASH"][1] = s_dict["CASH"][1] - (s_quantity * s_price)
        s_dict[s_symb] = [s_desc, s_quantity, s_price]

    return s_dict

def sellStock(s_dict: dict) -> dict:
    print("===== Sell Stock =====")

    stocks_only_dict = s_dict.copy()
    del stocks_only_dict["CASH"]

    s_symb = input("Enter Stock Symbol: ").upper().strip()

    # If there is are no stocks.
    if not stocks_only_dict:
        print("ERROR: ")
    
    else:
        pass


    return s_dict

def changePrice(s_dict: dict) -> dict:
    pass

def sellAll(s_dict: dict) -> dict:
    pass

while True:
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
