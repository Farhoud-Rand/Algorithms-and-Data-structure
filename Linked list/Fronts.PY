# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Single linked list class
class SLL:
    def __init__(self, data):
        self.head = Node(data)

    # Function to add at the end of linked list
    def add_node_to_end(self, num):
        newnode  = self.head           # Define a new node to go  through linked list nodes
        while ( newnode.next != None): # Go to the last node in the linked list
            newnode = newnode.next
        my_node = Node(num)            # Define new node with given data
        newnode.next = my_node         # Change the pointer of the last node

    # Function to add at the front of linked list
    def add_node_to_front(self, num):
        newnode = Node(num)            # Define a new node
        newnode.next = self.head       # Make the current head be the next node for the new node
        self.head = newnode            # Change the head

    #  Function to delete node form the middle of linked list
    def delete_node_from_middle(self, num):
        newnode = self.head                 # Define a new node to go  through linked list nodes
        while ( newnode.next.data != num ): # Go to the last node in the linked list
            newnode = newnode.next 

        newnode.next = newnode.next.next   # Change the next pointer

    #  Function to delete node form the front of linked list
    def delete_node_from_front(self):
        self.head = self.head.next          # Change the next pointer for the head node 
        
    # Function to travers linked list
    def travers_ll(self):
        newnode = self.head
        if (newnode != None):
            while ( newnode.next != None):
                print(newnode.data,"->")
                newnode = newnode.next     
            print(newnode.data, "--> NULL")
        else: 
            print("None")

    # Function that returns the first data in the first node 
    def front(self):
        if self.head == None:
            return None
        return self.head.data

    def findSum(self):
        # We first have to tell our train attendant that we want them to start at the front of the train
        runner = self.head
        sum=0
        //Since a Linked List does not know how many nodes is within it, we will not be able to use a for loop to             iterate, instead we'll use a while
        //Also we need to tell them when to stop otherwise they will just run off the end of the train
        while(runner !== null):
            //Since the runner is set to the current node, its value will be equal to the value of the node they                 are currently on
                sum+=runner.data
            //Tell our attendant to move to the next car
            runner=runner.next
        
        return sum
    
# ==================================================================================
# Testing code
my_linkedlist = SLL(8)
my_linkedlist.delete_node_from_front()
my_linkedlist.front()
my_linkedlist.add_node_to_end(30)
my_linkedlist.add_node_to_end(40)
my_linkedlist.add_node_to_end(140)
my_linkedlist.add_node_to_front(2)
my_linkedlist.delete_node_from_middle(40)
my_linkedlist.delete_node_from_front()
my_linkedlist.travers_ll()


