#La clase Cliente que contiene nombre, edad, correo e indica si se encuentra activo o no
class Cliente:
    def __init__(
        self,
        nombre: str,
        edad: int,
        correo: str,
        activo: bool
    ):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.activo = activo

    def __str__(self) -> str:
        estado = "Activo" if self.activo else "Inactivo"
        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} | "
            f"Correo: {self.correo} | "
            f"{estado}"
        )
