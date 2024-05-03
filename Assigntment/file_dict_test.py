name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, "r")

listDict = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        word = words[1]
        listDict[word] = listDict.get(word, 0) + 1
        # ở đây get là lấy ra giá trị của nó và số 0 là số mặc định của nó
        
most_prolific_sender = None
most_count = None
for key, value in listDict.items():
    if most_count is None or value > most_count:
        most_prolific_sender = key
        most_count = value
        
print(f"{most_prolific_sender} {most_count}")
    
        