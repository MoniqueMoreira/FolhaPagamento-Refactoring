from datetime import datetime

class Vendas():
    def __init__(self,venda = "--------", data = "-------"):
        self.venda = venda
        self.data = data

    def setVendas(self):
        venda = float(input("Digite o VAlOR da venda:\n>>>"))
        self.venda = venda
        self.data = datetime.now()
        print("Venda Cadastrada com Sucesso!!\n")
        Vendas.toVenda(self)
        h = input("ENTER")
    
    def getVendas(self):
        return self.venda
        
    def toVenda(self):
        print("Valor da Venda: {}\n   Data: {}".format(self.venda,self.data))