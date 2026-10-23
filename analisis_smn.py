import sys
from pathlib import Path
from funciones_smn import (
    leer_observaciones,
    mostrar_resumen,
    guardar_como_json,
    contar_archivos_en_directorios,
    cargar_desde_json,
    cantidad_ciudades,
    cantidad_ciudades_completas
)

def main():
    if len(sys.argv) == 1:
        print("aviso, no se indicó ningún archivo para procesar")
        cant_txt, cant_json = contar_archivos_en_directorios()
        print(f"archivos .txt en 'datos/': {cant_txt}")
        print(f"archivos .json en 'obs_json/': {cant_json}")
        return
        
    if len(sys.argv) > 2:
        print("aviso, se pasaron demasiados argumentos, el programa terminará sin hacer nada")
        return

    ruta_archivo = sys.argv[1]
    ruta = Path(ruta_archivo)

    if not ruta.exists():
        print(f"error: el archivo {ruta} no existe")
        return
    extension = ruta.suffix.lower()

    if extension == ".txt":
        print("archivo del SMN, convirtiendo a json...")
        try:
            observaciones = leer_observaciones(str(ruta))
            if not observaciones:
                print(f"aviso: el archivo '{ruta}' está vacío")
                return
            mostrar_resumen(observaciones)
            guardar_como_json(observaciones, str(ruta))
        except Exception as e:
            print(f"error al procesar el rchivo '{ruta}'. con error: {e}")
    elif extension == ".json":
        print("archivo json detectado")
        try:
            observaciones = cargar_desde_json(str(ruta))
            if not observaciones:
                print(f"aviso: el archivo '{ruta}' está vacío")
                return
            print(f"contidad de ciudades: {cantidad_ciudades(observaciones)}")
            print(f"cantidad de ciudades completas: {cantidad_ciudades_completas(observaciones)}")
        except Exception as e:
            print(f"error al procesar el archivo '{ruta}'. con error:{e}")
    else:
        print(f"error: formato de archivo no soportado ({extension})")
            
if __name__ == "__main__":
    main()