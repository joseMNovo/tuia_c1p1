import matplotlib.pyplot as plt
from collections import defaultdict, Counter

class Encuesta:
    def __init__(self, archivo: str):
        self.consumidores = cargar_consumidores(archivo)

        self.cantidades_grupos_etarios = self.analizar_rangos_edades()
        self.cantidades_generos = self.analizar_generos()
        self.cafe_favorito_por_grupo_etario = self.analizar_cafe_favorito_por_grupos_etarios()
        self.nivel_de_tueste_preferido_por_genero = self.analizar_nivel_de_tueste_por_genero()
        self.maximo_nivel_educativo = self.calcular_maximo_nivel_educativo()

    def analizar_rangos_edades(self) -> dict[str, int]:
        # cuenta cuántas personas hay en cada grupo de edad
        conteo = defaultdict(int)
        for consumidor in self.consumidores.values():
            conteo[consumidor.age] += 1
        return dict(conteo)

    def analizar_generos(self) -> dict[str, int]:
        # cuenta cuántas personas hay de cada género
        conteo = defaultdict(int)
        for consumidor in self.consumidores.values():
            conteo[consumidor.gender] += 1
        return dict(conteo)

    def analizar_cafe_favorito_por_grupos_etarios(self) -> dict[str, dict[str, int]]:
        # para cada grupo de edad, cuenta qué café es el favorito
        resultado = {}

        for consumidor in self.consumidores.values():
            grupo = consumidor.age
            cafe = consumidor.favorite

            if grupo not in resultado:
                resultado[grupo] = {}

            if cafe not in resultado[grupo]:
                resultado[grupo][cafe] = 0

            resultado[grupo][cafe] += 1

        return resultado

    def analizar_nivel_de_tueste_por_genero(self) -> dict[str, dict[str, int]]:
        # para cada género, cuenta qué nivel de tueste prefiere
        resultado = {}

        for consumidor in self.consumidores.values():
            genero = consumidor.gender
            tueste = consumidor.roast_level

            if genero not in resultado:
                resultado[genero] = {}

            if tueste not in resultado[genero]:
                resultado[genero][tueste] = 0

            resultado[genero][tueste] += 1

        return resultado

    def calcular_maximo_nivel_educativo(self) -> str:
        # cuenta cuál es el nivel educativo que aparece más veces
        conteo = Counter()
        for consumidor in self.consumidores.values():
            conteo[consumidor.education_level] += 1
        return conteo.most_common(1)[0][0] if conteo else None

    def graficar_grupos_etarios(self) -> None:
        # crea un gráfico circular que muestra la distribución por grupo de edad
        etiquetas = list(self.cantidades_grupos_etarios.keys())
        cantidades = list(self.cantidades_grupos_etarios.values())

        plt.figure(figsize=(8, 8))
        plt.pie(cantidades, labels=etiquetas, autopct='%1.1f%%', startangle=140)
        plt.title('Distribución por grupo etario')
        plt.axis('equal')
        plt.show()

    def graficar_cafe_favorito_por_grupos_etarios(self) -> None:
        # para cada grupo de edad, crea un gráfico de barras mostrando qué café prefieren
        for grupo_etario, cafes in self.cafe_favorito_por_grupo_etario.items():
            labels = list(cafes.keys())
            valores = list(cafes.values())

            plt.figure(figsize=(8, 4))
            plt.bar(labels, valores, color='tan')
            plt.title(f'Café favorito - {grupo_etario}')
            plt.xlabel('Café')
            plt.ylabel('Cantidad de consumidores')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
  
    def graficar_niveles_educativos(self) -> None:
        # crea un gráfico de barras que muestra cuántas personas hay en cada nivel educativo
        conteo = Counter()
        for c in self.consumidores.values():
            if c.education_level != 'NA':
                conteo[c.education_level] += 1

        labels = list(conteo.keys())
        valores = list(conteo.values())

        plt.figure(figsize=(7, 4))
        plt.bar(labels, valores, color='darkcyan')
        plt.title('Distribución del nivel educativo')
        plt.xlabel('Nivel educativo')
        plt.ylabel('Cantidad de consumidores')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def graficar_tueste_por_genero(self) -> None:
        # para cada género, crea un gráfico de barras mostrando qué nivel de tueste prefieren
        for genero, tuestes in self.nivel_de_tueste_preferido_por_genero.items():
            labels = list(tuestes.keys())
            valores = list(tuestes.values())

            plt.figure(figsize=(6, 4))
            plt.bar(labels, valores, color='sienna')
            plt.title(f'Nivel de tueste preferido - {genero}')
            plt.xlabel('Nivel de tueste')
            plt.ylabel('Cantidad de consumidores')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

# ejecuta todo el programa:
# 1. crea una encuesta con los datos del archivo
# 2. muestra el nivel educativo más común
# 3. muestra todos los gráficos
encuesta = Encuesta("coffee_survey.csv")
print("Nivel educativo más común:", encuesta.maximo_nivel_educativo)
encuesta.graficar_grupos_etarios()
encuesta.graficar_cafe_favorito_por_grupos_etarios()
encuesta.graficar_tueste_por_genero()
encuesta.graficar_niveles_educativos()
