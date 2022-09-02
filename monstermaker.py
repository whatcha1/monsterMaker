
# import your python library
import random

# make your class that will create your objects
class monsterMaker:
    #function that serves as a constructor for the class
    def __init__(self,name,kind):
        # passed in parameters name, kind get bound to the object in construction
        # self represents this instance of the object
        self.name = name
        self.kind = kind
    # this functions prints the object we have now created to the console
    def monsterBio(self):
        # with f"string" we can pass in variables easily with {variable}
        print(f"Your monster, {self.name} is a {self.kind}!")

# list of monster names [0,1,2]
monsterName = ["Dracula","Frankenstein","Casper"]
# list of monster kinds [0,1,2]
monsterKind = ["vampire","zombie","ghost"]

# randomize a choice from the monsterName list
randomName = random.choice(monsterName)
# randomize a choice from the monsterKind list
randomKind = random.choice(monsterKind)

# if the random choices do not equal the same place on their list [0,1,2] we loop the randomization of both till they do
while monsterKind.index(randomKind) != monsterName.index(randomName):
    # randomize a choice from the monsterName list
    randomName = random.choice(monsterName)
    # randomize a choice from the monsterKind list
    randomKind = random.choice(monsterKind)

#pass the now equally placed [0,1,2] variables into our monsterMaker class  constructor def __init__(self,randomName,randomKind):
monster = monsterMaker(randomName,randomKind)

# if statement to check if the above code worked, not needed after testing
# if monsterKind.index(randomKind) == monsterName.index(randomName):
# call your now created monster objects def monsterBio(self) function
monster.monsterBio()

# use input to take in user answers
userName = input("make you own monster! enter a Name!: ")
# loop to make sure the user doesnt leave the a blank answer
while userName == '':
    # repeat until the field isnt empty
    print("Please enter a monster name!")
    # use input to take in user answers
    userName = input("make you own monster! enter a Name!: ")
# use input to take in user answers
userKind = input("Enter your monsters kind!: ")
# loop to make sure the user doesnt leave the a blank answer
while userKind == '':
        # repeat until the field isnt empty
    print("Please enter a monster kind!: ")
    # use input to take in user answers
    userKind = input("Enter your monsters kind!: ")
# create a new user made object by passing the user's input as variables into the class
userMonster = monsterMaker(userName,userKind)
# call your now created monster objects def monsterBio(self) function
userMonster.monsterBio()
# we can show the values our object's variable(s) has by using . syntax on our object
print(userMonster.kind)