#dificulade de resolver equação de segundo grau

from time import sleep

#informar os cocientes da equação
#exeplo: ax² bx x
a=int(input("Digite o cociente A: "))
b=int(input("Digite o cociente B: "))
c=int(input("Digite o cociente C: "))

#resolver o delta 
delta=(b**2 - 4*a*c)
print("O delta é {}" .format(delta))

sleep(2)

#resolver o x1 e o x2
Res1=(-b - delta**1/2)/2*a
Res2=(-b + delta**1/2)/2*a

#printar resultados
print("As resoluções são: ")
print(Res1)
print(Res2)