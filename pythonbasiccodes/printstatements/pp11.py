"""**Printing Variables and Constants:**
    - Create a program that prints the value of a variable and a constant.

"""
name = input()

vowel_count = 0
consonant_count = 0

print("Vowels:")
for ch in name:
    if ch.lower() in "aeiou":
        print(ch)
        vowel_count += 1

print("Consonants:")
for ch in name:
    if ch.isalpha() and ch.lower() not in "aeiou":
        print(ch)
        consonant_count += 1

print("Total vowels:", vowel_count)
print("Total consonants:", consonant_count)