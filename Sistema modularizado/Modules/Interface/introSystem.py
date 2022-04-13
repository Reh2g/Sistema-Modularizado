def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def linha(tam=40):
    return '-' * tam


def intro(txt):
    print(linha())
    print(f'{txt}'.center(40))
    print(linha())


def menu(lst):
    intro('        \033[1mMENU PRINCIPAL\033[m')
    c = 1
    for item in lst:
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

    
def introNewUser():
    print('-' * 40)
    print('\033[1mNOVO CADASTRO\033[m'.center(48))
    print('-' * 40)
