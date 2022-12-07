import sqlite3
from character import character
from spells import spell
from rpgdata import rpgData
from tkinter import *
from tkinter import ttk

# Testing classes no interaction yet
#   create fireball spell
fireball = spell('fireball', 10, 5, "fire")
#   create heal spell
heal = spell('heal', -5, 5, 'light')
#   create gandalf character
Gandalf = character("Gandalf the grey", "human", 'wizard')
#   create Saruman character
saruman = character("Saruman the white", "human", 'wizard')
#   add spells to Gandalf
Gandalf.spells.append(fireball)
Gandalf.spells.append(heal)

#   testing
#Gandalf.display()

# load database through sqlite
#con = sqlite3.connect("characters.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS character(name, species, cClass)")


#data2 = (Gandalf.name, Gandalf.species, Gandalf.cClass)
#data3 = (saruman.name, saruman.species, saruman.cClass)
#   insert character into database
#cur.execute("INSERT INTO character VALUES(?, ?, ?)", data3)
#con.commit()

characterworld = rpgData()
#characterworld.start()
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
#   Set the Menu initially
menu= StringVar()
characterLabel = Label(frm)
characterSpeciesLabel = Label(frm)
characterClassLabel = Label(frm)
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


characterList = characterworld.GetNames(False)
#ttk.Label(frm, text=Gandalf.name).grid(column=0, row=0)
#ttk.Label(frm, text="class: "+Gandalf.cClass).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
current = ttk.OptionMenu(frm, menu, "select character", *characterList).grid(column=0, row=1)
ttk.Button(frm, text="find", command=lambda: characterSearch()).grid(column=1, row=1)
root.mainloop()


