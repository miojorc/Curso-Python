# =====> estruturas de repetição, while, for <=====

# =====> Ex:1 <=====

for i in range(20): #0 até n-1 -> 0 até 19
    print(i)

for i in range(5,15): # inicio 5 até n-1 14 -> 5 até 14
    print(i)

for i in range(0,20,5): # inicio 0, até n-1 19 incremento de 5
    print(i)

# =====> Ex:2 <=====

nome=""
for i in range(5):
    nome= nome + input("digite seu nome: ")

print(nome)

# =====> Ex:3 <=====

num=0
for i in range(5):
    num = num +i 

# print(num)

n=0
n=int(input("digite o numero que vc quer ver a tabuada: "))

for i in range(10):
    print(f"{n}x{i} =",n*i)


# =====> desafio próprio <=====

import time

HW = ['*','*','*','*','*','*','*','*','*','*','*']
texto = [""]


contador = 0

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

gabarito = "hello world"

# HW = gabarito.split()

# for A in HW: 
#     HW[contador] = '*'
#     contador+=1

# contador = 0

for A in gabarito:
    for L in alfabeto:
        HW[contador] = L
        for i in range(11):
            texto[0] += HW[i]
        print(texto[0])
        texto = [""]
        if(HW[contador] == gabarito[contador]): break
        time.sleep(0.05)
    contador+=1

# =====> Ex:4 <=====

n = 0
bigNumber = 0


for i in range(5):
    n = float(input("digite um numero: "))
    if(i==0): bigNumber = n
    if(n>bigNumber): bigNumber = n

print("o maior número é:", bigNumber)

print("maria linda") # foi uma amiga minha que colocou isso quando eu sai falar com o professor, preferi deixar no código

# =====> Ex:5 <=====

n = float(input("digite o preço do pão: "))
n1 = n

print("Panificadora pão de ontem - tabela de preços")

for i in range(1,51):
    print(i, "-" , "R$", round(n*(i), 2), end = "     ")
    if((i%5 == 0)): print()