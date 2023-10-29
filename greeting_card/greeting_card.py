from sys import stdin

input = stdin.readline
def greeting_card():
    n = int(input())
    s = set()
    for i in range(n):
        (x, y) = (int(c) for c in input().split())
        s.add((x, y))
    total = 0
    for (x, y) in list(s):
        points = [
            (x + 2018, y),
            (x - 2018, y),
            (x, y + 2018),
            (x, y - 2018),
            (x + 1118, y + 1680),
            (x - 1118, y + 1680),
            (x - 1118, y - 1680),
            (x + 1118, y - 1680),
            (x + 1680, y + 1118),
            (x - 1680, y + 1118),
            (x + 1680, y - 1118),
            (x - 1680, y - 1118),
        ]
        for point in points:
            if point in s:
                total += 1
        s.remove((x, y))
    return total

print(greeting_card())

