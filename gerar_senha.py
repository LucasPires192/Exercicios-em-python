import random   #importa a biblioteca random
from tkinter import * #importa tudo da biblioteca tkinter
from tkinter import ttk #importa a interface ttk da biblioteca tkinter

letra = 'abcdefghijklmnopqrstuvwxyz'    #Varaivel armazena as letras
caracter = '!@#$%&*()-_+=|\?/°,<.>;:{}[]'     #Varaivel armazena os caracteres especiais
numero = '0123456789'   #Varaivel que armazena os números
tamanho = 16    #Variavel que armazenda o tamanho da senha gerada

def gerarSenha(*args):
    _senha = ''     #Variavel interna da senha criada vazia
    _tamanho = tamanho  #Variavel interna armazenando o tamanho da senha

    for x in range(_tamanho):   #Inicio de um loop que rodar de acordo do tamanho da senha
        i = random.randint(0 , 2)   #Variavel i que armazena um valor aleatorio entre 0 e 2
        if i == 0:  #Caso a variavel i seja 0 ele vai escolher uma letra aleatorio da variavel letra
            caps = random.randint(0 , 1)    #Variavel que armazena um valor aleatorio entre 0 e 1
            if caps == 0:
                _senha += letra[random.randint(0 , 25)].lower() #Caso o valor for 0 a letra vai ser minuscula e concatena com os valor ja armazenado da variavel _senha
            elif caps == 1:
                _senha += letra[random.randint(0 , 25)].upper() #Caso o valor for 0 a letra vai ser maiuscula e concatena com os valor ja armazenado da variavel _senha
        elif i == 1:    #Caso a variavel i seja 1 ele vai escolher um caracter aleatorio da variavel caracteres e concatena com os valor ja armazenado da variavel _senha
            _senha += caracter[random.randint(0 , 27)]
        elif i == 2:    #Caso a variavel i seja 2 ele vai escolher um numero aleatorio da variavel numero e concatena com os valor ja armazenado da variavel _senha
            _senha += numero[random.randint(0 , 9)]
    return senha.set(_senha)    #Armazena o resultado da variavel interna _senha na variavel externa senha



root = Tk() #Chama o metodo que execulta a interface no tkinder
corBackground = 'deepskyblue'   #Variavel com a cor de background do App
largura_app = 325   #Define o largura do App
altura_app = 150    #Define o altura do App
larguta_tela = root.winfo_screenwidth() #Armazena o largura da tela do dispositivo
altura_tela =  root.winfo_screenmmheight()  #Armazena o altura da tela do dispositivo
pos_x = (larguta_tela / 2) - (largura_app / 2)  #Armazena a posicao do x do app
pos_y = (altura_tela / 2) + (altura_app / 2)    #Armazena a posicao do y do app
root.title('Gerador de senha')  #Cria o titulo da janela
root.geometry("%dx%d+%d+%d" % (largura_app , altura_app , pos_x , pos_y)) #Define o tamanho e a posicao que a tela vai abrir
style = ttk.Style() #Chama o metodo style e armazena na variavel style
style.configure('TFrame' , background = corBackground)  #Modifica o background dos style padrao dos frames 

mainframe = ttk.Frame(root , padding = '10')    #Cria o frame principal
mainframe.grid(column = 0 ,  row = 0 , sticky = (W , N , E , S))    
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe , background = corBackground , text = 'Senha gerada:' , anchor = 'center').grid(column = 0 , row = 0 , sticky = (W , E) , pady = '10') #Cria o label para o texto

senha = StringVar()
ttk.Label(mainframe , textvariable = senha , width = '50' , anchor = 'center').grid(column = 0 , row = 1 , sticky = (W , E) , pady = '10')  #Cria o label para mostrar o valor da variavel senha

ttk.Button(mainframe , text = 'Gerar' , command = gerarSenha).grid(column = 0 , row = 2 , pady = '10')  #Cria o botao pra execultar a funcao gerarSenha

root.bind("<Return>", gerarSenha) #Cria um atalho para tecla enter para exercultar a funcao gerarSenha 
root.mainloop() #Criacao do loop principal