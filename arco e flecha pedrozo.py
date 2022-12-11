import random
from time import sleep


nome=input(str("Digite seu Apelido "))

print("Olá {}, você foi convidado para uma batalha de arco e flecha".format(nome))
sleep(2)

print("Deseja se juntar a batalha?")

resposta=input("(sim ou não) ")

while resposta!="não":
    quit("Você foi condenado a guilhotina e morreu :(")

if resposta=="sim":
    print("Obrigado por se juntar, o outro batalhão está vindo por alguma das 10 entradas do reino, informe um numero de (1 a 10), caso acerte vencemos mas se errar tem a chance de sermos pegos despreparados")
sleep(5)

print("Seu inimigo já está a caminho")
sleep(2)

number=random.randint(1,10)

while number<11:
    numero=int(input("diga um número de 1 a 10: "))
    if number>=1 and numero<number:
        print("acho que é uma entrada de numero maior")
    elif numero==number:
        print("parabéns, você acertou e vencemos")
        break
    elif number<10 and numero>number:
        print("numero muito alto, talvez seja em uma entrada de numero menor")
    else:
        print("não existe essa entrada")
    sleep(2)
    print("vez do batalhão inimigo, ele terá 1 chance em 6 de te acertar")
    numero2=random.randint(1,6)
    number2=random.randint(1,6)
    sleep(2)
    if number2==numero2:
        print("seu inimigo o derrotou, o reino foi invadido e todos foram mortos")
        break
    else:
        print("os inimigos ainda não chegaram")