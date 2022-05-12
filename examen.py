import pandas as pd
import re

# Lectura
navegacion = pd.read_csv('navegacion.csv', sep = ';')
conversiones = pd.read_csv('conversiones.csv', sep = ';')

# Sacamos nuevas columnas a partir de la url
df_url = navegacion.loc[:, 'url_landing']
df_url.to_csv('url_landing.csv', index = False)
df_url = pd.read_csv('url_landing.csv', sep = '&')

# df_url.colums = ['url_landing', 'idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec']

df_url = pd.read_csv('prueba.csv', sep = ',')
columnas = df_url.columns
df_url = df_url.drop([columnas[len(columnas) - 1]], axis = 1)

# Concatenamos todos los datos
navegacion = navegacion.drop(['url_landing'], axis = 1)
df = pd.concat([navegacion, df_url], axis = 1)
df = df.drop_duplicates()

print(df.head())
df.to_csv('Url_final.csv', index = False)

convertidos = 0
usarios_navegando = df["id_user"]
usuarios_convertidos = conversiones["id_user"]
for user_nav in usarios_navegando:
    for user_conv in usuarios_convertidos:
        if user_nav == user_conv:
            convertidos += 1

print(f'Se han convertido {convertidos} personas, que son un {round(convertidos / df.shape[0] * 100, 2)} % de los usuarios que tenemos en la base de datos')


