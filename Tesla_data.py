import yfinance as yf
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import packaging.version

pd.set_option('display.max_columns', None)

tesla = yf.Ticker("TSLA")

tesla_data = tesla.history(period="max")

tesla_data.reset_index(inplace=True)

print(tesla_data.head())

