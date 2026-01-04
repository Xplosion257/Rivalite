"""
Some shortcuts for the library known as os.

These shortcuts make it a lot cleaner to clear the terminal, get environment variables, and etc.
"""

import os

def clear():
    """
    Clears the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")
