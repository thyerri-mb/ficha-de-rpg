

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
        if nome != "" and len(nome) >= 3 and nome.isalnum():
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
        bonus = "Carisma: "
    elif raca == "Elfo":
        mensagem = "Por ser um elfo, você terá 1 ponto a mais de intelecto"
        bonus = "Intelecto: "
    elif raca == "Anão":
        mensagem = "Por ser um anão, você terá 1 ponto a mais de vigor"
        bonus = "Vigor: "
    elif raca == "Goblin":
        mensagem = "Por ser um goblin, você terá 1 ponto a mais de agilidade"
        bonus = "Agilidade: "
    elif raca == "Ogro":
        mensagem = "Por ser um ogro, você terá 1 ponto a mais de força"
        bonus = "Força: "
    return mensagem, bonus
m = bonus_de_raca(raca)
print(m[0])

while True:
    print("Dentre guerreiro, ladino ou mago")
    classe = input("Qual a classe do seu personagem? ")
    try:
        e_numero = int(classe)
    except ValueError:
        e_numero = 0
        classe = classe.capitalize() #tá faltando aqui bardo, feiticeiro, bruxo, artifice... sla tá faltando
        if classe in ["Bárbaro", "Guerreiro", "Paladino", "Monge", "Caçador", "Ladino", "Acólito", "Místico", "Druida", "Mago", "Clérigo", "Psiônico"]:
            break
def coisas_de_classe(classe):
    if classe in ["Bárbaro", "Guerreiro", "Paladino", "Monge"]:
        arquetipo = [3, 1]
        recomendacao = "Força e Vigor"
    elif classe in ["Caçador", "Ladino", "Acólito", "Místico"]:
        arquetipo = [2, 2]
        recomendacao = "Agilidade e Carisma"
    elif classe in ["Druida", "Mago", "Clérigo", "Psiônico"]:
        recomendacao = "Intelecto"
        arquetipo = [1, 3]
    return arquetipo, recomendacao

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

pontos_de_atributo = 12 + nivel

atributos = ["Força: ","Agilidade: ","Vigor: ","Intelecto: ","Carisma: "]

valor_maximo = int(4+(nivel/2)) #Valor máximo de atributo.
identificacao = coisas_de_classe(classe)

print(f"Distribua {pontos_de_atributo} pontos entre os atributos:")
print("Força, Vigor, Agilidade, Intelecto e Carisma")
print("")
print(f"Por ser um {classe}, priorize colocar mais pontos em {identificacao[1]}")
print(f"Cada atributo deve ter pelo menos 1 ponto e nenhum deles deve exceder mais que {valor_maximo}")
print("")

atributinhos = 0
valores = []
valor_acola = pontos_de_atributo
while atributinhos < 5:
    if atributinhos == 0:
        i = input("Força: ")
    elif atributinhos == 1:
        i = input("Vigor: ")
    elif atributinhos == 2:
        i = input("Agilidade: ")
    elif atributinhos == 3:
        i = input("Intelecto: ")
    elif atributinhos == 4:
        i = input("Carisma: ")
    try:
        e_numero = i
        e_numero = int(e_numero)
        while 0 < e_numero <= valor_maximo:
            valor_acola = valor_acola-e_numero
            if valor_acola >= 0:
                valores.append(e_numero)
                atributinhos += 1
                break
            else:
                print("Você já excedeu seus pontos! Tente novamente")
                atributinhos = 0
                valor_acola = pontos_de_atributo
                valores.clear()
                break
    except ValueError:
        e_numero = 1
        atributinhos = atributinhos
atributos1 = dict(zip(atributos, valores))
print(atributos1)

aumentador = m[1]
atributos1[aumentador] += 1
boost = identificacao[0]
utopico = boost[0]
pv = (10 + nivel * utopico)
pm = (2 + nivel * utopico)

def Ficha():
    print("")
    print("== Ficha de Personagem ==")
    print("")
    print(f"Nome: {nome}", "	", f"Nível: {nivel}")
    print(f"Raça: {raca}", "	", f"Classe: {classe}")
    print("")
    for chave, valor in atributos1.items():
        print(f"{chave}: {valor}")
    print("")
    print(f"Pontos de Vida: {pv}", "	", f"Pontos de Mana: {pm}")
    return ""
i = Ficha()
print(i)