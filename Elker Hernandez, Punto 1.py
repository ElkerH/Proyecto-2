# Codigo para entrada de texto y validacion del ranfo de una palabara 
def verificar_palabra(palabra):# se ingresa una palabra cualquiera para la iniciacion del codigo
    longitud = len(palabra)# se generara una lista a partir de la palabra introducida
    
    if 4 <= longitud <= 8:# si las letras es igual o menor a 4 se ingresara un mensaje al igual que si la palabra es menor o igual 8
        print("La palabra es correcta.")# cuando la palabra esta en el rango de entre 4 y 8 letras se le validara como correcto 
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")# cuando la palabra es menor ala rango se le pondra cuantas letras faltan
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")# cuando sobrepasan el numero de letras 
        
# Ejemplo de uso
palabra = input("Ingresa una palabra: ")
verificar_palabra(palabra)
