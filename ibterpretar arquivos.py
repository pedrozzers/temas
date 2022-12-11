from turtle import pd

with open ('teste.txt') as teste:
    arquivo=teste.read()

print(arquivo)


with open ('book1.txt') as book1:
    line=book1.readlines()
    for line in book1:
    print(line)

import pandas as pd
book1=pd.read_excel("book1.xlsx")
print(book1.columns)
