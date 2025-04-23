from collections import Counter


def count_words(text: str) -> int:
    return len(text.split())


def count_letters(text: str) -> Counter:
    return Counter(text)


def print_letter_counts(letter_counts: Counter):
    for letter, count in letter_counts.most_common():
        if letter.isalpha():
            print(f"{letter}: {count}")
