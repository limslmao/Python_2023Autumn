##Its your turn 3.1
class Car:
    def __init__(self, color):
        self.color = color
        self.next = None
# Initiate the first element of the linked list.
head = Car("red") # Add new element.
ptr = head #Set the position of the pointer.
ptr.next = None #There is no next element now.
# Add next element into linked list.
new_data = Car("blue") # Add the next element.
ptr.next = new_data #Connect the elements.
new_data.next = head #Point to the head for circular architecture.
ptr = new_data #The position of the pointer should be the position of the new element.

# Traverse the linked list.
def traverse(head): 
    ptr = head
    while True:
        print('The color of the car is {}.'.format(ptr.color))
        if ptr.next==head:
            break
        ptr = ptr.next 
    print('Finish traverse!')
traverse(head)
