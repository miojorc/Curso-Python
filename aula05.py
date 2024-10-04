# =====> estrutura while <=====

i=0
while i <11:
    print("laço while:",i)
    i=i+1
else:
    print("acabou o loop")

# =====> Fibonachi <=====

# foi um desafio proposto por mim 

fibonachiI=1
preFibonachiI=1
preFibonachiII = 0

limite = 2**9999999

while fibonachiI < limite:
    fibonachiI = preFibonachiI + preFibonachiII
    print("fibonachi",fibonachiI)
    preFibonachiII = preFibonachiI
    preFibonachiI = fibonachiI
else:
    print("acabou o loop")

# =====> Ex: 1 <=====

i=9
while i <48:
    print("laço while:",i)
    i=i+1
else:
    print("acabou o loop")

# =====> Ex: 2 <=====

continuar = True
nome = ""
CPF = 0
telefone = 0

opcao = 0
print("==== Menu ====\n Digite 1 -Cadastrar nome\n Digite 2 -Cadastrar telefone\n Digite 3 -CPF\n Digite 4 -Sair")

while continuar:
    opcao = int(input("Digite uma opção do menu: "))
    if(opcao == 1):
        nome = input("digite seu nome: ")
    elif(opcao == 2):
        telefone = int(input("digite seu telefone: "))
    elif(opcao == 3):
        CPF = int(input("digite seu CPF: "))
    elif(opcao == 4):
        continuar = False
print("==== Dados Coletados ====",f"nome - {nome}", f"telefone - {telefone}", f"CPF - {CPF}", sep="\n Digite ")

# =====> array/lista <=====

array=["0"] #pesquisar como adicionar
print(array)
# 2 modos de adicionar
array.append("x1")
print(array)

array[0] = "1"
print(array)

array.remove("x1")
print(array)

array.pop(0)
print(array)

# =====> Ex: 3 <=====

continuar = True

mercado = []

item = ""

opcao = 0
print("==== Menu ====","1 - Para cadastrar novo item","2 - Para remover um produto da lista"
      ,"3 - para remover todos os produtos da lista ","4 - Para sair","5 - Exibir os produtos", sep = "\n Digite")

while continuar:
    opcao = int(input("Digite uma opção do menu: "))
    if(opcao == 1):
        mercado.append(input("digite um item: "))
    elif(opcao == 2):
        mercado.remove(input("digite o item a remover: "))
    elif(opcao == 3):
        mercado.clear()
    elif(opcao == 4):
        continuar = False
    elif(opcao == 5):
        print("==== Lista ====")
        for i in range(mercado.__len__()): #len(mercado)
            print("    " , mercado[i])
        if(len(mercado) == 0):
            print("    " , "Vazio")

print("==== Lista ====")
for i in range(mercado.__len__()):
    print("    " , mercado[i])

# =====> Ex: 4 <=====

numeros = [0,0,0,0,0,0,0,0,0,0]
soma = 0

for i in range(numeros.__len__()): 
    numeros[i] = int(input("digite um número: "))
    soma+=numeros[i]
for i in range(numeros.__len__()): #len(numeros)
    print("    " , numeros[i])

print(soma)