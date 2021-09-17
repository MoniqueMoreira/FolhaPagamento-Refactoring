from NullEmpregado import NullEmpregado
import pickle

class Registro():
    
    #lista para armazena 
    emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
    agenda_disp =  pickle.load(open( "agendas_disp.pickls", "rb" ))
    
    #Funções internas 
    def atul_lista():
        Registro.emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
        Registro.agenda_disp =  pickle.load(open( "agendas_disp.pickls", "rb" ))

    def salva_lista():
        pickle.dump( Registro.emp_cadastrados, open( "emp_cadastrados.pickls", "wb" ) )
        pickle.dump( Registro.agenda_disp, open( "agendas_disp.pickls", "wb" ) )

    #Funções Geral

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

    def mostra_agendas():
        print("Agendas Disponiveis:")
        for x in Registro.agenda_disp:
            x.toAgenda()
        f = input("ENTER")