"""
module for page content
"""

from dataclasses import dataclass


@dataclass
class Content:

    """
    dataclass for page content
    """

    homePageTitle = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
    market_tabs = ['US', 'Europe', 'India', 'Currencies', 'Crypto', 'Futures']
    market_index = {
        'US': ['Dow Jones', 'S&P 500', 'Nasdaq', 'Russell', 'VIX'],
        'Europe': ['DAX', 'FTSE 100', 'CAC 40', 'IBEX 30', 'STOXX 50']
    }
    search_text = "BTC/INR"
    search_heading = "Bitcoin to Indian Rupee"
