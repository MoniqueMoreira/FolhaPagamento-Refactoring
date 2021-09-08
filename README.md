# Projeto de Software: Folha de Pagamento(Refactoring)

*Primeiro Refactoring: Extract Method & Introduce Null Object

  No arquivo "Registo.py" antes existia um parte semelhante em alguns metodos que era um loop, para pode achar o empregado correspondente, separe ele em um metodo chamado get_Empregado(),  que irá olha os objetos(Empregados já cadastrados), e retorna o empregado selecionado, caso não encontre, ele irá retorna um objeto Null que tem caracterista semelhantes a Class Empregados, mais metodos que retorna outras um aviso que empregado não foi encontrado.
  
*Segundo Refactoring: Extract class & Template Method

  Nesta mesmo refactory foi mudado a chamada do Cartão de ponto, Vendas, Taxas para dentro da class Empregados, já que todos os empregados podem executar a ação, e para quando extiver tentando acessa um empregado não cadastrado(NullEmpregado) podemos não seja executado um ação fantasma.

*Terceiro Refactoring: Remove Assignments to Parameters

  Das class Taxas, Vendas era pedido o id do empregado, mais não era usado, foi retirado para torna a chamda do metodo mais simples.
