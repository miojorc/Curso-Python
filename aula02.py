# =====> String, int, float e input <=====

# =====> Ex:1 <=====

nome = ""
cpf = ""

nome = input("digite seu nome: ")
cpf = input("digite seu cpf: ") 

print("seu nome é", nome, "e seu cpf é", cpf)

convert to int or float
int() float()

n1 = int(input("digite 1 numero: ")) #5
n2 = float(input("digite o 2 numero: ")) #0.25
print(10+n1)
print(10.55+n2)

# =====> Ex:2 <=====

n1 = 0
n1 = int(input("digite 1 numero: ")) 

print(f"seu antecessor é: {n1-1}",f"seu sucessor é: {n1+1}")

anoAtual = 2024

n1 = 0

n1 = int(input("digite o ano que você nasceu: "))
anoAtual = int(input("digite o ano eu que estamos: "))

if(input("você ja fez aniversario s/n? ") == "s" or input("você ja fez aniversario s/n? ") == "S"): anoAtual -= 1

print(f"sua idade é: {anoAtual-n1}")

# =====> Ex:3 <=====

produtos = ["", ""]
precos = [0.0, 0.0]
valorTotal = 0.0

for x in range (len(produtos)): #usar tamanho da variavel
    produtos[x] = input(f"digite o nome do produto {x+1}: ")
    precos[x] = float(input(f"digite o preço do produto {produtos[x]}: "))

for x in range (len(produtos)): #usar o tamanho da variavel
    print(f"o preço atual do produto {produtos[x]} é:", end = "")

    if(x == 0): precos[x] -= round(precos[x]*0.1, 2)
    else: precos[x] -= round(precos[x]*0.25, 2)

    print(f" {precos[x]}")

for x in range (2): valorTotal += precos[x]
print(f"o valor total é: {valorTotal}")

# =====> Ex:4 <=====

F = 0.0
C = 0.0

F = float(input("digite a temperatura em °F: "))
C = round(5 * ((F-32) / 9), 2)

print(f"a temperatura em celsius é {C}°C")

# tipos que serão trabalhados: string, int, float e bool