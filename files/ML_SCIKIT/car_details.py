import os
#print(os.getcwd())
#print(os.listdir())


#1. Loading the dataset
import pandas as pd
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset = pd.read_csv(os.path.join(script_dir, 'Car details.csv'))
print(f'The length of the dataset is {len(dataset)}')
print(dataset.head())


