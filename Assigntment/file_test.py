# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

file_contents = fh.read()
print(file_contents.rstrip().upper())
