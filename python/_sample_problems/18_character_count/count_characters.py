def count_characters(word: str, char: str) -> int:
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count


word = input("Enter a string: ")
num = count_characters(word, "a")
print(f"Number of a's in {word}: {num}")
