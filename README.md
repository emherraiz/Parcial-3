# Parcial-3

## Link del repositorio

https://github.com/emherraiz/Parcial-3

## Enunciado

Descripción de la actividad
Pasos para realizar la práctica

1)     Leer los datos con python. Ficheros de navegación y de conversión

2)     Separar los datos en columnas, y obtener para cada línea de navegación: campaña, adgoup, advertisement y site link que se obtiene de la columna URL.

3)     Identificar si hay usuarios repetidos: id_user, gclid, cookie

Para los que no tienen id_user, hay que mirar el gclid, y si tampoco está hay que mirar la cookie

Y ordenar los datos según ts

4)     Unir los datos de navegación ya tratados con los datos de conversiones,creando una columna de 0 y 1 indicando si el usuario no ha convertido o si ha convertido. La unión se hace a partir de la columna id_suite, si esta está vacía sería por la de gclid, y si esta está vacía también por cookie.

Nota: tenemos 2 opciones

a)     Si hay usuarios repetidos nos quedamos con un solo dato

b)     Si nos quedamos con todos los datos repetidos buscar el más cercano a la conversión (este punto es más complicado, es solo para quienes se atrevan)

1)     Con estos datos ya unidos y tratados debemos realizar diferentes informes que se proponen en el apartado siguiente (Entrega individual)
