
from scipy.stats import norm
import numpy as np

def black_scholes(S, K, T, r, sigma, option_type='call', q=0.0):
    """
    Black-Scholes-Merton option pricing formula with continuous dividend yield.

    Parameters:
    - S : Spot price
    - K : Strike price
    - T : Time to maturity (in years)
    - r : Risk-free interest rate
    - sigma : Volatility of the underlying asset
    - option_type : 'call' or 'put'
    - q : Continuous dividend yield (default = 0)

    Returns:
    - Option price
    """
    if T <= 0 or sigma <= 0:
        return max(0.0, (S - K) if option_type == 'call' else (K - S))

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)

    return price

def bs_greeks(S, K, T, r, sigma, option_type='call', q=0.0):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        delta = np.exp(-q * T) * norm.cdf(d1)
        theta = (-S * sigma * np.exp(-q * T) * norm.pdf(d1)) / (2 * np.sqrt(T)) \
                - r * K * np.exp(-r * T) * norm.cdf(d2) + q * S * np.exp(-q * T) * norm.cdf(d1)
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    else:  # put
        delta = -np.exp(-q * T) * norm.cdf(-d1)
        theta = (-S * sigma * np.exp(-q * T) * norm.pdf(d1)) / (2 * np.sqrt(T)) \
                + r * K * np.exp(-r * T) * norm.cdf(-d2) - q * S * np.exp(-q * T) * norm.cdf(-d1)
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)

    gamma = (np.exp(-q * T) * norm.pdf(d1)) / (S * sigma * np.sqrt(T))
    vega = S * np.exp(-q * T) * norm.pdf(d1) * np.sqrt(T)

    return delta, gamma, vega, theta, rho
