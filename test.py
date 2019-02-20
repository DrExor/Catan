class Poblado:
    def __init__(self):
        numeros_poblado = []

        numero_territorios = 3 # Alrededor del poblado
        while len(numeros_poblado) < numero_territorios:
            try:
                x = int(input("Introduce el primer número del poblado (x > 2, x < 12, x !== 7, 0 para ignorar): "))

                if x == 0:
                    print("Tu poblado está en la costa y tiene 1 territorio menos")
                    numero_territorios = 2
                elif x < 2 or x == 7 or x > 12:
                    print ("Ese número no es válido, introduce un valor entre 2 y 12 excepto el 7")
                else:
                    numeros_poblado.append(x)
            except:
                print('Tienes que introducir un NUMERO!')
        
        self.numeros = numeros_poblado
    
    def calcular_probabilidad(self):
        print(self.numeros)
   

poblado1 = Poblado()
poblado1.calcular_probabilidad()

# class Territorio:
#     def __init__(self, tipo, numero):
#         self.tipo = tipo
#         self.numero = numero
    
#     def imprimir(self):
#         print("tipo: {}, número: {}".format(self.tipo, self.numero))
        
# bosque = Territorio("Madera", 5)

# print(bosque.numero)