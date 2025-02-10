class ListaIndexada:
    def __init__(self):
        self.valores = []  # Almacena los valores de la lista
        self.indices = []  # Lista de índices
        self.max_size = 10

    def insertar(self, valor):
        if len(self.valores) < self.max_size:
            self.valores.append(valor)
            self.indices.append(len(self.valores) - 1)  # Asigna el índice correspondiente
            return True
        return False

    def eliminar(self, valor):
        if valor in self.valores:
            idx = self.valores.index(valor)
            self.valores.pop(idx)
            self.indices.pop(idx)
            self.indices = list(range(len(self.valores)))  # Actualiza los índices
            return True
        return False

    def mostrar(self):
        print("\nLista Indexada:")
        print("-" * 30)
        if not self.valores:
            print("Lista vacía")
            return
        print("Índice  |  Valor")
        print("-" * 30)
        for i, v in zip(self.indices, self.valores):
            print(f"{i:^7} | {v:^6}")
        print("-" * 30)

