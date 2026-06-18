"""
Cambridge International AS & A Level Computer Science 9618
Paper 41 Practical - May/June 2024
Question: 2

Short description:
This question is about storing tree data using a Tree class.
The program reads tree details from a file, prints tree information,
and helps the user choose a suitable tree based on their requirements.
"""

class Tree:
def __init__(self, Pname, Pgrowth, Pheight, Pwidth, Pgreen):
# The constructor stores all the details for one Tree object.

    # PRIVATE TreeName : STRING             # I wrote these PRIVATE lines because in Paper 4 Python solutions,                               
    # PRIVATE HeightGrowth : INTEGER        # we are expected to show the private attributes and their data types like this.
    # PRIVATE MaxHeight : INTEGER
    # PRIVATE MaxWidth : INTEGER
    # PRIVATE Evergreen : STRING

    self.__TreeName = Pname
    self.__HeightGrowth = Pgrowth
    self.__MaxHeight = Pheight
    self.__MaxWidth = Pwidth
    self.__Evergreen = Pgreen

def GetTreeName(self):
 # Getter methods are used because the attributes are private.
    return self.__TreeName

def GetMaxHeight(self):
    return self.__MaxHeight

def GetGrowth(self):
    return self.__HeightGrowth

def GetMaxWidth(self):
    return self.__MaxWidth

def GetEverGreen(self):
    return self.__Evergreen


def ReadData():
# This function reads the tree data from Trees.txt
# and creates Tree objects from the data.


Array = []
try:
    f = open('Trees.txt', 'r')

    for count in range(9):
        # Each line has one tree's data separated by commas.
        Data = f.readline().strip().split(',')

        name = Data[0]
        growth = int(Data[1])
        maxheight = int(Data[2])
        width = int(Data[3])
        egreen = Data[4]

        # Creating a Tree object and adding it to the array.
        Array.append(Tree(name, growth, maxheight, width, egreen))

except IOError:
    print("Not found")

return Array


def PrintTrees(Tree1):
# This function receives one Tree object and prints its details.

n = Tree1.GetTreeName()
g = str(Tree1.GetGrowth())
h = str(Tree1.GetMaxHeight())
w = str(Tree1.GetMaxWidth())
e = str(Tree1.GetEverGreen())

# output changes slightly depending on whether the tree loses its leaves.
if e == 'No':
    print(n + " has a maximum height " + h + " a maximum width " + w + " and grows " + g +
          " cm a year. It loses its leaves each year")
else:
    print(n + " has a maximum height " + h + " a maximum width " + w + " and grows " + g +
          " cm a year. It does not lose its leaves")
```

def ChooseTrees(Array):
# This function lets the user enter the kind of tree they want
# and then searches for trees that match those requirements.

```
userheight = int(input("Enter your requirement for height"))
userwidth = int(input("Enter your requirement for width"))
usergreen = input("Should it be evergreen")

NewArray = []
Matched = False

for i in range(len(Array)):
    # tree only matches if height, width, and evergreen choice all fit.
    if (Array[i].GetMaxHeight() <= userheight and Array[i].GetMaxWidth() <= userwidth and
            Array[i].GetEverGreen() == usergreen):

        NewArray.append(Array[i])
        PrintTrees(Array[i])
        Matched = True

if not Matched:
    print("No tree matched requirement")

else:
    buy = input("Enter name of tree you want to buy from these")
    h = int(input("Enter height of tree when it is being bought"))

    for j in range(len(NewArray)):
        if NewArray[j].GetTreeName() == buy:
            # This tells how many years are needed for the tree
            # to grow from its current height to its maximum height.
            time = str(int((NewArray[j].GetMaxHeight() - h)/NewArray[j].GetGrowth() + 1))
            print("years for it to grow to max height is " + time)

# ***MAIN***

r = ReadData()         # Reading all tree records from the file into an array of Tree objects.

for g in range(len(r)):            # Printing basic details for each tree.

print(r[g].GetTreeName())
print(r[g].GetEverGreen())
print(r[g].GetMaxHeight())
print(r[g].GetMaxWidth())


PrintTrees(r[0])    # Printing the first tree using the PrintTrees function.


ChooseTrees(r)    # Let the user choose a tree based on their requirements.


