#Biblioteca - PySimpleGui

#Customização do front_end no PySimpleGui
import PySimpleGUI as sg

#Criar um Tema novo e customizar o layout:
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#000066',
										'TEXT': '#FFCC66',
										'INPUT': '#339966',
										'TEXT_INPUT': '#000000',
										'SCROLL': '#99CC99',
										'BUTTON': ('#003333', '#FFCC66'),
										'PROGRESS': ('#D1826B', '#CC8019'),
										'BORDER': 1, 'SLIDER_DEPTH': 0,
'PROGRESS_DEPTH': 0, 'ROUND': 15}

# Para usar seu tema criado, precisa sinaliza-lo com o código abaixo:
sg.theme('MyCreatedTheme')

# Chame o popup visual do tema e veja como ficou:
sg.popup_get_text('This how the MyNewTheme is created')	


