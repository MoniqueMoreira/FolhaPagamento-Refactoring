from datetime import datetime

class CartaoPonto():
    def __init__(self,id_emp="-------",data = "--------", hora = "---------"):
        self.id_emp = id_emp
        self.data =data
        self.hora = hora

    def setpPonto(self):
        self.data = datetime.now()
        self.hora = float(input("Digite a quantidade de Horas.minutos trabalhados:\n>>>"))
        print("Ponto Batido com sucesso:")
        CartaoPonto.toPonto(self)
        h = input("ENTER")
        
    def toPonto(self):
        print("   Data: {}\n   Horas Trabalhadas: {}".format(self.data,self.hora))
       
   
    def getPonto(self):
        return self.hora

    def newmethod113(self):
        return 
        