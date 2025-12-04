f = open('input_1.txt', 'r')
content = f.read()
dial_pos = 50
z_count = 0

for row in content.splitlines():
    direction = row[0]
    number = int(row[1:])%100

    dial_pos = (dial_pos-number)%100 if direction == "L" else (dial_pos+number)%100

    if(dial_pos == 0):
        z_count += 1

print(z_count)