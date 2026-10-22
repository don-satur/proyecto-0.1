import sys
from funciones_smn import leer_observaciones, mostrar_resumen

def main():
    if len(sys.argv) < 2:
        print("error, faltan argumentos")
        print("comando esperado: python analisis_smn.py ruta/archivo1.txt [ruta/archivo2.txt ...]")
        sys.exit(1)
    for i, ruta in enumerate(sys.argv[1:], start=1):
        print(f"\n >>> análisis de archivo {i}: {ruta} <<< ")
        
        try:
            datos = leer_observaciones(ruta)
            if not datos:
                print(f"aviso: el archivo '{ruta}' está vacío")
                continue
            mostrar_resumen(datos)
        except FileNotFoundError:
            print(f"error: no encuentro el archivo '{ruta}' o no existe")
        except Exception as e:
            print(f"error al procesar el archivo '{ruta}': {e}")

if __name__ == "__main__":
    main()