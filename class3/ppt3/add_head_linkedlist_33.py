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
#-----------------------------------------
##Its your turn 3.3
# Add a node to the first position of linked list.
newnode = Car('blue')
newnode.next = head
head = newnode
traverse(head)
