from tkinter import *

tkFenster = Tk()
tkFenster.title('Bills-Organizer - Rechnung Eingabe')
tkFenster.geometry('450x200') # breite-X-hohe x,y

def anzeigen(): #esta funcion sera llamada por el botonMostrar, muestra el contenido de una variable
    palabra = str(entry_rnummer.get())
    label_anzeigen.config(text = palabra)

def ende(): #esta funcion terminatodo con el boton "Exit"
    tkFenster.destroy()

    # LABELS #####################################
    # Etiqueta ROJA "Intro Palabra"
label_rnummer = Label(master=tkFenster, bg='red', text='Rechnungsnummer:')
label_rnummer.place(x=30, y=10, width=140, height=27)
    # Etiqueta AZUL "Cont Palabra"
label_ekdatum = Label(master=tkFenster, bg='blue', text='Einkaufdatum:')
label_ekdatum.place(x=30, y=40, width=140, height=27)
    # Etiqueta NARANJA "Cont Palabra"
label_lieferant = Label(master=tkFenster, bg='orange', text='Lieferant:')
label_lieferant.place(x=30, y=70, width=140, height=27)
    # Etiqueta VERDE "Cont Palabra"
label_bemerkung = Label(master=tkFenster, bg='green', text='Bemerkung:')
label_bemerkung.place(x=30, y=100, width=140, height=27)
    # Cuadro que muestra
label_anzeigen = Label(master=tkFenster, bg='gray', text='')
label_anzeigen.place(x=164, y=160, width=120, height=27)

# ENTRYS #####################################
# Entry rechnungsnummer
entry_rnummer = Entry(master=tkFenster, bg='red')
entry_rnummer.place(x=160, y=10, width=240, height=27)
# Cuadro de Entrada
entry_ekdatum = Entry(master=tkFenster, bg='blue')
entry_ekdatum.place(x=160, y=40, width=240, height=27)
# Cuadro de Entrada
entry_lieferant = Entry(master=tkFenster, bg='orange')
entry_lieferant.place(x=160, y=70, width=240, height=27)
# Cuadro de Entrada
entry_bemerkung = Entry(master=tkFenster, bg='green')
entry_bemerkung.place(x=160, y=100, width=240, height=27)

# BUTTONS #####################################
button_anzeigen = Button(master=tkFenster, text='Anzeigen...', command=anzeigen)
button_anzeigen.place(x=50, y=160, width=120, height=27)
# ergebniss = print("brutto= ", brutto, "bemerkung= ", s , "lieferant= ", lieferant, "ekdatum", ekdatum)
button_ende = Button(master=tkFenster, text='Exit', command=ende)
button_ende.place(x=300, y=160, width=120, height=27)

# CHECKBUTTONS
chkbutton_brutto = Checkbutton(master=tkFenster, text='Brutto Preise')
chkbutton_brutto.place(x=30, y=130)
tkFenster.mainloop()
