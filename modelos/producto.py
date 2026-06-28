#La clase Producto para el restaurante, cuenta con nombre, precio, cantidad en stock y disponibilidad.
class Producto:
    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        disponible: bool
    ):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock} | "
            f"{estado}"
        )
