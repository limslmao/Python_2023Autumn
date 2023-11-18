class Student:
    def __init__(self, name, math):
        self.name = name
        self.math = math
        self.next = None

head = Student("Bob", 88)
head.next = None

# Traverse the linked list.
def traverse(head): 
    ptr = head
    while ptr != None:
        print('The student name is {} and the math score is {}.'.format(ptr.name, ptr.math))
        ptr = ptr.next
    print('Finish traverse!')

traverse(head)
