import yfinance as yf
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import packaging.version

pd.set_option('display.max_column', None)

gme = yf.Ticker("GME")

gme_data = gme.history(period="max")

gme_data.reset_index(inplace=True)

print(gme_data.head())
