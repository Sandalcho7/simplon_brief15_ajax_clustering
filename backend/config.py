import pandas as pd

DATA_PATH = "data/mall_customers.csv"   # Path to our data csv
DATA = pd.read_csv(DATA_PATH)
DATA["Genre"] = DATA["Genre"].replace({"Male": 0, "Female": 1})
