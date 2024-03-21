def agregar(inventario):
    """ Agregar un nuevo producto al inventario, solicitando al usuario el nombre y la cantidad inicial del producto."""
    producto = input("Ingrese el nombre del nuevo producto: ")
    if producto not in inventario:
        cantidad = input("Ingrese la cantidad inicial del producto: ")
        while True:
            if (cantidad.isdigit()):
                inventario[producto] = cantidad
                print("Producto anexado con exito en el inventario.")
                break
            print("Ingrese cantidad valida")
    else:
        print("No puede agregar un producto ya existente.")
def eliminar(inventario):
    """ Eliminar un producto existente del inventario, solicitando al usuario el nombre del producto a eliminar"""
    producto = input("ingrese el nombre del producto a eliminar: ")
    if producto in inventario:
        del inventario[producto]
        print("Producto eliminado correctamente del inventario.")
    else:
        print("No puede eliminar un producto que no existe en el inventario.") 
def mostrar(inventario):
    """ Mostrar el inventario actual, que incluya el nombre y la cantidad de cada producto."""
    if inventario:
        for clave, cantidad in inventario.items():
            print(f"{clave}: {cantidad}")
    else:
        print("No hay nada...")

inventario = {}
while True:
    operacion = input("Secleccion una opcion: (1)Agregar un producto (2)Eliminar un producto (3)Mostrar el inventario (4)Salir: ")
    match operacion:
        case "1": agregar(inventario)
        case "2": eliminar(inventario)
        case "3": mostrar(inventario)
        case "4": break
        case _:  print("¿Te equivocaste? Intentalo de vuelta.")