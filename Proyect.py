import os
import matplotlib.pyplot as plt
import csv

archivo = r"C:\Users\mangt\Documents\Tec\estadisticas_videojuegos_final.csv"

#funciones para calcular promedio de ventas dependiendo de genero
def ventas(archivo,nombre):


    # Limpia la consola, 'cls' es para Windows, puedes usar 'clear' en sistemas Unix (Linux/macOS)
    os.system("cls")

    # Diccionario para almacenar los géneros por año de estudio y las ventas asociadas
    generos = {}

    # Abre el archivo CSV en modo lectura
    with open(archivo, 'r') as archivos:
        # Utiliza DictReader para leer el archivo como diccionario, donde las claves son los nombres de las columnas
        lector = csv.DictReader(archivos)
        
        # Recorre cada fila del archivo CSV
        for fila in lector:
            # Obtiene el género del juego de la columna 'genero del juego'
            gnro = fila['genero del juego']
            
            # Si el género empieza con 'terror', lo consideramos un juego de terror
            if gnro.startswith(nombre):
                # Obtiene el año del estudio del juego de la columna 'anio'
                estudio = fila['anio']
                
                # Convierte la cantidad de ventas de la columna 'cantidad de ventas' a un valor flotante
                cantidad = float(fila['cantidad de ventas'])
                
                # Si el año del estudio aún no está en el diccionario, lo añadimos con una lista vacía
                if estudio not in generos:
                    generos[estudio] = []
                
                # Añadimos la cantidad de ventas a la lista de ese año del estudio
                generos[estudio].append(cantidad)

    # Ponemos los estudios ordenados por año
    for estudio, cantidad in sorted(generos.items()):
        # Calcula el promedio de ventas sumando las ventas y dividiendo por el número de juegos
        promedio_de_ventas = sum(cantidad) / len(cantidad)
        
        # Imprime el resultado 
        print(f'Estudio del año: {estudio} - Promedio de ventas juegos de {nombre}: {promedio_de_ventas:.2f}')

  

#Funciones para generar graficas dependiendo de genero
def graficas(archivo,nombre):
    import csv
    import matplotlib.pyplot as plt

    # Diccionario para almacenar la popularidad de juegos de terror por año
    popularidad_por_genero = {}

    # Abre el archivo CSV en modo lectura
    with open(archivo, 'r') as archivos:
        # Utiliza DictReader para leer el archivo como diccionario, donde las claves son los nombres de las columnas
        lector = csv.DictReader(archivos)
        
        # Recorre cada fila del archivo CSV
        for fila in lector:
            # Verifica si el género del juego es 'terror'
            if fila['genero del juego'] == nombre:
                # Obtiene el año del juego de la columna 'anio'
                anio = fila['anio']
                # Convierte la cantidad de ventas de la columna 'cantidad de ventas' a un valor flotante
                cantidad = float(fila['cantidad de ventas'])
                
                # Si el año no está en el diccionario, inicializa su valor a 0
                if anio not in popularidad_por_genero:
                    popularidad_por_genero[anio] = 0
                
                # Suma la cantidad de ventas al año correspondiente
                popularidad_por_genero[anio] += cantidad

    # Ordena los años y obtiene la lista de datos (ventas) correspondiente
    anio = sorted(list(popularidad_por_genero.keys()))
    datos = list(popularidad_por_genero.values())
        
    #Crea la grafica
    plt.figure(figsize=(10, 6))
    plt.bar(anio, datos)
    plt.xlabel('año')
    plt.ylabel('Ventas ')
    plt.title(nombre)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    popularidad_por_genero = {}
   
    
#Funciones para generar una grafica de tendencia dependiendo de genero
def egraficas(archivo,nombre):
    import csv
    import matplotlib.pyplot as plt

    # Diccionario para almacenar la popularidad de juegos de terror por año
    popularidad_por_genero = {}

    # Abre el archivo CSV en modo lectura
    with open(archivo, 'r') as archivos:
        # Utiliza DictReader para leer el archivo como diccionario, donde las claves son los nombres de las columnas
        lector = csv.DictReader(archivos)
        
        # Recorre cada fila del archivo CSV
        for fila in lector:
            # Verifica si el género del juego es 'terror'
            if fila['genero del juego'] == nombre:
                # Obtiene el año del juego de la columna 'anio'
                anio = fila['anio']
                # Convierte la cantidad de ventas de la columna 'cantidad de ventas' a un valor flotante
                cantidad = float(fila['cantidad de ventas'])
                
                # Si el año no está en el diccionario, inicializa su valor a 0
                if anio not in popularidad_por_genero:
                    popularidad_por_genero[anio] = 0
                
                # Suma la cantidad de ventas al año correspondiente
                popularidad_por_genero[anio] += cantidad

        # Ordena los años y obtiene la lista de datos (ventas) correspondiente
    anio = sorted(list(popularidad_por_genero.keys()))
    datos = list(popularidad_por_genero.values())
    
    #genera grafica
    plt.figure(figsize=(10, 6))
    plt.plot(anio, datos)
    plt.xlabel('año')
    plt.ylabel('Ventas ')
    plt.title(nombre)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

   

