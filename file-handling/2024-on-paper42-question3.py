"""
Cambridge International AS & A Level Computer Science 9618
Paper 4 Practical - October/November 2024
Paper: 42
Question: 3

Short description:
This question was about reading a high score table from a text file.
The data is stored in a 2D array, then printed before and after sorting.
The sorting part is the main tricky bit because it sorts by level first, and then by score if the level is the same.
"""

def ReadData():
    try:
        f = open("HighScoreTable.txt", "r")  # This opens the file so the high score data can be read.

        for x in range(7):
            id = f.readline().strip()  # First line of each record is the player ID.
            level = f.readline().strip()  # 2nd line is the level reached.
            score = f.readline().strip()  # 3rd line is the score.

            HighScores[x][0] = id  # Store ID in the first column.
            HighScores[x][1] = level  # Store level in the second column.
            HighScores[x][2] = score  # Store score in the third column.

        f.close()  # Close the file after reading all the records.

    except IOError:
        print("file doesnt exist")  # This runs if the file cannot be opened.

    return HighScores


def OutputHighScores(Array):
    for x in range(7):   # Go through each row for player in the 2D array.
        pid = Array[x][0]
        lvl = Array[x][1]
        s = Array[x][2]

        print(pid + " reached level " + lvl + " with a score of " + s)


def SortScores(HighScores):
    for t in range(len(HighScores) - 1):
        for x in range(len(HighScores) - t - 1):
            if HighScores[x][1] < HighScores[x+1][1]:  # If the next level is higher, the rows need to swap.
                for y in range(3):  # Since this is a 2D array, the whole row has to be swapped.
                    temp = HighScores[x][y]
                    HighScores[x][y] = HighScores[x + 1][y]
                    HighScores[x + 1][y] = temp

            elif HighScores[x][1] == HighScores[x+1][1]:  # If the levels are the same, then we compare the scores.
                if HighScores[x][2] < HighScores[x+1][2]:  # Higher score should come first.
                    for y in range(3):  # Again, the full row is swapped, not only the score.
                        temp = HighScores[x][y]
                        HighScores[x][y] = HighScores[x + 1][y]
                        HighScores[x + 1][y] = temp

    return HighScores

# ****main*****

HighScores = []

HighScores = [["" for i in range(3)] for y in range(7)]  # This creates a 2D array: 7 players and 3 values for each.

HighScores = ReadData()  # Read the data from the file into the 2D array.

print("Before")
OutputHighScores(HighScores)  # Print the scores before sorting.

HighScores = SortScores(HighScores)  # Sort by level first, then score.

print("After")
OutputHighScores(HighScores)  # Print the scores again after sorting.
