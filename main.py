import pandas as pd
import numpy as np

def drop_columns(df):
	for col in df.columns:
		if "Unnamed" in col:
			df.drop(columns=col, inplace=True)
	return df

def add_columns(df):
	df['Received to Submitted'] = ''
	df['Received to Started'] = ''
	df['Started to Submitted'] = ''
	return df	

def merge_workbooks(df_new, df):
	df_final = drop_columns(df)
	df_new = drop_columns(df_new)
	df_new = add_columns(df_new)
	df_final = df_final.append(df_new, ignore_index=True)
	return df_final


df = pd.read_excel('Master Submitted Log.xlsx')
df_new = pd.read_excel('Master Submitted Log New.xlsx')

final_df = merge_workbooks(df_new, df)
print(final_df.head(20))

