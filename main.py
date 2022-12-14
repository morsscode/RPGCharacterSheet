import sqlite3
from character import character
from spells import spell
from rpgdata import rpgData
from tkinter import *
from tkinter import ttk

# creating instances of the spell class
fireball = spell('fireball', 10, 5, "fire")
heal = spell('heal', -5, 5, 'light')
#   creating instances of the character class
Gandalf = character("Gandalf the grey", "human", 'wizard')
saruman = character("Saruman the white", "human", 'wizard')
#   add spells to Gandalf
Gandalf.spells.append(fireball)
Gandalf.spells.append(heal)

#   create instance of rpg class
characterworld = rpgData()
#   start the command line interface
#characterworld.start()

#   function to select character from dropdown and display characteristics
def characterSearch(frm,search):
    characterLabel = Label(frm)
    characterSpeciesLabel = Label(frm)
    characterClassLabel = Label(frm)
    #currentCharacter = .get()
    #   print character details in command line
    data = characterworld.findCharacter(search, False)
    #   display character name
    characterLabel["text"] = "name: " + str(data[0])
    characterLabel.grid(column=1, row=1)
    #   display character species
    characterSpeciesLabel["text"] = "Species: " + str(data[1])
    characterSpeciesLabel.grid(column=1, row=2)
    # display character class
    characterClassLabel["text"] = "Class: " + str(data[2])
    characterClassLabel.grid(column=1, row=3)
def newGuiCharacter():
    rootc = Tk()
    rootc.geometry('300x200+350+50')
    frmc = ttk.Frame(rootc, padding=10)
    addedlabel = Label(frmc)
    frmc.grid()
    ttk.Label(frmc, text="name:").grid(column=0, row=0)
    ttk.Label(frmc, text="species:").grid(column=0, row=1)
    ttk.Label(frmc, text="class:").grid(column=0, row=2)
    inputname = ttk.Entry(frmc)
    inputspecies = ttk.Entry(frmc)
    inputclass = ttk.Entry(frmc)
    inputname.grid(column=2, row=0)
    inputspecies.grid(column=2, row=1)
    inputclass.grid(column=2, row=2)
    ttk.Button(frmc, text="Quit", command=rootc.destroy).grid(column=1, row=3)
    ttk.Button(frmc, text="Create", command=lambda: values()).grid(column=0, row=3)
    def values():
        newname = inputname.get()
        newspecies = inputspecies.get()
        newclass = inputclass.get()
        print(newname)
        addedlabel.grid(column=2, row=3)
        if characterworld.GuiAdd(str(newname), str(newspecies), str(newclass)):
            addedlabel["text"] = "character added"
        else:
            addedlabel["text"] = "character already exits"
        global characterList
        characterList = characterworld.GetNames(False)
        characterList.append(newname)
    rootc.mainloop()

def maingui():
    #   set up Gui
    root = Tk()
    root.title("characters")
    root.geometry('300x200+50+50')
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    #   Set the character Menu initially
    menu = StringVar()
    #   character label variables
    characterLabel = Label(frm)
    characterSpeciesLabel = Label(frm)
    characterClassLabel = Label(frm)
    #   set up grid layout of display
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)
    current = ttk.OptionMenu(frm, menu, "select character", *characterList).grid(column=0, row=1)
    ttk.Button(frm, text="find", command=lambda: characterSearch(frm, menu.get())).grid(column=0, row=2)
    ttk.Button(frm, text="create new", command=lambda: newGuiCharacter()).grid(column=0, row=3)
    root.mainloop()

#   get list of characters from instance of world class
characterList = characterworld.GetNames(False)
maingui()



