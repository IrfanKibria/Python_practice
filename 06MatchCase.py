Age = int(input("Enter Your Age: "))

match Age:
    case 18:
        print("you can apply")


'''
Need to learn from different courses

'''

Vote = int(input("Enter your Option: "))

match Vote:
    case 0:
        print("You vote Amir")

    case 1:
        print("You vote jiku")

    case _:
        print("Invalid vote")