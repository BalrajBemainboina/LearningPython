f = open('DataFile', 'r')  # Opening file with read mode
f1 = open('FileCreated', 'w') # Opening File with write mode
f1.write("something ") # Write content into file
f1.writelines("Written") # Write a line into file
f1.close() # Close a file
f2 = open('FileCreated', 'a') # Open a File with append mode,
f2.write("Data Appended") # Data will be appended in file.
f2.close()
for i in f:
    print(i,end="")
f.close()
