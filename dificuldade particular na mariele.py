#código para calcular hipotenusa solução de um problema pessoal
#Na aula da mariele não sei resolver hipotenusa então criei esse programa


co = int(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

#resolver a hipotenusa
hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("\n**************************\n")

print("O valor da hipotenusa é: {}".format(hipotenusa))