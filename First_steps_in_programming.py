#

def Execute():
    print("1 - HelloSoftUni")
    print("2 - Nums1to10")
    print("3 - RectangleArea")
    print("4 - InchesToCantimeters")
    print("5 - GreetingByName")
    print("6 - ConcatenateData")
    print("7 - ProjectsCreation")
    print("8 - PetShop")
    print("9 - YardGreening")
    print("0 - Exit")
    choice = input("Select a function": )
    if(choice == 1):
        HelloSoftUni()
    elif(choice == 2):
        Nums1to10()
    elif(choice == 3):
        RectangleArea()
    elif(choice == 4):
        InchesToCantimeters()
    elif(choice == 5):
        GreetingByName()
    elif(choice == 6):
        ConcatenateData()
    elif(choice == 7):
        ProjectsCreation()
    elif(choice == 8):
        PetShop()
    elif(choice == 9):
        YardGreening()
    elif(choice == 0):
        print("Have a nice day :)")
    else:
        print("Invalid input")
        Execute()


def HelloSoftUni():
    print("Hello SoftUni")
    Execute()

def Nums1to10():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
    Execute()

def RectangleArea():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area = a*b
    print(area)
    Execute()

def InchesToCantimeters():
    a = float(input("Enter inches amount: "))
    print(a*2.54)
    Execute()

def GreetingByName():
    name = input("What's your name?")
    print("Hello, " + name + "!")
    Execute()

def ConcatenateData():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    town = input("Enter your hometown: ")
    print('You are ' + first_name + " " + last_name + ", a " + str(age) + "-years old person from " + town + ".")
    Execute()

def ProjectsCreation():
    name = input("Enter your name: ")
    projects = int(input("Enter the amount of projects you are working on"))
    hours = projects * 3
    print("The architect " + name + " will need " + str(hours) + " hours to complete " + str(projects) + " project/s.")
    Execute()

def PetShop():
    dogs = int(input("Enter what amount of dog food you want to aquire: "))
    cats = int(input("Enter what amount of cat food you want to aquire: "))
    total = dogs * 2.5 + cats * 4
    print(str(total) + " lv.")
    Execute()

def YardGreening():
    sqm = float(input("Enter the Area you want to Green in square meters: "))
    total = sqm * 7.61
    discount = total * 0.18
    final = total - discount
    print("The final price is: " + str(final) + " lv.")
    print("The discount is: " + str(discount) + " lv.")
    Execute()