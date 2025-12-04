f = open('input_2.txt', 'r')
content = f.read()

total = 0

for r in content.split(","):
    min = int(r.split("-")[0])
    max = int(r.split("-")[1])

    for val in range(min,max):
        if(str(val)[0:len(str(val))//2] == str(val)[len(str(val))//2:len(str(val))]):
            total += val

print(total)