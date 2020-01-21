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

def calculate_column(df):
	for index, row in df.iterrows():
		df.loc[index, 'Received to Submitted'] = wd.networkdays(row['Received'], row['Submitted'])
		df.loc[index, 'Started to Submitted'] = wd.networkdays(row['Started'], row['Submitted'])
		df.loc[index, 'Received to Started'] = wd.networkdays(row['Received'], row['Started'])
		df.loc[index, 'Place'] = row['Type'][0:2]
	return df

def create_csv(df, name):
	return df.to_csv(name)

def get_area(df, df_reference):
	df = df.merge(df_reference, on='name', how='left')
	return df

def apply_transforms(df):
	df = drop_columns(df)
	df = add_columns(df)
	df = calculate_column(df)
	df = get_area(df=df,df_reference=df_name)
	return df

def display_pivot(df):
	table = df.pivot_table(
		index=['Place','name'], 
		values=['Received to Submitted', 'Started to Submitted', 'Received to Started'], 
		aggfunc=np.mean)
	return table

df = pd.read_excel('Master Submitted Log.xlsx')
df_name = pd.read_excel('Name Log.xlsx')

df = apply_transforms(df)
print(df.head())
# create_csv(df, 'MasterSubmitted.csv')
df_table = display_pivot(df)
print(df_table)






