def qubic_square(n):
    '''This is called Doc String. In here we define the function or method we use in program. 
       In this program we make a function which return qubic squre of any number. we have to use doc string
       right below to functions or above the program body. if we use it another place we could not track it. '''
    
    print(n**3)


a = int(input("Enter a number: "))

qubic_square(a)
print(qubic_square.__doc__)  # By this method we can see the doc string we use in the function