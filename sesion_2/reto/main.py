import pandas as pd

path = 'spotify_data.csv' 

spotify_data = pd.read_csv(path, encoding = 'latin1')

print(type(spotify_data))

print(spotify_data)