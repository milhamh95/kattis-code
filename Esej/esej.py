import random
from sys import stdin

def generate_random_word(length):
    letter = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(letter) for _ in range(length))

def generate_essay(A, B):
    words_required = B
    unique_words_required = B // 2
    used_words = set()

    # Generate the unique words first
    while len(used_words) < unique_words_required:
        max_word_len = random.randint(1, 15)
        word = generate_random_word(random.randint(1, 15))
        if word not in used_words:
            used_words.add(word)

    essay_words = list(used_words)

    while len(essay_words) < words_required:
        essay_words.append(random.choice(essay_words))

    while len(essay_words) < A:
        max_word_len = random.randint(1, 15)
        word = generate_random_word(max_word_len)
        essay_words.append(word)

    return " ".join(essay_words)


input = stdin.readline
A, B = map(int, input().split())
print(generate_essay(A, B))

# import random
# from sys import stdin
#
# def generate_random_word(length=5):
#     letter = "abcdefghijklmnopqrstuvwxyz"
#     return ''.join(random.choice(letter) for _ in range(length))
#
# def generate_essay(A, B):
#     words_required = B
#     unique_words_required = B // 2
#     used_words = set()
#
#     # Generate the unique words first
#     while len(used_words) < unique_words_required:
#         word = generate_random_word(random.randint(1, 15))
#         if word not in used_words:
#             used_words.add(word)
#
#     essay_words = list(used_words)
#
#     while len(essay_words) < words_required:
#         essay_words.append(random.choice(essay_words))
#
#     while len(essay_words) < A:
#         essay_words.append(generate_random_word(random.randint(1, 15)))
#
#     return " ".join(essay_words)
#
#
# input = stdin.readline
# A, B = map(int, input().split())
# print(generate_essay(A, B))


# import random
#
# def generate_random_word(length=5):
#     """Generate a random word of the given length."""
#     letter = "abcdefghijklmnopqrstuvwxyz"
#     return ''.join(random.choice(letter) for _ in range(length))
#
# def generate_essay(A, B):
#     words_required = B
#     unique_words_required = B // 2
#     used_words = set()
#     max_word_len = random.randint(1, 15)
#
#     while len(used_words) < unique_words_required:
#         word = generate_random_word(max_word_len)
#         if word not in used_words:
#             used_words.add(word)
#
#     essay_words = list(used_words)
#
#     while len(essay_words) < words_required:
#         essay_words.append(random.choice(essay_words))
#
#     # edge case: make sure the essay has at least A words
#     while len(essay_words) < A:
#         essay_words.append(generate_random_word(max_word_len))
#
#     return " ".join(essay_words)
#
# A, B = map(int, input().split())
# print(generate_essay(A, B))
