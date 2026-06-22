'''
Cambridge International AS & A Level Computer Science 9618
Paper 42 Practical - October/November 2023
Question: 3

This question was about using OOP for game characters.
First, it required a Character class with methods like Learn(), ReturnAge(), and getters/setters.
Then it added a MagicCharacter subclass, where Learn() works differently depending on the character's element.
'''

import datetime

class Character:
    def__init__(self, cn, db, intel, spd):
        self.__CharacterName = cn       # PRIVATE CharacterName: STRING
        self.__DateOfBirth = db         # PRIVATE DateOfBirth: DATE
        self.__Intelligence = intel     # PRIVATE Intelligence: REAL
        self.__Speed = spd              # PRIVATE Speed : INTEGER
        # I wrote these PRIVATE lines because in Paper 4 Python solutions,
        # we are expected to show the private attributes and their data types like this.

def GetIntelligence(self):
    # Getter for intelligence because the attribute is private.
    return self.__Intelligence

def GetName(self):
    # Getter for the character name.
    return self.__CharacterName

def SetIntelligence(self, intel2):
    # Setter used when the intelligence value needs to be changed.
    self.__Intelligence = intel2

def Learn(self):
    # Normal characters increase intelligence by 10%.
    self.__Intelligence = self.__Intelligence * 1.1

def ReturnAge(self):
    # This tells the character's age in 2023.
    return 2023 - self.__DateOfBirth.year


class MagicCharacter(Character):
    def__init__(self, cn, db, intel, spd, element):
    # Character is the superclass/parent class.
    # MagicCharacter is the subclass/child class, so it inherits the normal character details..
        Character.__init__(self, cn, db, intel, spd)
        # This is the extra attribute only for MagicCharacter.
        self.__element = element                # PRIVATE element : STRING

def Learn(self):
    # This Learn method will override the Learn method from Character.
    # Magic characters increase intelligence differently depending on their element.

    if self.__element == "fire" or self.__element == "water":
        super().SetIntelligence(super().GetIntelligence() * 1.2)    #super() lets us use methods from the superclass. 
                                                                    # Here, I get the current intelligence from Character and increase it by 20%, then set the new value.

    elif self.__element == "earth":
        super().SetIntelligence(1.3 * super().GetIntelligence())

    else:
        super().SetIntelligence(1.1 * super().GetIntelligence())


# *** MAIN ***

# Create a normal Character object and test the Learn method.

FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)            # datetime.datetime(year, month, day) is used here to create a date of birth. 
                                                                                      # For example, datetime.datetime(2019, 1, 1) means 1 January 2019.
FirstCharacter.Learn()

name = FirstCharacter.GetName()
age = str(FirstCharacter.ReturnAge())
intelligence = str(FirstCharacter.GetIntelligence())

print(name + " is " + age + " years old and has intelligence " + intelligence)

# Creating a MagicCharacter object and test its own Learn method.

FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75, 22, "fire")     # Magic character has all the normal character attributes &the extra element attribute.
FirstMagic.Learn()               ## Since the element is fire, intelligence increases by 20%.

name2 = FirstMagic.GetName()
intelligence2 = str(FirstMagic.GetIntelligence())
age2 = str(FirstMagic.ReturnAge())

print(name2 + " is " + age2 + " years old and has intelligence " + intelligence2)

