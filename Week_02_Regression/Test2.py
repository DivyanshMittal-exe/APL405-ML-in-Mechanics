import os
import matplotlib.pyplot as plt
import numpy as np
from Week2_Q2_Template import mr
import pandas as pd


mr_o = mr()
df = pd.read_csv('prob2data.csv')
df = df[['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']]


print(mr_o.predict(df.mean(),df.std()))

