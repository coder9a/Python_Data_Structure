from Create_Queue import Queue
# Create empty Queue object
q = Queue()
# display menu
choice = 0
while choice<5:
    print('Queue Operations')
    print('1. Add Elements')
    print('2. Delete Elements')
    print('3. Search an Element')
    print('4. Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        element = float(input('Enter element : '))
        q.add(element)
    elif choice == 2:
        element = q.delete()
        if element == -1:
            print('Queue is empty')
        else:
            print('Deleted element = ', element)
    elif choice == 3:
        element = input('Enter element : ')
        pos = q.search(element)
        if pos == -1:
            print('Queue is empty ')
        elif pos == -2:
            print('Element not found in the Queue')
        else:
            print('Element found at position ', pos)
    else:
        break

print('Queue : ', q.display())