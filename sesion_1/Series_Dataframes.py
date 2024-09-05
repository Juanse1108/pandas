#Vamos a importar la biblioteca Pandas y la llamamos pd
import pandas as pd
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],
    #index=[1,7,10,30]
)
psg_dict = { 1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}
psg_players_dict = pd.Series(psg_dict)
#print(psg_players)
print(psg_players_dict)
print(psg_players_dict[7])
print(psg_players_dict[0:3])

dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [1.91, 1.95, 1.78, 1.93],
        'Goles': [2, 0, 0, 1]}

# Crear un dataframe a partir de un diccionario y indices personalizados
df = pd.DataFrame(dict, index=[1, 7, 10, 30])
print(df)