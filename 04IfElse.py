Age = int(input('Enter Your age: '))
print("Input age is: ",Age)

if Age>18 and Age<=70:
    print("You can Drive")

elif Age>70:
    print("You can not Drive. Over Aged")

else:
    print("You can not Drive. Below aged")