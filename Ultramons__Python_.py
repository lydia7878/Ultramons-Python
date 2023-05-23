# creating a text-based pokemon battle simulator with ultraman monsters

import random

# create a class that stores name, health, attack, defense, speed
class Kaiju:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

# create a class that stores Kaiju objects
# this will store the roster to select from during the teambuilding process, and store the selected teams of the players
class Monsters:
    def __init__(self):
        self.monsters = []
    
        # add and remove functions
    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monster):
        self.monsters.remove(monster)

# creates the Monsters objects
Teambuilder = Monsters()
P1team = Monsters()
P2team = Monsters()

# define the playable Kaiju, their stats, and store them in Monsters
Gomess = Kaiju("Gomess", 100, 145, 120, 85)
Teambuilder.add_monster(Gomess)

Litra = Kaiju("Litra", 100, 115, 80, 125)
Teambuilder.add_monster(Litra)

Goro = Kaiju("Goro", 100, 82, 140, 92)
Teambuilder.add_monster(Goro)

Namegon = Kaiju("Namegon", 100, 90, 200, 35)
Teambuilder.add_monster(Namegon)

Juran = Kaiju("Juran", 100, 115, 119, 12)
Teambuilder.add_monster(Juran)

Peguila = Kaiju("Peguila", 100, 130, 134, 110)
Teambuilder.add_monster(Peguila)

Gorgos = Kaiju("Gorgos", 100, 78, 175, 50)
Teambuilder.add_monster(Gorgos)

Mongula = Kaiju("Mongula", 100, 86, 86, 95)
Teambuilder.add_monster(Mongula)

Balloonga = Kaiju("Balloonga", 100, 74, 265, 65)
Teambuilder.add_monster(Balloonga)

Larugeus = Kaiju("Larugeus", 100, 113, 67, 140)
Teambuilder.add_monster(Larugeus)

Garamon = Kaiju("Garamon", 100, 91, 233, 75)
Teambuilder.add_monster(Garamon)

Pagos = Kaiju("Pagos", 100, 165, 118, 90)
Teambuilder.add_monster(Pagos)

Kemur = Kaiju("Kemur", 100, 128, 36, 130)
Teambuilder.add_monster(Kemur)

Bostang = Kaiju("Bostang", 100, 170, 42, 150)
Teambuilder.add_monster(Bostang)

Sudar = Kaiju("Sudar", 100, 150, 72, 70)
Teambuilder.add_monster(Sudar)

Goga = Kaiju("Goga", 100, 112, 180, 40)
Teambuilder.add_monster(Goga)

Todora = Kaiju("Todora", 100, 108, 165, 80)
Teambuilder.add_monster(Todora)

# randomly picks a monster from the list and adds it to the opponents team
# selected monster is removed from play
def Oppselectsmonster():
    oppchoice = random.randint(1, len(Teambuilder.monsters))
    P2team.add_monster(Teambuilder.monsters[oppchoice - 1])
    Teambuilder.remove_monster(Teambuilder.monsters[oppchoice - 1])

# the player selects a monster from the list
# selected monsters are removed from play
def Selectamonster():
    lock = 1
    while (lock == 1):
        print("\nSelect a Kaiju to add to your team: ")
        for i, monster in enumerate(Teambuilder.monsters):
            print(f"{i+1}. {monster.name}")
        playerchoice = int(input("\n> "))
        if (playerchoice > len(Teambuilder.monsters) or playerchoice <= 0):
            print("\nERROR: Your choice is out of bounds, please try again.")
        else:
            playerchoice2 = input(f"\nSelect {Teambuilder.monsters[playerchoice - 1].name}? (1 for YES, 0 for NO)\n\n> ")
            if (playerchoice2 == "1" or playerchoice2 == "y" or playerchoice2 == "Y" or playerchoice2 == "YES" or playerchoice2 == "Yes" or playerchoice2 == "yes"):
                P1team.add_monster(Teambuilder.monsters[playerchoice - 1])
                Teambuilder.remove_monster(Teambuilder.monsters[playerchoice - 1])
                Oppselectsmonster()
                # print player and opponent teams to the screen after the monster has been chosen
                print("\nPLAYER TEAM:")
                for i, monster in enumerate(P1team.monsters):
                    print(f"{monster.name}")
                print("\nCPU TEAM:")
                for i, monster in enumerate(P2team.monsters):
                    print(f"{monster.name}")
                lock = 0

def Turncounter(turn):
    turn = turn + 1
    print(f"\n=============================================================\nTURN: {turn}\n=============================================================")
    return turn

# startup screen
print("This is a developmental build. Please report any bugs or issues.")

# each player selects 6 monsters for their team
selectedteam = 0
while(selectedteam < 6):
    Selectamonster()
    selectedteam = selectedteam + 1

# player and opponent choose a monster to lead with
lock2 = 1
while (lock2 == 1):
    print("\nThe match is about to begin. Select a monster to lead with: ")
    for i, monster in enumerate(P1team.monsters):
        print(f"{i+1}. {monster.name}")
    playerlead = int(input("\n> "))
    if (playerlead > 6 or playerlead <= 0):
        print("\nERROR: Your choice is out of bounds, please try again.")
    else:
        opplead = random.randint(1, len(P2team.monsters))
        playeractive = P1team.monsters[playerlead - 1]
        oppactive = P2team.monsters[opplead - 1]
        lock2 = 0

turn = 0

