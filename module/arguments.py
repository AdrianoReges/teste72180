import sys
from dotenv import load_dotenv
import os

sys.path.insert(0, '/Users/adrianoreges/Documents/coder/python/aula8')

load_dotenv()


a = 1
var_b = 2

var_env = os.environ.get('VARIAVEL')

# def main(a, main_b):
#     value = test_args(a=a, b=main_b)
#     print(sys.argv)
#     script = sys.argv[0]
#     print(f'{script=:}')
#     print(f'Argumento na posicao 3: {sys.argv[3]}')
#     return script

def main():
    # print(sys.argv)
    # list_args = sys.argv
    # for arg in list_args:
    #     print(f'{arg} = {type(arg)}')
    try:
        if sys.argv[1] == 'test':
            print('Eu salvo o meu dataframe em um DB de HOMOLOG')
        elif sys.argv[1] == 'prod':
            print('Eu salvo o meu dataframe em um DB de PROD')
    except IndexError:
        print('Nao foram passados argumentos')
        print(var_env)

def test_args(a, b):
    ...

main()
