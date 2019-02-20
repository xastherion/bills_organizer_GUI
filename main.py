#   BILLS_ORGANIZER
from tkinter import Label, Entry, Button, Tk, Checkbutton, StringVar
# -------------
tkFenster = Tk()
tkFenster.title('Bills-Organizer - Rechnung Eingabe')
tkFenster.geometry('500x460') # breite-X-hohe x,y
# -------------

# FUNKTIONEN ###########################################
def weiter():
    schreiben()
    eingaben_art()

def schreiben(): # Schreibt alle vars in lista und lista in archivo
    lista = [var_rnummer.get(), ';', var_ekdatum.get(),';', var_lieferant.get(),';', var_bemerkung.get(),';', var_name.get(),';', var_preis.get(),';', var_menge.get(), '\n']
    archivo = open('rechnungen.csv', 'a')
    archivo.write("\t".join(lista))

def eingaben_rech(): # ENTRYS RECHNUNG ###################################### Entry rechnungsnummer
    global var_rnummer, var_ekdatum, var_lieferant, var_bemerkung, entry_rnummer, entry_ekdatum, entry_lieferant, entry_bemerkung, var_brutto, chkbutton_brutto
    var_rnummer     = StringVar()
    var_ekdatum     = StringVar()
    var_lieferant   = StringVar()
    var_bemerkung   = StringVar()
    entry_rnummer   = Entry(tkFenster, textvariable=var_rnummer).  place(x=dist_hor[1], y=dist_ver[1], width=ancho[1], height=alto)
    entry_ekdatum   = Entry(tkFenster, textvariable=var_ekdatum).  place(x=dist_hor[1], y=dist_ver[2], width=ancho[1], height=alto)
    entry_lieferant = Entry(tkFenster, textvariable=var_lieferant).place(x=dist_hor[1], y=dist_ver[3], width=ancho[1], height=alto)
    entry_bemerkung = Entry(tkFenster, textvariable=var_bemerkung).place(x=dist_hor[1], y=dist_ver[4], width=ancho[1], height=alto)
    var_brutto      = StringVar()
    chkbutton_brutto = Checkbutton(tkFenster, text='Brutto Preise', variable=var_brutto).place(x=dist_hor[1], y=dist_ver[5])

def eingaben_art():     # accept entrys and delete olds entrys
    global entry_name, entry_preis, entry_menge, var_name, var_preis, var_menge
    var_name    = StringVar(tkFenster, value='')
    var_preis   = StringVar(tkFenster, value='')
    var_menge   = StringVar(tkFenster, value='')
    entry_name  = Entry(tkFenster, textvariable=var_name). place(x=dist_hor[1], y=dist_ver[7], width=ancho[1], height=alto)
    entry_preis = Entry(tkFenster, textvariable=var_preis).place(x=dist_hor[1], y=dist_ver[8], width=ancho[1], height=alto)
    entry_menge = Entry(tkFenster, textvariable=var_menge).place(x=dist_hor[1], y=dist_ver[9], width=ancho[1], height=alto)

def etiketten():
    Label(tkFenster, text='RECHNUNG ---'). place(x=dist_hor[0], y=dist_ver[0], width=ancho[0], height=alto)
    Label(tkFenster, text='Rechnungsnr.:').place(x=dist_hor[0], y=dist_ver[1], width=ancho[0], height=alto)
    Label(tkFenster, text='Einkaufdatum:').place(x=dist_hor[0], y=dist_ver[2], width=ancho[0], height=alto)
    Label(tkFenster, text='Lieferant   :').place(x=dist_hor[0], y=dist_ver[3], width=ancho[0], height=alto)
    Label(tkFenster, text='Bemerkung   :').place(x=dist_hor[0], y=dist_ver[4], width=ancho[0], height=alto)
    Label(tkFenster, text='ARTIKEL ----'). place(x=dist_hor[0], y=dist_ver[6], width=ancho[0], height=alto)
    Label(tkFenster, text="Name  : ").     place(x=dist_hor[0], y=dist_ver[7], width=ancho[0], height=alto)
    Label(tkFenster, text="Preis : ").     place(x=dist_hor[0], y=dist_ver[8], width=ancho[0], height=alto)
    Label(tkFenster, text="Menge : ").     place(x=dist_hor[0], y=dist_ver[9], width=ancho[0], height=alto)
    # BUTTONS
    Button(tkFenster, text='Speicher & Weiter', command=weiter).place(x=dist_hor[0], y=dist_ver[11], width=ancho[2], height=alto)
    Button(tkFenster, text='Exit ohne speicher', command=ende). place(x=dist_hor[2], y=dist_ver[11], width=ancho[2], height=alto)

def ende(): #esta funcion terminatodo con el boton "Exit"
    tkFenster.destroy()

# GEOMETRIE  ##########################################
alto        = '30'              # alto estandar para cada boton, entrada o etiqueta
ancho       = ['100', '300', '150']    # ancho para etiquetas y botones
dist_hor    = ['30' , '160', '290']                               # distancias entre columnas
dist_ver    = ['30' , '60', '90', '120', '150', '180', '210', '240', '270', '300', '330', '360', '390']     # distancias entre lineas

#   GUI_ARTIKEL
etiketten()         # baut die fenster mit die notwendige etiketten
eingaben_rech()     # last
eingaben_art()

# --------
tkFenster.mainloop()
# --------
