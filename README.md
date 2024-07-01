Predicción de Consumo de Energía
Este repositorio pertenece a la empresa Smart Energy Technologies y se centra en la predicción e imputación de datos relacionados con el consumo de energía. Próximamente, se incorporarán variational autoencoders (VAEs) para mejorar las predicciones.
Bibliotecas Utilizadas
El proyecto utiliza las siguientes bibliotecas de Python:
Pandas,NumPy,Matplotlib,Scikit-learn,Seaborn,Statsmodels,datetime,os
Versión de Python
El código está escrito en Python 3.12.3.
Conjuntos de Datos
Los datos con valores faltantes se encuentran en archivos CSV denominados “1-11 Lecturas 2”.
El conjunto de datos combinado y limpiado se llama “combined_cleaned_data”.
Métodos de Predicción
Para las predicciones, se han utilizado los siguientes métodos:Nearest,ffill,from_derivates
El objetivo es lograr que las predicciones tengan una correlación de Pearson cercana a 1 con los datos reales. Además, se puede evalúar el rendimiento utilizando el Root Mean Square Error (RMSE).
