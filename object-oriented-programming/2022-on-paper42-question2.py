"""
Cambridge International AS & A Level Computer Science 9618
Paper 4 Practical - October/November
Paper: 42
Question: 2

Short description:
This question required using a class to store character details for a game.
Each character has a name, an X coordinate, and a Y coordinate.
The program reads character data from a file, searches for a character by name,
changes the character's position based on user input, and outputs the new coordinates.
"""


class Character:
    def __init__(self, pname, x, y):
        # This is the constructor for the Character class.
        # It is called whenever a new Character object is created.
        # pname, x, and y are passed into the object when it is made.
        self.__name = pname         # PRIVATE Name As STRING
        self.__XCoordinate = x      # PRIVATE XCoordinate As INTEGER
        self.__YCoordinate = y      # PRIVATE YCoordinate As INTEGER
                                    # I wrote these PRIVATE lines because in Paper 4 Python solutions
                                    # we are expected to show the private attributes and their data types like this.

    
    def GetName(self):
        # This method returns the character's name.
        # Since the name is private, we use this method to access it outside the class.
        return self.__name

    def GetX(self):
        # returns the X coordinate of the character.
        return self.__XCoordinate

    def GetY(self):
        # returns the Y coordinate of the character.
        return self.__YCoordinate

    def ChangePosition(self, Xchange, Ychange):
        # This method changes the character's position.
        # Xchange is added to the current X coordinate.
        # Ychange is added to the current Y coordinate.
        self.__XCoordinate = self.__XCoordinate + Xchange
        self.__YCoordinate = self.__YCoordinate + Ychange


# ***main***

# This array will store all the Character objects read from the file.
    CharacterArray = []

try:
    # Open the file that contains the character data.
    # The file is opened in read mode because we only need to read from it.
    f = open('Characters.txt', 'r')

    # The question uses 10 characters, so this loop repeats 10 times.
    for i in range(10):
        # Each character has three lines in the file:
        # name, X coordinate, and Y coordinate.
        name = f.readline().strip()

        # The coordinates are read from the file and converted to integers.
        cx = int(f.readline().strip())
        cy = int(f.readline().strip())

        # A new Character object is created using the values read from the file.
        # The object is then added to CharacterArray.
        CharacterArray.append(Character(name, cx, cy))

except IOError:
    # This runs if the file cannot be found or opened.
    print("file does not exist")


# index is used to store the position of the selected character in CharacterArray.
# It starts at -1 because no matching character has been found yet.
index = -1

# This loop keeps running until the user enters a character name that exists.
while index == -1:
    user = input("Enter the character's name")

    # This loop checks each character in the array.
    for b in range(10):
        # Get the name of the current character.
        h = CharacterArray[b].GetName()

        # The names are compared in lowercase so the search is not case-sensitive.
        if user.lower() == h.lower():
            # If the entered name matches, we store the index of that character.
            index = b


# done2 is used to control the loop for getting a valid movement letter.
done2 = False

# This loop keeps asking until the user enters one of the accepted letters.
while not done2:
    letter = input("Choose letter A, W, S, D")

    # Check whether the entered letter is one of the valid options.
    if letter == 'A' or letter == 'S' or letter == 'W' or letter == 'D':
        done2 = True

        # If the user enters A, the character moves left.
        if letter.upper() == 'A':
            CharacterArray[index].ChangePosition(-1, 0)

        # This branch changes the Y coordinate by +1.
        elif letter.upper() == 'W':
            CharacterArray[index].ChangePosition(0, 1)

        # This branch changes the Y coordinate by -1.
        elif letter.upper() == 'S':
            CharacterArray[index].ChangePosition(0, -1)

        # If the user enters D, the character moves right.
        elif letter.upper() == 'D':
            CharacterArray[index].ChangePosition(1, 0)

# Get the updated X and Y coordinates after the position has been changed.
# They are converted to strings so they can be joined with the output message.
Newcx = str(CharacterArray[index].GetX())                            
Newcy = str(CharacterArray[index].GetY())                  

# Output the selected character's name and new coordinates.
print(CharacterArray[index].GetName() + " has changed coordinates to X = " + Newcx + " and Y = " + Newcy)
