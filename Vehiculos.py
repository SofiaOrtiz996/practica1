class Vehiculo (self, marca, modelo, año, velocidad_actual, nivel_combustible):
    def_init_(self,marca,modelo,año, velocidad_actual,nivel_combustible):
        self.__marca= marca
        self.__modelo= modelo
        self.__año= año
        self.__velocidad_actual= velocidad_actual
        self.__nivel_combustible= nivel_combustible
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        return self.__marca= marca
    