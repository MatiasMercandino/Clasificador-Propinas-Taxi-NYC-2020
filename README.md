# Clasificador de Propinas para Viajes en Taxi en NYC (2020)

Inspirado en la charla "Keeping up with Machine Learning in Production" de Shreya Shankar.

Este notebook muestra la construcción de un modelo de machine learning de juguete, usando datos de viajes de los taxis amarillos de Nueva York para el año 2020, proporcionados por la NYC Taxi and Limousine Commission (TLC).

## Descripción
La idea es encontrar aquellos viajes donde la propina dejada por el pasajero fue alta, es decir, mayor al 20% del costo del viaje.

Para ello ajustaremos un modelo de clasificación binaria RandomForest usando los datos de los viajes de enero de 2020. Probaremos el modelo resultante sobre los datos de los viajes de febrero de 2020. Compararemos el desempeño del modelo en ambos casos usando la métrica de f1-score.

## Diccionario de datos
- https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Requisitos
- [Google Colab](https://colab.research.google.com/)

## Uso
- Abre el notebook en Google Colab.
- Ejecuta las celdas paso a paso para reproducir el análisis.
