from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Función para cargar imagen
def cargar_imagen(ruta_imagen):
    return Image.open(ruta_imagen)

# Función 1: Redimensionar imagen según la plataforma
def redimensionar_imagen(imagen, plataforma):
    tamaños = {
        "youtube": (1280, 720),
        "instagram": (1080, 1080),
        "twitter": (1024, 512),
        "facebook": (1200, 630)
    }
    
    plataforma = plataforma.lower() 
    if plataforma not in tamaños:
        raise ValueError("Plataforma no soportada.")
    
    imagen.thumbnail(tamaños[plataforma], Image.LANCZOS)
    return imagen

# Función 2: Ajuste de contraste
def ajustar_contraste(imagen):
    ajustador = ImageEnhance.Contrast(imagen)
    imagen_contraste = ajustador.enhance(5)
    return imagen_contraste

# Función 3: Aplicar filtros
def aplica_filtro(imagen, nombre_filtro):
    filtros = {
        "desenfoque": ImageFilter.BLUR,
        "contorno": ImageFilter.CONTOUR,
        "detalle": ImageFilter.DETAIL,
        "realce_bordes": ImageFilter.EDGE_ENHANCE,
        "realce_bordes_mayor": ImageFilter.EDGE_ENHANCE_MORE,
        "relieve": ImageFilter.EMBOSS,
        "encontrar_bordes": ImageFilter.FIND_EDGES,
        "afilar": ImageFilter.SHARPEN,
        "suavizar": ImageFilter.SMOOTH
    }
    nombre_filtro = nombre_filtro.lower() 
    if nombre_filtro not in filtros:
        raise ValueError("Filtro no soportado.")
    
    imagen_filtrada = imagen.filter(filtros[nombre_filtro])
    return imagen_filtrada

# Función 4: Boceto para pintores
def crear_boceto(ruta_imagen, persona=True):
    if not persona:
        raise ValueError("La imagen no contiene una persona.")
    
    imagen = cv2.imread(ruta_imagen)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    imagen_borroso = cv2.GaussianBlur(imagen_gris, (5, 5), 0)
    
    bordes = cv2.Canny(imagen_borroso, 50, 150)
    
    boceto = cv2.bitwise_not(bordes)

    return boceto

def mostrar_resultado(ruta_imagen, boceto):
    imagen = Image.open(ruta_imagen)
    boceto_imagen = Image.fromarray(boceto)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(imagen)
    plt.subplot(1, 2, 2)
    plt.title("Boceto")
    plt.imshow(boceto_imagen, cmap='gray')
    plt.show()


# Función 5: Menú de opciones
def menu():
    print("=====================")
    print("BIENVENIDO A FOTOAPP:")
    print("=====================")
    print("")
    print("Seleciona lo que desee hacer::")
    print("1. Redimensionar imagen para una plataforma")
    print("2. Ajustar contraste de una imagen")
    print("3. Aplicar un filtro a una imagen")
    print("4. Crear un boceto para pintores")
    print("5. Salir del programa")
    
    opcion = input("Seleccione una opción (1-5): ")
    return int(opcion)

def main():
    try:
        while True:
            opcion = menu()
            if opcion in [1, 2, 3, 4]:
                ruta = input("Ingrese la ruta de la imagen: ")
                imagen_original = cargar_imagen(ruta)

            if opcion == 1:
                plataforma = input("Ingrese la plataforma (youtube, instagram, twitter, facebook): ").lower()
                imagen_cargada = redimensionar_imagen(imagen_original, plataforma)
                imagen_cargada.show()
            elif opcion == 2:
                imagen_contraste = ajustar_contraste(imagen_original)
                plt.figure(figsize=(10, 5))
                plt.subplot(1, 2, 1)
                plt.title("Original")
                plt.imshow(imagen_original)
                plt.subplot(1, 2, 2)
                plt.title("Contraste Ajustado")
                plt.imshow(imagen_contraste)
                plt.show()
            elif opcion == 3:
                print("Los filtros disponibles son: desenfoque, contorno, detalle, realce_bordes, realce_bordes_mayor, relieve, encontrar_bordes, afilar, suavizar")
                nombre_filtro = input("Ingrese el filtro a aplicar: ").lower()
                imagen_filtrada = aplica_filtro(imagen_original, nombre_filtro)
                plt.figure(figsize=(10, 5))
                plt.subplot(1, 2, 1)
                plt.title("Original")
                plt.imshow(imagen_original)
                plt.subplot(1, 2, 2)
                plt.title("Filtro Aplicado")
                plt.imshow(imagen_filtrada)
                plt.show()
            elif opcion == 4:
                try:
                    boceto = crear_boceto(ruta)
                    mostrar_resultado(ruta, boceto)
                except ValueError as e:
                    print(e)
            elif opcion == 5:
                print("Saliendo del programa...... ¡Nos vemos!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()

