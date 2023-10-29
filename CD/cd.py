from sys import stdin

cds = stdin.readline().split()
jackcds = int(cds[0])
jillcds = int(cds[1])

jackcdsset = set()
for _ in range(jackcds):
    jackcdsset.add(int(stdin.readline()))

jillcdsset = set()
for _ in range(jillcds):
    jillcdsset.add(int(stdin.readline()))

counter = 0
for num in jackcdsset:
    if num in jillcdsset:
        counter += 1

print(counter)