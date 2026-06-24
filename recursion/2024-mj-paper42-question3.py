"""
Cambridge International AS & A Level Computer Science 9618
Paper 4 Practical - May/June 2024
Paper: 42
Question: 3

Short description:
This question was about insertion sort and binary search.
The insertion sort is shown in both recursive and iterative form.
I found insertion sort a bit tricky at first and with recursive it's even more confusing so watching a visual representation on YouTube can help with understanding how the values are shifted into the correct position.
The binary search is also recursive, so it keeps searching smaller parts of the sorted array.
"""

def RecursiveIteration(NumberArray1, Elements):
    if Elements <= 1:
        return NumberArray1  # Base case: if there is only one item, it is already sorted.

    else:
        RecursiveIteration(NumberArray1, Elements - 1)  # First, sort the smaller part of the array.

        LastItem = NumberArray1[Elements - 1]  # This is the item we now need to insert in the right place.
        CheckItem = Elements - 2  # This starts checking from the item just before LastItem.

    LoopAgain = True

    if CheckItem < 0:
        LoopAgain = False  # This means we have reached the start of the array.

    elif NumberArray1[CheckItem] < LastItem:
        LoopAgain = False  # If the item before it is smaller, LastItem is already in the right place.

    while LoopAgain:
        NumberArray1[CheckItem + 1] = NumberArray1[CheckItem]  # Shift the bigger value one place to the right.
        CheckItem = CheckItem - 1  # Move backwards to check the next item.

        if CheckItem < 0:
            LoopAgain = False  # Stop if there are no more items before this.

        else:
            if NumberArray1[CheckItem] < LastItem:
                LoopAgain = False  # Stop when the correct position for LastItem is found.

    NumberArray1[CheckItem + 1] = LastItem  # Put LastItem into the empty/correct position.
    return NumberArray1


def IterativeIteration(Array, Elements):
    # This is the normal loop version of insertion sort.

    for i in range(1, Elements):
        FirstData = Array[i]  # This is the value being inserted into the sorted part.
        PreviousIndex = i

        while PreviousIndex > 0 and FirstData < Array[PreviousIndex - 1]:
            Array[PreviousIndex] = Array[PreviousIndex - 1]  # Moving the bigger value one place right.
            PreviousIndex = PreviousIndex - 1  # Keep moving backwards.

        Array[PreviousIndex] = FirstData  # Put FirstData where it belongs.

    return Array


def BinarySearch(Array, First, Last, ToFind):
    # Binary search is used to find a value quickly in a sorted array using the mid value.
    # Here we write it recursively, so it calls itself on a smaller half each time.

    if First > Last:
        return -1  # Base case: the search area is finished, so the value was not found.

    else:
        Mid = int((First + Last + 1)/2)  # Find the middle index of the current search area.

        if ToFind == Array[Mid]:
            return Mid  # The value has been found.

        elif ToFind > Array[Mid]:
            return BinarySearch(Array, Mid + 1, Last, ToFind)  # Search the right half.

        else:
            return BinarySearch(Array, First, Mid - 1, ToFind)  # Search the left half.


# ***** Main ********

NumberArray = [100, 85, 644, 22, 15, 8, 1]    # DECLARE NumberArray : ARRAY[0:6] OF INTEGER

x = RecursiveIteration(NumberArray, 7)  # Sort the array using the recursive insertion sort.
print("Recursive")
print(x)

j = IterativeIteration(NumberArray, 7)  # Sort the array using the iterative insertion sort.
print("Iteration")
print(j)

ReturnVal = BinarySearch(x, 0, 7, 644)  # Search for 644 using recursive binary search.

if ReturnVal == -1:
    print("Not Found")
else:
    print(ReturnVal)
