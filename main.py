from PySimpleGUI import PySimpleGUI as sg
from random import choice
from numpy import size
from time import sleep

#jogada do computador
papel = 'papel'
tesoura = 'tesoura'
pedra = 'pedra'
lista = [papel, tesoura, pedra]
escolha_pc = choice(lista)

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Suas Opções:')],
            [sg.Text('PEDRA',size=(13,0))],
            [sg.Text('PAPEL',size=(13,0))],
            [sg.Text('TESOURA',size=(13,0))],
            [sg.Text('Qual é a sua jogada?'), sg.Input(key='jogador',size=(7,0))],
            [sg.Button('Vamos nessa!!')],
            
            [sg.Output(size=(30, 10))]
        ]
        # Janela
        self.janela = sg.Window('JO KEN PO').layout(layout)
        



    def Iniciar(self):
       while True:
          # Extrair os dados da tela
          self.button, self.values = self.janela.Read()
          escolha_jogador = self.values['jogador']         
          print('JO')
          sleep(0.5)
          print('KEN')
          sleep(0.5)
          print('PO!!!')
          sleep(0.5)          
          print(f'O computador jogou: {escolha_pc}')
          print(f'Você jogou: {escolha_jogador}')

          #jogador escolheu papel
          if escolha_jogador == 'papel' and escolha_pc == papel:
             print('EMPATOU!!')
          elif escolha_jogador == 'papel' and escolha_pc == tesoura:
             print('Parece que você perdeu :c !!')
          elif escolha_jogador == 'papel' and escolha_pc == pedra:
             print('PARABÉNS!! Você ganhou')

          #jogador escolheu tesoura   
          elif escolha_jogador == 'tesoura' and escolha_pc == tesoura:
             print('EMPATOU!!')
          elif escolha_jogador == 'tesoura' and escolha_pc == pedra:
             print('Parece que você perdeu :c !!')
          elif escolha_jogador == 'tesoura' and escolha_pc == papel:
             print('PARABÉNS!! Você ganhou')

          #jogador escolheu pedra
          elif escolha_jogador == 'pedra' and escolha_pc == pedra:
             print('EMPATOU!!')
          elif escolha_jogador == 'pedra' and escolha_pc == papel:
             print('Parece que você perdeu :c !!')
          elif escolha_jogador == 'pedra' and escolha_pc == tesoura:
             print('PARABÉNS!! Você ganhou')             


          
        

tela = TelaPython()
tela.Iniciar()






