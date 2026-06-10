while True:
    nome = input("Qual o nome do seu personagem? ")
    try:
        e_numero = int(nome)
        print("")
    except ValueError:
        e_numero = 0
        if nome != "":
            break
        else:
            print("")

raca = "i"
while raca != "H" or raca != "A" or raca != "E":
    raca = input("Qual a raça do seu personagem? Humano (H), anão (A) ou elfo (E)? ")
    if raca == "H" or raca == "A" or raca == "E":
        break
if raca == "H":
    raca = "Humano"
    print("Por ser um humano, você terá +1 ponto de carisma")
elif raca == "A":
    raca = "Anão"
    print("Por ser um anão, você terá +1 ponto de constituição")
else:
    raca = "Elfo"
    print("Por ser um elfo, você terá +1 ponto de inteligência")

recomendacao = ""
clas = ""
while clas != "G" or raca != "M" or raca != "L":
    clas = input("Qual a classe do seu personagem? Guerreiro (G), mago (M) ou ladino (L)? ")
    if clas == "G" or clas == "M" or clas == "L":
        break
if clas == "G":
    clas = "Guerreiro"
    recomendacao = "Força, para aumentar seu ataque e Constituição, para aumentar seus pontos de vida"
elif clas == "M":
    clas = "Mago"
    recomendacao = "Sabedoria, para aumentar seus pontos de magia e Inteligência, para aumentar sua quantidade de magias"
else:
    clas = "Ladino"
    recomendacao = "Destreza, para aumentar sua furtividade e Carisma, para aumentar sua enganação"

nivel = 0
while True:
    nivel = input("Qual o nível do seu personagem? ")
    try:
        e_numero = int(nivel)
        nivel = int(nivel)
        if nivel < 1 or nivel > 20 or (nivel % 2 != 0 and nivel % 2 != 1):
            print("Insira um valor inteiro entre 1 e 20")
        else:
            break
    except ValueError:
        e_numero = 0
        print("Insira um valor inteiro entre 1 e 20")     
        
print("")

pda = 12 + nivel #Pontos de atributo.
Fo = 0
Co = 0
De = 0
In = 0
Sa = 0
Ca = 0
atributos = [Fo, Co, De, In, Sa, Ca]
vma = int(4+(nivel/2)) #Valor máximo de atributo.
total = 0
erro = 0

while total != pda or erro == 1:
    print(f"Distribua {pda} pontos entre os atributos:")
    print("Força, Constituição, Destreza, Inteligência, Sabedoria e Carisma")
    print("")
    print(f"Por ser um {clas}, priorize colocar mais pontos em {recomendacao}")
    print(f"Cada atributo deve ter pelo menos 1 ponto e nenhum deles deve exceder mais que {vma}")
    print("")
    
    Fo = int(input("Força: "))
    Co = int(input("Constituição: "))
    De = int(input("Destreza: "))
    In = int(input("Inteligência: "))
    Sa = int(input("Sabedoria: "))
    Ca = int(input("Carisma: "))
    print("")
    total = Fo + Co + De + In + Sa + Ca
    
#Checar se algum atributo excede o máximo permitido pelo nível.
    if Fo > vma or Co > vma or De > vma or In > vma or Sa > vma or Ca > vma:
        erro = 1
        print("Há um ou mais atributos com mais pontos do que o máximo!")
#Checar se algum atributo é zero.
    elif Fo < 1 or Co < 1 or De < 1 or In < 1 or Sa < 1 or Ca < 1:
        erro = 1
        print("Há um ou mais atributos com menos pontos do que o mínino!")
    else:
        if total > pda:
            erro = 1
            print(f"Você colocou {total-pda} pontos a mais do que tem para distribuir!")
        elif total < pda:
            erro = 1
            print(f"Você deixou {pda-total} pontos sobrando para distribuir!")
        else:
            erro = 0
            break
        
if raca == "Humano":
    Ca = (Ca+1)
elif raca == "Anão":
    Co = (Co+1)
elif raca == "Elfo":
    In = (In+1)

pv = (10 + nivel*Co)
if clas == "Guerreiro":
    pv = (pv + nivel * 2)
elif clas == "Ladino":
    pv = (pv + nivel)

pm = (2 + nivel * In)
if clas == "Mago":
    pm = (pm + nivel * 2)
elif clas == "Ladino":
    pm = (pm + nivel)
def Ficha():
    print("")
    print("== Ficha de Personagem ==")
    print("")
    print(f"Nome: {nome}")
    print(f"Raça: {raca}", "	", f"Classe: {clas}")
    print("")
    print(f"Força: {Fo}", "	", f"Constituição: {Co}")
    print(f"Destreza: {De}", "	", f"Inteligência: {In}")
    print(f"Sabedoria: {Sa}", "	", f"Carisma: {Ca}")
    print("")
    print(f"Pontos de Vida: {pv}", "	", f"Pontos de Mana: {pm}")
    return ""
i = Ficha()
print(i)