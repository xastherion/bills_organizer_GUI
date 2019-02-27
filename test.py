from tkinter import Tk, Label

master = Tk()
master.geometry('500x460')

msgs = {
    'msg_leer': '***',
    'msg_fileimp': 'file.pdf importiert, Quell-Datei ist gelöscht!',
    'msg_keinimp': 'für diese Rechnung wurde keine PDF-Datei importiert!'
}

def leer():
    #print(k)
    Label(master, text = msgs['msg_leer'] ).place( x = 10, y = 10, width = 30, height = 30)


def fileimp():
    print(msgs['msg_fileimp'])


def keinimp():
    print(msgs['msg_keinimp'])


leer()
fileimp()
keinimp()

master.mainloop()
