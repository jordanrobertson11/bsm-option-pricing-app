from math import log,e,sqrt
from scipy import stats
import numpy as np
    
class OptionPricing:

    def __init__(self, stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time_to_expiry, rate, volatility):

        self.stock_price = stock_price
        self.strike_price = strike_price
        self.div_1 = div_1
        self.div_1_ex = div_1_ex
        self.div_2 = div_2
        self.div_2_ex = div_2_ex
        self.time_to_expiry = time_to_expiry
        self.rate = rate
        self.volatility = volatility
    
    def calculate(self):
    
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
            
            time_to_expiry = time to maturity in years
            rate = risk free rate of return
            volatility = volatility of the asset
            

            Returns
            ..........
            [call, put] = a list of the estimated dollar values for the call and put option
        
        '''

        dividend_1_present_value = self.div_1 * e**(round(-self.div_1_ex, 4) * self.rate)
        dividend_2_present_value = 0
        
        if self.div_2_ex < self.time_to_expiry:
            dividend_2_present_value = self.div_2 * e**(round(-self.div_2_ex, 4) * self.rate)

        combined_dividend_present_value = round(dividend_1_present_value + dividend_2_present_value, 4)
        ex_dividend_stock_price = round(self.stock_price - combined_dividend_present_value, 4)

        d1 = round((log(ex_dividend_stock_price / self.strike_price) + (self.rate + (self.volatility**2)/2) * self.time_to_expiry) / (self.volatility * sqrt(self.time_to_expiry)), 4) 
        d2 = round(d1 - self.volatility * sqrt(self.time_to_expiry), 4)

        n_d1_pos = round(stats.norm.cdf(d1), 4)
        n_d2_pos = round(stats.norm.cdf(d2), 4)
        n_d1_neg = round(stats.norm.cdf(-d1), 4)
        n_d2_neg = round(stats.norm.cdf(-d2), 4)

        call = round(ex_dividend_stock_price * n_d1_pos - self.strike_price * e**(-self.rate * self.time_to_expiry) * n_d2_pos, 2)
        put = round(self.strike_price * e**(-self.rate * self.time_to_expiry) * n_d2_neg - ex_dividend_stock_price * n_d1_neg, 2)

        return [call, put]
