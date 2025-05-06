# monte carlo pricing program

import numpy as np
import math

class Stochastic Process:

  def time_step(self):
    dW = np.random.normal(0, math.sqrt(self.delta_t))
    dS = self.drift*self.current_asset_price*self.data_t + self.asset_volatility*self.current_asset_price*dW
    self.asset_prices.append(self.current_asset_price + dS)
    self.current_asset_price = self.current_asset_price + dS

  def __init__(self, asset_price, drift, delta_t, asset_volatility):
    self.current_asset_price = asset_price
    self.asset_prices = []
    self.asset_prices.append(asset_price)
    self.drift = drift
    self.delta_t = delta_t
    self.asset_volatility = asset_volatility

  
