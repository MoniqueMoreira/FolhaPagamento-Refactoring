from Taxas import Taxas
from Vendas import Vendas
from CartaoPonto import CartaoPonto
from datetime import datetime
from Sindicato import Sindicato
from Banco import Banco

class Empregados(Sindicato,Banco,CartaoPonto,Vendas,Taxas):

    def __init__(self,id_emp = "-------------",data_cad = "-------------",nome ="-------------",endereco="-------------",tipo = "-------------",pagamento = "-------------",agenda_emp = "-------------",dia = "-------------",mes= "-------------",ult_salario= "-------------",sindicato = "-------------"):
        self.id_emp = id_emp
        self.data_cad= data_cad
        self.nome = nome
        self.endereco= endereco
        self.tipo = tipo
        self.pagamento = pagamento
        self.agenda_emp = agenda_emp
        self.dia = dia
        self.mes = mes
        self.ult_salario = ult_salario
        self.sindicato = sindicato
        self.pontos= []
        self.vendas = []
        self.taxas = []
        
    def cadrastra(self, id_emp):
        print("Cadrastra NOVO Empregado:\n")
        self.id_emp = id_emp
        Empregados.setNome(self)
        Empregados.setEndereco(self)
        Empregados.setPagamento(self)
        Empregados.setSindicato(self)
       
    def setNome(self):
        nome = str(input("Digite o NOME do empregado\n>>>"))
        self.nome = nome.title()

    def setEndereco(self):
        endereco = str(input("Digite o ENDEREÇO do empregado\n>>>"))
        self.endereco = endereco.title()
    
    def setSindicato(self):
        i=0
        while(i!=1):
            k = int(input("O empregado PERTENCE AO SINDICATO?\n1-Sim\n2-Não\n>>>"))
            if k != 1 and k != 2:
                print("DADO INVÁLIDO")
            else:
                if k == 1:
                    self.sindicato = "Sim"
                    Sindicato.cadrastra_emp(self,self.id_emp)
                    i=1
                elif k==2:
                    self.sindicato = "Não"
                    i=1
                else:
                    print("DADO INVÁLIDO")

    def setPagamento(self):
        i=0
        while(i!=1):
            k = int(input("Digite o TIPO DE PAGAMENTO\n1-Correios\n2-Em Mãos\n3-Conta bancária\n>>>"))
            if k != 1 and k !=2  and k != 3:
                print("FORMA DE PAGAMNTO INVÁLIDA")
            else:
                if k==1:
                    self.pagamento = "Correios"
                    i=1
                elif k==2:
                    self.pagamento = "Em Mãos"
                    i=1
                elif k==3:
                    self.pagamento = "Conta bancária"
                    Banco.cadrastra(self)
                    i=1
                else:
                    print("FORMA DE PAGAMNTO INVÁLIDA")

    def setNovo_Ponto(self):
        novo_ponto = CartaoPonto()
        novo_ponto.setPonto()
        self.pontos.append(novo_ponto)

    def setNova_Venda(self):
        new_venda = Vendas()
        new_venda.setVendas()
        self.vendas.append(new_venda)

    def setNova_Taxa(self):
        new_taxa = Taxas()
        new_taxa.setTaxa()
        self.taxas.append(new_taxa)

    def setNova_Agenda(self):
        ag = int(input("Digite a Agenda Desejada:\n1-Semanalmente\n2-Bi-Semanalmente\n3-Mensalmente\n4-Anualmente\n>>>"))
        if ag==1 or ag==2:
            if ag == 1:
                self.agenda_emp = "Semanalmente"
            else:
                self.agenda_emp = "Bi-Semanalmente"

            self.dia = input("Digite o Dia da Semana Disponivel na Agenda:\n>>>").capitalize()
        elif ag==3:
            self.agenda_emp = "Mensalmente"
            self.dia = int(input("Digite o Dia do Mês Disponivel na Agenda:\n>>>"))
        else:
            self.agenda_emp = "Anualmente"
            self.dia = int(input("Digite o Dia do Mês Disponivel na Agenda:\n>>>"))
            self.mes = int(input("Digite o Mês do Ano Disponivel na Agenda:\n>>>"))
        self.ult_salario = "-------------"

    def toEmpregados(self):
        print("Data de Cadastro: {}".format(self.data_cad))
        print("ID: {}".format(self.id_emp))
        print("Nome: {}".format(self.nome))
        print("Endereço: {}".format(self.endereco))
        print("Tipo de Agenda: {}".format(self.agenda_emp))
        print("Dia/Dia da Semana: {}".format(self.dia))
        print("Forma de Pagamento: {}".format(self.pagamento))
        if self.pagamento == "Conta bancária":
            Banco.toBanco(self)
        print("Ultimo pagamento: {}".format(self.ult_salario))
        print("Pertence ao Sindicato: {}".format(self.sindicato))
        if self.sindicato == "Sim":
            Sindicato.toEmp_sind(self)
        print("Tipo de Empregado: {}".format(self.tipo))        

    def desconto(self):
        totalT = 0
        tx_sind = 0
        if self.sindicato == "Sim":
            tx_sind = self.getTaxa()
            print("Taxa Do Sindicato: {:.2f}".format(tx_sind))   
            for i in self.taxas:
                adicionais = i.getTaxas()
                totalT = totalT + adicionais
            print("Taxas de Serviço: {:.2f}".format(totalT))
        return totalT + tx_sind
        
    def dados_receber(self):
        print("tudo ok")
        print("Nome: {}, ID: {}, Forma de Pagamanto: {}".format(self.nome,self.id_emp,self.pagamento))
        if self.pagamento == "Correios":
            print("Endereço: {}".format(self.endereco))
        elif self.pagamento == "Conta bancária":
            print("Conta: ",self.getConta())
            print("Agencia: ",self.getAgencia())
