import pandas as pd
import numpy as np
import workdays as wd


def drop_columns(df):
	for col in df.columns:
		if "Unnamed" in col:
			df.drop(columns=col, inplace=True)
	return df

def add_columns(df):
	df['Received to Submitted'] = ''
	df['Received to Started'] = ''
	df['Started to Submitted'] = ''
	df['Place'] = ''
	return df	

# def merge_workbooks(df_new, df):
# 	df_new = drop_columns(df_new)
# 	df_new = add_columns(df_new)
# 	df_final = df.append(df_new, ignore_index=True)
# 	return df_final

def calculate_column(df):
	for index, row in df.iterrows():
		df.loc[index, 'Received to Submitted'] = wd.networkdays(row['Received'], row['Submitted'])
		df.loc[index, 'Started to Submitted'] = wd.networkdays(row['Started'], row['Submitted'])
		df.loc[index, 'Received to Started'] = wd.networkdays(row['Received'], row['Started'])
		df.loc[index, 'Place'] = row['Type'][0:2]
	return df

def create_csv(df, name):
	return df.to_csv(name)

df = pd.read_excel('Master Submitted Log.xlsx')
# df_new = pd.read_excel('Master Submitted Log New.xlsx')

# df = merge_workbooks(df_new, df)
df = drop_columns(df)
df = add_columns(df)
df = calculate_column(df)

create_csv(df, 'MasterSubmitted.csv')





