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
    
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self,modelo):
        return self.__modelo= modelo
    
    def get_año(self):
        return self.__año
    def set_año(self,año):
        return self.__año= año

    def get_velocidad_actual(self):
        return self.__velocidad_actual
    def set_velocidad_actual(self,velocidad_actual):
        if velocidad_actual >=0:
            self.__velocidad_actual= velocidad_actual