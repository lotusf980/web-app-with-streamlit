import yfinance as yf
import streamlit as st 

st.write("""
# 📈 Simple Stock Price App

Shown are the **closing price** and ***volume*** of Google! 
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'  

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)  

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2025-05-31')  

# Open High Low Close Volume Dividends Stock Splits

# Closing Price Chart
st.write("## 📊 Closing Price")
st.line_chart(tickerDf['Close'])

# Volume Chart
st.write("## 📊 Volume Price")
st.line_chart(tickerDf['Volume'])
