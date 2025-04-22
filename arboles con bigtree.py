# ===========================================
# By: Andrea Valentina Delgado Ruiz - Nelson Andres Urrea Calvo
# Name: Implementación de Taller 1 - árboles con Bigtree
# ===========================================

from bigtree import Node
from bigtree import preorder_iter

root = Node("a")

b = Node("b",  parent=root)
c = Node("c",  parent=root)
d = Node("d",  parent=root)
f = Node("f",  parent=b)
g = Node("g",  parent=b)
i = Node("i",  parent=c)
j = Node("j",  parent=c)
k = Node("k", parent=d)

def menu():
    arbol = None
    nodos = {}  # Diccionario para guardar los nodos por su nombre
    while True :
        print(' ')
        print("\nMenú, escriba el número de la opción que desea usar:")
        print("1. Mostrar árbol")
        print("2. Crear y agregar elementos al árbol")
        print("3. Peso del árbol")
        print("4. Orden")
        print("5. Altura")
        print("0. Salir")
        print(' ')

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            if arbol is None:
                print('Primero cree un árbol con la opción 2')
                print('Si desea ver un ejemplo, ingrese el número 7; si no, ingrese cualquier otro valor.')
                ejm = input('Ingrese un valor: ')
                if ejm == '7':
                   root.hshow()
            else:
                arbol.hshow()

        elif opcion == '2':
            if arbol is None:
                raiz_nombre = input("Ingrese el nombre de la raiz ")
                nodo_padre = Node(raiz_nombre, parent=arbol)
                nodos[raiz_nombre] = nodo_padre
                arbol = nodo_padre

            else:
                nombre = input("Ingrese el nombre del nuevo nodo: ")
                padre_nombre = input("Ingrese el nombre del nodo padre: ")
                # Creamos el nuevo nodo padre
                if padre_nombre not in nodos:
                    nodo_padre = Node(padre_nombre, parent=arbol)
                    nodos[padre_nombre] = nodo_padre
                else:
                    nodo_padre = nodos[padre_nombre]

                # Creamos el nuevo nodo hijo
                if nombre not in nodos:
                    nuevo_nodo = Node(nombre, parent=nodo_padre)
                    nodos[nombre] = nuevo_nodo
                    print(f"Nodo '{nombre}' agregado como hijo de '{padre_nombre}'.")
                
            
           
            
        elif opcion == '3':
            recorrido = [node.node_name for node in preorder_iter(arbol)]
            print('Peso del árbol: ' + str(len(recorrido)))
        
        elif opcion == '4':
            print('Cada nodo puede tener tantos hijos sean necesarios,' \
            ' porque cada nodo en si es una lista')

        elif opcion == '5':
            print('Altura: '+str(arbol.max_depth))

        elif opcion == '0':
            print('Fin del programa')
            break
        
        else:
            print('Ingrese un número válido')

menu()
