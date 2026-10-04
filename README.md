# Personal Text Analyzer

A Python script that takes a sentence as input and demonstrates common string methods, including string immutability in Python.

## What it does

- Takes a sentence as input
- Converts it to uppercase and lowercase
- Finds its length
- Extracts the first character, last character, and first three characters
- Replaces the word "Python" with "programming" using `.replace()`
- Prints the original sentence again afterward to demonstrate that the replace did NOT change the original string, since strings are immutable in Python

## How to run

```bash
python text_analyzer.py
```

You'll be prompted to enter a sentence.

## Example

Using the sentence: `I am learning Python`

```
======= Personal Text Analyzer =======

Original: I am learning Python
Uppercase: I AM LEARNING PYTHON
Lowercase: i am learning python
Length: 21
First character: I
Last character: n
First three characters: I a
Modified: I am learning programming
Original after modification: I am learning Python
```

Notice the last two lines: `.replace()` returns a brand new string (`Modified`), while the original `sentence` variable stays untouched. This shows string immutability — strings can't be changed in place in Python.

## Status

This is a small learning project exploring Python string methods.

Planned improvements:
- Handle sentences without the word "Python" gracefully (currently `.replace()` just does nothing if it's not found, which is fine, but could print a note)
- Add word count and reversed sentence
- Add input validation for empty input

## Author

Built while learning Python fundamentals: string methods and string immutability.
