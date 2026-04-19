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

    def get_nivel_combustible(self):
        return self.__nivel_combustible
    def set_nivel_combustible(self, nivel_combustible):
        if 0<=nivel_combustible and nivel_combustible<=100:
            self.__nivel_combustible= nivel_combustible
    
    def aumentar_velocidad (self, acelerar):
        if acelerar >0:
            self.__velocidad_actual += acelerar
            self.__nivel_combustible -= acelerar*0.1
            if self.__nivel_combustible <0:
                self.__nivel_combustible=0
    
    def viaje (self, distancia):
        consumo= distancia/10
        if self.__nivel_combustible>= consumo:
            return True
        return False
    
    def info (self):
        print ("***Informacion del Vehiculo***")
        print ("Marca: ", self.__marca)
        print("Modelo: ", self.__modelo)
        print("Año: ", self.__año)
        print("Velocidad Actual: ", self.__velocidad_actual, "Km/h")
        print("Nivel de Combustible: ", self.__nivel_combustible, "%")