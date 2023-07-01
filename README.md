# nw-detest-wv
DE test for on demand ingestion and analysis using python

Proof of Concept setup using 

# Restricciones
- La solución debe estar implementada en un notebook .ipynb usando python 3
- La solución debe ser escalable a 100 millones de entradas. Se recomienda simplificar los datos mediante un modelo de datos. Agregue pruebas de que la solución es escalable.
- La solución debe estar escrita en Python usando una base de datos SQL
# Requisitos

1. Procesos automatizados para ingerir y almacenar los datos bajo demanda
    - Los viajes que son similares en términos de origen, destino y hora del día deben agruparse. Describa el enfoque que utilizó para agregar viajes similares.
2. Un servicio que es capaz de proporcionar la siguiente funcionalidad:
    - Devuelve el promedio semanal de la cantidad de viajes para un área definida por un bounding box y la región
    - Informar sobre el estado de la ingesta de datos sin utilizar una solución de polling

# Diseño

Se desarrolla la solucion en una jupyter notebook, y como backend se utiliza sqlite, ya que para una prueba de concepto es suficiente, ya que no requiere ninguna configuracion extra y para el uso de un unico usuario es factible su uso, sobra decir que para una solucion productiva se deberia desplegar una base de datos mysql o postgres o conectarse a solucion corporativa disponible
Para monitorear o reportar sobre el proceso de ingesta, se puede usar un servicio de 'message queue' como pub/sub en GCP, para que al iniciar y terminar la carga de datos se envie un mensaje desde la db y esto sea procesado por la notebook. esto no fue configurado ya que no esta conectado el servicio en este repositorio.
Ya que no se define un criterio de similitud en los requerimientos, decidi agrupar por bins/buckets tanto de coordenadas como de tiempo, redondeando las coordenadas a 3 decimales o aproximadamente un grid de ~110m, y el tiempo a viajes dentro de la misma hora de 0 a 59 minutos
Para la contenerizacion de la solucion se utiliza docker composer, que es suficiente para manejar la prueba de concepto, para una solucion productiva lo recomendado es esar kubernetes para orquestracion sin embargo, es factible utilizar docker composer en este caso ya que la complejidad de servicios es minima.
Aunque es completamente innecesario seperar la instancia de sqlite en su propio contenedor para este uso, lo hice con la intencion de demostrar las buenas practicas al momento de contenerizar una aplicacion (1 servicio por contenedor) y de permitir el cambio de db sin afectar el diseño inicial.

Los supuestos asumidos son que la data no trae duplicados
