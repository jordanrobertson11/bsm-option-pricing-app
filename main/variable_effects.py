########## How the different variables effect the call/put value ##########

########## Spot price ##########

# Call option

plt.plot(range(60, 140), [black_scholes_merton(x, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility)[0] for x in range(60, 140)], lw=2.5)
plt.yticks(range(5, 55, 5), ['$' + str(i) for i in range(5, 55, 5)])
plt.xticks(range(60, 150, 10), ['$' + str(i) for i in range(60, 150, 10)])

plt.xlabel('Spot Price')
plt.ylabel('European Call Value')
plt.grid();

# Put option

plt.plot(range(60, 140), [black_scholes_merton(x, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility)[1] for x in range(60, 140)], lw=2.5, color='red')
plt.yticks(range(0, 40, 5), ['$' + str(i) for i in range(0, 40, 5)])
plt.xticks(range(60, 150, 10), ['$' + str(i) for i in range(60, 150, 10)])

plt.xlabel('Spot Price')
plt.ylabel('European Put Value')
plt.grid();

########## Strike price ##########

# Call option

plt.plot(range(60, 140), [black_scholes_merton(stock_price, x, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility)[0] for x in range(60, 140)], lw=2.5)
plt.yticks(range(5, 55, 5), ['$' + str(i) for i in range(5, 55, 5)])
plt.xticks(range(60, 150, 10), ['$' + str(i) for i in range(60, 150, 10)])

plt.xlabel('Strike Price')
plt.ylabel('European Call Value')
plt.grid();

# Put option

plt.plot(range(60, 140), [black_scholes_merton(stock_price, x, div_1, div_1_ex, div_2, div_2_ex, time, rate, volatility)[1] for x in range(60, 140)], lw=2.5, color='red')
plt.yticks(range(0, 40, 5), ['$' + str(i) for i in range(0, 40, 5)])
plt.xticks(range(60, 150, 10), ['$' + str(i) for i in range(60, 150, 10)])

plt.xlabel('Strike Price')
plt.ylabel('European Put Value')
plt.grid();

########## Volatility ##########

# Call option

plt.plot(np.arange(.01, .5, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, x)[0] for x in np.arange(.01, .5, .01)], lw=2.5)
plt.yticks(range(10, 26, 2), ['$' + str(i) for i in range(10, 26, 2)])

plt.xlabel('Volatility')
plt.ylabel('European Call Value')
plt.grid();

# Put option

plt.plot(np.arange(.01, .5, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, rate, x)[1] for x in np.arange(.01, .5, .01)], lw=2.5, color='red')
plt.yticks(range(0, 16, 2), ['$' + str(i) for i in range(0, 16, 2)])

plt.xlabel('Volatility')
plt.ylabel('European Put Value')
plt.grid();

########## Time ##########

# Call option

plt.plot(np.arange(.25, 5, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, x, rate, volatility)[0] for x in np.arange(.25, 5, .01)], lw=2.5)
plt.yticks(range(10, 40, 5), ['$' + str(i) for i in range(10, 40, 5)])

plt.xlabel('Time in Years')
plt.ylabel('European Call Value')
plt.grid(); 

# Put option

plt.plot(np.arange(.25, 5, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, x, rate, volatility)[1] for x in np.arange(.25, 5, .01)], lw=2.5, color='red')
plt.yticks(range(3, 10, 1), ['$' + str(i) for i in range(3, 10, 1)])

plt.xlabel('Time in Years')
plt.ylabel('European Put Value')
plt.grid(); 

########## Interest Rates ##########

# Call option

plt.plot(np.arange(.001, .075, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, x, volatility)[0] for x in np.arange(.001, .075, .01)], lw=2.5)
plt.yticks(range(13, 18, 1), ['$' + str(i) for i in range(13, 18, 1)])

plt.xlabel('Interest Rate')
plt.ylabel('European Call Value')
plt.grid(); 

# Put option

plt.plot(np.arange(.001, .075, .01), [black_scholes_merton(stock_price, strike_price, div_1, div_1_ex, div_2, div_2_ex, time, x, volatility)[1] for x in np.arange(.001, .075, .01)], lw=2.5, color='red')
plt.yticks(range(5, 9, 1), ['$' + str(i) for i in range(5, 9, 1)])

plt.xlabel('Interest Rate')
plt.ylabel('European Put Value')
plt.grid(); 
