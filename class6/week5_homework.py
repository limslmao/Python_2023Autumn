class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
Eddy = Employee("Eddy", 43)

Amy = Employee("Amy", 25)
Amy.next=Eddy

Esme = Employee("Esme", 32)
Eddy.next=Esme

def traverse(head):
    ptr = head
    while ptr != None:
        print("The employee name is {} and the age is {}.".format(ptr.name, ptr.age))
        ptr = ptr.next
    print("Finish traverse!")

traverse(Amy)