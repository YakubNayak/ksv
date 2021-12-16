# Opening a file
f= open("python.txt","r")
Counter = 0
# Reading from file
Content = f.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1      
print("This is the number of lines in the file")
print(Counter)
