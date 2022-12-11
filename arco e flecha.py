import random
from time import sleep

#feito por Lucas Fuchs

nome=input(str("Digite seu nome de usuário "))

print("Olá {}, você foi desafiado para um duelo de arco e flecha".format(nome))
sleep(2)

print("Deseja aceitar o duelo?")

resposta=input("(sim ou não) ")

while resposta!="sim":
    quit("flw cagão")

if resposta=="sim":
    print("Ok, você terá que dizer um número, se seu oponente estiver na plataforma que você adivinhar (1 a 10) , você o derrota, caso o contrário ele terá a chance de revidar")
sleep(5)

print("Seu inimigo já está posicionado")
sleep(2)

number=random.randint(1,10)

while number<11:
    numero=int(input("diga um número de 1 a 10: "))
    if number>=1 and numero<number:
        print("numero muito baixo")
    elif numero==number:
        print("parabéns, você ganhou")
        break
    elif number<10 and numero>number:
        print("numero muito alto")
    else:
        print("numero fora de questao")
    sleep(2)
    print("vez do seu inimigo, ele terá 1 chance em 6 de te acertar")
    numero2=random.randint(1,6)
    number2=random.randint(1,6)
    sleep(2)
    if number2==numero2:
        print("seu inimigo o matou, você perdeu")
        break
    else:
        print("seu oponente errou")