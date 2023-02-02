print("---------------PhoneBook---------------")

#print('''Instruction\n  d for displaying contacts \n e for exiting the book \n u for updating book \n a for adding contact \n r for removing  \n f for finding contact   ''')
#contacts={}
#exit = True

'''def display():
    for key,value in contacts.items():
        print(key,value)

def update():
     name = input("enter name u wish to update: ")
     number = (input("enter number: "))
     contacts.update({name:number})

def remove():
    name = input("enter name :")
    contacts.pop(name)

def finding():
    name = input("enter name of contact: ")
    contacts.get(name)

def adding():
    name = input("enter name: ")
    number = (input("enter number : "))
    contacts.update({name:number})
 
while True:
    enter1 = input("enter command: ")

    if enter1 =="d":
        display()

    if enter1 =="u":
        update()
    if enter1 == "a":
        adding()
    if enter1 == "f":
        finding()

    if enter1 =="r":
        remove()

    if enter1=="e":
        break'''

print('''Instruction\n  d for displaying contacts \n e for exiting the book \n u for updating book \n a for adding contact \n r for removing  \n f for finding contact   ''')
contacts={}
while True:
    enter1 = input("enter command: ")
    


    if enter1 =="d":
        print("\n\t NAME   Ph.No")
        for key,value in contacts.items():
         #print("\n\t NAME  Ph.No")
         print("\n\t",key,"  ",value)
         

    elif enter1 =="u":
        name = input("enter name u wish to update: ")
        number =  (input("enter number: "))
        contacts.update({name:number})

    elif enter1 =="r":
        name = input("enter name :")
        contacts.pop(name)

    elif enter1 =="f":
        name = input("enter name of contact: ")
        print(contacts.get(name))

    elif enter1 =="a":
        name = input("enter name: ")
        number = (input("enter number : "))
        contacts.update({name:number})
        
    elif enter1 =="e":
        break
