def cabecalho(msg):
    print(linha())
    print('{:^55}'.format(msg))
    print(linha())


def menu(lista_opc):
    for c in range(0, len(lista_opc)):
        print('{}{}{} - {}{}{}'.format('\033[1;37m', c+1, '\033[m', '\033[1;36m',  lista_opc[c], '\033[m'))
    print(linha())


def linha():
    return '='*55


def LeiaInt(msg):
    verify = False
    while True:
        try:
            i = int(input(msg))
        except:
            print(f'\033[1;31mErro! por favor digite um numero inteiro valido valido\033[m')
        else:
            return i


def opc(opc):
    opção = LeiaInt(opc)
    return opção


def opcMenu(msg):
    while True:
        option = opc('sua opção?:')
        if option == 1:
            return option
        if option == 2:
            return option
        if option == 3:
            return option
        else:
            print('\033[1;31mErro! opção invalida\033[m')