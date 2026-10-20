# Tarea 3 - Procesamiento Batch y Análisis de Datos Masivos (UNAD)

Este repositorio contiene la solución para el componente de **Procesamiento en Batch** de la Tarea 3 del curso de Big Data. Se implementó un pipeline completo de análisis sobre la demanda de pasajeros de transporte masivo en Colombia utilizando **Apache Spark (PySpark)** en un entorno putty.

---

## 📁 Archivos del Repositorio
* **`batch_analysis.py`**: Script principal en PySpark que realiza la carga, limpieza, agregaciones y visualización de datos.
* **`Transporte.csv`**: Dataset oficial extraído del portal de datos abiertos de Colombia (`datos.gov.co`) con registros de afluencia de pasajeros en sistemas como Transmilenio, MIO, SITVA, Megabús, entre otros.

---

## 🛠️ Tecnologías Utilizadas
* **Apache Spark (PySpark)**: Motor de procesamiento distribuido en lote.
* **Python**: Lenguaje de programación base.
* **Linux / PuTTY**: Entorno de ejecución en Máquina Virtual.

---

## 🚀 Instrucciones de Ejecución

Para ejecutar el proyecto en tu entorno local o virtual de Spark:

1. Asegúrate de tener los archivos `batch_analysis.py` y `Transporte.csv` en el mismo directorio de trabajo.
2. Abre la terminal de Linux y ejecuta el siguiente comando:

```bash
spark-submit batch_analysis.py
