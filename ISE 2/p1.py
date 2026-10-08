import re
from collections import Counter

def analyze_text(text):
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", "").replace("\n", ""))

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    word_frequency = Counter(words)

    sentences = re.findall(r'[.!?]+', text)
    sentence_count = len(sentences)

    lines = text.splitlines()
    line_count = len(lines)

    vowels = "aeiou"
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    vowel_frequency = Counter(char for char in text.lower() if char in vowels)

    common_words = Counter(words).most_common(5)

    return {
        "Characters": characters,
        "Characters (without spaces)": characters_no_spaces,
        "Words": word_count,
        "Word frequency": word_frequency,
        "Sentences": sentence_count,
        "Lines": line_count,
        "Vowels": vowel_count,
        "Vowel frequency": vowel_frequency,
        "Most common words": common_words
    }

print("=== Simple Text Analysis Tool ===")
print("Enter your text below.")
print("Type 'END' on a new line when finished.\n")

text_lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    text_lines.append(line)

text = "\n".join(text_lines)

if text.strip():
    result = analyze_text(text)

    print("\n=== Analysis Result ===")
    print(f"Characters: {result['Characters']}")
    print(f"Characters (without spaces): {result['Characters (without spaces)']}")
    print(f"Total Words: {result['Words']}")
    print(f"Sentences: {result['Sentences']}")
    print(f"Lines: {result['Lines']}")
    print(f"Total Vowels: {result['Vowels']}")

    print("\nCount of Each Word:")
    for word, count in result["Word frequency"].items():
        print(f"{word}: {count}")

    print("\nCount of Each Vowel:")
    for vowel in "aeiou":
        print(f"{vowel}: {result['Vowel frequency'].get(vowel, 0)}")

    print("\nMost Common Words:")
    for word, count in result["Most common words"]:
        print(f"{word}: {count}")
else:
    print("No text was entered.")