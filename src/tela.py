from traceback import print_stack
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        sg.change_look_and_feel('dark')

        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='tx-nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='tx-idade')],
            [sg.Checkbox('Gmail',key='ck-gmail'),sg.Checkbox('Outlook',key='ck-outlook'),sg.Checkbox('Yahoo',key='ck-yahoo')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim','cartoes',key=('aceitaCartao')),sg.Radio('Não','cartoes',key=('nAceitaCartao'))],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key=('sliderVelocidade'))],
            [sg.Button('Enviar Dados',size=(25,0),key='bt-enviar')],
            [sg.Output(size=(30,20))]
        ]
        #Window
        self.janela = sg.Window('Dados do Usuário').layout(layout)
        

    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['tx-nome']
            idade = self.values['tx-idade']
            aceita_gmail = self.values['ck-gmail']
            aceita_outlook = self.values['ck-outlook']
            aceita_yahoo = self.values['ck-yahoo']
            aceita_cartoes = self.values['aceitaCartao']
            naceita_cartoes = self.values['nAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita Cartao: {aceita_cartoes}')
            print(f'aceita yahoo: {naceita_cartoes}')
            print(f'Velocidade Script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()