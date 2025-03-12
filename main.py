#programa para gestion de productos de uuna lista de mercado 
nombreUsuario=None

#delarando variables 
productos=[]
producto={}

#crear un menu de opciones 
print("*** MerqueoAPP ***")
print("1. Agregar Producto a tu lista de mercado")
print("2. Mostrar  tu lista de mercado")
print("3. Modificar  tu lista de mercado")
print("4. Retirar producto de  tu lista de mercado")
print("Presiona 5 para SALIR")

opcion=100
while opcion != 5:
    opcion=int(input("Digita una opcion del menu: "))

    if opcion == 1:
       
        #Poblando lista y diccionarios en python}
        #asignando claves a un diccionario 
        producto["id"]=5 #general de fotrma aletoria este numero (unico)
        producto["nombre"]=input("Digita el nombre del producto:")
        producto["presentacion"]=input("Digita la presenatcion del producto: ")
        producto["cantidad"]=int(input("Digita la cantidad:"))
        producto["precio"]=int(input("Digita el precio del producto: "))

        #asignando una lista a un diccionario 
        productos.append(producto)
        
       
        

    elif opcion == 2:
        #Recorrer una lista
        for  productoIterado in  productos:
            print(productoIterado["nombre"])
            print(productoIterado["precio"])
            

    elif opcion == 3:
       #preguntarle al usuario cual producto quiere comprar 
       IdProductoABuscar=int(input("cual es el Id de producto a modificar"))
       #recorrer la lista para buscar el eleumento que quiero modificar 
       for productoBuscado in productos:
           if IdProductoABuscar==productoBuscado["id"]:
               print("encontrado")
            else:
               print("no enc0o0ntrado") 
                  
       #modicicar la o las propiedades pedidas 

    elif opcion == 4:
        print ("Retirando un producto  ")
    else:
        print("Opcion invalida")
     
       
