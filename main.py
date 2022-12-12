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

#   set up Gui
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
#   Set the character Menu initially
menu= StringVar()
#   character label variables
characterLabel = Label(frm)
characterSpeciesLabel = Label(frm)
characterClassLabel = Label(frm)

#   function to select character from dropdown and display characteristics
def characterSearch():
    currentCharacter = menu.get()
    #   print character details in command line
    data = characterworld.findCharacter(currentCharacter, False)
    #   display character name
    characterLabel["text"] = "name: " + str(data[0])
    characterLabel.grid(column=0, row=2)
    #   display character species
    characterSpeciesLabel["text"] = "Species: " + str(data[1])
    characterSpeciesLabel.grid(column=0, row=3)
    # display character class
    characterClassLabel["text"] = "Class: " + str(data[2])
    characterClassLabel.grid(column=0, row=4)


#   get list of characters from instance of world class
characterList = characterworld.GetNames(False)

#   set up grid layout of display
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
current = ttk.OptionMenu(frm, menu, "select character", *characterList).grid(column=0, row=1)
ttk.Button(frm, text="find", command=lambda: characterSearch()).grid(column=1, row=1)
root.mainloop()


