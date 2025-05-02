import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import log,e,sqrt
from scipy import stats
from datetime import date

# st.title('Black Scholes Merton Option Pricing Calculator')
# st.header()
# st.subheader()
# st.text()
# st.write('# Black Scholes Merton Option Pricing Calculator')
# st.write('---')

# stock_price = 214.72
# strike_price = 200.00

# div_1 = 6.45
# div_1_ex = 0.265753425
# div_2 = 6.65 
# div_2_ex = 0.764383562

# time = 0.9726
# rate = 0.037778
# volatility = 0.4305

stock_price = 161.94
strike_price = 160
rate = 0.001
volatility = 0.2888
year = 2022
month = 2
day = 18

div_1 = 0.88
div_1_ex = 0
div_2 = 0
div_2_ex = 0

def black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility):

    '''
        Function which returns the dollar values of a call and a put option using the Black Scholes Merton option pricing formula, this
        variation takes input for up to two dividends and their ex-dividend dates
    
        Parameters
        ..........
        stock_price = the current spot price of the asset
        strike_price = the strike price of the options contract
        
        div_1 = price of the first dividend
        div_1_ex = ex-dividend date for first dividend
        div_2 = price of the second dividend
        div_2_ex = ex-dividend date for second dividend
        
        time = time to maturity in years
        rate = risk free rate of return
        volatility = volatility of the asset
        

        Returns
        ..........
        [call, put] = a list of the estimated dollar values for the call and put option
    
    '''

    dividend_1_present_value = div_1 * e**(round(-div_1_ex, 4) * rate)
    dividend_2_present_value = 0
    
    if div_2_ex < time:
        dividend_2_present_value = div_2 * e**(round(-div_2_ex, 4) * rate)

    combined_dividend_present_value = round(dividend_1_present_value + dividend_2_present_value, 4)
    ex_dividend_stock_price = round(stock_price - combined_dividend_present_value, 4)

    d1 = round((log(ex_dividend_stock_price / strike_price) + (rate + (volatility**2)/2) * time) / (volatility * sqrt(time)), 4) 
    d2 = round(d1 - volatility * sqrt(time), 4)

    n_d1_pos = round(stats.norm.cdf(d1), 4)
    n_d2_pos = round(stats.norm.cdf(d2), 4)
    n_d1_neg = round(stats.norm.cdf(-d1), 4)
    n_d2_neg = round(stats.norm.cdf(-d2), 4)

    call = round(ex_dividend_stock_price * n_d1_pos - strike_price * e**(-rate * time) * n_d2_pos, 2)
    put = round(strike_price * e**(-rate * time) * n_d2_neg - ex_dividend_stock_price * n_d1_neg, 2)

    return [call, put]

def annualised_days(date_1, date_2):
    return (date_1 - date_2).days/365

todays_date = date.today()
exercise_date = date(year, month, day)
time = abs(annualised_days(todays_date, exercise_date))

if strike_price < stock_price:
    print('The call option is in-the-money and the put option is out-of-the-money')
elif strike_price > stock_price:
    print('The call option is out-of-the-money and the put option is in-the-money')
else:
    print('The options are at-the-money')

print(black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility))