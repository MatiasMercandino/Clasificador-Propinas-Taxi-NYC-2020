#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def load_data(year: int, month: int) -> pd.DataFrame:
    filename = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet"
    return pd.read_parquet(filename)

