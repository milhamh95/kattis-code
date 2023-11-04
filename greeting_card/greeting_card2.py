n = int(input())
points = set()
for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

count = 0
for x, y in points:
    if (x + 2018, y) in points: count += 1
    if (x - 2018, y) in points: count += 1
    if (x, y + 2018) in points: count += 1
    if (x, y - 2018) in points: count += 1
    if (x + 1680, y + 1118) in points: count += 1
    if (x - 1680, y - 1118) in points: count += 1
    if (x + 1680, y - 1118) in points: count += 1
    if (x - 1680, y + 1118) in points: count += 1
    if (x + 1118, y + 1680) in points: count += 1
    if (x - 1118, y - 1680) in points: count += 1
    if (x + 1118, y - 1680) in points: count += 1
    if (x - 1118, y + 1680) in points: count += 1

print(count // 2)