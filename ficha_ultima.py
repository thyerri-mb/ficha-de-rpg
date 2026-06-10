forca = 0
agilidade = 0
vigor = 0
intelecto = 0
carisma = 0
while True:
    nome = input("Qual o nome do seu personagem? ")
    try:
        e_numero = int(nome)
    except ValueError:
        e_numero = 0
        if nome != "" and len(nome) >= 3:
            nome = nome.capitalize()
            break
while True:
    print("Dentre humano, elfo, anão, goblin e ogro")
    raca = input("Qual a raça do seu personagem? ")
    try:
        e_numero = int(raca)
    except ValueError:
        e_numero = 0
        raca = raca.capitalize()
        if raca in ["Humano", "Elfo", "Anão", "Goblin", "Ogro"]:
            break   
def bonus_de_raca(raca):
    if raca == "Humano":
        mensagem = "Por ser um humano, você terá 1 ponto a mais de carisma"
        bonus = "Carisma"
    elif raca == "Elfo":
        mensagem = "Por ser um elfo, você terá 1 ponto a mais de intelecto"
        bonus = "Intelecto"
    elif raca == "Anão":
        mensagem = "Por ser um anão, você terá 1 ponto a mais de vigor"
        bonus = "Vigor"
    elif raca == "Goblin":
        mensagem = "Por ser um goblin, você terá 1 ponto a mais de agilidade"
        bonus = "Agilidade"
    elif raca == "Ogro":
        mensagem = "Por ser um ogro, você terá 1 ponto a mais de força"
        bonus = "Força"
    return mensagem, bonus
m = bonus_de_raca(raca)
print(m[0])

while True:
    classe = input("Qual a classe do seu personagem? ")
    try:
        e_numero = int(classe)
    except ValueError:
        e_numero = 0
        classe = classe.capitalize()
        if classe in ["Bárbaro", "Guerreiro", "Paladino", "Monge", "Caçador", "Ladino", "Acólito", "Místico", "Druida", "Mago", "Clérigo", "Psiônico"]:
            break
def vida_e_mana(classe):
    if classe in ["Bárbaro", "Guerreiro", "Paladino", "Monge"]:
        arquetipo = [3, 1]
    elif classe in ["Caçador", "Ladino", "Acólito", "Místico"]:
        arquetipo = [2, 2]
    elif classe in ["Druida", "Mago", "Clérigo", "Psiônico"]:
        arquetipo = [1, 3]
    return arquetipo

while True:
    nivel = input("Qual o nível do seu personagem? ")
    try:
        e_numero = int(nivel)
        nivel = int(nivel)
        if nivel < 1 or nivel > 20:
            print("Insira um valor inteiro entre 1 e 20")
        else:
            break
    except ValueError:
        e_numero = 0
        print("Insira um valor inteiro entre 1 e 20")     

pda = 12 + nivel
atributos = {
    "Força": forca,
    "Agilidade": agilidade,
    "Vigor": vigor,
    "Intelecto": intelecto,
    "Carisma": carisma }
print(atributos)
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
    
    forca = int(input("Força: "))
    vigor = int(input("Constituição: "))
    agilidade = int(input("Destreza: "))
    intelecto = int(input("Intelecto: "))
    carisma = int(input("Carisma: "))
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
aumentador = m[1]
atributos[aumentador] += 1

identificacao = vida_e_mana(classe)
pv = (10 + nivel * identificacao[1])
pm = (2 + nivel * identificacao[1])

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