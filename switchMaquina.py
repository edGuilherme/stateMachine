import random

fim = False
vida = 10
fome = 0
print("O jogo inicia com o Troll dormindo a caverna.")
print("Ele possui"+ " " + str(vida) + " " + "de vida e" + " " + str(fome) + " " + "de fome.")
while True:
    estado = input("Qual a próxima ação do jogo?")
    fome +=1
    if fome > 4:
        estado = "Come"

    match estado:
        case "Dorme":
            if vida <=9:
                vida += 1
            print("O troll está dormindo com" + " " + str(vida) + " " + "de vida e" + " " + str(fome) + " " + "de fome.")

        case "Come":
            fome -=3
            vida -=1
            print("O troll foi comer e agora está com" + " " + str(vida) + " " + "de vida e" + " " + str(fome) + " " + "de fome.")

        case "Luta":
            vidaInimigo = random.randint(1, 4)
            ataqueInimigo = random.randint(1, 2)
            ataqueTroll = random.randint(2, 4)
           #while True:
                #lógica da batalha

            print("A vida do inimigo é" + " " + str(vidaInimigo))
            print("A vida do Troll é " + " " + str(vida))


        case "Morre":
            fim = True
            print("O troll morreu")
        case _:
            print("Digite um comando válido: Dorme, Come ou Luta")
    if fim == True:
        break






