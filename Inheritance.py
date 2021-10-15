#Membuat program dengan iheritance

class form:
    #List 
    def __init__(self,data,out):
        self.data = input(data)
        self.output = input(out)
    
    def info(self):
        return print('Nama {}'.format(self.data))
        
class names(form):
    def __init__(self,data,out):
        super().__init__(data,out)
    def info(self):
        print('Nama : {}, Sekolah : {}'.format(self.data.casefold(),self.output.swapcase()))
        
    
data = names('--------Selamat Datang------ \nSilahkan Mengisi Fomulir Pendaftaran \nNama:',"Sekolah : ")

data.info()