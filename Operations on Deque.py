from collections import deque
# Create empty dequeue object
d = deque()
# display menu
choice = 0
while choice<5:
    print('Dequeue Operations')
    print('1. Add Element at front')
    print('2. Remove Element from front')
    print('3. Add Element at rear')
    print('4. Remove Element from rear')
    print('5. Remove Element from middle')
    print('6. Search an Element')
    print('7. Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        element = float(input('Enter element : '))
        d.appendleft(element)
    elif choice == 2:
        if(len(d)) == 0:
            print('Deque is empty')
        else:
            d.popleft()
    elif choice == 3:
        element = input('Enter element')
        d.append(element)
    elif choice == 4:
        if len(d) == 0:
            print('Deque is empty')
        else:
            d.pop()
    elif choice == 5:
        element = input('Enter element ')
        try:
            d.remove(element)
        except ValueError:
            print('Element not found')
    elif choice == 6:
        element = input('Enter element ')
        c = d.count(element)
        print('No of times element found = ', c)
    else:
        break
# Display the deque elements using for loop
print('Deque = ',end='')
for i in d:
    print(i, ' ', end='')
print()