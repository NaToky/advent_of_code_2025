def parts_equal(val: str, n: int) -> bool:
    if len(val) % n != 0:
        return False

    part_len = len(val) // n
    first = val[:part_len]

    for i in range(1, n):
        if val[i*part_len:(i+1)*part_len] != first:
            return False

    return True


with open("input_2.txt") as f:
    content = f.read().strip()

invalid_ids = set()

for r in content.split(","):
    r = r.strip()
    low, high = map(int, r.split("-"))

    for val in range(low, high + 1):
        s = str(val)
        if any(parts_equal(s, n) for n in range(2, len(s) + 1)):
            invalid_ids.add(val) 

print(sum(invalid_ids))
