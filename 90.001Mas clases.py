# crear clases para un juego, monstruus y armas

#creando clase armas, esta clase va  a tener las caracrteristicas principales de todas las armas del juego

class arma ():
    def __init__(self,nombre,dano,durabilidad, rareza,nivel):
        self.__nombre=nombre
        self.__dano=dano
        self.__durabilidad=durabilidad
        self.__rareza=rareza
        self.__nivel=nivel

    def __ataque(self,monstruo):
        if monstruo['vida']>0 and self.__durabilidad>0:
            monstruo['vida']-=self.__dano- monstruo['defensa']
            self.__durabilidad-=3
            if monstruo['vida']<=0:
                print('el monstruo ha muerto')
        elif monstruo['vida']>0 and self.__durabilidad<=0:
            print("Debes incrementar la durabilidad de tu arma")
            monstruo['vida']-=1
            if monstruo['vida']<=0:
                print('el monstruo ha muerto')
        else:
            print('El monstruo ha muerto')

    def __str__(self):
         return self.__nombre,self.__dano,self.__durabilidad,self.__rareza,self.__nivel


#creando  una subclase de arma: Espadas

class Espada(arma):
    def __init__(self,nombre,dano,durabilidad, rareza,nivel,perforacion):
        #llama a clase arma
        arma.__init__(self,nombre,dano,durabilidad, rareza,nivel)
        #atributo clase Espada
        self.__perforacion=perforacion

    def __ataque(self,monstruo):
        if monstruo['vida']>0 and self.__durabilidad>0:
            monstruo['vida']-=self.__dano - (monstruo['defensa']-self.__perforacion)
            self.__durabilidad-=3
            if monstruo['vida']<=0:
                print('el monstruo ha muerto')
        elif monstruo['vida']>0 and self.__durabilidad<=0:
            print("Debes incrementar la durabilidad de tu arma")
            monstruo['vida']-=1
            if monstruo['vida']<=0:
                print('el monstruo ha muerto')
        else:
            print('El monstruo ha muerto')


#creando objeto Espada

espada_furia_indeleble=Espada("Furia Indeleble",10,60,"Comun",2,4)

print(espada_furia_indeleble.__str__())

#arma a distancia

class arma_distancia(arma):
    def __init__(self,nombre,dano,durabilidad, rareza,nivel,golpe_critico):
        arma.__init__(self,nombre,dano,durabilidad, rareza,nivel)
        self.__init__golpe_critico=golpe_critico

        def __ataque(self, monstruo):
            if monstruo['vida'] > 0 and self.__durabilidad > 0:
                monstruo['vida'] -= self.__dano+(self.__dano *golpe_critico/100) - monstruo['defensa']
                self.__durabilidad -= 1
                if monstruo['vida'] <= 0:
                    print('el monstruo ha muerto')
            elif monstruo['vida'] > 0 and self.__durabilidad <= 0:
                print("Debes incrementar la durabilidad de tu arma")
                monstruo['vida'] -= 1
                if monstruo['vida'] <= 0:
                    print('el monstruo ha muerto')
            else:
                print('El monstruo ha muerto')

#creando objeto arma a distancia

pisto_locker=arma_distancia("Gatillo Divino",3,40,3,"Extravagante",10)

print(pisto_locker.__str__())

#creando clase monstruo

class monstruo():
    def __init__(self,nombre,vida,ataque,defensa,elemento):
        self.__nombre=nombre
        self.__vida=vida
        self.__ataque=ataque
        self.__defensa=defensa
        self.__elemento=elemento

    def __str__(self):
        return self.__nombre,self.__vida,self.__ataque, self.__defensa,self.__elemento

#objeto monstruo

monstruo_bosque=monstruo("Arbol maldito",67,12,20,'Tierra')
print(monstruo_bosque.__str__())