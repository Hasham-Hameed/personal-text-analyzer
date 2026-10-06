# String Toolkit Analyzer

A Python script that takes a sentence and runs it through almost every common string method — case conversion, cleaning, searching, counting, and checking.

## What it does

- Converts the sentence to uppercase, lowercase, capitalized, and title case
- Strips leading/trailing whitespace
- Counts characters, words, and occurrences of the letter "a"
- Finds the first and last character
- Finds the position of the word "Python" in the sentence
- Checks if the sentence starts with "Hello" and ends with "."
- Checks if the cleaned sentence is alphanumeric
- Replaces "Python" with "programming"

## How to run

```bash
python string_toolkit_analyzer.py
```

You'll be prompted to enter a sentence.

## Example

Using the sentence: `Hello, I am learning Python.`

```
====== Personal Text Analyzer ======

Original: Hello, I am learning Python.
Uppercase: HELLO, I AM LEARNING PYTHON.
Lowercase: hello, i am learning python.
Capitalized: Hello, i am learning python.
Title: Hello, I Am Learning Python.
Cleaned: Hello, I am learning Python.

Characters: 29
First character: H
Last character: .

Words: 5
Number of a's: 2
Position of Python: 21

Starts with Hello: True
Ends with .: True
Only letters/numbers: False

After replacement: Hello, I am learning programming.
```

## Status

This is a small, growing learning project exploring Python string methods in depth. It's an expanded version of an earlier, simpler text analyzer.

Planned improvements:
- Handle empty input gracefully
- Let the user choose which word to search/replace instead of hardcoding "Python"
- Add reversed sentence and vowel/consonant count

## Author

Built while learning Python fundamentals: string methods, slicing, and boolean checks.

## Regards

Hasham Hameed