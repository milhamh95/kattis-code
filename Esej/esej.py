import random
from sys import stdin

input = stdin.readline



min_words, max_words = map(int, input().split())
print(generate_essay(min_words, max_words))
