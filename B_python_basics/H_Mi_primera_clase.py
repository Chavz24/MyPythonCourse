print("*"*8, 'Mi primera clase',"*"*8,'\n')

class impresora():
    def __init__(self):
        self.__alimentador_corriente = False
        self.__encendido=False
        self.__coneccion_pc=False
        self.__alimentador_papel=False
        self.__coneccion_internet=False
        self.__coneccion_wireless=False

    def __chequeo_papel(self,):
        print("Chequeo de papel")
        tiene_papel=self.__alimentador_papel
        if tiene_papel:
            return True
        else:
            return False

    def enciende_impresora(self,conectar_impresora):
        self.__alimentador_corriente=conectar_impresora
        if self.__alimentador_corriente:
           self.__alimentador_papel = self.__chequeo_papel()
        if conectar_impresora and self.__alimentador_papel:
            self.__encendido=True
            return 'Impresora encendida y con papel'
        elif conectar_impresora and self.__alimentador_papel==False:
            return 'Impresora encendida y sin papel'
        else:
            return 'Impresora no conectada'

    def poner_papel (self,papel_aqui):
        self.__alimentador_papel=papel_aqui
        if papel_aqui:
            return True
        else:
            return False
    def estado(self):
        print(f'''
        La impresora esta conectada:{self.__alimentador_corriente },
        La impresora esta encendida:{self.__encendido},
        La impresora esta conectada al ordenador:{self.__coneccion_pc},
        La impresora tiene papel:{self.__alimentador_papel},
        La impresora esta conectada a internet:{self.__coneccion_internet},
        La impresora esta conectada wireless: {self.__coneccion_wireless}''')

periferico1=impresora()
periferico1.poner_papel(True)
print(periferico1.enciende_impresora(True))


periferico1.estado()