#Da la bienvenida
def cuales_faltan():
    # Dar bienvenida
    os. system("cls") 
    print("Bienvenido al programa cuales faltan")

    


#Opciones para el menu del progrma
def opciones():
    #Opciones para el primer menu
    os. system("cls") 
    print (f"ok, {nombre} que quieres hacer ")
    opc = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Programa sobre datos de generos en juegos"
                "\n 2. Programa sobre datos de consolas en juegos"
                "\n 3. Salir"
                "\n "
                ))
    if opc < 0 or opc > 5:
        os. system("cls") 
        print("OPCION INVALIDA")
        opc = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Programa sobre datos de generos en juegos"
                "\n 2. Programa sobre datos de consolas en juegos"
                "\n 3. Salir"
                "\n "
                ))
    return opc
def opciones2():
    #Opciones para el submenu 1
    os. system("cls") 
    opc2 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Ventas por año"
                "\n 2. Grafica sobre genero y ventas"
                "\n 3. Tendencias por Año"
                "\n 4. Salir"
                "\n "
                ))
    if opc2 < 0 or opc2 > 5:
        os. system("cls") 
        print("OPCION INVALIDA")
        opc2 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Ventas por año"
                "\n 2. Grafica sobre genero y ventas"
                "\n 3. Tendencias por Año"
                "\n 4. Salir"
                "\n "
                ))
    return opc2
def opciones3():
    os. system("cls") 
    opc3 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Promedio de usuarios"
                "\n 2. Grafica de consolas por año y usuarios"
                "\n 3. Tendencias año y usuarios por consola"
                "\n 4. Salir"
                "\n "
                ))
    if opc3 < 0 or opc3 > 5:
        os. system("cls") 
        print("OPCION INVALIDA")
        opc3 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Promedio de usuarios"
                "\n 2. Grafica de consolas por año y usuarios"
                "\n 3. Tendencias año y usuarios por consola"
                "\n 4. Salir"
                "\n "
                ))
    return opc3
def opciones2_2():
    #Opciones para el submenu de los generos
    os. system("cls") 
    opc2_2 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Arcade"
                "\n 2. Aventura"
                "\n 3. Acción"
                "\n 4. Carreras"
                "\n 5. Deportes"
                "\n 6. Musical"
                "\n 7. Peleas"
                "\n 8. Puzle"
                "\n 9. Rol"
                "\n 10. Sandbox"
                "\n 11. Terror"
                "\n 12. Salir"
                "\n "
                ))
    if opc2_2 < 0 or opc2_2 > 13:
        os. system("cls") 
        print("OPCION INVALIDA")
        opc2_2 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. Arcade"
                "\n 2. Aventura"
                "\n 3. Acción"
                "\n 4. Carreras"
                "\n 5. Deportes"
                "\n 6. Musical"
                "\n 7. Peleas"
                "\n 8. Puzle"
                "\n 9. Rol"
                "\n 10. Sandbox"
                "\n 11. Terror"
                "\n 12. Salir"
                "\n "
                ))
    return opc2_2

def opciones3_1():
    os. system("cls") 
    opc3_1 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. PLAYSTATION"
                "\n 2. XBOX"
                "\n 3. PC"
                "\n 4. NINTENDO SWITCH"
                "\n 5. MOBILE"
                "\n 6. Salir"
                "\n "
                ))
    if opc3_1 < 0 or opc3_1 > 6:
        os. system("cls") 
        print("OPCION INVALIDA")
        opc3_1 = int(input("De las siguientes opciones elige el programa que quieras usar: "
                "\n 1. PLAYSTATION"
                "\n 2. XBOX"
                "\n 3. PC"
                "\n 4. NINTENDO SWITCH"
                "\n 5. MOBILE"
                "\n 6. Salir"
                "\n "
                ))
    return opc3_1


    
    
# Salida para submenu
def salida():
    #Te pregunta si quieres salir del submenu
    while True:
                    s_n = input("Quieres salir? (si/no) ")
                    s_n = s_n.lower()
                    if s_n.lower() == "si":
                        break
                    elif s_n.lower() == "no":
                        print("Tecleaste que no quieres salir. Teclea 'si' cuando quieras salir.")
                    else:
                        print("Por favor, responde solo con 'si' o 'no'.")

