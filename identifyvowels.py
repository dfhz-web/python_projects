def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_lower = word.lower()
    count = 0
    found_vowels = []

    for char in word_lower:
        if char in vowels:
            count += 1
            if char not in found_vowels:
                found_vowels.append(char)

    return count, found_vowels

word = input("Enter a word: ")
count, found_vowels = count_vowels(word)

print(f"The word '{word}' has {count} vowels.")
if count > 0:
    print(f"The vowels found in the word are: {', '.join(found_vowels)}")