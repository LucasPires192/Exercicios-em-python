from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
            _peso_ = int(peso.get())
            _altura_ = float(altura.get())
            valor.set(round(_peso_ / (_altura_ * _altura_) , 4))
    except ValueError:
         pass  

root = Tk()
root.title('Calculador de IMC')
root.configure(background = 'deepskyblue')
style = ttk.Style()
style.configure('TFrame' , background = 'deepskyblue')
style.configure('customFrame.TFrame' , background = 'white')

mainframe = ttk.Frame(root , padding = '20')
mainframe.grid(column = 0 , row = 0 , sticky = (W , N , E , S))

'''root.columnconfigure(0 , weight = 0)
root.rowconfigure(0 , weight = 0)'''

frameAltura = ttk.Frame(mainframe , padding = '10' , style = 'customFrame.TFrame')
frameAltura.grid(column = 1 , row = 1 , sticky = (W , E))
ttk.Label(frameAltura , background = 'white' , text = 'Altura' , width = '15' , anchor = 'sw').grid(column = 0 , row = 0 , padx = '5' , pady = '5'  , sticky = (W , E))

altura = StringVar()
altura_entrada = ttk.Entry(frameAltura , width = 7 , textvariable = altura)
altura_entrada.grid(column = 1 , row = 0 ,  sticky = (W , E))

framePeso = ttk.Frame(mainframe , padding = '10' , width = '15' , style = 'customFrame.TFrame')
framePeso.grid(column = 1 , row = 2 , sticky = (W , E))
ttk.Label(framePeso , background = 'white' , text = 'Peso' , width = '15' , anchor = 'sw').grid(column = 0 , row = 0 , padx = '5' , pady = '5' , sticky = (W , E))

peso = StringVar()
peso_entrada = ttk.Entry(framePeso, width = 7 , textvariable = peso)
peso_entrada.grid(column = 1 , row = 0  , sticky = (W , E))

frameValor = ttk.Frame(mainframe , padding = '10' , width = '15' , style = 'customFrame.TFrame')
frameValor.grid(column = 4 , row = 1 , sticky = (W , E))
valor = StringVar()
ttk.Label(frameValor, background="white", textvariable=valor, anchor="center").grid(column=4, row=1, sticky= (W , E))

ttk.Label(mainframe , background = 'deepskyblue' ,  text  = 'Resultado: ' , anchor = 'center').grid(column = 3 , row = 1  , sticky = (W , E))

botao_calcular = ttk.Button(mainframe, text="Calcular", command=calcular)
botao_calcular.grid(column=4, row=2 , sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

altura_entrada.focus()
root.bind('<Return>' , calcular)
    
root.mainloop()