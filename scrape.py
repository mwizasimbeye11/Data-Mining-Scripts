import os
import pandas as pd

# Read dataset, 
corn_data = pd.read_csv('datasets/corn_maize_images.csv', error_bad_lines=False)

plant_disease_name = corn_data[['Disease common name']]
plant_disease_name = plant_disease_name.fillna('Normal')
plant_urls = corn_data[['url']]

for x in plant_disease_name.iterrows():
	print x

