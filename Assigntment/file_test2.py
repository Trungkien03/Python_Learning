# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):   
        colon_index = line.find(":")
        value = float(line[colon_index + 1:].strip())

                # Add the value to the total and increment the count
        total += value
        count += 1

if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines with 'X-DSPAM-Confidence:' found in the file.")
    fh.close()
