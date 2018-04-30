from tkinter import *

window= Tk()


def kg_to_various():
    resultado1 = float(entrada.get())*1000
    painel1.delete("1.0", END)
    painel1.insert(END, resultado1)
    resultado2 = float(entrada.get())*2.20462
    painel2.delete("1.0", END)
    painel2.insert(END, resultado2)
    resultado3 = float(entrada.get())*35.275
    painel3.delete("1.0", END)
    painel3.insert(END, resultado3)


entrada = StringVar()
entrada= Entry(window, textvariable=entrada)
entrada.grid(row=1, column=1)

botao = Button(window, text = "Converter", command = kg_to_various)
botao.grid(row = 1, column = 3)

label1 =Label(window, text = "Conversor Kgs em Gramas\nPounds e Ounces")
label1.grid(row = 1, column=0)

label2=Label(window, text="Kg(s)")
label2.grid(row=1, column=2)

label3 = Label(window, text="Gramas")
label3.grid(row=3, column=1)

label4 = Label(window, text="Pounds")
label4.grid(row=3, column=2)

label5 = Label(window, text= "Ounces")
label5.grid(row=3, column=3)

painel1 = Text(window, height=1, width=10)
painel1.grid(row=2, column=1)

painel2 = Text(window, height=1, width=10)
painel2.grid(row=2, column=2)

painel3 = Text(window, height=1, width=10)
painel3.grid(row=2, column=3)

window.mainloop()
