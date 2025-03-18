from tkinter import*
from tkinter import ttk

def calcular(*args):
    try:
        value = float(milhas.get())
        km.set(int(1.60934 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.geometry('300x250')
root.title("Milhas para Quilometros")
style = ttk.Style()
style.configure("TFrame", background="DeepSkyBlue")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0,  row=0
, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

milhas = StringVar()
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

km = StringVar()
ttk.Label(mainframe, background="white", textvariable=km, anchor="center").grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calcular).grid(column=2, row=4, sticky=W)

ttk.Label(mainframe, background="DeepSkyBlue", text="Milhas" ).grid(column=3, row=1, sticky=(W , E, N, S))
ttk.Label(mainframe,background="DeepSkyBlue", text="é equivalente a").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, background="DeepSkyBlue", text="Km").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)
    
milhas_entry.focus()
root.bind("<Return>", calcular)

root.mainloop()