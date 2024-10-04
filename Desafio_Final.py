perguntas={
    "Telefonou para vítima?" : 0,
    "Esteve no local do crime?" : 0,
    "Mora perto da vítima?" : 0,
    "Devia para vítima?" : 0,
    "Já trabalhou com a vítima" : 0
}

resposta=""
soma=0

for chave in perguntas.keys():
    print(chave, end=" ")
    resposta=input("S/N: ")
    if(resposta == "S" or resposta == "s"):
        perguntas[chave] = 1

for chave in perguntas.keys():
    soma+=perguntas[chave]

if(soma<2):
    print("você é inocente")
elif(soma<5):
    print("você é cúmplice")
else:
    print("você é assasino")