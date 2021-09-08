from datetime import datetime

class Taxas():
    def __init__(self,id_emp="--------", add ="-------", motivo = "--------", data = "--------" ):
        self.id_emp = id_emp
        self.add = add
        self.motivo = motivo
        self.data = data

    def cadastrar(self,id_emp):
        self.id_emp = id_emp
        motivo  = input("Motivo da taxa:\n>>>").capitalize()
        self.motivo =motivo
        add = float(input("Valor da TAXA:\n>>>"))
        self.add = add
        self.data = datetime.now()
        print("Taxa de Serviço Cadastrada com Sucesso!!\n")
        Taxas.toTaxa(self)
        
    def getTaxas(self):
        return self.add

    def toTaxa(self):
        print("   Motivo da taxa: {}\n   Valor da taxa: {}\n   Data: {}".format(self.motivo,self.add,self.data))
        h= input("ENTER")