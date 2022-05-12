import pandas as pd
import re

# Lectura
navegacion = pd.read_csv('navegacion.csv', sep = ';')
conversiones = pd.read_csv('conversiones.csv', sep = ';')


df_url = navegacion.loc[:, 'url_landing']
df_url.to_csv('url_landing.csv', index = False)
df_url = pd.read_csv('url_landing.csv', sep = '&')

print(df_url.iloc[1][:])

df_url.to_csv('prueba.csv')
print(df_url.head())
