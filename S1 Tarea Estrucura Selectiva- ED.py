#Diseñar un algoritmo tal que dados como datos dos variables de tipo
#entero, obtenga el resultado de la siguiente función:
num=int(input("Ingrese numero entero: "))
v=int(input("Ingrese v: "))
class Switcher:
   def switch(self, opcion):
       resp = 0
       return getattr(self, 'Case_' + str(opcion), lambda: resp)()
   def Case_1(self):
       resp =100*v
       return resp
   def Case_2(self):
       resp = 100**v
       return resp
   def Case_3(self):
       resp = 100/v
       return resp

opcion = Switcher()
print(opcion.switch(num))
