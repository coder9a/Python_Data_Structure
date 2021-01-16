# Create an empty linked list
ll = []

# add some string type elements to ll
ll.append('America')
ll.append('India')
ll.append('Russia')

#display the linked list
print('Existing list is : ', ll)

# display menu
choice = 0
while choice<5:
    print('Linked list Operations')
    print('1. Add Elements')
    print('2. Remove Elements')
    print('3. Replace Elements')
    print('4. Search an Element')
    print('5. Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        element  = input('Enter element : ')
        pos = int(input('At what position : '))
        ll.insert(pos, element)
    elif choice == 2:
        try:
            element = input('Enter element : ')
            ll.remove(element)
        except ValueError:
            print('Element not found ')
    elif choice == 3:
        element = input('Enter new element : ')
        pos = int(input('At what position ? '))
        ll.pop(pos)
        ll.insert(pos, element)
    elif choice == 4:
        element = input('Enter new element : ')
        try:
            pos = ll.index(element)
            print('Element found at position : ', pos)
        except ValueError:
            print('Element not found')
    else:
        break

print('List : ', ll)