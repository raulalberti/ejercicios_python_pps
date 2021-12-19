#ACTIVIDAD 3 Ejercicio Clase_Persona

class Persona:
    def __init__(self, nombre="", edad=0, dni="", telefono="", email=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email

        @property
        def nombre(self):
            return self.__nombre

        @property
        def edad(self):
            return self.__edad

        @property
        def dni(self):
            return self.__dni

        @property
        def telefono(self):
            return self.__telefono

        @property
        def email(self):
            return self.__email

        @nombre.setter
        def nombre(self,nombre):
            self.__nombre = nombre

        def valida_dni(self):
            letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
            if len(self.__dni) != 9:
                print('Has introducido un DNI incorrecto')
                self.__dni = ''
            else:
                letra = self.__dni[8]
                num = int(self.__dni[:8])
                if letra.upper() != letras[num % 23]:
                    print('Has introducido un DNI incorrecto')
                    self.__dni = ''

        @dni.setter
        def dni(self,dni):
            self.__dni = dni
            self.valida_dni()

        @edad.setter
        def edad(self,edad):
            if edad < 0:
                print('Has introducido una edad incorrecta')
                self.__edad = 0
            else:
                self.__edad = edad

        @telefono.setter
        def telefono(self, telefono):
            if telefono == '':
                print('Introduce un teléfono')
                self.__telefono = telefono
            else:
                self.__telefono = telefono

        @email.setter
        def email(self, email):
            if email == '':
                print('No has introducido un email')
                self.__email = email
            else:
                self.__email = email

    def mostrar(self):
        return 'Nombre:'+self.nombre+' Edad:'+str(self.edad)+' DNI:'+self.dni+' Telefono:'+self.telefono+' Email:'+self.email

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona('Jose',17,'26145864S','952473694','pepito@yahoo.com')

print(persona1.mostrar())
print(persona1.es_mayor_de_edad())
