from lib.arquivo import *
from lib.interface import *
from time import sleep
mes = (NomeMes())
try:
    CriaArqMes()
    print(CriaArqMes())
except:
    print('essa fatura vai para o mes de {}'.format(mes))
while True:
    cabecalho('MENU PRINCIPAL')
    lista_de_opc = ['VER EXTRATO', 'REGISTRAR GASTOS', 'SAIR DO PROGRAMA']
    menu(lista_de_opc)
    opc_do_cliente = opcMenu('sua opção:')
    if opc_do_cliente == 2:
        sleep(0.2)
        cabecalho('    \033[45mREGISTRAR GASTOS\033[m')
        while True:
            quantia = (LeiaReal(f'Quanto gastou hoje, {dia}/{n_mes}/{ano} ?R$'))
            local = str(input('E aonde gastou? '))
            Registrar(quantia, local)
            e = opcontinue('quer continuar?')
            if e == 'n':
                break
    elif opc_do_cliente == 1:
        sleep(0.2)
        cabecalho('       \033[1;45mEXTRATO\033[m')
        MostraArq(f'{mes}')
    elif opc_do_cliente == 3:
        sleep(0.2)
        break
print('Finalizando...NÃO ESQUEÇA DE REGISTRAR SEMPRE')



