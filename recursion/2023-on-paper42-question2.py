"""
Cambridge International AS & A Level Computer Science 9618
Paper 42 Practical - October/November 2023
Question: 2

Short description:
This question was about finding the total of all divisors of a number.
First, the question used an iterative function, then it asked for the same logic using recursion.
The recursive function keeps reducing the number being checked until it reaches the base case.
"""


def IterativeCalculate(Number):
    Total = 0
    ToFind = Number  # I store the original number because Number will keep decreasing in the loop.

    while Number != 0:
        if ToFind % Number == 0:  # If there is no remainder, then Number is a divisor of ToFind.
            Total = Total + Number

        Number = Number - 1  # Move down to check the next smaller number.

    return Total


v = IterativeCalculate(10)
print(v)


def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0  # Base case: once Number reaches 0, there are no more possible divisors to check.

    else:
        if ToFind % Number == 0:
            # If Number is a divisor, add it and then check the next smaller number.
            return Number + RecursiveValue(Number-1, ToFind)

        else:
            # If Number is not a divisor, just move on to the next smaller number.
            return RecursiveValue(Number-1, ToFind)


b = RecursiveValue(50, 50)
print(b)
