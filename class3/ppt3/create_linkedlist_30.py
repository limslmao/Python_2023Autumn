class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

# Initiate the first element of single linked list.
head = Car('red')
head.next = None

print(head)
print(head.color)

