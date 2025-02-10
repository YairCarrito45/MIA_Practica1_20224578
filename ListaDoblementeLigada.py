from Nodo import *

class ListaDoblementeLigada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista
        self.cola = None  # Último nodo de la lista
        self.tamaño = 0
        self.max_size = 10  # Tamaño máximo

    def insertar(self, valor):
        if self.tamaño >= self.max_size:
            return False  # Si la lista está llena, retorna False
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1
        return True

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente  # Actualiza la cabeza si el primer nodo se elimina

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior  # Actualiza la cola si el último nodo se elimina

                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        print("\nLista Doblemente Ligada:")
        print("-" * 30)
        if not self.cabeza:
            print("Lista vacía")
            return
        actual = self.cabeza
        while actual:
            if actual.siguiente:
                print(f"{actual.valor} <->", end=" ")
            else:
                print(f"{actual.valor}", end=" ")
            actual = actual.siguiente
        print("-> NULL")
        print("-" * 30)
