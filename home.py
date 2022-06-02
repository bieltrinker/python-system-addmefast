from PySimpleGUI import PySimpleGUI as sg
import os

#Design do monitor
sg.theme('Reddit')

#Iniciando construção do monitor
menu = [

    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar Login')],
    [sg.Button('Entrar')]

]

monitor = [

    [sg.Text('Parabéns, você acessou a primeira tela disponível.')],
    [sg.Button('Sair')]

]

#Tela inicial após o código executar
janela = sg.Window('PAINEL - CAOATEC', menu)

#janela_1

    

#Sistema de funcionamento
while True:
    ev, valores = janela.read()
    if ev == sg.WINDOW_CLOSED:
        monitor = sg.Window('PAINEL - CAOATEC', monitor)
        break
    if ev == 'Entrar':
        if valores['usuario'] == 'pedro' and valores['senha'] == '12345':
            print('Acessando Menu')
            

        

