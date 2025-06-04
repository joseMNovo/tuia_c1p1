import csv

# 7 
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


# 8 
def cargar_consumidores(nombre_archivo):
    consumidores = {}

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # convierte: (where_drink) de texto a lista
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


# 9 
def filtrar_por_atributo_valor(consumidores, atributo, valor):
    resultado = {}

    for cid, consumidor in consumidores.items(): #cid = clave del id del consumidor, lo elegui para una variable en el bucle
        # condicional para verificar q tenga atributo, importante
        if hasattr(consumidor, atributo):
            valor_atributo = getattr(consumidor, atributo)

            # en el caso que el atributo sea unna lista (como where_drink), verificamos si el valor está dentro
            if isinstance(valor_atributo, list):
                if valor in valor_atributo:
                    resultado[cid] = consumidor
            else:
                # sino si es un valor simple, verificamos igualdad
                if valor_atributo == valor:
                    resultado[cid] = consumidor

    return resultado


# 10 
if __name__ == "__main__":

    consumidores = cargar_consumidores("coffee_survey.csv")

    consumidoras = filtrar_por_atributo_valor(consumidores, "gender", "Female")

    edades_mayores_44 = ["45-54 years old", "55-64 years old", "65+ years old"]

    # un bucle para filtrar los +44
    consumidoras_mayores_44 = {}
    for cid, consumidor in consumidoras.items():
        if consumidor.age in edades_mayores_44:
            consumidoras_mayores_44[cid] = consumidor

    print("Consumidoras mayores de 44 años:")
    for consumidor in consumidoras_mayores_44.values():
        print(consumidor)