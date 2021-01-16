from Create_Stack import Stack
# Create empty stack object
s = Stack()
# display menu
choice = 0
while choice<5:
    print('Stack Operations')
    print('1. PUSH Elements')
    print('2. POP Elements')
    print('3. PEEP Elements')
    print('4. Search an Element')
    print('5. Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        element = input('Enter element : ')
        s.push(element)
    elif choice == 2:
        element = s.pop()
        if element == -1:
            print('Stack is empty')
        else:
            print('Popped element = ', element)
    elif choice == 3:
        element = s.peep()
        print('Topmost element = ', element)
    elif choice == 4:
        element = input('Enter element : ')
        pos = s.search(element)
        if pos == -1:
            print('Stack is empty ')
        elif pos == -2:
            print('Element not found in the stack')
        else:
            print('Element found at position ', pos)
    else:
        break

print('Stack : ', s.display())