from sys import stdin

input = stdin.readline
totalWords = int(input())
words = set()
last_letter = ''
player = 1
result = "Fair Game"

for _ in range(totalWords):
    word = input()
    if word in words:
        result = f"Player {player} lost"
        break

    if last_letter == '':
        last_letter = word[-2]
    elif word[0] != last_letter:
        result = f"Player {player} lost"
        break

    words.add(word)
    last_letter = word[-2]
    player = 2 if player == 1 else 1

print(result)