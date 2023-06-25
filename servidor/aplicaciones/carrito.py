class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, Vinilo):
        id = str(Vinilo.id) 
        if id not in self.carrito.keys():
            self.carrito[id] ={
                "Vinilo_id": Vinilo.id,
                "nombre":Vinilo.nombre_vinilo,
                "acumulado":Vinilo.precio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"] += 1 
            self.carrito[id]["acumulado"] += Vinilo.precio
        self.guardar_carrito()
        
    def comprarahora(self, Vinilo):
        id = str(Vinilo.id) 
        if id not in self.carrito.keys():
            self.carrito[id] ={
                "Vinilo_id": Vinilo.id,
                "nombre":Vinilo.nombre_vinilo,
                "acumulado":Vinilo.precio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"] += 1 
            self.carrito[id]["acumulado"] += Vinilo.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def elminar(self, Vinilo):
        id = str(Vinilo.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Vinilo):
        id = str(Vinilo.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1 
            self.carrito[id]["acumulado"] -= Vinilo.precio
            if self.carrito[id]["cantidad"] <= 0 : self.elminar(Vinilo)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True 