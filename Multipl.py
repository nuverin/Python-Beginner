#Metode Order resolution 

class a:
    def show(self):
        print('Date a')
class b:
    def show(self):
        print('Date b')

class c(b,a):
    pass

form = c()
form.show()

print(c.mro())