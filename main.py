#Aquí se desarrolla el programa principal
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    #Se crea el nombre del restaurante
    restaurante = Restaurante("Proyecto S5")

    #Se crean los productos a dar en el restaurante
    producto1 = Producto(
        "Salchipapa",
        2.50,
        20,
        True
    )

    producto2 = Producto(
        "Papipollo",
        3.50,
        10,
        True
    )

    #Se crean los clientes
    cliente1 = Cliente(
        "Erika España",
        29,
        "et.espanav@uea.com.ec",
        True
    )

    cliente2 = Cliente(
        "Ariel Vélez",
        29,
        "aavelez@gmail.com",
        False
    )

    #Se agregan los productos al restaurante creado
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    #Se agregan los clientes al restaurante creado
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    #Se muestra la información guardada
    print("Proyecto S5 Presenta")
    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()
