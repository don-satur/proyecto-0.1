# Proyecto-0.1 para programación 1
Este proyecto procesa, analiza y convierte datos meteorológicos registrados por el servicio meteorológico nacional (SMN) utilizando una programación modular en python, manejando rutas con 'pathlib', detección de codificaciones ('utf-8' y 'latin-1') y manejo de datos en formato JSON

## Estructura del proyecto:
- Analisis_smn.py: script principal que maneja la entrada por la terminal (usando 'sys.argv')
- Funciones_smn.py: módulo que contiene las funciones para el procesamiento de los archivos, cálculos estadísticos y serialización
- datos/: carpeta contenedora de texto (.txt) con las mediciones y observaciones meteorológicas
- obs_json/: carpeta contenedora de los archivos generados en formato .json con fechas convertidas a formato 'ISO 8601'

## De dónde salen los datos:
Los datos se obtienen de la página oficial del SMN:
1. Ingresar a la página de descarga de datos: https://www.smn.gob.ar/descarga-de-datos
2. Descargar el archivo comprimido (.rar) correspondiente a las observaciones actuales
3. Descomprimir el archivo .rar descargado
4. Mover el archivo .txt resultante dentro de la carpeta datos/ del repositorio

## Cómo ejecutar el programa y su salida esperada:
El programa tiene varios posibles modos de ejecución y salidas desde la terminal dependiendo de los argumentos cargados:
- Sin argumentos:
   Muestra el conteo de archivos en las carpetas 'datos/' y 'obs_json/'
```bash
python3 analisis_smn.py
```
Salida esperada:
```text
aviso, no se indicó ningún archivo para procesar
archivos .txt en 'datos/': ...
archivos .json en 'obs_json/': ...
```

- Demasiados argumentos:
   Más de un archivo pasado como parámetro
```bash
python3 analisis_smn.py datos/observaciones_smn.txt datos/observaciones_1_smn.txt
```
Salida esperada:
```text
aviso, se pasaron demasiados argumentos, el programa terminará sin hacer nada
```

- Procesar un archivo de texto (.txt):
   Genera el resumen de los datos en la terminal y guarda el 'JSON' en 'obs_json/'
```bash
python3 analisis_smn.py datos/observaciones_smn.txt
```
Salida esperada:
```text
archivo del SMN, convirtiendo a json...
===== RESUMEN DE OBSERVACIONES =====
periodo de observaciones: desde 09/09/2026 15:00 hasta 10/09/2026 13:00
total de ciudades procesadas:  121
ciudades con datos completos:  25
horarios reportados:  09:00, 10:00, 11:00, 12:00, 13:00, 15:00
----------------------------------------
top 5 temperaturas más altas: 
  -Rivadavia: 28.0 °C
  -Orán: 27.4 °C
  -Pcia. Roque Saenz Peña: 26.7 °C
  -Tartagal: 26.4 °C
  -Resistencia: 26.3 °C

top 5 temperaturas más bajas:
  -Base Belgrano II: -28.6 °C
  -Base San Martín: -24.8 °C
  -Base Orcadas: -24.3 °C
  -Base Marambio: -15.5 °C
  -Base Esperanza: -9.5 °C
  ...
  ...
el directorio 'obs_json' no existe, creándolo...
convirtiendo a json y guardando en obs_json/observaciones_smn.json...
conversión y guardado exitosos
```

- Procesar un archivo JSON (.json):
   Muestra la cantidad de ciudades registradas y también muestra la cantidad de ciudades registradas con los datos completos
```bash
python3 analisis_smn.py obs_json/observaciones_smn.json
```
Salida esperada:
```text
archivo json detectado
contidad de ciudades: 121
cantidad de ciudades completas: 25
```

- Manejo de excepciones y errores:
1. Si el archivo no existe:
```bash
python3 analisis_smn.py datos/no_existe.txt
```
Salida esperada:
```text
error: el archivo 'datos/no_existe.txt' no existe
```

2. Si el formato de archivo no es soportado:
```bash
python3 analisis_smn.py datos/archivo.csv
```
Salida esperada:
```text
error: formato de archivo no soportado (.csv)
```