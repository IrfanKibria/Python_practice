questions =[ 
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
["What is my name?", "imran", "akram", "arfan", "irfan", 4],
]
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for Taka$ {level[i]} \nQuestion is: {question[0]}")
    print("Options are: ")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter Your Answer: "))
    if(reply == question[-1]):#here in my questions correct answer is in index 4, we can simple write 4 or -1.
        print(f"correct answer, you have won {level[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 7500000
        elif(i==16):
            money = 70000000
    elif(reply == 0):
        money = level[i-1]
        print("You wana quite.")
        break
    else:
        print("Wrong Answer")
        break

print(f"your take home money is: {money}")
