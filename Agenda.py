class Agenda():

    def __init__(self, tipo = "-----------",dia="-------------",mes = "---------------"):
        self.tipo = tipo
        self.dia = dia
        self.mes = mes

    def criar_agenda(self):
        f = 0
        while(f!=1):
            tipo = int(input("Esolha o tipo da agenda\n1-Semanalmente\n2-Bi-Semanalmente\n3-Mensalmente\n4-Anual\n>>>"))
            if tipo == 1 or tipo == 2:
                if tipo == 1:
                    self.tipo = "Semanalmente"
                else:
                    self.tipo = "Bi-Semanalmente"
                    
                dia = int(input("Escolha o dia da semana:\n1-Segunda-feira\n2-Terça-feira\n3-Quarta-feira\n4-Quinta-feira\n5-Sexta-feira\n>>>"))
                if dia == 1:
                    self.dia = "Segunda-feira"
                    f=1
                elif dia == 2:
                    self.dia = "Terça-feira"
                    f=1
                elif dia == 3:
                    self.dia = "Quarta-feira"
                    f=1
                elif dia == 4:
                    self.dia = "Quinta-feira"
                    f=1
                else:
                    self.dia = "Sexta-feira"
                    f=1
            elif tipo == 3:
                self.tipo = "Mensalmente"
                self.dia = int(input("Digite o Dia do mês(Ex. 18,Se for ultimo dia do Mês coloque ""$"")\n>>>"))
                f=1
            elif tipo == 4:
                self.tipo = "Anualmente"
                self.dia = int(input("Digite o Dia do mês(Ex. 18,Se for ultimo dia do Mês coloque ""$"")\n>>>"))
                self.mes = int(input("Digite o Mês do ano(Ex. 7)\n>>>"))
                f=1
            else:
                print("OPÇÃO INVÁLIDA")

    def toAgenda(self):
        print("Tipo da Agenda: {}, Dia/Dia da Semana: {}, Mês: {}".format(self.tipo,self.dia,self.mes))

    def setSemanalmente(self):
        self.tipo = "Semanalmente"
        self.dia = "Sexta-feira"

    def setMensalmente(self):
        self.tipo = "Mensalamente"
        self.dia = "$"

    def setBiSemanalmente(self):
        self.tipo = "Bi-Semanalmente"
        self.dia = "Sexta-feira"

