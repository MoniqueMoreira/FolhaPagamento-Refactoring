'''
    MUITO CUIDADO ESCUTAR ESTÁ FUNÇÃO, ELA REDEFINE TODAS AS LISTA USADAS NO PROGRAMAR
'''

from Agenda import Agenda
import pickle
# Lista que vai ter os empregados cadastrados 
emp_cadastrados=[]
pickle.dump( emp_cadastrados, open( "emp_cadastrados.pickls", "wb" ) )

#Lista de agendas padrões
agenda_disp = []
sem_pad = Agenda()
sem_pad.setSemanalmente()
agenda_disp.append(sem_pad)
men_pad = Agenda()
men_pad.setMensalmente()
agenda_disp.append(men_pad)
bi_pad = Agenda()
bi_pad.setBiSemanalmente()
agenda_disp.append(bi_pad)
pickle.dump( agenda_disp, open( "agendas_disp.pickls", "wb" ) )

#Lista com dia da semana 
DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]
pickle.dump( DIAS, open( "dias.pickls", "wb" ) )
