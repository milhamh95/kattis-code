def num_to_word(num, length):
    """Converts a number to its corresponding word representation."""
    word = ''
    for _ in range(length):
        word = chr(ord('a') + num % 26) + word
        num //= 26
    return word

def generate_esej(A, B):
    """Produces an essay that meets the given constraints."""
    essay = []
    target_distinct = (A + B) // 2
    length = 1

    while len(essay) < target_distinct:
        for num in range(26 ** length):
            essay.append(num_to_word(num, length))
            if len(essay) == target_distinct:
                break
        length += 1

    return ' '.join(essay)

# Example usage
A, B = map(int, input().split())
output = generate_esej(A, B)
print(output)
