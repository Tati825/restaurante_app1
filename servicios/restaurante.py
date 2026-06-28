#La clase Restaurante para administrar todo
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        print(f"\n--- Productos de {self.nombre} ---")

        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        print(f"\n--- Clientes de {self.nombre} ---")

        for cliente in self.clientes:
            print(cliente)
