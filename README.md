# Procesamiento en Batch - Análisis de Demanda de Pasajeros en Colombia

Este repositorio contiene la solución para el componente de **Procesamiento en Batch** (Tarea 3 - Big Data). Se diseñó e implementó un pipeline distribuido para analizar la afluencia de pasajeros en los sistemas de transporte masivo en Colombia utilizando **Apache Spark (PySpark)** en un entorno Linux virtualizado.

---

## 📁 Archivos del Repositorio

* `batch_analysis.py`: Script principal en PySpark que ejecuta el ciclo de vida completo de análisis (lectura, transformación, agregaciones y generación de reporte).
* `Transporte.csv`: Dataset oficial extraído del portal de datos abiertos (`datos.gov.co`) con registros detallados de demanda en sistemas como TransMilenio, SITVA, MIO, Megabús, Transmetro, entre otros.

---

## 🛠️ Tecnologías Utilizadas

* **Apache Spark / PySpark**: Procesamiento en lote distribuido mediante DataFrames y RDDs.
* **Python**: Lenguaje principal de desarrollo.
* **Linux (Ubuntu) & PuTTY**: Entorno de ejecución en servidor virtualizado.
* **Matplotlib / Pandas**: Generación y renderizado de gráficos estadísticos.

---

## ⚙️ Flujo de Procesamiento Realizado

El script `batch_analysis.py` realiza automáticamente los siguientes pasos:
1. **Carga e Ingesta:** Carga del archivo `Transporte.csv` delimitado en DataFrames de Spark.
2. **Limpieza y Filtrado:** Eliminación de valores nulos, formateo de tipos de datos numeric/string y filtrado de registros inconsistentes.
3. **Análisis Exploratorio (EDA) y Agregaciones:** Cálculo de:
   * Demanda acumulada (`total_pasajeros`) por Ciudad y Sistema.
   * Promedio diario (`promedio_pasajeros`).
   * Picos máximos registrados (`max_pasajeros`).
4. **Visualización:** Generación de gráfica de barras comparativa con los resultados consolidados.

---

## 📊 Visualización de Resultados

A continuación se presenta el resultado del procesamiento en lote con la demanda acumulada por sistema:

![Total de Pasajeros por Sistema](grafica_resultados.png)

---

## 🚀 Instrucciones de Ejecución

Para ejecutar el pipeline en tu entorno local o en la máquina virtual de Spark:

1. Asegúrate de tener los archivos `batch_analysis.py` y `Transporte.csv` en el mismo directorio de trabajo.
2. Abre la terminal de Linux e inicia el procesamiento con `spark-submit`:

```bash
spark-submit batch_analysis.py
