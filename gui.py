from tkinter import *
from tkinter import ttk
#   setting up a gui clas. Running through main currently
class gui:
    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        characterLabel = Label(frm)
        characterSpeciesLabel = Label(frm)
        characterClassLabel = Label(frm)
