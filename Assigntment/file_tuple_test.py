name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, "r")

hour_count = {}

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hour_count[hour] = hour_count.get(hour, 0) + 1
        
for hour, countHour in sorted(hour_count.items()):
    print(f"{hour} {countHour}")
