#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], …
}


#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], ...
}


def stock_marca(stock, marca):
    encontrado = []
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            cantidad = stock.get(modelo, [0, 0])[1]
            encontrado.append((modelo, cantidad))
    if encontrado:
        print(f"Stock de productos de la marca {marca} :")
        for modelo, cantidad in encontrado:
            print(f"Modelo: {modelo}, Stock: {cantidad}")
    else:
        print(f"No se encontraron productos de la marca {marca}:")



def busqueda_precio(precio_minimo,precio_maximo):
    encontrado = []
    for modelo, datos in productos.items():
        precio = stock.get(modelo, [0, 0])[0]
        if precio_minimo <= precio <= precio_maximo:
            encontrado.append((modelo, datos[0, precio]))
    if encontrado:
        print("Productos encontrados:")
        for modelo, marca, precio in encontrado:
            print(f"Modelo: {modelo}, Marca: {marca}, Preciio: {precio}")
    else:
        print("No se encontraron productos en ese rango de precios.")


def actualizar_precio(modelo, precio_nuevo):
    if modelo in stock:
        stock[modelo][0] = precio_nuevo
        return True
    else:
        return False
    
def menu():
    print("***MENÚ***")
    print("1. Stock Marca")
    print("2.Busqueda por precio")
    print("3.Actualizar precio")
    print("4.salir")