# Implementando un modelo de Random Forest como clasificador de Propinas para Viajes en Taxi en NYC (2020)

Inspirado en la charla "Keeping up with Machine Learning in Production" de Shreya Shankar.

Este notebook muestra la construcción de un modelo de machine learning, usando datos de viajes de los taxis amarillos de Nueva York para el año 2020, proporcionados por la NYC Taxi and Limousine Commission (TLC).

## Descripción
La idea es encontrar aquellos viajes donde la propina dejada por el pasajero fue alta, es decir, mayor al 20% del costo del viaje.

Para ello ajustaremos un modelo de clasificación binaria RandomForest usando los datos de los viajes de enero de 2020. Probaremos el modelo resultante sobre los datos de los viajes de febrero de 2020. Compararemos el desempeño del modelo en ambos casos usando la métrica de f1-score.

## Estructura
proyecto/
├── documentos/
│ └── diccionario_de_datos.pdf
├── model/
│ └── random_forest_enero.joblib
├── notebook/
│ └── .notebook_final
├── src/
│ ├── init.py
│ ├── load_data.py
│ ├── features.py
│ ├── visualización.py
│ └── README.md
└── requirements.txt


## Uso

1. Descarga el repositorio

2. Importa las carpetas y librerias

3. Carga los datos y utiliza las funciones que vienen dentro de las librerias importadas
- load_data.py: Función para cargar los datos.
- features.py: Funciones para el preprocesamiento y comparación de distribuciones.

4. Ejecuta el notebook


