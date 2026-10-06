sentence = input("Enter a sentence: ")

upper_sentence = sentence.upper()

lower_sentence = sentence.lower()

capitalize_sentence = sentence.capitalize()

title_sentence = sentence.title()

cleaned_sentence = sentence.strip()

length = len(cleaned_sentence)

first_character = cleaned_sentence[0]

last_character = cleaned_sentence[-1]

number_of_words = len(cleaned_sentence.split())

a_count = cleaned_sentence.lower().count("a")

python_position = sentence.find("Python")

hello_start = sentence.startswith("Hello")

dot_end = sentence.endswith(".")

alnum_check = cleaned_sentence.isalnum()

replaced_sentence = sentence.replace("Python","programming")

print("====== Personal Text Analyzer ======")
print(" ")
print(f"Original: {sentence}")
print(f"Uppercase: {upper_sentence}")
print(f"Lowercase: {lower_sentence}")
print(f"Capitalized: {capitalize_sentence}")
print(f"Title: {title_sentence}")
print(f"Cleaned: {cleaned_sentence}")
print(" ")
print(f"Characters: {length}")
print(f"First character: {first_character}")
print(f"Last character: {last_character}")
print(" ")
print(f"Words: {number_of_words}")
print(f"Number of a's: {a_count}")
print(f"Position of Python: {python_position}")
print(" ")
print(f"Starts with Hello: {hello_start}")
print(f"Ends with .: {dot_end}")
print(f"Only letters/numbers: {alnum_check}")
print(" ")
print(f"After replacement: {replaced_sentence}")