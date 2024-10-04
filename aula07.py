# ==> estruturas de dados <==

#lista -> lista=[] valores mutaveis # array
#tupla -> tupla=() valores imutavel # const array
#dicionario -> dici={} chave e valor mutaveis

# lista=[]
# tupla=("senai","aluno")
# dicionario={} # key : value
# dicionario["escola"]="senai"
# dicionario["salas"]=20
# dicionario["alunos 1"]=800

# #dicionario.pop("salas")
# #dicionario.clear() #limpa o dicionario inteiro
# print(dicionario.values()) # retorna apenas os valores
# print(dicionario.keys()) # retorna apenas as chaves
# #print(dicionario)

# #percorrendo todos os valores de um dicionario

# #percorrer atraves das chaves
# for chave in dicionario.keys():
#     print(chave,dicionario[chave])

# #percorre atraves dos valores
# for valores in dicionario.values():
#     print(valores)

# #percorrer atravez de chave e valor
# for chave, valor in dicionario.items():
#     print(chave, valor)

Dados={}

Dados["Nome: "    ] =     input("Digite seu nome: "  )
Dados["Idade: "   ] = int(input("Digite seu idade: "))
Dados["CPF: "     ] =     input("Digite seu CPF: "   )

if(Dados["Idade: "] >= 18):
    print("Dados Cadastrados:")
    for chave in Dados.keys():
        print(chave,Dados[chave])
else:
    print(Dados["Nome: "],", você é menor de idade", sep="")