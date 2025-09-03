# StatisticsOnMachineLearning

Este repositorio está dedicado al estudio y aplicación de la estadística en aprendizaje automático, combinando fundamentos teóricos con implementaciones prácticas en Python.

<p align="center">
  <img src="/images/QRcode.png" alt="Qr" width="180" style="margin-right:40px;"/>
  <img src="/images/Octocat.png" alt="Octocat" width="180"/>
</p>

---

# Class README

Bienvenidos a esta clase, donde exploraremos conceptos fundamentales de estadística aplicados al aprendizaje automático mediante ejemplos prácticos y ejercicios guiados.

---

## Contenido

### Planeación, obtención e interpretación de información
- Tipo de muestra  
- Parámetros que analizar  
- Población  
- Tamaño de muestra  
- Tipos de errores estadísticos  
- Software de análisis estadístico  

### Evaluaciones y mediciones estadísticas en investigación
- Tipo de orden en los resultados  
- Estadística descriptiva  
- Tipo de prueba estadística  
- Regresión simple  
- Prueba de resultados por categoría  
- Prueba para variables paramétricas  
- Prueba para variables no paramétricas  
- Análisis de varianza  

---

## Estructura
- `Python/`: notebooks con ejemplos y demostraciones.  
- `utils/`: scripts para generar figuras educativas (encuestas, población vs. muestra, Venn).  
- `images/`: recursos gráficos utilizados en el README.  
- `requirements.txt`: dependencias recomendadas.  

---

## Requisitos
- Python 3.8+  
- Librerías recomendadas:  
  - numpy  
  - pandas  
  - matplotlib  
  - scipy  
  - scikit-learn  
- (Opcional) Uso de entorno virtual:  
  ```bash
  python -m venv venv
  # En Linux/Mac
  source venv/bin/activate
  # En Windows (PowerShell)
  .\venv\Scripts\Activate.ps1
  ```

---

## Instrucciones

1. Clona el repositorio  
   ```bash
   git clone <url>
   cd StatisticsOnMachineLearning
   ```

2. Instala las dependencias  
   ```bash
   pip install -r requirements.txt
   ```

3. Explora los notebooks en `Python/` y los scripts en `utils/`.

4. Ejecuta los ejemplos y ejercicios para reforzar los conceptos.

---

## Cómo ejecutar los scripts de `utils/`
- Encuesta (gráfico de pastel):  
  ```bash
  python utils/encuestas.py  # genera encuesta.png
  ```
- Diagrama tipo Gantt (población, muestra y split 80/20):  
  ```bash
  python utils/poblacionMuestra.py  # genera gantt_poblacion_muestra_split.png
  ```
- Diagrama de Venn (población vs muestra):  
  ```bash
  python utils/poblacionMuestraVenn.py  # genera venn_poblacion_muestra.png
  ```

---

## Recursos adicionales
- Documentación oficial de Python: https://docs.python.org/3/
- Numpy: https://numpy.org/doc/
- Pandas: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/documentation.html
- Matplotlib: https://matplotlib.org/stable/users/index.html

---

## Temas de la clase
Consulta `Temas.txt` para un listado sintético de los temas cubiertos.

---

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar el contenido o agregar ejemplos, por favor abre un Pull Request o crea un Issue.

---

## Contacto
Para dudas o sugerencias, contacta al mantenedor.

