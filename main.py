# pylint: disable-all

import numpy as np
from scipy.stats import norm

def d_bachelier(F_t, K, sigma, t, T):
    B = sigma*np.sqrt(T-t)
    A = (F_t-K)/B
    return A

def discount(r,t,T):
    return np.exp(-r*(T-t))

def N(x):
    return norm.cdf(x)

def dN(x):
    return np.exp(-x*x*0.5)/(np.sqrt(2*np.pi))

def call(F_t, K, r, sigma, t, T):
    D = d_bachelier(F_t, K, sigma, t, T)
    B = sigma*np.sqrt(T-t)
    return discount(r,t,T)*((F_t-K)*N(D) + B*dN(D))

def put(F_t, K, r, sigma, t, T):
    D = d_bachelier(F_t, K, sigma, t, T)
    B = sigma*np.sqrt(T-t)
    return discount(r,t,T)*(-(F_t-K)*N(-D) + B*dN(D))

if __name__ == '__main__':
    print('bachelier model')