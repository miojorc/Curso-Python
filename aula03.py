# operadores: > >= < <= == != or e and
# se ultiliza or para || e and para && 

# =====> Ex:1 <=====

x = 25
# if encadeado
if (x < 20):
    print("Teste 1.1")
if (x < 30):
    print("Teste 2.1")
# elif
if (x < 20):
    print("Teste 1.2")
elif (x < 30):
    print("Teste 2.2")

# =====> Ex:2 <=====

idade= 0
idade = int(input("digite sua idade (em numeros): "))

if(idade < 0 or idade > 120):
    print("idade invalida")
elif(idade < 18):
    print("você não pode acessar o site por ser menor de idade")
else:
    print("você pode acessar o site")

# =====> Ex:3 <=====

Continuar = True
Numero = 0.0
Media = 0.0

Continuidade = 0.0
SomaDeNumero = 0.0

NumeroDeNotas = 0
NumeroDeNotas = int(input("digite o número de notas para a média: "))

while(Continuar):
    Numero = float(input(f"digite sua {Continuidade+1}° nota : "))
    Continuidade += 1
    SomaDeNumero += Numero
    # if(input("deseja colocar mais uma nota y/n?") == "n"): Continuar = False
    if(NumeroDeNotas <= Continuidade): Continuar = False
Media = SomaDeNumero/Continuidade

print("sua media é:", Media)

if(Media < 5): print("Reprovado")
elif(Media > 5 and Media < 7): print("Recuperação")
else: print("Aprovado")

# =====> Ex:4 <=====

altura = 0.0
peso = 0.0

altura = float(input("digite seu altura : "))
peso = float(input("digite seu peso : "))

IMC = 0.0

IMC = round(peso/(altura*altura),2)

if(IMC < 17):
    print("Muito abaixo do peso")
elif (IMC < 18.49): 
    print("Abaixo do peso")
elif (IMC < 24.99): 
    print("Peso normal")
elif (IMC < 29.99): 
    print("Acima do peso")
elif (IMC < 34.99): 
    print("Obesidade I")
elif (IMC < 40): 
    print("Obesidade II")
elif (IMC < 200): 
    print("Obesidade III (mórbida)")
else:
    print("Mister bombastic")
print("IMC", IMC)