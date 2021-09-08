from Empregados import Empregados
from datetime import datetime

class Assalariado(Empregados):

    def __init__(self,id_emp = "--------",data_cad = "---------",nome ="--------",endereco="--------",tipo = "--------",pagamento = "--------",agenda_emp = "-----------",dia = "------------",mes= "-------------",sindicato = "------------",salario ="------------" ):
        super().__init__(nome=nome, dia=dia, agenda_emp=agenda_emp, data_cad=data_cad, endereco=endereco, id_emp=id_emp, tipo=tipo, sindicato=sindicato, pagamento=pagamento)
        self.salario = salario

    def setcadrasta (self,id_emp):
        self.tipo = "Assalariado"
        self.agenda_emp = "Mensalmente"
        super().cadrastra(id_emp)
        Assalariado.setSalario(self)
        Assalariado.setData(self)

    def setData(self):
        self.data_cad = datetime.now()
        self.mes = self.data_cad.month
        self.dia = "$"

    def modificar_cadrastro(self):
        i=0
        while(i!=1):
            k=int(input("Deseja ALTERA qual dados do empregado:\n1-Nome\n2-Endereço\n3-Forma de Pagamento\n4-Sindicato\n5-Valor Salário\n>>>"))
            if k == 1:
                super().setNome()
                i=1
            elif k==2:
                super().setEndereco()
                i=1
            elif k==3:
                super().setPagamento()
                i=1
            elif k==4:
                super().setSindicato()
                i=1
            elif k==5:
                Assalariado.setSalario()
                i=1
            else:
                print("Opção Inválida")

    def setSalario(self):
        salario = float(input("Digite SALÁRIO do empregado\n>>>"))
        self.salario = salario
    
    def toEmpregado(self):
        super().toEmpregados()
        print("   Salario: {}".format(self.salario))

    def receber(self):
        total_geral = 0
        print("Nome: {}, ID: {}, Forma de Pagamanto: {}".format(self.nome,self.id_emp,self.pagamento))
        if self.pagamento == "Correios":
            print("Endereço: {}".format(self.endereco))
        elif self.pagamento == "Conta bancária":
            print("Conta: ",self.getConta())
            print("Agencia: ",self.getAgencia())
        total = float(self.salario)
        print("Salario: {:.2f}".format(total))
        totalT = 0
        tx_sind = 0 
        if self.sindicato == "Sim":
            tx_sind = self.getTaxa()
            print("Taxa Do Sindicato: {:.2f}".format(tx_sind))
            for i in self.taxas:
                adicionais = i.getTaxas()
                totalT = totalT + adicionais
            print("Taxas de Serviço: {:.2f}".format(totalT))

        total_geral = total_geral + total - totalT -tx_sind
        print("Total a receber: {:.2f}".format(total_geral))