from NullEmpregado import NullEmpregado
import pickle
from Agenda import Agenda
from Comissionado import Comissionado
from Horista import Horista
from Assalariado import Assalariado
import random

class Registro():
    #lista para armazena 
    emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
    agenda_disp =  pickle.load(open( "agendas_disp.pickls", "rb" ))
    
    #Funções internas 
    def atul_lista():
        Registro.emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
        Registro.agenda_disp =  pickle.load(open( "agendas_disp.pickls", "rb" ))

    def gera_id():
        k=0
        while(k!=1):
            x = random.randrange(1,1000)
            for i in Registro.emp_cadastrados:
                if i.id_emp == x:
                    break
            return x

    def salva_lista():
        pickle.dump( Registro.emp_cadastrados, open( "emp_cadastrados.pickls", "wb" ) )

    #Funções que reger Empregados

    def get_empregados():
        obj = NullEmpregado()
        k=int(input("Sabe o ID do funcionario?\n1-Sim\n2-Não\n3-Volta\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadastrados:
                if emp == i.id_emp:
                    return i
            return obj
        elif k==3:
                return
        else:
            print("OPÇÃO INVÁLIDA")

    def mostra_emp():
        num_emp = len(Registro.emp_cadastrados)
        print("Empregados Disponíveis: {}\n".format(num_emp))
        for i in Registro.emp_cadastrados:
            i.toEmpregado()
            print()
        h=input("ENTER")

    def add_empregado():
        id_emp=Registro.gera_id()
        i=0
        while(i!=1):
            k= int(input("Digite TIPO\n1-Horista\n2-Assalariado\n3-Comissionado\n4-Volta\n>>>"))
            if k == 1:
                new = Horista()
                new.setcadrasta(id_emp)
                i=1
            elif k==2:
                new = Assalariado()
                new.setcadrasta(id_emp)
                i=1
            elif k==3:
                new = Comissionado()
                new.setcadrasta(id_emp)
                i=1
            elif k==4:
                return
            else:
                print("TIPO INVÁLIDO")
        Registro.emp_cadastrados.append(new)
        Registro.salva_lista()
        print("Empregado cadastradro com  sucesso!!!")
        new.toEmpregado()
        h=input("ENTER")

    def remover_empregado():
        i = Registro.get_empregados()
        if type(i) != NullEmpregado: 
            Registro.emp_cadastrados.remove(i)
            print("Empregado Removido com Sucesso!!")
            Registro.salva_lista()
            k=input("ENTER")
            return
        else:
            print("Empregado Não cadastrado")
            k = input("ENTER")
        
    def altera_dados():
        i = Registro.get_empregados()
        i.modificar_cadrastro()
        Registro.salva_lista()
        i.toEmpregado()
        h=input("ENTER")
        return
    
    #Cartão de ponto
    def cartao_ponto():
        i = Registro.get_empregados()
        i.setNovo_Ponto()
        Registro.salva_lista()
        return

    def ver_cartao_ponto():
        i = Registro.get_empregados()
        print("Pontos Até o Momento: {}\n".format(len(i.pontos)))
        for d in i.pontos:
            d.toPonto()
        k = input("ENTER")
        return
    
    #Vendas
    def ver_vendas():
        i = Registro.get_empregados()
        print("Vendas Até o Momento: {}\n".format(len(i.vendas)))
        for d in i.vendas:
            d.toVenda()
            print()
        h = input("ENTER")
        return
    
    def lanca_vendas():
        i = Registro.get_empregados()
        i.setNova_Venda()
        Registro.salva_lista()
        return

    #Taxas
    def ver_taxas():
        i = Registro.get_empregados()
        print("Taxas Até o Momento: {}\n".format(len(i.taxas)))
        for d in i.taxas:
            d.toTaxa()
        print()
        h = input("ENTER")
        return

    def lanca_taxa():
        i = Registro.get_empregados()
        i.setNova_Taxa()
        Registro.salva_lista()
        return

    #Agenda
    def criar_agenda():
        nAgenda =[]
        print("Nova Agenda:")
        nAgenda = Agenda()
        nAgenda.criar_agenda()
        Registro.agenda_disp.append(nAgenda)
        pickle.dump( Registro.agenda_disp, open( "agendas_disp.pickls", "wb" ) )
        print("Nova agenda foi cria com Sucesso!!!")

    def mostra_agendas():
        print("Agendas Disponiveis:")
        for x in Registro.agenda_disp:
            x.toAgenda()
        f = input("ENTER")

    def muda_agenda_emp():
        k = int(input("Sabe o ID do Empregado:\n1-Sim\n2-Não\n3-Volta\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadastrados:
                if emp == i.id_emp:
                    Registro.mostra_agendas()
                    ag = int(input("Digite a Agenda Desejada:\n1-Semanalmente\n2-Bi-Semanalmente\n3-Mensalmente\n4-Anualmente\n>>>"))
                    x = 0
                    while(x!=1):
                        if ag==1 or ag==2:
                            if ag == 1:
                                i.agenda_emp = "Semanalmente"
                            else:
                                i.agenda_emp = "Bi-Semanalmente"
                            i.dia = input("Digite o Dia da Semana Disponivel na Agenda:\n>>>").capitalize()
                            x=1
                        elif ag==3:
                            i.agenda_emp = "Mensalmente"
                            i.dia = int(input("Digite o Dia do Mês Disponivel na Agenda:\n>>>"))
                            x=1
                        elif ag==4:
                            i.agenda_emp = "Anualmente"
                            i.dia = int(input("Digite o Dia do Mês Disponivel na Agenda:\n>>>"))
                            i.mes = int(input("Digite o Mês do Ano Disponivel na Agenda:\n>>>"))
                            x=1
                        else:
                            print("Opção inválida")
                    i.ult_salario = "-------------"
                    pickle.dump( Registro.emp_cadastrados, open( "emp_cadastrados.pickls", "wb" ) )
                    k = input("ENTER")
                    return
            print("Empregado Não Cadastrado")
            k = input("ENTER")
        elif k==4:
            return
        else:
            print("OPÇÃO INVÁLIDA")
            k = input("ENTER")

    def undo():
        print("Opção indisponivel no momento")

    def remo():
        print("Opção indisponivel no momento")