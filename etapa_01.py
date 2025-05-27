import csv

def contar_rangos_edad(nombre_archivo: str) -> dict[str, int]:
  conteo = {}
  
  with open(nombre_archivo, 'r', encoding='utf-8') as datos:
    lector_csv = csv.reader(datos)
    
    encabezado = next(lector_csv)
    
    indice_edad = encabezado.index('age')
    
    for fila in lector_csv:
      rango_edad = fila[indice_edad]
      if rango_edad in conteo:
        conteo[rango_edad] += 1
      else:
        conteo[rango_edad] = 1

  return conteo

#print("Conteo de rangos de edad:", contar_rangos_edad("coffee_survey.csv"))

def contar_lugares_consumo(nombre_archivo: str) -> dict[str, int]:
  conteo = {}
  
  with open(nombre_archivo, 'r', encoding='utf-8') as datos:
    lector_csv = csv.reader(datos)
    
    encabezado = next(lector_csv)
    
    indice_lugar = encabezado.index('where_drink')
    
    for fila in lector_csv:
      lugar_consumo = fila[indice_lugar]
      lugares = lugar_consumo.split(', ')
      
      for lugar in lugares:
        if lugar == '':
          continue
        if lugar in conteo:
          conteo[lugar] += 1
        else:
          conteo[lugar] = 1

  return conteo

#print("Conteo de lugares de consumo:", contar_lugares_consumo("coffee_survey.csv"))

def procesamiento_columna(nombre_archivo: str, columna: str) -> dict[str, int]:
    conteo = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as datos:
        lector_csv = csv.reader(datos)
        
        encabezado = next(lector_csv)
        
        indice_columna = encabezado.index(columna)
        
        for fila in lector_csv:
            valor = fila[indice_columna]
            
            if columna == 'where_drink':
                valores = valor.split(', ')
                for v in valores:
                    if v == '':
                        continue
                    if v in conteo:
                        conteo[v] += 1
                    else:
                        conteo[v] = 1
            elif columna == 'brew':
                valores = valor.split(', ')
                for v in valores:
                    v = v.strip()
                    if v == '':
                        continue
                    if v in conteo:
                        conteo[v] += 1
                    else:
                        conteo[v] = 1
            else:
                if valor in conteo:
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
