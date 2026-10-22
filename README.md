# proyecto-0 para programación 1
este proyecto procesa los datos meteorológicos registrados por el servicio meteorológico nacional (SMN) utilizando una programación modular en python

## estructura del proyecto
- analisis_smn.py: script principal que maneja la entrada por la terminal (usando 'sys.argv')
- funciones_smn.py: módulo que contiene las funciones para realizar la lógica del procesamiento de archivos
- datos/: carpeta contenedora de los archivos de texto con las mediciones y observaciones

## cómo ejecutar el programa:
ejecutar el script desde la terminal pasando las rutas de los archivos como argumentos
```bash
python analisis_smn.py datos/estado_tiempo20260920.txt datos/estado_tiempo20260917.txt```