from module.math import Matematica
from module.test import imprimir
def execute():
    context = Matematica(a=6, b=2)
    print(f'Soma: {context.somar()}')
    print(f'Subtração: {context.subtrair()}')
    print(f'Multiplicação: {context.multiplicar()}')
    
    with open('./aula6/arquivo.txt', 'w') as file:
        file.write(imprimir())

execute()