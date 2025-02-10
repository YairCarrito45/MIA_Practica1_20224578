class ListaContigua:
    def __init__(self):
        self.lista = []  # Lista vacía
        self.max_size = 10  # Tamaño máximo de la lista

    def insertar(self, valor):
        if len(self.lista) < self.max_size:  # Verifica si hay espacio en la lista
            self.lista.append(valor)  # Agrega el valor al final de la lista
            return True
        return False  # Retorna False si la lista está llena

    def eliminar(self, valor):
        if valor in self.lista:  # Verifica si el valor está en la lista
            self.lista.remove(valor)  # Elimina el valor
            return True
        return False  # Retorna False si el valor no está en la lista

    def mostrar(self):
        print("\nLista Contigua:")
        print("-" * 20)
        if not self.lista:
            print("Lista vacía")
            return
        for i, valor in enumerate(self.lista):  # Muestra los elementos con su índice
            print(f"[{i}] -> {valor}")
        print("-" * 20)