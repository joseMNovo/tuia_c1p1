import csv

# clase que representa a una persona que toma cafe con sus caracteristicas
class Consumidor:
    def __init__(self, submission_id, age, gender, cups, where_drink, favorite,
                 roast_level, caffeine, education_level, employment_status):
        self.submission_id = submission_id
        self.age = age
        self.gender = gender
        self.cups = cups
        self.where_drink = where_drink  # lista de lugares
        self.favorite = favorite
        self.roast_level = roast_level
        self.caffeine = caffeine
        self.education_level = education_level
        self.employment_status = employment_status

    def __str__(self):
        return (f"Consumidor {self.submission_id}: Edad={self.age}, Género={self.gender}, "
                f"Tazas/día={self.cups}, Lugares={self.where_drink}, Café favorito={self.favorite}, "
                f"Tueste={self.roast_level}, Cafeína={self.caffeine}, Educación={self.education_level}, "
                f"Trabajo={self.employment_status}")


# funcion que lee el archivo csv y crea objetos consumidor con los datos
def cargar_consumidores(nombre_archivo):
    consumidores = {}

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # convierte la columna where_drink de texto a lista separando por comas
            lugares = fila['where_drink'].split(',') if fila['where_drink'] else []
            lugares = [lugar.strip() for lugar in lugares]

            consumidor = Consumidor(
                submission_id=fila['submission_id'],
                age=fila['age'],
                gender=fila['gender'],
                cups=fila['cups'],
                where_drink=lugares,
                favorite=fila['favorite'],
                roast_level=fila['roast_level'],
                caffeine=fila['caffeine'],
                education_level=fila['education_level'],
                employment_status=fila['employment_status']
            )

            consumidores[consumidor.submission_id] = consumidor

    return consumidores


# funcion que filtra los consumidores segun un atributo y valor especifico
def filtrar_por_atributo_valor(consumidores, atributo, valor):
    resultado = {}

    # recorre cada consumidor y verifica si coincide con el filtro pedido
    for cid, consumidor in consumidores.items():
        if hasattr(consumidor, atributo):
            valor_atributo = getattr(consumidor, atributo)

            # si el atributo es una lista busca el valor dentro de ella
            if isinstance(valor_atributo, list):
                if valor in valor_atributo:
                    resultado[cid] = consumidor
            else:
                # si no es lista compara directamente los valores
                if valor_atributo == valor:
                    resultado[cid] = consumidor

    return resultado


# codigo principal que ejecuta el programa
if __name__ == "__main__":

    consumidores = cargar_consumidores("coffee_survey.csv")

    consumidoras = filtrar_por_atributo_valor(consumidores, "gender", "Female")

    edades_mayores_44 = ["45-54 years old", "55-64 years old", "65+ years old"]

    # filtra las consumidoras mayores de 44 años
    consumidoras_mayores_44 = {}
    for cid, consumidor in consumidoras.items():
        if consumidor.age in edades_mayores_44:
            consumidoras_mayores_44[cid] = consumidor

    print("Consumidoras mayores de 44 años:")
    for consumidor in consumidoras_mayores_44.values():
        print(consumidor)