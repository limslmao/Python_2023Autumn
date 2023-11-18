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
#-----------------------------------------
##Its your turn 3.4
# Find the last position object of linked list.
ptr = head
while ptr.next != None:
    ptr = ptr.next
# Create new object and add a node to the last position of linked list.
newnode = Car('black')
ptr.next = newnode
newnode.next = None
traverse(head)
