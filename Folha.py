from datetime import datetime
import pickle

class Folha():

    emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
    DIAS = pickle.load(open( "dias.pickls", "rb" ))
    emp_recebeu = []

    def atualizar_lista():
        Folha.emp_cadastrados =  pickle.load(open( "emp_cadastrados.pickls", "rb" ))
        Folha.DIAS = pickle.load(open( "dias.pickls", "rb" ))
        Folha.emp_recebeu = []

    def limpar():
        for x in Folha.emp_recebeu:
            x.pontos= []
            x.vendas = []
            x.taxas = []
        pickle.dump( Folha.emp_cadastrados, open( "emp_cadastrados.pickls", "wb" ) )

    def folha():

        dia,mes,ano = input("Digite o Dia/Mês/Ano respectivamente(Ex. 23/07/2021):\n>>>").split('/')
        ano = int(ano)
        dia = int(dia)
        mes = int(mes)

        data=datetime(year=ano,month=mes,day=dia)
        indice_da_semana = data.weekday()
        dia_da_semana = Folha.DIAS[indice_da_semana]
        
        # definindo ultimo dia do mes
        if mes == 1 or mes ==3 or mes == 5 or mes==7 or mes==8 or mes==10 or mes==12:
            ult_dia = 31
        elif mes == 2:
            ult_dia = 29
        elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
            ult_dia = 30

        for x in Folha.emp_cadastrados:
            
            if x.agenda_emp == "Semanalmente":
                if x.dia == dia_da_semana:
                    if x.ult_salario == "-------------":
                        x.receber()
                        x.ult_salario = data
                        Folha.emp_recebeu.append(x)
                    else:
                        ult_sal = int(x.ult_salario.day)
                        if ((ult_sal + 7)%ult_dia) == dia:
                            x.receber()
                            x.ult_salario = data
                            Folha.emp_recebeu.append(x)

            elif x.agenda_emp == "Bi-Semanalmente":
                if x.dia == dia_da_semana:
                    if x.ult_salario == "-------------":
                        x.receber()
                        x.ult_salario = data
                        Folha.emp_recebeu.append(x)
                    else:
                        ult_sal = int(x.ult_salario.day)
                        if ((ult_sal + 14)%ult_dia) == dia:
                            x.receber()
                            x.ult_salario = data
                            Folha.emp_recebeu.append(x)

            elif x.agenda_emp == "Mensalmente":
                if x.dia == dia or (x.dia == "$" and dia == ult_dia):
                    if x.ult_salario == "-------------":
                        x.receber()
                        x.ult_salario = data
                        Folha.emp_recebeu.append(x)
                    else:
                        ult_sal =int(x.ult_salario.month)
                        if ult_sal+1 == mes: 
                            x.receber()
                            x.ult_salario = data
                            Folha.emp_recebeu.append(x)
            else: #Anualmente
                if (x.dia == dia or (x.dia == "$" and dia == ult_dia))  and x.mes == mes:
                    if x.ult_salario == "-------------":
                        x.receber()
                        x.ult_salario = data
                        Folha.emp_recebeu.append(x)
                    else :
                        ult_sal =int(x.ult_salario.year)
                        if ult_sal+1 == ano:
                            x.receber()
                            x.ult_salario = data
                            Folha.emp_recebeu.append(x)
            print()
        k = int(input("Se todos Empregados da lista já tiver sido computados e devidamente pagos, digite:\n1 - Para para limpar seus dados, como CARTÃO DE PONTO, TAXAS DE SERVIÇO, VENDAS, entre outros\n2- Caso queira recalcular o pagamento para este dia\n>>"))
        if k == 1:
            Folha.limpar()
            print("Empregados pagos com sucesso!!!")
        elif k == 2:
            print("Folha NÃO SALVA, isto impede de calcular o próximos salário corretamente")
        k = input("ENTER")