import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    aleatorio = random.random() * 100
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada,tentativas))

        chute_str = input("Digite um número de 1 a 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Digite um número de 1 a 100")
            continue

        print("Você digitou: ", chute_str)


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O número secreto é menor que o seu chute.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}.".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O número secreto é maior que o seu chute.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}.".format(numero_secreto, pontos))

    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()