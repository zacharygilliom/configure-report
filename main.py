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

df = pd.read_excel('Master Submitted Log.xlsx')
df = drop_columns(df)
df = add_columns(df)
for row in df:
	df['Received to Submitted'] = 1
print(df.head())

# # def calculate_column(df):
# 	for row in df:


# def merge_workbooks():
# 	df_final = pd.read_excel('C:\\Users\\zacha\\PycharmProjects\\configure-report\\Master Submitted Log Final.xlsx')
# 	df_final = drop_columns(df_final)
# 	df_new = pd.read_excel('C:\\Users\\zacha\\PycharmProjects\\configure-report\\Master Submitted Log.xlsx')
# 	df_new = drop_columns(df_new)
# 	df_new = add_columns(df_new)
# 	df_final = df_final.append(df_new, ignore_index=True)
# 	df_final.to_excel('C:\\Users\\zacha\\PycharmProjects\\configure-report\\Master Submitted Log Final.xlsx')
# 	df_final.to_csv(path_or_buf='C:\\Users\\zacha\\PycharmProjects\\configure-report\\MasterSubmittedCSV.csv', index=False)
# 	return df_final
# 	# return file

# print(merge_workbooks())



