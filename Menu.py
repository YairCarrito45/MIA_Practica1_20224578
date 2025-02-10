from typing import *
from ListaContigua import *
from ListaLigada import *
from ListaDoblementeLigada import *
from ListaIndexada import *

import os

class MenuGestor:
    def __init__(self):
        # Diccionario que almacena las diferentes listas disponibles
        self.listas: Dict = {
            1: ListaContigua(),
            2: ListaLigada(),
            3: ListaDoblementeLigada(),
            4: ListaIndexada()
        }
    
    def limpiar_pantalla(self):
        # Limpia la pantalla de la consola según el sistema operativo
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self):
        # Muestra el menú principal con las opciones disponibles
        print("\n=== SIMULACIÓN DE LISTAS ===")
        print("1. Lista Contigua (Arreglo)")
        print("2. Lista Ligada (Simple)")
        print("3. Lista Doblemente Ligada")
        print("4. Lista Indexada")
        print("5. Salir")
        print("=========================")
    
    def mostrar_menu_operaciones(self):
        # Muestra el menú de operaciones para cada tipo de lista
        print("\n=== OPERACIONES ===")
        print("1. Insertar datos")
        print("2. Eliminar datos")
        print("3. Mostrar datos visualmente")
        print("4. Volver al menú principal")
        print("==================")
    
    def manejar_insercion(self, lista) -> None:
        # Maneja la inserción de elementos en la lista seleccionada
        try:
            valor = int(input("Ingrese el valor a insertar: "))
            if lista.insertar(valor):
                print("Elemento insertado correctamente")
            else:
                print("La lista está llena")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    def manejar_eliminacion(self, lista) -> None:
        # Maneja la eliminación de elementos en la lista seleccionada
        try:
            valor = int(input("Ingrese el valor a eliminar: "))
            if lista.eliminar(valor):
                print("Elemento eliminado correctamente")
            else:
                print("Elemento no encontrado")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    def operar_lista(self, lista) -> None:
        # Controla el flujo de operaciones dentro de la lista seleccionada
        while True:
            self.mostrar_menu_operaciones()
            try:
                opcion = int(input("\nSeleccione una opción: "))
                
                if opcion == 1:
                    self.manejar_insercion(lista)
                elif opcion == 2:
                    self.manejar_eliminacion(lista)
                elif opcion == 3:
                    lista.mostrar()
                elif opcion == 4:
                    break  # Regresa al menú principal
                else:
                    print("Opción inválida")
                    
            except ValueError:
                print("Por favor, ingrese un número válido")
    
    def ejecutar(self):
        # Ejecuta el menú principal y permite la selección de listas
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu_principal()
            
            try:
                opcion = int(input("\nSeleccione una opción: "))
                if opcion == 5:
                    print("¡Hasta luego!")
                    break  # Finaliza el programa
                elif opcion in self.listas:
                    self.operar_lista(self.listas[opcion])
                else:
                    print("Opción inválida")
            except ValueError:
                print("Por favor, ingrese un número válido")

def main():
    # Función principal que inicia el menú
    menu = MenuGestor()
    menu.ejecutar()

if __name__ == "__main__":
    main()
