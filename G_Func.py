from Registro import Registro
from Agenda import Agenda

class G_Func(Registro):

    #Chamada
    def Ação():
        k= int(input("Deseja:\n1-Lança Venda\n2-Ver Vendas\n3-Lança Taxa\n4-Ver Taxas\n5-Bater Ponto\n6-Ver Ponto\n7-Ver Agendas Disponiveis\n8-Cria Nova Agenda\n9-Volta\n>>>"))
        if k==1:
            G_Func.lanca_vendas()
        elif k==2:
            G_Func.ver_vendas()
        elif k==3:
            G_Func.lanca_taxa()
        elif k==4:
            G_Func.ver_taxas()
        elif k==5:
            G_Func.cartao_ponto()
        elif k==6:
            G_Func.ver_cartao_ponto()
        elif k==7:
            G_Func.mostra_agendas()
        elif k==8:
            G_Func.criar_agenda()
        else:
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
        Registro.salva_lista()
        print("Nova agenda foi cria com Sucesso!!!")

    def mostra_agendas():
        print("Agendas Disponiveis:")
        for x in Registro.agenda_disp:
            x.toAgenda()
        f = input("ENTER")

    