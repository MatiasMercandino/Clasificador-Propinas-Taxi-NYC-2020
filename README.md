# Implementando un modelo de Random Forest como clasificador de Propinas para Viajes en Taxi en NYC (2020)

Inspirado en la charla "Keeping up with Machine Learning in Production" de Shreya Shankar.

Este notebook muestra la construcción de un modelo de machine learning, usando datos de viajes de los taxis amarillos de Nueva York para el año 2020, proporcionados por la NYC Taxi and Limousine Commission (TLC).

## Descripción
La idea es encontrar aquellos viajes donde la propina dejada por el pasajero fue alta, es decir, mayor al 20% del costo del viaje.

Para ello ajustaremos un modelo de clasificación binaria RandomForest usando los datos de los viajes de enero de 2020. Probaremos el modelo resultante sobre los datos de los viajes de febrero de 2020. Compararemos el desempeño del modelo en ambos casos usando la métrica de f1-score.

## Estructura y Uso
proyecto/
├── data/
│ └── .gitkeep
├── documentos/
│ └── diccionario_de_datos.pdf
├── model/
│ └── random_forest_enero.joblib
├── notebook/
│ └── .gitkeep
├── src/
│ ├── init.py
│ ├── dataset.py
│ ├── features.py
│ ├── visualization.py
│ └── README.md
└── requirements.txt



## Instalación

1. Clonar el repositorio:

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd proyecto

2. Crear un entorno virtual e instalar las dependencias:

python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt

3. Asegúrate de tener los datos necesarios en la carpeta data.

4. Estructura de los Archivos en src
- dataset.py: Función para cargar los datos.
- features.py: Funciones para el preprocesamiento y comparación de distribuciones.
- visualization.py: Funciones para la visualización de la importancia de las características.



