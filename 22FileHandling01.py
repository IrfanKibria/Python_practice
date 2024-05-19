"""Here we are learning about file handling in python
in here we learn Read, open and close files"""

'''In open function there are 2 parameters. They are filename and which operation we want to do like 'r' for read,
'w' for write, 'a' for append etc'''


'''when we use binary or different extension file we will use t after the function. such as: 'rt', 'wt', 'at' etc  '''



#Read a file
'''Here at first we create a file manually and then add some content. Then open the file as read mode by "r". then we
extarct the content form the file via read function'''

f = open("23Flilehandleingsample.txt", "r")#here we can use 'rt'. rt means read text. r and rt works similar
# print(f)
text = f.read()#By this we extract the content from the file
print(text)


#Write a File
'''when we use w or wt in open function in a existing file it will overwrite the file. preveous content will
erase after run the program'''
'''In this section we worked with previous file. in that file has other content but by this code it will change.
because w function check if the file existing then it will overwritte on it. if the file is not found then it
will create a file then add the content'''

f = open("23Flilehandleingsample.txt", "w")
f.write("I am writting mode")
f.close#first line we open a file 2nd line doing our operation in this line we close the file

'''Here we are create a new file and add a content'''
f= open("24Sample 2.txt", "w")
f.write("This is new file")
f.close

'''Now we use here append function a in the sample2 file. we add a line on the file'''

f = open("24Sample 2.txt", "a")
f.write("This is new append line in preveous file we created by using w")
f.close

'''Now we read the file we created by using w and add a line by using a'''

f = open("24Sample 2.txt", "r")
text = f.read()
print(text)


'''using close function is annoying. we can use "with" function for solution
If we work with with funftion we do not have to close the file. we can use all the function like r, w, a in
with function'''

with open("24Sample 2.txt", "a") as f:
    f.write("we use with fuction to append another line.")

with open("24Sample 2.txt", "r") as f:
    text = f.read()
    print(text)

