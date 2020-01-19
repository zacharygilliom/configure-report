import pandas as pd 
import numpy as np
import datetime as datetime
import workdays as wd
from datetime import *

# def clean_dates(df, col):
	# df[col] = df[col].astype('datetime64[D]')
	# print(df.dtypes)
	# return df

# def merge_workbooks(df_new, df):
# 	df_new = drop_columns(df_new)
# 	df_new = add_columns(df_new)
# 	df_final = df.append(df_new, ignore_index=True)
# 	return df_final


df = pd.read_excel('Master Submitted Log.xlsx')

# df['Received'] = df['Received'].values.astype('datetime64[D]')
# df['Submitted']
# df = clean_dates(df, 'Received')
# df = clean_dates(df, 'Submitted')
# df = clean_dates(df, 'Started')

print(df.dtypes)

for index, row in df.iterrows():
	x = wd.networkdays(row['Received'], row['Submitted'])
	print(x-1)


print(df.head())