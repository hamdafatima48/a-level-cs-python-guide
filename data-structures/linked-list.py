"""
Basic Linked List Example

This file is a general linked list example for A-Level Computer Science.

It shows how a linked list can be initialised, how a new node can be added,
how the list can be searched, and how a node can be deleted.

In this style of linked list, the actual nodes are stored in an array.
The "next" value works like a pointer because it tells us the index of the next node.

start_ptr tells us where the actual linked list starts.
free_ptr tells us where the free/unused nodes start.
"""


class Node:
    def __init__(self):
        self.data = ""         # class made. every node is treated as an object. Each object stores its own data and a link to the next node.
        self.next = -1         # next stores the index of the next node, -1 means there is no next node


def initialize():
    # making free list here.
    # also initialize the head pointer.
    global start_ptr, free_ptr, link_list

    start_ptr = -1  # -1 means the linked list is empty at the start
    free_ptr = 0    # free list starts from index 0 because all nodes are free at first

    for i in range(9):
        link_list[i].data = ""           # giving initial values to nodes
        link_list[i].next = i + 1        # each free node points to the next free node

    link_list[9].data = ""
    link_list[9].next = -1  # last free node points to -1 because there is no node after it


def print_all():
    global start_ptr, link_list

    current = start_ptr  ptr  # We always begin from start_ptr because it tells us where the linked list actual 

    if current == -1:
        print("The linked list is empty.")  # if start_ptr is -1, no nodes have been added yet

    else:
        while current != -1:
            print(link_list[current].data)   # printed data of one node
            current = link_list[current].next  # incremented pointer to next node


def add_node(name):
    global start_ptr, free_ptr

    if free_ptr == -1 or free_ptr > len(link_list):  # if freeptr is -1 means no space left
        print("No free nodes available to add.")
        return False

    else:
        new_node_index = free_ptr  # we know where to add new value, in main we set freeptr to 0
        free_ptr = link_list[free_ptr].next  # new starting point of free list

        link_list[new_node_index].data = name  # Name added in new node
        link_list[new_node_index].next = -1  # New node at end of linklist, end always points to -1

        if start_ptr == -1 or link_list[start_ptr].data > name:
            link_list[new_node_index].next = start_ptr  # if linklist was empty or name being added was smaller than
            start_ptr = new_node_index   # first node then we make the new node the first node

        else:
            current = start_ptr  # name was not smaller , we check data of all nodes to add in the appropriate position
            previousptr = 0      # previousptr is needed because we have to link the previous node to the new node

            while current != -1 and link_list[current].data < name:
                previousptr = current
                current = link_list[current].next  # keep moving until we find where the new name should go

            link_list[new_node_index].next = current  # new node points to the node that should come after it
            link_list[previousptr].next = new_node_index  # previous node now points to the new node

        return True


def search(search_item):
    global start_ptr

    found = False
    current = start_ptr   # checking from start

    while current != -1 and not found:    # loop until not end of list and not found
        if link_list[current].data == search_item:
            found = True
        else:
            current = link_list[current].next   # moving to next node

    if found:
        print(search_item + " found in the linked list.")
    else:
        print(search_item + " not found in the linked list.")

    return found


def delete_node(delete_data):
    global start_ptr, free_ptr

    exist = search(delete_data)      # checking if data exists in the list

    if start_ptr != -1 and exist:
        found = False
        current = start_ptr     # checking from start
        previous_ptr = current

        while current != -1 and not found:   # stopping when found or end of list
            if link_list[current].data == delete_data:
                found = True
            else:
                previous_ptr = current   # we will need previous ptr to end connection of node from both ends
                current = link_list[current].next

        if current == start_ptr:    # if found at first node
            start_ptr = link_list[current].next  # start pointer moves to the next node

        else:
            link_list[previous_ptr].next = link_list[current].next   # ended connection

        link_list[current].next = free_ptr   # deleted node point to free list node
        free_ptr = current    # deleted node added to start of free list

    else:
        print("Empty link list or data not in the linklist")


def print_status():
    # This module must print how many nodes are left in Free List and
    # ... how many nodes are used in the link list.
    pass


# ********** Display Menu Procedure ***************
def display_menu():
    print("1 To Add a Node ")
    print("2 to Print All")
    print("3 to Search Name in link list")
    print("4 to Delete a node from link list")
    print("5 to Print Status ")
    print("6 to Quit the program")


# ********* End of module *************************


# *********** Main Module *************************

link_list = [Node() for i in range(10)]  # creating 10 empty Node objects
start_ptr = -1  # this will point to the first used node in the linked list
free_ptr = 0    # this will point to the first free node

# call initialize module here
initialize()

choice = ""

while choice != "6":
    display_menu()
    choice = input("Enter your selection ")

    if choice == '1':
        # adding some names to test the linked list
        # the add_node function will place them in sorted order
        add_node("Kashif")
        add_node("Basit")
        add_node("Rania")
        add_node("Absar")
        add_node("Faraz")

    elif choice == '2':
        print_all()  # prints the current linked list from start_ptr onwards

    elif choice == '3':
        search("Faraz")  # testing a name that should be in the list
        search("dd")     # testing a name that should not be in the list

    elif choice == '4':
        delete_node("Rania")  # deleting a node from the middle/end depending on current order
        delete_node("Basit")  # deleting another node to test if links update properly

    elif choice == '5':
        pass

    elif choice == '6':
        print("Good bye..............")

    else:
        print("Invalid Menu option selected!!!!!")
