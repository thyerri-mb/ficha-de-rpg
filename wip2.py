while True:
    matriz = [
        "Bárbaro		Guerreiro	Paladino",
        "Artífice	Ladino		Bardo",
        "Druida		Mago		Clérigo"
    ]
    print("Dentre as classes:")
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])

    classe = input("Qual a classe do seu personagem? ")
    try:
        e_numero = int(classe)
    except ValueError:
        e_numero = 0
        classe = classe.capitalize() #tá faltando aqui bardo, feiticeiro, bruxo, artifice... sla tá faltando
        if classe in ["Bárbaro", "Guerreiro", "Paladino", "Artífice", "Ladino", "Bardo", "Druida", "Mago", "Clérigo"]:
            break