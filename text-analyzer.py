sentence = input("Enter a sentence: ")

upper_sentence = sentence.upper()

lower_sentence = sentence.lower()

length_sentence = len(sentence)

first_character = sentence[0]

last_character = sentence[-1]

first_three_characters = sentence[0:3]

new_sentence = sentence.replace("Python","programming")

print("======= Personal Text Analyzer =======")
print(" ")
print(f"Original: {sentence}")
print(f"Uppercase: {upper_sentence}")
print(f"Lowercase: {lower_sentence}")
print(f"Length: {length_sentence}")
print(f"First character: {first_character}")
print(f"Last character: {last_character}")
print(f"First three characters: {first_three_characters}")
print(f"Modified: {new_sentence}")
print(f"Original after modification: {sentence}")