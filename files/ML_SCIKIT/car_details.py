import os
#print(os.getcwd())
#print(os.listdir())


#1. Loading the dataset
import pandas as pd
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset = pd.read_csv(os.path.join(script_dir, 'Car details.csv'))
print(f'The length of the dataset is {len(dataset)}')
print(dataset.head())


#2. Preprocessing the dataset
# Dropping the columns that we are not going to use
dataset.drop(['name'], axis =1, inplace = True) # axis = 0 means dropping the rows and 1 means columns
print(dataset.head())


# 3. Dealing with missing values 
# i. Identifying if there are any missing values
print(dataset.isna().sum())

#ii. Dropping the rows which has missing values
dataset = dataset.dropna()
print(f'The length of the dataset is {len(dataset)}.')

#4. Dealing with duplicated rows
#i. Checking if there is any duplicated rows in the dataset
print(dataset.duplicated().any()) # we use any() here to stop scanning the duplicates the moment it finds true so that it's not much time consuming even for larger datasets

#ii. Dropping all the duplicates values
dataset = dataset.drop_duplicates()
print(f'The length of the dataset after dropping duplicates is {len(dataset)}.')

#Checking the datatypes of each column 
print(dataset.dtypes)

#5. Removing units from column mileage, engine and max_power
def remove_unit(df, column_name):
    t = []
    for i in df[column_name]:
        number = str(i).split(' ')[0]
        t.append(number)
    return t
dataset['mileage'] = remove_unit(dataset, 'mileage')
dataset['engine'] = remove_unit(dataset, 'engine')
dataset['max_power'] = remove_unit(dataset, 'max_power')

#Changing the datatype from object to string
#dataset['mileage'] = dataset['mileage'].to_string() we can't do this because it's job is to render as one big string not each column
dataset['mileage'] = pd.to_numeric(dataset['mileage']) # here we are using to_numeric because (eg. "23.40" is still a string just it's unit is removed. so we need to convert it to numeric)
dataset['engine'] = pd.to_numeric(dataset['engine'])
dataset['max_power'] = pd.to_numeric(dataset['max_power'])
print(dataset.head())


# Adding 'age' column and dropping the year column
dataset['age'] = 2026 - dataset['year']
dataset.drop(['year'], axis = 1, inplace = True) #inplace = true modifies the data tdirectly instead of creating a new copy
print(dataset.head())

#Getting a summary of numerical columns
print(dataset.describe())