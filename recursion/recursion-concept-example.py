"""
This file is a general example to understand recursion.

Recursion means that a function calls itself again and again until it reaches a stopping point.
That stopping point is called the base case.
For every recursive problem, the base case has to be decided according to that specific situation. 
It is the condition where the function should stop calling itself. 

In this example, both functions count how many vowels are in a string.

The first function, iterativevowels(), uses a loop.
The second function, recursivevowels(), does the same thing using recursion.

The main idea is:
- the iterative version repeats using a loop
- the recursive version repeats by calling itself with a smaller part of the string
- the base case is when the string becomes empty
- once the string is empty, the function stops calling itself and starts returning the answers back
"""


def iterativevowels(value):
    # This function counts vowels using iteration, which means using a loop which is pretty basic.

    total = 0

    lengthstring = len(value)
    # I am saving the original length here because the string will become shorter inside the loop.


    for x in range(lengthstring):
        # Each time, I will check the first character of the current string.
        firstcharacter = value[0]

        # If the first character is a vowel, I add 1 to total.
        if (firstcharacter == 'a' or firstcharacter == 'e' or firstcharacter == "i" or firstcharacter == "o" or
                firstcharacter == "u"):
            total = total + 1

        value = value[1:len(value)]        # This removes the first character.
        # So in the next loop, the next character becomes the first character.
      

    # After the loop has checked every character, total is returned.
    return total


# Testing the iterative function.
s = iterativevowels("hellooo")
print(s)


def recursivevowels(value):
    # This function counts vowels using recursion.
    # Instead of using a loop, the function keeps calling itself with a shorter string.

    # Base case:
    # If the string is empty, there is nothing left to check.
    # So the function returns 0 and stops calling itself.
    value = value.lower()  # This makes the string lowercase, so capital vowels like A or E are counted too.
    if value == "":
        return 0

    # Here I check the first character of the string.
    # If it is a vowel, I count 1 for this character.
    # Then I call the same function again with the rest of the string.
    elif value[0] == 'a' or value[0] == 'e' or value[0] == "i" or value[0] == "o" or value[0] == "u":
        return 1 + recursivevowels(value[1:len(value)])

    # If the first character is not a vowel, I do not add 1.
    # I just call the function again with the rest of the string.
    else:
        return recursivevowels(value[1:len(value)])


# testing the recursive function.
temp = recursivevowels("hellooo")
print(temp) 
# if code is correct both return values will be same
