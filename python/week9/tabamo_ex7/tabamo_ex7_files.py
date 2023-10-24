"""
Module for saving and loading the stock portfolio.
"""
# Exercise 7 - Tabamo, Euan Jed S. - October 24, 2023

import os

# NOTE:
# Ensures that the file is saved to the same directory as the Python file.
# This is so that the file wouldn't be saved wherever the Python Interpreter was run.
file_dir = os.path.dirname(__file__)
inv_path = os.path.join(file_dir, "inventory.dat")
hist_path = os.path.join(file_dir, "history.dat")

# NOTE: encoding="utf-8" in accordance with PEP 597 https://peps.python.org/pep-0597/

def loadPortfolio(s_dict: dict[str, list]) -> dict:
    """Loads the portfolio from a file.

    Args:
        s_dict (dict[str, list]): the portfolio
    """
    # Checks if the file exists
    if os.path.isfile(inv_path) is False:
        print("\nERROR: inventory.dat file not found!")
        return s_dict

    s_dict.clear()
    f_h = open(inv_path, "r", encoding="utf-8")
    for line in f_h:
        data = line.split(",")
        # Cash
        if len(data) == 2:
            s_dict[data[0]] = ["Cash", float(data[1]), 1.00]
        # Stocks
        else:
            s_dict[data[0]] = [data[1], float(data[2]), float(data[3].rstrip("\n"))]

    print("\nINFO: Successfully loaded portfolio!")
    return s_dict

def savePortfolio(s_dict: dict[str, list]) -> None:
    """Saves the portfolio to a file.

    Args:
        s_dict (dict[str, list]): the portfolio
    """
    f_h = open(inv_path, "w", encoding="utf-8")
    for key, value in s_dict.items():
        if key == "CASH":
            f_h.write(f"{key},{value[1]}\n")
        else:
            f_h.write(f"{key},{value[0]},{value[1]},{value[2]}\n")
    f_h.close()

    print("\nINFO: Successfully saved portfolio!")


# Additional functions to also load and save history

def loadHistory(history: list) -> list:
    # Checks if the file exists
    if os.path.isfile(hist_path) is False:
        return history
    
    history.clear()
    f_h = open(hist_path, "r", encoding="utf-8")
    for line in f_h:
        data = line.split(",")
        history.append([data[0], data[1], float(data[2]), float(data[3].rstrip("\n"))])

    return history

def saveHistory(history: list) -> None:
    f_h = open(hist_path, "w", encoding="utf-8")
    for lst in history:
        symbol, description, quantity, value = lst
        f_h.write(f"{symbol},{description},{quantity},{value}\n")

    f_h.close()