#Bienvenida
print("Hola somos videojuegos y sus consumidores")
nombre = input("Como te llamas? ")





    
# Hace que las funciones de opciones sean ejecutadas y en cada uno use la funcion que se necesita utilizando un ciclo while para que el programa funcione hasta que te salgas
while True:
    opc = opciones()
    
    if opc == 1:
        while True:
            opc2 = opciones2()
            
            if opc2 == 1: 
               while True:
                opc2_2 = opciones2_2()
                if opc2_2 == 1: 
                    ventas(archivo,"arcade")
                
            
                elif opc2_2 == 2:
                    ventas(archivo,"aventura")

                elif opc2_2 == 3:
                    ventas(archivo,"accion")
                
                elif opc2_2 == 4:
                    ventas(archivo,"carreras")

                if opc2_2 == 5: 
                    ventas(archivo,"deportes")
                
            
                elif opc2_2 == 6:
                    ventas(archivo,"musical")

                elif opc2_2 == 7:
                    ventas(archivo,"peleas")
                
                elif opc2_2 == 8:
                    ventas(archivo,"puzle")

                if opc2_2 == 9: 
                    ventas(archivo,"rol")
                
            
                elif opc2_2 == 10:
                    ventas(archivo,"sandbox")

                elif opc2_2 == 11:
                    ventas(archivo,"terror")
                

                elif opc2_2 == 12:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break
                
                salida()
            
            if opc2 == 2: 
               while True:
                opc2_2 = opciones2_2()
                if opc2_2 == 1: 
                    graficas(archivo,"arcade")
                    
                    
            
                elif opc2_2 == 2:
                    graficas(archivo,"aventura")

                elif opc2_2 == 3:
                    graficas(archivo,"accion")
                
                elif opc2_2 == 4:
                    graficas(archivo,"carreras")

                if opc2_2 == 5: 
                    graficas(archivo,"deportes")
                
            
                elif opc2_2 == 6:
                    graficas(archivo,"musical")

                elif opc2_2 == 7:
                    graficas(archivo,"peleas")
                
                elif opc2_2 == 8:
                    graficas(archivo,"puzle")

                if opc2_2 == 9: 
                    graficas(archivo,"rol")
                
            
                elif opc2_2 == 10:
                    graficas(archivo,"sandbox")

                elif opc2_2 == 11:
                    graficas(archivo,"terror")
                

                elif opc2_2 == 12:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break
                
                

            if opc2 == 3: 
              while True:
                opc2_2 = opciones2_2()
                if opc2_2 == 1: 
                    egraficas(archivo,"arcade")
                    
                    
            
                elif opc2_2 == 2:
                    egraficas(archivo,"aventura")

                elif opc2_2 == 3:
                    egraficas(archivo,"accion")
                
                elif opc2_2 == 4:
                    egraficas(archivo,"carreras")

                if opc2_2 == 5: 
                    egraficas(archivo,"deportes")
                
            
                elif opc2_2 == 6:
                    egraficas(archivo,"musical")

                elif opc2_2 == 7:
                    egraficas(archivo,"peleas")
                
                elif opc2_2 == 8:
                    egraficas(archivo,"puzle")

                if opc2_2 == 9: 
                    egraficas(archivo,"rol")
                
            
                elif opc2_2 == 10:
                    egraficas(archivo,"sandbox")

                elif opc2_2 == 11:
                    egraficas(archivo,"terror")
                

                elif opc2_2 == 12:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break
                
                

                
            elif opc2 == 4:
                os.system("cls") 
                print("Seleccionaste la opción de salir. Saliste del submenu")
                break
            
    
    if opc == 2:
        while True:
            opc3 = opciones3()
            if opc3 == 1:
               while True: 
                opc3_1 = opciones3_1()
                if opc3_1 == 1: 
                    ventas(archivo,"PlayStation")
                    salida()
            
                elif opc3_1 == 2:
                    ventas(archivo,"Xbox")
                    salida()

                elif opc3_1 == 3:
                    ventas(archivo,"PC")
                    salida()

                elif opc3_1 == 4:
                    ventas(archivo,"Nintendo Switch")
                    salida()

                elif opc3_1 == 5:
                    ventas(archivo,"Mobile")
                    salida()
                    
                elif opc3_1 == 6:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break

            elif opc3 == 2: 
               while True: 
                opc3_1 = opciones3_1()
                if opc3_1 == 1: 
                    graficas(archivo,"PlayStation")
                    
            
                elif opc3_1 == 2:
                    graficas(archivo,"Xbox")
                    

                elif opc3_1 == 3:
                    graficas(archivo,"PC")
                   

                elif opc3_1 == 4:
                    graficas(archivo,"Nintendo Switch")
                    

                elif opc3_1 == 5:
                    graficas(archivo,"Mobile")
                    
                    
                    
                elif opc3_1 == 6:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break

            elif opc3 == 3: 
               while True: 
                opc3_1 = opciones3_1()
                if opc3_1 == 1: 
                    egraficas(archivo,"PlayStation")
                    
            
                elif opc3_1 == 2:
                    egraficas(archivo,"Xbox")
                    

                elif opc3_1 == 3:
                    egraficas(archivo,"PC")
                   

                elif opc3_1 == 4:
                    egraficas(archivo,"Nintendo Switch")
                    

                elif opc3_1 == 5:
                    egraficas(archivo,"Mobile")
                   
                    
                elif opc3_1 == 6:
                    os.system("cls") 
                    print("Seleccionaste la opción de salir. Saliste del submenu")
                    break

            elif opc3 == 4:
                os.system("cls") 
                print("Seleccionaste la opción de salir. Gracias por usar el programa")
                break
            
    
    elif opc == 3:
        os.system("cls") 
        print("Seleccionaste la opción de salir. Gracias por usar el programa")
        break