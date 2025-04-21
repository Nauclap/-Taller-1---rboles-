# ===========================================
# By: Andrea Valentina Delgado Ruiz - Nelson Andres Urrea Calvo
# Name: Implementación de árboles con listas enlazadas
# ===========================================

#Los nodos se ingresan por teclado
#Debe contener los métodos de peso, orden y altura

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.hijo = None
        self.padre = None
        self.siguiente = None 

class Hijos:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    # Insertar al final
    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.contador = self.contador + 1
        else:

            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Buscar elemento
    def BuscarPadre(self,padre):
        hayPadre = False
        if self.cabeza is None:
            print('no se puede buscar padre porque la lista esta vacia')
            return hayPadre
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.data == padre:
                    hayPadre = True
                    break
                actual = actual.siguiente
            if hayPadre:
                return actual
            else:
                #print('No se encontro el numero ingresado, se rotarna False')
                return hayPadre
    # Mostrar hacia adelante    
    def mostrarAdelante(self):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            actual = self.cabeza
            while True:
                print(actual.data)
                actual = actual.siguiente
                if actual is None:
                    break

    def recorrerArbol(self):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            print('Primer nivel')
            self.mostrarAdelante()
            print('Segundo nivel')
            actual = self.cabeza
            actualInicial = self.cabeza
            actual2 = None
    
            while actual.hijo is not None:
                actual.hijo.mostrarAdelante()
                actual = actual.siguiente
                if actual is None: 
                    print('Siguiente nivel')
                    actual2 = actualInicial.hijo.cabeza
                    if actualInicial.siguiente is not None:
                        actualInicial = actualInicial.siguiente
                    if actual2 is not None:
                        actual = actual2
                        actualInicial = actual2
                    else:
                        break

    def AlturaArbol(self):
        contador = 0
        if self.cabeza is None:
            return contador
        else:
            contador += 1
            actual = self.cabeza
            actualInicial = self.cabeza
            actual2 = None
            if actual.hijo is not None:
                contador += 1
            while actual.hijo is not None:
                actual = actual.siguiente
                if actual is None: 
                    contador += 1
                    actual2 = actualInicial.hijo.cabeza
                    if actualInicial.siguiente is not None:
                        actualInicial = actualInicial.siguiente
                    if actual2 is not None:
                        actual = actual2
                        actualInicial = actual2
                    else:
                        break
            return contador


    def insertarHijo(self, numero, padre):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            posicionPadre = self.BuscarPadre(padre)
            if posicionPadre is not False:
                if posicionPadre.hijo is not None:
                    posicionPadre.hijo.agregarFinal(numero)
                    self.contador = self.contador + 1
                else:
                    posicionPadre.hijo = Hijos()
                    posicionPadre.hijo.agregarFinal(numero)
                    self.contador = self.contador + 1
            else:
            
                actual = self.cabeza
                actualInicial = self.cabeza
                actual2 = None
        
                while actual.hijo is not None:
                    posicionPadre = actual.hijo.BuscarPadre(padre)
                    if posicionPadre is not False:
                        if posicionPadre.hijo is not None:
                            posicionPadre.hijo.agregarFinal(numero)
                            self.contador = self.contador + 1
                            break
                        else:
                            posicionPadre.hijo = Hijos()
                            posicionPadre.hijo.agregarFinal(numero)
                            self.contador = self.contador + 1
                            break
                    actual = actual.siguiente
                    if actual is None: 
                        actual2 = actualInicial.hijo.cabeza
                        if actualInicial.siguiente is not None:
                            actualInicial = actualInicial.siguiente
                        if actual2 is not None:
                            actual = actual2
                            actualInicial = actual2
                        else:
                            break

nivel1 = Hijos()
nivel1.agregarFinal(9)
nivel1.insertarHijo(5,9)
nivel1.insertarHijo(3,9)
nivel1.insertarHijo(34,9)
nivel1.insertarHijo(1,5)
nivel1.insertarHijo(7,5)
nivel1.insertarHijo(12,5)
nivel1.insertarHijo(8,3)
nivel1.insertarHijo(4,3)
nivel1.insertarHijo(6,34)
nivel1.insertarHijo(2,1)
nivel1.insertarHijo(23,1)
nivel1.insertarHijo(11,7)
nivel1.insertarHijo(16,12)

#nivel1.recorrerArbol()

def menu():
    arbol = nivel1
    while True :
        print(' ')
        print("\nMenú, escriba el número de la opción que desea usar:")
        print("Este programa solo soporta árboles con altura 3")
        print("1. Mostrar árbol por niveles")
        print("2. Crear arbol desde 0")
        print("3. Agregar elemento")
        print("4. Peso del árbol")
        print("5. Orden")
        print("6. Altura")
        print("0. Salir")
        print(' ')

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            arbol.recorrerArbol()

        if opcion == '2':
            numero = input('Ingrese el número de la raiz: ')
            arbol = Hijos()
            arbol.agregarFinal(numero)

        elif opcion == '3':
            
            numero = input('Ingrese el número que desea ingresar: ')
            padre = input('Ingrese el padre del número anterior: ')
            arbol.insertarHijo(int(numero),int(padre))
            print('Numero '+str(numero)+ ' ingresado')
            
        elif opcion == '4':
            print('Peso del árbol: '+str(arbol.contador))
        
        elif opcion == '5':
            print('Cada nodo puede tener tantos hijos sean necesarios,' \
            ' porque cada nodo en si es una lista')

        elif opcion == '6':
            print('Altura del árbol: '+ str(arbol.AlturaArbol()))

        elif opcion == '0':
            print('Fin del programa')
            break
        
        else:
            print('Ingrese un número válido')

menu()
        


