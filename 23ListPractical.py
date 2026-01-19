'''Create a Python script that reads commands to perform list operations and updates the list accordingly. 
Support commands like insert, remove, append, sort, pop, reverse, and print.'''

if __name__ == '__main__':
    N = int(input())
    lst= []

    for a in range(N):
        opl = input().split()
        command = opl[0]

        if command == 'insert':
            indx = int(opl[1])
            element = int(opl[2])
            lst.insert(indx, element)

        elif command == 'print':
            print(lst)

        elif command == 'remove':
            element = int(opl[1])
            lst.remove(element)

        elif command == 'append':
            element = int(opl[1])
            lst.append(element)

        elif command == 'sort':
            lst.sort()
        
        elif command == 'pop':
            lst.pop()

        elif command == 'reverse':
            lst.reverse()
    print(lst)