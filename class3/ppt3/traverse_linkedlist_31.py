class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

# Initiate the first element of single linked list.
head = Car('red')
head.next = None
#-----------above: linkedlist_create----------------

##Its your turn 3.1
# Traverse the linked list.
def traverse(head): 
    ptr = head
    while ptr != None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next
    print('Finish traverse!')

traverse(head)