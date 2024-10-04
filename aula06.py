# =====> funcoes <=====
# print() input() pop() remove() round()
# def nome_para_funcao (): 

# =====> Exemplo: 1 <=====

def soma():
    print("exemplo de uma funcao sem parametros,",1+1)

soma()

# =====> Exemplo: 2 <=====

#funcao com parametro ou argumento

def soma2(num1,num2):
    print("exemplo com argumento",num1+num2)

soma2(10,15)

# =====> Exemplo: 3 <=====

#variavel de contexto de escopo

x=10

def exemplo():
    x=15

exemplo()
print(x)

#retorno
def exemplo2(a,b):
    return a+b

soma=exemplo2(25,25)
print(soma)

# =====> Ex: 1 <=====

operacao = ""

while((operacao != "E") and (operacao != "e")):
    def calc(n1, op, n2):
        if(op == "+"): return n1 + n2
        elif(op == "-"): return n1 - n2
        elif(op == "*"): return n1 * n2
        elif(op == "/"): return n1 / n2

    N1 = float(input("escreva o primeiro número:"))

    operacao = str(input("escreva o tipo de calculo, \"+\", \"-\", \"*\" e \"/\""))

    N2 = float(input("escreva o segundo  número:"))

    print(calc(N1, operacao, N2))

    operacao = str(input("digite E para sair "))

# =====> Ex: 2 <=====

continuar = True

opcao = 0
dinheiro = 0

print("==== Menu ====","1 - Para converter dolar para real","2 - Para converter real para dolar"
      ,"3 - Para sair ", sep = "\n Digite")

def convert(n,nT):
    if(nT==1):return round(n*5.5,2)
    if(nT==2):return round(n/5.5,2)

while continuar:
    opcao = int(input("Digite uma opção do menu: "))
    if(opcao == 1):
        dinheiro = int(input("digite o valor a converter: "))
        print("valor convertido R$",convert(dinheiro,opcao))
    elif(opcao == 2):
        dinheiro = int(input("digite o valor a converter: "))
        print("valor convertido $",convert(dinheiro,opcao))
    elif(opcao == 3):
        continuar = False
    else:
        print("Opção invalida")

# =====> Ex: 3 <=====

continuar = True

opcao = 0
dinheiro = 0

transferencia = 0

operacoes = []

def Deposit(n1):
    global dinheiro
    dinheiro+=n1

def Saque(n1):
    global dinheiro
    dinheiro-=n1

def Extrato():
    for i in range(operacoes.__len__()):
        print("--" , operacoes[i], "--")
    print("seu saldo: R$",dinheiro)

def transacao(T1,T2,OP):
    global transferencia, operacoes, Deposit, Saque
    transferencia = float(input(f"digite o valor do {T1}: "))
    operacoes.append(f"você {T2} R${transferencia}") 
    if(OP): Deposit(transferencia)
    else: Saque(transferencia)
    print(f"você {T2} R${transferencia}")

print("\t==== Menu ====","1 - Para depositar","2 - Para pegar o dinheiro"
      ,"3 - ver extrato ", "4 - Sair ", sep = "\nDigite ")

while continuar:
    opcao = int(input("Digite uma opção do menu: "))
    if(opcao == 1):
        transacao("deposito", "depositou", True)
    elif(opcao == 2):
        transacao("saque", "sacou", False)
    elif(opcao == 3):
        Extrato()
    elif(opcao == 4):
        continuar = False
    else:
        print("Opção invalida")