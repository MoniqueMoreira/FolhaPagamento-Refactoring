class Banco():

    def __init__(self,ag="-------",conta="-------"):
        self.ag = ag
        self.conta = conta

    def cadrastra(self):
        Banco.setAgencia(self)
        Banco.setConta(self)

    def modificar(self):
        h = int(input("Deseja mudar :\n1-AGENCIA\n2-CONTA\n>>>"))
        if h==1:
            Banco.setAgencia(self)
        elif h==2:
            Banco.setConta(self)
        else:
            print("OPÇÃO INVÁLIDA")

    def setAgencia(self):
        ag = input("Digite a AGENCIA:\n>>>")
        self.ag = ag
    
    def setConta(self):
        conta = input("Digite a CONTA\n>>>")
        self.conta =conta

    def getConta(self):
        return self.conta
        
    def getAgencia(self):
        return self.ag

    def toBanco(self):
        print("   Agencia: {}\n   Conta: {}".format(self.ag,self.conta))