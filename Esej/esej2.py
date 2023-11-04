def increment_word(word):
    """Increments a word treating it as a number in base-26."""
    word_list = list(word)
    i = len(word_list) - 1
    while i >= 0:
        if word_list[i] != 'z':
            word_list[i] = chr(ord(word_list[i]) + 1)
            return ''.join(word_list)
        else:
            word_list[i] = 'a'
            i -= 1
    return 'a' + ''.join(word_list)


def generate_esej(A, B):
    """Produces an essay that meets the given constraints."""
    essay = set()
    max_length = 1  # Start with a word length of 1
    target_distinct = (A + B) // 2

    while len(essay) < target_distinct:
        word = 'a' * max_length
        while len(word) == max_length and len(essay) < target_distinct:
            essay.add(word)
            word = increment_word(word)
        max_length += 1  # Increase the word length if we haven't reached our target

    # Convert the set to a list and return
    return ' '.join(list(essay))


# Example usage
A, B = map(int, input().split())
output = generate_esej(A, B)
print(output)