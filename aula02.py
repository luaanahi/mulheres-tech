"""print("Qual a sua idade?")
idade = int(input())

if idade >= 18:
    print("ACESSO LIBERADO! BOA FESTA!")
else:
    print("ACESSO NEGADO! VOCÊ É MENOR DE IDADE")"""

    # CÓDIGO PARA LIBERAR ACESSO SOMENTE PARA MAIORES DE 19 ANOS

"""print("Qual a sua idade?")
idade = int(input())

if idade < 19:
    print("ACESSO NEGADO! VOCÊ É MENOR DE IDADE")
elif idade == 18:
    print("VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁ ACESSO!")
else:
    print("ACESSO LIBERADO! BOA FESTA!")"""


    # código para saber se o aluno foi aprovado, reprovado ou ficou para recuperação

"""print("Digite a nota do primeiro bimestre: ")
B1 = float(input())    # aqui pedimos para o código entender que o valor que pedimos para o usuário digitar, seja interpretado como valor inteiro
print("Digite a nota do segundo bimestre: ")
B2 = float(input())
print("Digite a nota do terceiro bimestre: ")
B3 = float(input())
print("Digite a nota do quarto bimestre: ")
B4 = float(input())
media = (B1 + B2 + B3 + B4) / 4
print("a média é ", media)

if media >= 7:
    print("APROVADO")
elif media <= 5:
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")"""


    # CÓDIGO PARA SABER SE UMA PESSOA É APTA PARA PARTICIPAR DO PROJETO MULHERES TECH OU NÃO

"""print("Qual seu gênero? (F ou M)")
genero = input().upper()
print("Qual município você mora?")
municipio = input().lower()

if genero == "F" and municipio == "rio de janeiro":
    print("você pode participar do mulheres tech")
else:
    print("você não pode participar do mulheres tech")"""


    #código para o exercício de liberar acesso à filme apenas a maiores de 18 anos ou 16 com responsáveis

print("Qual sua idade?")
idade = int(input())

if idade >= 18:
    print("Acesso liberado! Bom filme\nAproveite nossos combos de pipoca e refrigerante")

elif idade >= 16:
    print("O filme selecionado é para maiores de 18 anos\nPara acessar você precisa estar acomapanho de um responsável\nVocê está com algum responsável?")
    responsavel = input().upper()
    if responsavel == "SIM":
        print("Acesso liberado! Bom filme\nAproveite nossos combos de pipoca e refrigerante")
    else:
        print("Você só pode ver o filme acompanhado de um responsável")

else:
    print("Acesso negado! Você é menor de idade")