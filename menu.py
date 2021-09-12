from G_Func import G_Func
from G_Empregados import G_Empregados
from Folha import Folha
import os
from Registro import Registro
clear = lambda: os.system('cls')

def menu():
    i=0
    while(i!=1):
        clear()
        Registro.atul_lista()
        print("----Bem-Vindo ao menu Principal----\nEscolha uma das opções abaixo:\n")
        z = int(input("1- Gerenciar Empregados\n2- Gerenciar Funções\n3- Roda Folha\n4- Sair\n>>>"))
        clear()
        if z==1:
            G_Empregados.Ação()
        elif z==2:
            G_Func.Ação()
        elif z==3:
            Folha.atualizar_lista()
            Folha.folha()
        elif z==4:
            break 
        else:
            print("Opção Inválida")
            h = input("ENTER")

menu()