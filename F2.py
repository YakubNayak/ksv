f=open('dict.txt','a+')
#f.write("Welcome python concepts")
print("File name:",f.name)  #  dict.txt
print("File Mode:",f.mode)   # write
print("is File readable:",f.readable())  # False
print("is File Writeable:",f.writable())  # True

print("is file is closed:",f.closed)  # False
f.close()
print("is file is closed:",f.closed)  # True
