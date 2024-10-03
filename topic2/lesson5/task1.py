vowels = ["a", "e", "i", "o", "u", "y"]

input_string = input()
vowels_count = 0
novowels_count = 0
vowels_set = set()

for char in input_string:
    if char in vowels:
        vowels_set.add(char)
        vowels_count+=1
    else:
        novowels_count+=1
print(f"Vowels: {vowels_count} Consonants: {novowels_count}")
if len(vowels_set) != len(vowels):
    print(False)
