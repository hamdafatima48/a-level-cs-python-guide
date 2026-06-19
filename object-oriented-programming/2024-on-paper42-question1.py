"""
Cambridge International AS & A Level Computer Science 9618
Paper 42 Practical - October/November 2024
Question: 1

Short description:
This question was about using OOP for a game with characters and events.
It required an EventItem class for event details and a Character class for character skills.
The program compares two characters across five events and decides who wins each event and the group.
"""

class EventItem:
def__init__(self, name, typ, diff):
# Paper 4 expects us to show the private attributes and their data types.
  self.__EventName = name           # PRIVATE EventName : STRING
  self.__Type = typ                 # PRIVATE Type : STRING
  self.__Difficulty = diff          # PRIVATE Difficulty : INTEGER
  

# Getter methods are needed because the attributes are private.
def GetName(self):
    return self.__EventName

def GetDifficulty(self):
    return self.__Difficulty

def GetEventType(self):
    return self.__Type


class Character():
def__init__(self, name, jmp, swm, rn, drv):
  # This class stores one character and their skill levels.
  # These skills are later compared with the difficulty of each event.
  self.__CharacterName = name         # PRIVATE CharacterName : STRING
  self.__Jump = jmp                   # PRIVATE Jump : INTEGER
  self.__Swim = swm                   # PRIVATE Swim : INTEGER
  self.__Run = rn                     # PRIVATE Run : INTEGER
  self.__Drive = drv                  # PRIVATE Drive : INTEGER

def GetName(self):
    return self.__CharacterName

def CalculateScore(self, eventtype, difficulty):
    # This is the main method in the question.
    # It chooses the correct skill depending on the event type.
    if eventtype.lower() == "jump":
        difference = difficulty - self.__Jump
    elif eventtype.lower() == "swim":
        difference = difficulty - self.__Swim
    elif eventtype.lower() == "run":
        difference = difficulty - self.__Run
    elif eventtype.lower() == "drive":
        difference = difficulty - self.__Drive
    else:
        return 0

    # The difference shows how much harder the event is than the character's skill.
    # A smaller difference means a better chance of completing the event.
    if difference < 0:
        chances = 100
    elif difference == 1:
        chances = 80
    elif difference == 2:
        chances = 60
    elif difference == 3:
        chances = 40
    elif difference == 4:
        chances = 20
    else:
        return 0

    return chances

# ****MAIN****


Group = [EventItem for i in range(5)]
# This line is only an initial setup for the group.
# The actual EventItem objects are added to Group after they are created.

# Each event object will store the event name, the event type, and the difficulty.
Event1 = EventItem("Bridge", "jump", 3)
Event2 = EventItem("Water Wade", "swim", 4)
Event3 = EventItem("100 mile run", "run", 5)
Event4 = EventItem("Gridlock", "drive", 2)
Event5 = EventItem("Wall on wall", "jump", 4)

# Now all five event objects are stored in one list.

Group = [Event1, Event2, Event3, Event4, Event5]

# These two Character objects store the skill values in this order:
# jump, swim, run, drive.

Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2,  2,  3, 4)

# These count how many events each character wins.
TarzWins = 0
GeniWins = 0

for i in range(5):
# For each event, both characters are given a score using the same event type and difficulty.
  Tarzscore = Tarz.CalculateScore(Group[i].GetEventType(), Group[i].GetDifficulty())
  Geniscore = Geni.CalculateScore(Group[i].GetEventType(), Group[i].GetDifficulty())

# The higher score wins the event.
if Tarzscore > Geniscore:
    TarzWins = TarzWins + 1
    print("Tarz won " + Group[i].GetName())
elif Geniscore > Tarzscore:
    GeniWins = GeniWins + 1
    print("Geni won " + Group[i].GetName())
else:
    print(Group[i].GetName() + " was draw")

# Finally, the number of events won by each character is compared.
if TarzWins > GeniWins:
  print("Tarz won with " + str(TarzWins) + " points")
elif TarzWins < GeniWins:
  print("Geni won with " + str(GeniWins) + " points")
else:
  print("Draw group")

