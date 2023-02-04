import zombiedice , random
# roll then take the lead to chose to roll or not 
class MyZombie:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# roll in a random way (1-0)

class MyFirstZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults and random.randint(0,1) == 1:
            diceRollResults = zombiedice.roll() 


# check if there is 2 brains to break, else roll 

class MySecondZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
        
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# break if there are two shutGuns 

class MyThirdZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotGuns = 0
        while diceRollResults is not None:
            shotGuns += diceRollResults['shotgun']
            if shotGuns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# take the lead to roll four times but if there are two shotguns it will break

class MyFourthZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        rolling = 4
        shotGuns = 0
        while diceRollResults is not None and rolling > 0:
            shotGuns += diceRollResults['shotgun']
            rolling = rolling - 1
            if shotGuns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# check if shotguns ia greater than brains to break, else continue

class MyFifthZombie:
    def __init__(self, name):
        # All zombies must have a name:
        rolling = 4
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotGuns = 0
        brains = 0
        while diceRollResults is not None:
            shotGuns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotGuns < brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


zombies = (

            MyZombie(name='My Zombie Bot'),
            MyFirstZombie(name='My First Zombie'),
            MySecondZombie(name='My Second Zombie'),
            MyThirdZombie(name='My Third Zombie'),
            MyFourthZombie(name='My Fourth Zombie'),
            MyFifthZombie(name='My Fifth Zombie'),
            # Add any other zombie players here.
            )
# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)