
class car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = self.model+" "+self.make+" "+self.year+"."
        return long_name.title()


    def read_odometer(self):
        """devuelve la lectura de kilometros recorridos"""
        print("el total de kilometros recorridos es de: "+str(self.odometer))

    #creando metodo para modificar valor de read_odometer
    def update_odometer_read(self, recorrido):
        """modifica la lectura de kilometros recorridos"""
        if recorrido >= self.odometer:
            self.odometer = recorrido
        else:
            print("no puedes retroceder el conteo de kilometros recorridos")

    #creando metodo para incrementar kilometraje
    def increment_odometer_read(self, miles):
        """incrementa la lectura de kilometraje"""
        self.odometer += miles

class electric_car(car):
    def _init_(self, make, model,year):
        super()._init_(make, model, year)
        self.bateria = 70

    def tama_bateria(self):
        """a attempt to describe the size of the battery of a car"""
        print("el tamanio de la bateria es de: "+str(self.bateria))
tesla = electric_car('tesla','model s','2018')
print(tesla.descriptive_name())
tesla.tama_bateria()
