#membuat program menghitung jumlah orang yang masuk keangkot
class hero:
 
    #private variabel
    __jumlh = 0

    def __init__(self,inputname,inputhealth,atk,armor):
        self.__name = inputname
        self.__healt = inputhealth
        self.__atk = atk
        self.__arm = armor
        self.__level = 1
        self.__Ex = 0

        self.__healthmax = self.__healt * self.__level
        self.__atks = self.__atk * self.__level
        self.__armor = self.__arm * self.__level


        self.__hs = self.__healt
        hero.__jumlh += 1

    @property
    def info(self):
        return "{} level {}: \nhealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__hs,self.__healthmax,self.__atks,self.__armor)
    
    @property
    def exp(self):
        pass
    @exp.setter
    def exp(self,addexp):
        self.__Ex += addexp
        if(self.__Ex >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__Ex -= 100

            self.__healthmax = self.__healt * self.__level
            self.__atks = self.__atk * self.__level
            self.__armor = self.__arm * self.__level

sata = hero('Nvus',100, 50, 10)
ala = hero('aska', 100, 2, 1)
print(sata.info)
        
sata.exp = 100
sata.exp = 10
print(sata.info)