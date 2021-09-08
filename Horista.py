from Banco import Banco
from Empregados import Empregados
from datetime import datetime

class Horista(Empregados):

    def __init__(self,id_emp = "--------",data_cad = "---------",nome ="--------",endereco="--------",tipo = "--------",pagamento = "--------",agenda_emp = "-----------",dia = "------------",mes= "-------------",sindicato = "------------",hora ="------------" ):
        super().__init__(id_emp=id_emp, data_cad=data_cad, nome=nome, endereco=endereco, tipo=tipo, pagamento=pagamento, agenda_emp=agenda_emp, dia=dia, mes=mes, sindicato=sindicato)
        self.hora = hora 

    def setcadrasta (self,id_emp):
        self.tipo = "Horista"
        self.agenda_emp = "Semanalmente"
        super().cadrastra(id_emp)
        Horista.setHora(self)
        Horista.setData(self)

    def setData(self):
        self.data_cad = datetime.now()
        self.dia = "Sexta-feira"

    def modificar_cadrastro(self):
        i=0
        while(i!=1):
            k=int(input("Deseja ALTERA qual dados do empregado:\n1-Nome\n2-Endereço\n3-Forma de Pagamento\n4-Sindicato\n5-Valor hora\n>>>"))
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
                Horista.setHora(self)
                i=1
            else:
                print("Opção Inválida")

    def setHora(self):
        hora = float(input("Digite VALOR/HORA do empregado\n>>>"))
        self.hora = hora
    
    def toEmpregado(self):
        super().toEmpregados()
        print("   Valor/Hora: {}".format(self.hora))

    def receber(self):
        total_geral =0
        print("Nome: {}, ID: {}, Forma de Pagamanto: {}".format(self.nome,self.id_emp,self.pagamento))
        if self.pagamento == "Correios":
            print("Endereço: {}".format(self.endereco))
        elif self.pagamento == "Conta bancária":
            print("Conta: ",self.getConta())
            print("Agencia: ",self.getAgencia())
        valor = 0
        total = 0
        for i in self.pontos:
            hora = i.getPonto()
            if hora > 8 :
                extra = (hora - 8)*self.hora*1.5
                valor = 8*self.hora
            else:
                valor = hora*self.hora
                extra = 0
            total = total + valor + extra
        print("Total por Horas trabalhadas: {:.2f}".format(total))
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

    