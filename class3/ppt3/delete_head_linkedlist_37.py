class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

# Initiate the first element of single linked list.
head = Car('red')
head.next = None

# Traverse the linked list.
def traverse(head): 
    ptr = head
    while ptr != None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next
    print('Finish traverse!')

# Add a node to the first position of linked list.
newnode = Car('blue')
newnode.next = head
head = newnode

# Find the last position object of linked list.
ptr = head
while ptr.next != None:
    ptr = ptr.next
# Create new object and add a node to the last position of linked list.
newnode = Car('black')
ptr.next = newnode
newnode.next = None

##Its your turn 3.5
#Find the position you want to add object.
ptr = head
while ptr.color != "red":
    ptr = ptr.next
# Create new object and add a node to the middle of linked list.
newnode = Car('pink')
newnode.next = ptr.next
ptr.next = newnode

##Its your turn 3.6
#Find the object before the object you want to delete.
ptr = head
while ptr.next.color != "pink":
    ptr = ptr.next
#Delete the object from the middle of linked list.
delete = ptr.next
ptr.next = delete.next

#-----------------------------------------
##Its your turn 3.7
delete = head
head = head.next
traverse(head)
