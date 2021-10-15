class hero:
     
    #private variabel
   def __init__(self,inputname):
        self.name = inputname
   def show(self,tipe):
       print("Show info diclass hero")
       print("{} health: {}".format(
            self.name,
            tipe
            )
       )
class hero1(hero):
    def __init__(self, inputname):
        super().__init__(inputname)

    def show(self):
        print("Show info diclass hero1")
        print('{} \n\tTipe: Intelegent, \n\tHealth : {}',format(
            self.name
        ))
lsia = hero1('Sina')

lsia.show()