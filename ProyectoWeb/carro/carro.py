class Carro:
    # Creamos un constructor para crear la sesión y el carro 
    def __init__(self, request): # Creamos el self y la petición
        self.request= request # Almacenamos la petición actual p/utilizarla más adelante
        self.session= request.session # Iniciamos la sesión
        # Contruímos un carro de compras para esta sesión q´el usuario iniciará
        carro= self.session.get("carro")
        if not carro:
            carro= self.session["carro"]={}
        else:
            self.carro= carro
    # Agregar productos al carro
    def agregar(self, producto):
        # Si el producto no está en el carro (o no encuentra el id del producto):
        if str(producto.id) not in self.carro.keys(): #  REVISAR -> () antes de str
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        # Si el producto ya está en el carro:
        else:
            for key, value in self.carro.items(): # P/cada clave/valor q´tengamos en ntro. carro
                if key == str(producto.id): # Comp. si la clave se correponde con el id del prod.
                    value["cantidad"]= value["cantidad"]+1 # Incrementar en 1 la cantidad
                    break
        # Tanto si hay o no prod. esto debe almacenarse en la sesión
        self.guardar_carro()

    # Creamos la función que nos permite guardar la sesión
    def guardar_carro(self):
        self.session["carro"]= self.carro
        self.session.modified= True

    # Eliminamos el producto
    def eliminar(self, producto):
        producto.id= str(producto.id)
        if producto.id in self.carro:
            del self.carro["producto.id"]
            self.guardar_carro()

    # Restar unidades de un producto
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"]= value["cantidad"]-1
                # Si hay solo 1 prod. que eliminar
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    # Limpiar el carro
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified= True

