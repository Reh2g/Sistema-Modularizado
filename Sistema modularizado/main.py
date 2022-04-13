# Bibliotecas

from time import sleep

# Modulos

from Modules.Interface.introSystem import *
from Modules.Archive.archive import *

# PROGRAMA PRINCIPAL

archive = 'users.txt'

if not arquivoExiste(archive):
    criarArquivo(archive)

while True:
    answer = menu(['Ver pessoas cadastradas',
    'Cadastrar nova pessoa',
    'Sair do programa'])
    if answer == 1:

# Opção de listar o conteúdo de um arquivo

        lerArquivo(archive)
    elif answer == 2:

# Opção de cadastrar uma nova pessoa

        intro('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('idade: ')
        cadastrar(archive, nome, idade)
    elif answer == 3:

# Opção de sair do sistema

        intro('\033[1mSaindo do sistema... Até logo!\033[m')
        sleep(1)
        print('\033[1;36mUwU\033[m'.center(49))
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(1.3)
