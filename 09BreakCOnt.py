a = int(input("Enter a number which you want to make Multiplication table: "))
for i in range(15):
        if(i==10):
            break
        print(f"{a} * {i+1} = {a*(i+1)}")



a = int(input("Enter a number which you want to make Multiplication table: "))
for i in range(15):
        if(i==10):
            print("Skip the Itretion")
            continue
        print(f"{a} * {i} = {a*(i)}")
