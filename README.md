# Projeto de Software: Folha de Pagamento(Refactoring)

## Primeiro Refactoring: Extract Method & Introduce Null Object

  No arquivo "Registo.py" antes existia um parte semelhante em alguns metodos que era um loop, para pode achar o empregado correspondente, separe ele em um metodo chamado get_Empregado(),  que irá olha os objetos(Empregados já cadastrados), e retorna o empregado selecionado, caso não encontre, ele irá retorna um objeto Null que tem caracterista semelhantes a Class Empregados, mais metodos que retorna outras um aviso que empregado não foi encontrado.
  
  obs.: fiz mudaças semelhantes na parte da agenda, redirecionei a parte da procura de empregados para metodo get_Empregado(), e realoquei a parte de modificar a agenda do funcionario para class empregados.
  
## Segundo Refactoring: Extract class & Template Method & Move Method

  Nesta mesmo refactory foi mudado a chamada do Cartão de ponto, Vendas, Taxas para dentro da class Empregados, já que todos os empregados podem executar a ação, e para quando extiver tentando acessa um empregado não cadastrado(NullEmpregado) podemos não seja executado um ação fantasma.

## Terceiro Refactoring: Remove Assignments to Parameters

  Das class Taxas, Vendas era pedido o id do empregado, mais não era usado, foi retirado para torna a chamda do metodo mais simples.
  
obs.: fiz mudaças semelhantes na parte da agenda, redirecionei a parte da procura de empregados para metodo get_Empregado(), e realoquei a parte de modificar a agenda do funcionario para class empregados(Move Method).

## Quarto Refactoring: Consolidate Duplicate Conditional Fragments
  
  Diminuir a quantidade de if's juntado as ações repetidas que ocoriam na parte da escolha dos dias da semana para "Semanalmente" e "Bi-Semanalmente", também optei por tira o loop.
  
## Quinto Refactoring: Move Method & Move Accumulation to Collecting Parameter
  
  Nas class Horista/ Assalariado/ Comissionado, separei o method "receber" em quatro partes, agora o novo "receber" que vai chamar os outros method's, o "quant_receber" que ira calcular o valor que a empresa Bruto que empressa tem que paga, exemplo o horista, vai calcular as valores por hora, o e outro dois method que agora estão na class Empregados, que e o "dados_receber" que vai mostra as informações do empregado e sua forma de pagamento, e method "desconto", que mostra e retorna se o empregado pertencer ao sindicato, as sua taxas e deconta do salario bruto.
  Optei por transferir os dois method's para class Empregados pois ele usava o method para qualquer tipo de empregado, isto fazia com que hovesse repetição de codigo nas subclasses.

## Sexto Refactoring: Mediator & Large Class & Strategy 

  Nesta parte da refotoração tentei corrigir dois problemas proeminente, o primeiro era que a class "regristro" estava muito grande, existia muitos method's então searei em outras duas class que chamei de G_Empregados(G: Gerenciador) e G_Função,a G_Empregados seria responsavel diretamente pelos method's que iria mecher com os objetos Empregados, já a G_Func será responsavel por executa as outras funções que o programa exigia, a class Registro ficou responsavel por armazena as lista, e por se class "pai" das outras dua class onde ficaria funções usada por ambas para não ter repetição do codigo.
  Com a class Registro dividida foi possivel criar um mediador, que seria responsavel por fazer a chamada das funções dos method's, sem a necessidade de if's aninhados.
  
  obs.: Nesta parte do refatoramento foi que deu mais trabalho em si, queria fazer um 'Strategy', mais com era muitos if's para cria class para cada preferir so deixar os if's de necessarios para interação com usuario.Também pelo fato de nem todas as class construir um objeto em si, foi muito dificil de criar classe que só conteria method's para chamar outras class,  isto dificultou a separação de subclass.
