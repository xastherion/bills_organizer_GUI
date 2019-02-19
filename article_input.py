from tkinter import Label, Entry, Button, Tk, StringVar
#--- FUNCTIONS --------
def weiter():
    schreiben()
    eingaben()

def schreiben():
    lista = [var_name.get(), ',', var_preis.get(), ',', var_menge.get(), '\n']
    archivo = open('rechnungen.csv', 'a')
    archivo.write("\t".join(lista))

def eingaben():     # accept and delete olds entrys
    global entry_name, entry_preis, entry_menge, var_name, var_preis, var_menge
    var_name = StringVar(master, value='')
    entry_name = Entry(master, textvariable=var_name).  place(x=dist_hor[1], y=dist_ver[0], width=ancho[1], height=alto)
    var_preis = StringVar(master, value='')
    entry_preis = Entry(master, textvariable=var_preis).place(x=dist_hor[1], y=dist_ver[1], width=ancho[1], height=alto)
    var_menge = StringVar(master, value='')
    entry_menge = Entry(master, textvariable=var_menge).place(x=dist_hor[1], y=dist_ver[2], width=ancho[1], height=alto)

def ende(): #esta funcion terminatodo con el boton "Exit"
    master.destroy()
#--------
master = Tk()
master.title('Bills-Organizer : Artikel Eingabe v.02')
master.geometry("500x500")
#--------
alto = '30'              # alto estandar para cada boton, entrada o etiqueta
ancho = ['100', '300']   # ancho para etiquetas y botones
dist_hor =  ['30', '160']                               # distancias entre columnas
dist_ver =  ['30', '60', '90', '120', '150', '180']     # distancias entre lineas
# LABELS
label_name  = Label(master, text="Name  : "). place(x=dist_hor[0], y=dist_ver[0],  width=ancho[0], height=alto)
label_preis = Label(master, text="Preis : "). place(x=dist_hor[0], y=dist_ver[1],  width=ancho[0], height=alto)
label_menge = Label(master, text="Menge : "). place(x=dist_hor[0], y=dist_ver[2],  width=ancho[0], height=alto)
eingaben()
# BUTTONS
Button(master, text='Weiter', command=weiter).place(x=dist_hor[0], y=dist_ver[4],   width=ancho[0], height=alto)
Button(master, text='Ende', command=ende).    place(x=dist_hor[1], y=dist_ver[4],   width=ancho[0], height=alto)
#--------
master.mainloop()
#--------
