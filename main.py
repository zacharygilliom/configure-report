import pandas as pd
import numpy as np
import workdays as wd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style="darkgrid")

# Excel Data File gets created with blank columns.  We want to take those out.
def drop_columns(df):
	for col in df.columns:
		if "Unnamed" in col:
			df.drop(columns=col, inplace=True)
	return df

# We want to do some calculations for our analysis later.  Creating empty columns
def add_columns(df):
	df['Received to Submitted'] = ''
	df['Received to Started'] = ''
	df['Started to Submitted'] = ''
	df['Place'] = ''
	return df	

# We now want to populate our calculated columns. 
def calculate_column(df):
	for index, row in df.iterrows():
		df.loc[index, 'Received to Submitted'] = wd.networkdays(row['Received'], row['Submitted'])
		df.loc[index, 'Started to Submitted'] = wd.networkdays(row['Started'], row['Submitted'])
		df.loc[index, 'Received to Started'] = wd.networkdays(row['Received'], row['Started'])
		df.loc[index, 'Place'] = row['Type'][0:2]
	return df

def create_csv(df, name):
	return df.to_csv(name)

# When showing our data, it's really usefule to have just the location data.
def get_area(df, df_reference):
	df = df.merge(df_reference, on='name', how='left')
	return df

# So that we don't have to use multiple lines to call the functions, lets do it in a single function so we don't have so many 
# local variables.
def apply_transforms(df):
	df = drop_columns(df)
	df = add_columns(df)
	df = calculate_column(df)
	df = get_area(df=df,df_reference=df_name)
	df = get_category(df=df, df_reference=df_category)
	return df

# This is a simple pivot of some of our data that we want to use for calculation.
def display_location_pivot(df):
	table = df.pivot_table(
		index=['Place','name'], 
		values=['Received to Submitted', 'Started to Submitted', 'Received to Started'], 
		aggfunc=np.mean)
	return table

def display_type_pivot(df):
	table = df.pivot_table(
		index='Type',
		values='Received to Submitted',
		aggfunc=np.mean)
	return table

# this will hep us create our category to organize our Received to Submitted Data.
# Want to try to find a better way of doing this. Dictionary?  Custom Function?
def create_category(df):
	df['Category'] = ''
	for index, row in df.iterrows():
		if row['Received to Submitted'] == 0:
			df.loc[index, 'Category'] = '1'
		elif row['Received to Submitted'] == 1:
			df.loc[index, 'Category'] = '1'
		elif row['Received to Submitted'] == 2:
			df.loc[index, 'Category'] = '2'
		elif row['Received to Submitted'] == 3:
			df.loc[index, 'Category'] = '3'
		elif row['Received to Submitted'] == 4:
			df.loc[index, 'Category'] = '4'
		elif row['Received to Submitted'] == 5:
			df.loc[index, 'Category'] = '5'
		elif row['Received to Submitted'] == 6:
			df.loc[index, 'Category'] = '6'
		elif row['Received to Submitted'] == 7:
			df.loc[index, 'Category'] = '7'
		elif row['Received to Submitted'] == 8:
			df.loc[index, 'Category'] = '8'
		elif row['Received to Submitted'] == 9:
			df.loc[index, 'Category'] = '9'
		elif row['Received to Submitted'] == 10:
			df.loc[index, 'Category'] = '10'
		elif 11 <= row['Received to Submitted'] <= 20:
			df.loc[index, 'Category'] = '11-20'
		elif 21 <= row['Received to Submitted'] <=30:
			df.loc[index, 'Category'] = '21-30'
		elif 31 <= row['Received to Submitted'] <= 60:
			df.loc[index, 'Category'] = '31-60'
		elif row['Received to Submitted'] >= 61:
			df.loc[index, 'Category'] = '61+'
	return df

# this will merge our category dataframe with our master dataframe, so we can get our category on our
# main dataframe.
def get_category(df, df_reference):
	df = df.merge(df_reference, on='Received to Submitted', how='left')
	return df

def slice_name(df, val):
	df = df[df['name'] == val]
	return df

# Import both our main spreadhseet and our reference table
df = pd.read_excel('Master Submitted Log.xlsx')
df_name = pd.read_excel('Name Log.xlsx')

# Create Dataframe of another reference table.
df_category = pd.DataFrame({'Received to Submitted': [i for i in range(0,200)]})
df_category = create_category(df_category)

# Apply all of our transformation functionsto our dataframe and save it as a CSV file
df = apply_transforms(df)
# create_csv(df, 'MasterSubmitted.csv')

# Create our two pivot tables and print them out
df_location_table = display_location_pivot(df)
df_type_table = display_type_pivot(df)
print(df_location_table, df_type_table)

# simple barplots to show some of our data
# sns.barplot(x=df['Type'], y=df['Received to Started'], hue=df['name'], palette="Dark2")
# sns.barplot(x=df['Type'], y=df['Started to Submitted'], hue=df['name'], palette="Dark2")
# sns.barplot(x=df['Type'], y=df['Received to Submitted'], hue=df['name'], palette="Dark2")
# sns.catplot(x='name', y='Received to Submitted', kind='bar', data=df, hue='Type')
# plt.show()


# Added Distribution plots of some of our calculations.
# sns.kdeplot(data=df['Received to Submitted'], shade=False )
# sns.kdeplot(data=df['Started to Submitted'], shade=False)
# sns.kdeplot(data=df['Received to Started'], shade=False)
# plt.show() 

# some more EDA

# sns.barlot(x=df[df['Place'] == 'JT']['name'], y=df['Received to Submitted'], palette="Dark2")
for company in df.name.unique():
	sns.kdeplot(data=df[df['name'] == company]['Received to Submitted'], shade=False, label=company)

plt.show()