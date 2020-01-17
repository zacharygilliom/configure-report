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
	return df	

def merge_workbooks(df_new, df):
	df_new = drop_columns(df_new)
	df_new = add_columns(df_new)
	df_final = df.append(df_new, ignore_index=True)
	return df_final

def calculate_column(df):
	for index, row in df.iterrows():
		days_received_to_submit = wd.networkdays(row['Received'], row['Submitted'])
		df.loc[index, 'Received to Submitted'] = days_received_to_submit
		days_start_to_submit = wd.networkdays(row['Started'], row['Submitted'])
		df.loc[index, 'Started to Submitted'] = days_start_to_submit
		days_received_to_start = wd.networkdays(row['Received'], row['Started'])
		df.loc[index, 'Received to Started'] = days_received_to_start
	return df

df = pd.read_excel('Master Submitted Log.xlsx')
df_new = pd.read_excel('Master Submitted Log New.xlsx')


df = merge_workbooks(df_new, df)
df = calculate_column(df)
print(df)

# final_df = merge_workbooks(df_new, df)
# final_df = calculate_column(final_df)
# final_df = clean_dates(final_df)
# print(df_new)
