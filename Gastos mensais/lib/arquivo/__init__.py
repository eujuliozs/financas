from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='10032005Jc%',
    database='gastos_mensais'
)

cursor = db.cursor()

ano = datetime.now().year
dia = datetime.now().day
dia_da_semana = datetime.now().weekday
n_mes = datetime.now().month


def NomeMes():
    num = n_mes
    lista_meses = ['','janeiro', 'fevereiro', 'março', 'maio',
                   'abril', 'junho', 'julho', 'agosto',
                   'setembro', 'outubro', 'novembro', 'dezembro']
    for c in range(0, len(lista_meses)):
        global mes
        if num == c and dia > 15:
            mes = lista_meses[c+1]
            return mes
        if num == c and dia <= 15:
            mes = lista_meses[c]
            return mes


mes = NomeMes()


def CriaArqMes(nome):
    cursor.execute(f'CREATE TABLE {mes} (dia datetime, quantia int, local varchar(50), registroID int PRIMARY KEY AUTO_INCREMENT, local varchar(50))')
    return f'tabela de {mes} criado'


def LeiaReal(msg):
    while True:
        try:
            r = str(input(msg)).replace(',', '.')
            r = float(r)
        except:
            print(f'\033[1;31mErro! por favor digite um numero real valido\033[m')
        else:
            return r


def opcontinue(msg):
    while True:
        e = str(input(msg))
        if e == '':
            print('Erro.', end='')

        try:
            e = e.strip().lower()[0]
        except:
            print('opçao invalida')
        else:
            if e in 'sn':
                return e


def linha(tam=55):
    return '='*tam


def Registrar(quantia=0, local=''):
    hoje = datetime.now()
    formatted_date = hoje.strftime('%Y-%m-%d')
    cursor.execute(f'INSERT INTO {mes} (dia, quantia, local) VALUES(%s ,%s, %s)',(formatted_date, quantia, local))
    db.commit()


def MostraArq(arquivo):
    cursor.execute(f'SELECT quantia, local, dia FROM {mes}')
    for e in cursor:
        print('R${:<4} local: {} registrado: {:>10}'.format(e[0], e[1],e[2]))
    cursor.execute(f'select sum(quantia) from {mes}')
    y = (cursor.fetchall())
    for a in y:
        for b in a:
            print(f'Total: R${b}')







