import csv

# cuenta cuantas personas hay en cada rango de edad
def contar_rangos_edad(nombre_archivo: str) -> dict[str, int]:
  conteo = {}
  
  with open(nombre_archivo, 'r', encoding='utf-8') as datos:
    lector_csv = csv.reader(datos)
    
    encabezado = next(lector_csv)
    
    indice_edad = encabezado.index('age')
    
    # recorre cada fila y suma 1 al contador del rango de edad correspondiente
    for fila in lector_csv:
      rango_edad = fila[indice_edad]
      if rango_edad in conteo:
        conteo[rango_edad] += 1
      else:
        conteo[rango_edad] = 1

  return conteo

#print("Conteo de rangos de edad:", contar_rangos_edad("coffee_survey.csv"))

# cuenta cuantas personas toman cafe en cada lugar
def contar_lugares_consumo(nombre_archivo: str) -> dict[str, int]:
  conteo = {}
  
  with open(nombre_archivo, 'r', encoding='utf-8') as datos:
    lector_csv = csv.reader(datos)
    
    encabezado = next(lector_csv)
    
    indice_lugar = encabezado.index('where_drink')
    
    # recorre cada fila, separa los lugares por coma y suma 1 al contador de cada lugar
    for fila in lector_csv:
      lugares = fila[indice_lugar].split(', ')
      
      for lugar in lugares:
        if lugar == '':
          continue
        if lugar in conteo:
          conteo[lugar] += 1
        else:
          conteo[lugar] = 1

  return conteo

#print("Conteo de lugares de consumo:", contar_lugares_consumo("coffee_survey.csv"))

# funcion general que cuenta valores en cualquier columna del csv
def procesamiento_columna(nombre_archivo: str, columna:str) -> dict[str,int]:

   conteo = {}

   with open(nombre_archivo, 'r', encoding='utf-8') as datos:
    lector_csv = csv.reader(datos)
    
    encabezado = next(lector_csv)
    
    indice = encabezado.index(columna)
    
    # recorre cada fila, separa por coma si hay varios valores y cuenta cada uno
    for fila in lector_csv:
      valores = fila[indice].split(", ")
      
      for valor in valores:
        if valor == '':
          continue
        elif valor in conteo:
          conteo[valor] += 1
        else:
          conteo[valor] = 1
    
    
    if "NA" in conteo:
        del conteo["NA"]
    
    return conteo

# Prueba
print("Conteo de age:", procesamiento_columna("coffee_survey.csv", "age"))
print("-" * 50)
print("Conteo de lugares de consumo:", procesamiento_columna("coffee_survey.csv", "where_drink"))
print("-" * 50)
print("Conteo de cups:", procesamiento_columna("coffee_survey.csv", "cups"))
print("-" * 50)
print("Conteo de brew:", procesamiento_columna("coffee_survey.csv", "brew"))
print("-" * 50)
