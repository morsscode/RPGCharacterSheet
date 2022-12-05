#   RPG character class. Opens the characters database and then allows you to interact with it.
import sqlite3


class rpgData:
    def __init__(self):
        # load database through sqlite
        self.con = sqlite3.connect("characters.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS character(name, species, cClass)")

    def displayAll(self):
        for row in self.cur.execute("SELECT name FROM character"):
            name = row[0]
            print(name)

    def findCharacter(self, name, display=True):
        if self.cur.execute("SELECT * FROM character WHERE name == '" + name + "'").fetchone() != None:
            for row in self.cur.execute("SELECT name, cClass, species FROM character"):
                charactername, cClass, species = row[0], row[1], row[2]
                if charactername == name:
                    if display:
                        print("name: "+str(charactername))
                        print("species: "+str(species))
                        print("class: "+str(cClass))
                    return True
        else:
            print("no character with this name")

    def updateName(self):
        name = input("enter name")
        newname = input("enter new name")
        if self.findCharacter(name, False):
            text = "UPDATE character SET name = '" + newname + "' WHERE name == '" + name + "'"
            if self.cur.execute("SELECT * FROM character WHERE name == '" + name + "'").fetchone() != None:
                print("character already exists")
                self.findCharacter(newname)
            else:
                self.cur.execute(text)
                self.con.commit()
                self.findCharacter(newname)
        else:
            print("character not found")

    def addCharacter(self):
        print("new character creation")
        name = input("enter character name: ")
        if self.cur.execute("SELECT * FROM character WHERE name == '" + name + "'").fetchone() != None:
            print("character already exists")
        else:
            cClass = input("enter class: ")
            species = input("enter species: ")
            self.cur.execute("INSERT INTO character VALUES('" + name + "', '"+species+"', '"+cClass+ "')")
            self.con.commit()
            print("character added")
    def deleteCharacter(self):
        name = input("enter character to delete")
        if self.cur.execute("SELECT * FROM character WHERE name == '" + name + "'").fetchone() != None:
            self.cur.execute("DELETE FROM character WHERE name = '"+name+"'")
            self.con.commit()
            print("character deleted")
        else:
            print("character not found")

    def start(self):
        while True:
            step = input(
                """
 press 1 to add a new character
 press 2 to find a character"
 press 3 to show all current characters
 press 4 to update a characters name
 press 5 to delete a character
 press 9 to exit
 input: """
            )
            match step:
                case "1":
                    self.addCharacter()
                case "2":
                    name = input("enter character to find")
                    self.findCharacter(name)
                case "3":
                    print("current characters")
                    self.displayAll()
                case "4":
                    self.updateName()
                case "5":
                    self.deleteCharacter()
                case "9":
                    print("exiting")
                    break
                case _:
                    print("not recognized")
