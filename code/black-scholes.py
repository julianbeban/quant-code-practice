# Modeling European Option price through Black-Scholes formula
# European options, (as opposed to American options), can only be exercised at maturity

import numpy as np
from scipy.stats import norm

#define formula inputs
r = 0.01 # risk-free rate
S = 20 # current stock price
K = 40 # stock price
T = 250/365 #days out of the year remaining until expiry
sigma = 0.30 # volatility - the standard deviation of continuously compounded annual returns of the stock

def blackScholes(r, S, K, T, sigma, type = "c"):
    "Calculate option price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price   
    except:
        print("Confirm all inputs above!")

print("Option Price is:  ", round(blackScholes(r, S, K, T, sigma, type = "c"), 2))

