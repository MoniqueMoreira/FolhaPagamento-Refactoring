class Sindicato():

    def __init__(self,id_emp="-------",id_sind="-------",taxa_sind="-------",pago="-------"):
        self.id_emp = id_emp
        self.id_sind = id_sind
        self.taxa_sind = taxa_sind

    def cadrastra_emp(self, id_emp):
        self.id_emp = id_emp
        self.id_sind = id_emp + 1000
        Sindicato.setTaxa(self)

    def setTaxa(self):
        taxa_sind = float(input("Digite a TAXA POR SALÁRIO do sindicato:\n>>>"))
        self.taxa_sind = taxa_sind

    def getTaxa(self):
        return self.taxa_sind
    
    def toEmp_sind(self):
        print("   ID do Sindicato: {}\n   Taxas Mensal: {}".format(self.id_sind,self.taxa_sind))
