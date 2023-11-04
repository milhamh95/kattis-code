from sys import stdin

input = stdin.readline
def greeting_card():
    n = int(input())
    s = set()
    for i in range(n):
        (x, y) = (int(c) for c in input().split())
        s.add((x, y))
    total = 0
    # https://chat.openai.com/share/8b61b941-bd4d-4c2e-bac5-5df546c4e724
    # we search endpoint with pythaogra theorem
    # 1. add / minus 2018
    # 2. diagonal using pythagoras theorem -> 2018 ^ 2 = 1118 ^ 2 + 1680 ^ 2
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

# from sys import stdin
#
# input = stdin.readline
#
# def greeting_card():
#     n = int(input())
#     s = set()
#
#     for _ in range(n):
#         x, y = map(int, input().split())
#         s.add((x, y))
#
#     total = 0
#     # Since we'll be iterating over and modifying the set, we need to work on a copy of it.
#     for (x, y) in list(s):
#         # Directly check and add the counts in the loop, reducing the need for another loop
#         total += (x + 2018, y) in s
#         total += (x - 2018, y) in s
#         total += (x, y + 2018) in s
#         total += (x, y - 2018) in s
#         total += (x + 1118, y + 1680) in s
#         total += (x + 1118, y - 1680) in s
#         total += (x - 1118, y + 1680) in s
#         total += (x - 1118, y - 1680) in s
#         total += (x + 1680, y + 1118) in s
#         total += (x + 1680, y - 1118) in s
#         total += (x - 1680, y + 1118) in s
#         total += (x - 1680, y - 1118) in s
#         s.remove((x, y))
#
#     return total
#
# print(greeting_card())

# from sys import stdin
#
# input = stdin.readline
#
# def greeting_card():
#     n = int(input())
#     s = set()
#
#     for _ in range(n):
#         x, y = map(int, input().split())
#         s.add((x, y))
#
#     total = 0
#     # Precompute the possible offsets
#     offsets = [
#         (2018, 0), (-2018, 0), (0, 2018), (0, -2018),
#         (1118, 1680), (1118, -1680), (-1118, 1680), (-1118, -1680),
#         (1680, 1118), (1680, -1118), (-1680, 1118), (-1680, -1118)
#     ]
#
#     for (x, y) in s.copy():  # Use a copy to iterate
#         for dx, dy in offsets:
#             total += (x + dx, y + dy) in s
#         s.discard((x, y))  # Use discard instead of remove
#
#     return total
#
# print(greeting_card())