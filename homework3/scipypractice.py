import numpy as np
import pandas as pd
from scipy import stats, optimize, integrate
import matplotlib.pyplot as plt

df = pd.read_csv("hubble_data (1).csv")
print(df.head())
print(df.describe())