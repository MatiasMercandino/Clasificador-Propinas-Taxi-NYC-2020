# Test de Kolmogorov-Smirnov (KS)
El test de Kolmogorov-Smirnov (KS) se utiliza para proporcionar una visión más profunda de por qué el rendimiento del modelo varía entre los meses. Aunque las métricas de rendimiento (accuracy, precision, recall, F1-score) te dicen cómo está funcionando el modelo, no te explican por qué está funcionando de esa manera. Aquí es donde el test de KS resulta útil.

## Propósito del Test de Kolmogorov-Smirnov
1- Identificar cambios en los datos:
- El test KS compara las distribuciones de las características entre los datos de entrenamiento (enero) y los datos de prueba (cada mes restante).
- Si las distribuciones de las características cambian significativamente entre meses, esto puede explicar por qué el modelo tiene un rendimiento variable.

2- Validar la consistencia de los datos:
- Verifica si los datos de prueba provienen de la misma distribución que los datos de entrenamiento.
- Ayuda a detectar cambios en la población de datos o en el comportamiento subyacente, que podrían afectar el rendimiento del modelo.
