#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    'work_hours',
    "pickup_minute",
    "passenger_count",
    'trip_distance',
    'trip_time',
    'trip_speed'
]
categorical_feat = [
    "PULocationID",
    "DOLocationID",
    "RatecodeID",
]
features = numeric_feat + categorical_feat
EPS = 1e-7

def preprocess(df, target_col):
    df = df[df['fare_amount'] > 0].reset_index(drop=True)  # avoid divide-by-zero
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = df['tip_fraction'] > 0.2
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.seconds
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] + EPS)
    df = df[['tpep_dropoff_datetime'] + features + [target_col]]
    df[features + [target_col]] = df[features + [target_col]].astype("float32").fillna(-1.0)
    df[target_col] = df[target_col].astype("int32")
    return df.reset_index(drop=True)

def compare_distributions(dfa: pd.DataFrame, dfb: pd.DataFrame, features: list) -> pd.DataFrame:
    """Compare the distributions of two datasets."""
    from scipy import stats
    statistics = []
    p_values = []

    for feature in features:
        statistic, p_value = stats.ks_2samp(dfa[feature], dfb[feature])
        statistics.append(statistic)
        p_values.append(p_value)
    
    comparison_df = pd.DataFrame(data={'feature': features, 'statistic': statistics, 'p_value': p_values})
    comparison_df = comparison_df.sort_values(by='p_value', ascending=True)

    return comparison_df

