import dataset

miBase = dataset.connect("sqlite:///datos.db")

tabla = miBase["Productos"]

while True:
    opciones = input("\nS - Salir\nA - Agregar\nL Listar\n")

    match opciones:
        case "S":
            break

        case "A":
            agregarProducto = input("\nProducto a Agregar: ").strip()
            precioAgregar = float(input("\nPrecio Producto: ").strip())
            agregarCategoria = input("\nCategoria Producto: ").strip()
            agregar = {"Nombre":agregarProducto,"Precio":precioAgregar,"Categoria":agregarCategoria}
            tabla.insert(agregar)

        case "L":
            for cada_item in tabla:
                print(cada_item)



