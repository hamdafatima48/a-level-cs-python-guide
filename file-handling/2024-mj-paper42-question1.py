"""
Cambridge International AS & A Level Computer Science 9618
Paper 4 Practical - May/June 2024
Paper: 42
Question: 1

Short description:
This question was about file handling and a word game.
The program reads the main word and all possible answers from a text file.
Then the user keeps entering words until they type "no", and the program checks which answers they got correct.
"""

def Readwords(filename):
    global WordArray  # using global because I need to update the main WordArray inside this function
    global NumberWords  # same here, because the number of words is counted while reading the file

    try:
        f = open(filename, 'r')  # opens whichever file the user chose

        for line in f:
            WordArray.append(line.strip())  # adds each word to the array, without the extra newline
            NumberWords = NumberWords + 1  # counting how many lines were read

        NumberWords = NumberWords - 1  # because the first word is the main word, not one of the answers
        f.close()

    except IOError:
        print("file doesnt exist")  # just in case the file is missing or the name is wrong

    Play()  # once the file is read, the game can start


def Play():
    global WordArray
    global NumberWords

    print("The word is " + WordArray[0])  # the first word in the file is the main word
    print(NumberWords)  # this shows how many answers are possible

    WordArray[0] = ""  # clearing this so the main word does not appear later as a missed answer

    correct = 0  # this will count the correct answers entered by the user

    user = input("Enter your word greater than 3 letters")

    while user.lower() != "no":  # the user keeps entering words until they type no
        answer = False  # this starts as False because we have not found the word yet
        i = 1  # starting from 1 because index 0 was the main word

        while i < NumberWords + 1 and not answer:
            if user.lower() == WordArray[i]:
                WordArray[i] = ""  # clearing the word once it is found, so it cannot be used again
                answer = True

            i = i + 1  # moving to the next word in the array

        if answer:
            print("Correct " + user + " is an answer")
            correct = correct + 1  # only add to correct if the word was actually found

        else:
            print("This is not an answer")

        user = input("Enter you word")  # ask for the next word

    percentage = (correct/NumberWords) * 100  # this tells what percentage of answers the user found
    print("Percentage of answers is " + str(percentage) + "%")

    print("The answers you did not enter are:")

    for h in range(NumberWords + 1):
        if WordArray[h] != "":
            print(WordArray[h])  # anything still left in the array was not guessed by the user


# *****MAIN******

WordArray = []  # this will store the main word and all the possible answers
NumberWords = 0  # starts at 0 before anything is read from the file

choice = input("Please select your file , 'easy, 'medium', 'hard' ")

if choice.lower() == "hard":
    Readwords('Hard.txt')

elif choice.lower() == "easy":
    Readwords('Easy.txt')

elif choice.lower() == "medium":
    Readwords('Medium.txt')
