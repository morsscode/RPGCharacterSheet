import sqlite3
from character import character
from spells import spell
from rpgdata import rpgData

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
characterworld.start()


