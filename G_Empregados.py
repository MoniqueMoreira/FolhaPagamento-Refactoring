
from Registro import Registro
from NullEmpregado import NullEmpregado
from Comissionado import Comissionado
from Horista import Horista
from Assalariado import Assalariado
import random


class G_Empregados(Registro):

    #Chamada
    def Ação():
        z= int(input("1-Adicionar Novo Empregado\n2-Remover Empregado\n3-Mostra Empregados\n4-Altera Dados Empregado\n5-Mudar Agenda do Empregado\n6-Volta\n>>>"))
        if z==1:
            G_Empregados.add_empregado()
        elif z==2:
            G_Empregados.remover_empregado()
        elif z==3:
            Registro.mostra_emp()
        elif z==4:
            G_Empregados.altera_dados()
        elif z==5:
            G_Empregados.muda_agenda_emp()
        else:
            return
    #Funções que reger Empregados
    def gera_id():
        k=0
        while(k!=1):
            x = random.randrange(1,1000)
            for i in Registro.emp_cadastrados:
                if i.id_emp == x:
                    break
            return x

    def add_empregado():
        id_emp=G_Empregados.gera_id()
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

    def muda_agenda_emp():
        i = Registro.get_empregados()
        Registro.mostra_agendas()
        i.setNova_Agenda()
        Registro.salva_lista()
        return