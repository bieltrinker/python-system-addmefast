from PySimpleGUI import PySimpleGUI as sg
import os

#Design do monitor
sg.theme('Reddit')

#Iniciando construção do monitor
monitor = [

    [sg.Text('Parabéns, você acessou a primeira tela disponível.')],
    [sg.Button('Sair')],
    [sg.Text('',size=(100, 30))]

]


#Tela inicial após o código executar
monitor = sg.Window('PAINEL - CAOATEC', monitor, finalize=True)
monitor.maximize() 

#Sistema de funcionamento
while True:
    ev2, receber_informacao = monitor.read()
    if ev2 == monitor.WINDOW_CLOSED:
        janela = sg.Window('PAINEL - CAOATEC', monitor)        
        break
            

        