# game will end when one of the players teams reach 0 in length
while(len(P1team.monsters) > 0 and len(P2team.monsters) > 0):
    turn = Turncounter(turn)
    print("\nYOUR SIDE: \n")
    print(f"{playeractive.name} ({playeractive.health} / 100) Speed: {playeractive.speed}")
    print("\nCPU SIDE: \n")
    print(f"{oppactive.name} ({oppactive.health} / 100) Speed: {oppactive.speed}")

    playeraction = int(input("\nEnter '1' to ATTACK, Enter '0' to SWITCH monsters\n> "))
    oppaction = random.randint(0, 1)

    # adds exception if you pick SWITCH when you are unable to
    if(playeraction == 0 and len(P1team.monsters) == 1):
        print(f"You do not have any monsters to switch to! {playeractive.name} must attack!")
        playeraction = 1

    if(oppaction == 0 and len(P2team.monsters) == 1):
        oppaction = 1

    # if player switches
    if(playeraction == 0 and playeraction != 1):
        lock4 = 1
        while (lock4 == 1):
            print("\nSelect the monster you want to SWITCH to: ")
            for i, monster in enumerate(P1team.monsters):
                print(f"{i+1}. {monster.name}")
            playerswitch = int(input("\n> "))
            if (playerswitch > len(P1team.monsters) or playerswitch <= 0):
                print("\nERROR: Your choice is out of bounds, please try again.")
            elif (P1team.monsters[playerswitch - 1].name == playeractive.name):
                print("\nERROR: You can't switch with a monster that's currently in battle!")
            else:
                print(f"\n{playeractive.name}, SWITCH with {P1team.monsters[playerswitch - 1].name}!")
                playeractive = P1team.monsters[playerswitch - 1]
                lock4 = 0
    
    # if opponent switches
    if(oppaction == 0 and oppaction != 1):
        oppswitch = random.randint(1, len(P2team.monsters))
        while(oppactive.name == P2team.monsters[oppswitch - 1].name):
            oppswitch = random.randint(1, len(P2team.monsters))
        print(f"\nYour opponent had their {oppactive.name} SWITCH with {P2team.monsters[oppswitch - 1].name}...")
        oppactive = P2team.monsters[oppswitch - 1]

    # if player attacks
    oppmonsterlives = 0
    if(playeraction == 1 and playeraction != 0):
        damagedealt = playeractive.attack + 100 - oppactive.defense
        if(damagedealt < 0):
            damagedealt = 0
        if (playeractive.speed > oppactive.speed or oppaction == 0):
            oppactive.health = oppactive.health - damagedealt
            print(f"\n{playeractive.name} dealt {damagedealt} damage to {oppactive.name}!")
            # if opponent's monster is slain
            if(oppactive.health <= 0):
                print(f"\n{oppactive.name} was slain.")
                P2team.remove_monster(oppactive)
                if(len(P2team.monsters) == 0):
                    print("\nThe dust slowly settles...")
                else:
                    opprevenge = random.randint(1, len(P2team.monsters))
                    oppactive = P2team.monsters[opprevenge - 1]
                    print(f"\nThe oppponent had their slain monster SWITCH to {oppactive.name}...")
                    oppaction = 0
            else:
                 oppmonsterlives = 1

    # if opponent attacks
    playermonsterlives = 0
    if(oppaction == 1 and oppaction != 0):
        damagerecieved = oppactive.attack + 100 - playeractive.defense
        if(damagerecieved < 0):
            damagerecieved = 0
        if (oppactive.speed > playeractive.speed or playeraction == 0 or oppmonsterlives == 1):
            playeractive.health = playeractive.health - damagerecieved
            print(f"\n{oppactive.name} dealt {damagerecieved} damage to {playeractive.name}!")
            # if player's monster is slain
            if(playeractive.health <= 0):
                print(f"\n{playeractive.name} was slain.")
                P1team.remove_monster(playeractive)
                if(len(P1team.monsters) == 0):
                    print("\nOh no!")
                else:
                    lock3 = 1
                    while (lock3 == 1):
                        print("\nSelect a monster to SWITCH to: ")
                        for i, monster in enumerate(P1team.monsters):
                            print(f"{i+1}. {monster.name}")
                        playerrevenge = int(input("\n> "))
                        if (playerrevenge > len(P1team.monsters) or playerrevenge <= 0):
                            print("\nERROR: Your choice is out of bounds, please try again.")
                        elif ( P1team.monsters[playerrevenge - 1].name == playeractive.name):
                            print("\nERROR: You can't switch with a monster that's currently in battle!")
                        else:
                            playeractive = P1team.monsters[playerrevenge - 1]
                            print(f"\nYou call on {playeractive.name} to switch with your slain monster...")
                            lock3 = 0
            else:
                playermonsterlives = 1
    
        if (playermonsterlives == 1 and playeractive.speed < oppactive.speed):
                oppactive.health = oppactive.health - damagedealt
                print(f"\n{playeractive.name} dealt {damagedealt} damage to {oppactive.name}!")
                # if opponent's monster is slain
                if(oppactive.health <= 0):
                    print(f"\n{oppactive.name} was slain.")
                    P2team.remove_monster(oppactive)
                    if(len(P2team.monsters) == 0):
                        print("\nThe dust slowly settles...")
                    else:
                        opprevenge = random.randint(1, len(P2team.monsters))
                        oppactive = P2team.monsters[opprevenge - 1]
                        print(f"\nThe oppponent had their slain monster SWITCH to {oppactive.name}...")
                        oppaction = 0
                else:
                     oppmonsterlives = 1

# game over screen
if(len(P1team.monsters) > 0):
    print("\nYour opponent has no monsters left standing. You have won the battle!\n")
else:
    print("\nAll of your monsters have been slain. Your opponent has won the battle...\n")