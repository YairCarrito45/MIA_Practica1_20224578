from Nodo import * 

class ListaLigada:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
        self.max_size = 10

    def insertar(self, valor):
        if self.tamaño >= self.max_size:
            return False
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza  # Inserta el nuevo nodo al inicio
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        return True

    def eliminar(self, valor):
        if not self.cabeza:
            return False
        
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente  # Elimina el primer nodo
            self.tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente  # Salta el nodo eliminado
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        print("\nLista Ligada:")
        print("-" * 20)
        if not self.cabeza:
            print("Lista vacía")
            return
        actual = self.cabeza
        while actual:
            print(f"{actual.valor} ->", end=" ")
            actual = actual.siguiente
        print("NULL")
        print("-" * 20)
