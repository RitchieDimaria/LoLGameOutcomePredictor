import pandas as pd

# Sample DataFrames
df1 = pd.read_csv('./full_data_40.csv')
df1 = df1.head(10000)

df2 = pd.read_csv('./extraFeaturesForDataset.csv')


# Concatenate DataFrames along rows
result_df = pd.concat([df1, df2], axis=1)
result_df = result_df.drop(result_df.columns[0], axis=1)
result_df.to_csv("mergedDataset.csv")