
import pickle
import sqlite3
from character import hi, character
from spells import spell

#   create fireball spell
fireball = spell('fireball', 10, 5, "fire")
#   create heal spell
heal = spell('heal', -5, 5, 'light')
#   create gandalf character
Gandalf = character("Gandalf the grey", "human", 'wizard')
#   add spells to Gandalf
Gandalf.spells.append(fireball)
Gandalf.spells.append(heal)
Gandalf.display()
#   trying to store through pickle
#with open('company_data.pkl', 'wb') as outp:
#    pickle.dump(Gandalf, outp, pickle.HIGHEST_PROTOCOL)

# load database through sqlite
con = sqlite3.connect("characters.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS character(name, species, cClass)")

Gandalf.display()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
data2 = (Gandalf.name, Gandalf.species, Gandalf.cClass)
#data2 = ("test", "test", "test")
#cur.execute("INSERT INTO character VALUES(?, ?, ?)", data2)
con.commit()

for row in cur.execute("SELECT name, cClass, species FROM character WHERE name = 'Gandalf the grey'"):
    name, cClass, species = row[0], row[1], row[2]
    print(name)
    #print(name)
data = 'gandalf the gray'
#res = cur.execute("SELECT name, cClass, species FROM character WHERE name = 'gandalf the gray'")


