# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


# Prompt for a file name
fname = input("Enter file name: ")
fileA = open(fname, "r")
try:
    unique_words = []

        # Read each line in the file
    for line in fileA:
            # Split the line into words
            words = line.split()

            # Iterate over each word in the line
            for word in words:
                # Check if the word is already in the list
                if word not in unique_words:
                    # If not, append it to the list
                    unique_words.append(word)

        # Sort the list of unique words
    unique_words.sort()

        # Print the sorted list of unique words
    print(unique_words)

except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
