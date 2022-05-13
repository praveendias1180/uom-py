fhandle = open("myfile.txt")
fcontents = fhandle.readline()
print(fcontents)
fhandle.close()

fhandle = open("myfile.txt", "w")
mystring = "This is how \n files are written"
fhandle.write(mystring)
fhandle.close()
