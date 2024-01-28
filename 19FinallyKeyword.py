'''By use finally function, that following code in finally function will always executed'''


def func1():
    try:
        l = [2,4,6,7,8]
        i = int(input("Enter a index number of that list: "))
        print(l[i])
        return 1
    except:
        print('some error occoured')
        return 0

    finally:
        print("here are some code also")


x = func1()
print(x)