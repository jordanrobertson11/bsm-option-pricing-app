from option_pricing import OptionPricing
import streamlit as st
import matplotlib.pyplot as plt
from datetime import date, timedelta
import seaborn as sns
import numpy as np

with st.sidebar:
    st.write('# Black Scholes Merton Option Pricing Calculator')
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px;">
            <span>Created By:</span>
            <a href="https://www.linkedin.com/in/jzrobertson">
                <img src="https://img.icons8.com/?size=100&id=98960&format=png&color=000000" width="50" height="50">
            </a>
            <a href="https://github.com/jordanrobertson11">
                <img src="https://img.icons8.com/?size=100&id=62856&format=png&color=000000" width="50" height="50">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')

    st.write('## Inputs')

    stock_price = st.number_input("Current Asset Price", value=100.00)
    strike_price = st.number_input("Strike Price", value=90.00)
    exercise_date = st.date_input("Exercise Date", date.today() + timedelta(days=1))
    volatility = st.number_input("Volatility (σ)", value=0.50)
    rate = st.number_input("Risk-Free Interest Rate", value=0.05)

    st.write('## Dividends (Optional)')

    div_1 = st.number_input("Dividend 1 Price", value=0.00)
    div_1_ex_date = st.date_input("Dividend 1 Ex-Dividend Date", date.today())
    div_2 = st.number_input("Dividend 2 Price", value=0.00)
    div_2_ex_date = st.date_input("Dividend 2 Ex-Dividend Date", date.today())

todays_date = date.today()
time_to_expiry = abs((todays_date - exercise_date).days / 365)
div_1_ex = abs((todays_date - div_1_ex_date).days / 365)
div_2_ex = abs((todays_date - div_2_ex_date).days / 365)

options = OptionPricing(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time_to_expiry, rate, volatility)
call_price, put_price = options.calculate()
print(f"Call Price: {call_price}, Put Price: {put_price}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div style="text-align: center; background-color: rgba(0, 128, 0, 0.7); color: white; padding: 20px; border-radius: 10px;">
            <p style="font-size: 48px;">Call</h2>
            <p style="font-size: 24px;">${call_price:.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="text-align: center; background-color: rgba(255, 0, 0, 0.7); color: white; padding: 20px; border-radius: 10px;">
            <p style="font-size: 48px;">Put</h2>
            <p style="font-size: 24px;">${put_price:.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

price_range = np.arange(stock_price * 0.5, stock_price * 1.5, 10)

