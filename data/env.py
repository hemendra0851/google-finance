"""
module for environment variables
"""
from dataclasses import dataclass


@dataclass
class Env:
    """
    dataclass for environment variables
    """

    url = "https://www.google.com/finance/"
    browser = "chrome"
