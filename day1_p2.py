f = open('input_1.txt', 'r')
content = f.read()

dial_pos = 50
z_count = 0

for row in content.splitlines():
    direction = row[0]
    number = int(row[1:])

    step = 1 if direction == "R" else -1

    for _ in range(1, number + 1):
        dial_pos += step
        dial_pos %= 100
        z_count += dial_pos == 0

print(z_count)
