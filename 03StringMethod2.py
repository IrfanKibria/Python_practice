'''Here we are also practiceing some string method like find, index,
isalnum, '''

# find and index are same but find return -1 value and index return error
name = "Irfan Kibria Talha"

a = name.find("Talha")

print(a)


name = "Irfan Kibria Talha"

a = name.index("Talha")

print(a)




name = "IrfanKibriaTalha"

a = name.find("Talhaaa")

print(a)

'''
name = "Irfan Kibria Talha"

a = name.index("Talhaaa")

print(a)
'''

# isalnum use for to know the string is alpha numeric or not. isalnum lontains A to Z and a to z and 0 to 9
# if any other character even space is in the string then it will show false
# isalpha contains A to Z and a to z. Any other character even space in string it will show false
# islower will true when the strings all character in lower form.
# isprinable is true when all characters are printable.
# swapcase is a method which is turn uppercase to lower case and lower case to uppercase
# title method use for capitalize every word's first letter
name = 'IrfanKibriaTalha'
print(name.isalnum())

name = 'Irfan Kibria Talha'
print(name.isalpha())

name = "irfan kibria talha 00"
print(name.islower())

name = "Irfan \nKibria \nTalha"
print(name)
print(name.isprintable())

name = 'iRFAN kibRIA TalHA'
print(name.swapcase())

string = 'I am irfan kibria talha, i am a good boy'
print(string.title())