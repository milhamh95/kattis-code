from sys import stdin

# Solution 4
input = stdin.readline
counter = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    jack = {int(input()) for _ in range(n)}
    jill = {int(input()) for _ in range(m)}
    print(len(jack.intersection(jill)))

# Solution 3
# input = stdin.readline
# counter = 0
# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break
#
#     jack = {int(input()) for _ in range(n)}
#     counter = sum(1 for _ in range(m) if int(input()) in jack)
#     print(counter)

# Solution 2
# Time complexity -> O(n)
# Space complexity -> O(n)
# input = stdin.readline
# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break
#
#     jackcdsset = set()
#     for _ in range(n):
#         jackcdsset.add(int(input()))
#
    # counter = 0
    # for _ in range(m):
    #     cd = int(input())
    #     if cd in jackcdsset:
    #         counter += 1
#
#     print(counter)

# Solution 1
# Time complexity -> O(n)
# Space complexity -> O(n)
# cds = stdin.readline().split()
# jackcds = int(cds[0])
# jillcds = int(cds[1])
#
# jackcdsset = set()
# for _ in range(jackcds):
#     jackcdsset.add(int(stdin.readline()))
#
# jillcdsset = set()
# for _ in range(jillcds):
#     jillcdsset.add(int(stdin.readline()))
#
# counter = 0
# for num in jackcdsset:
#     if num in jillcdsset:
#         counter += 1
#
# print(counter)