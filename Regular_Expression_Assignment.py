
import re

# Question 1: Check whether a string contains only a-z, A-Z, and 0-9
print("\nQuestion 1")
tests = ["ABCDEFabcdef123450", "*&%@#!}{"]

for text in tests:
    if re.fullmatch(r"[a-zA-Z0-9]+", text):
        print(text, "- Valid")
    else:
        print(text, "- Invalid")


# Question 2: Match a followed by zero or more b's
print("\nQuestion 2")
tests = ["ab", "abc", "a", "ab", "abb"]

for text in tests:
    print(text, bool(re.match(r"ab*", text)))


# Question 3: Match a followed by one or more b's
print("\nQuestion 3")
tests = ["ab", "abc", "a", "ab", "abb"]

for text in tests:
    print(text, bool(re.match(r"ab+", text)))


# Question 4: Find lowercase letters joined by an underscore
print("\nQuestion 4")
tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]

for text in tests:
    print(text, re.findall(r"[a-z]+_[a-z]+", text))


# Question 5: Match a word at the beginning of a string
print("\nQuestion 5")
tests = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]

for text in tests:
    result = re.match(r"\w+", text)
    print(result.group() if result else "No match")


# Question 6: Find words containing the letter z
print("\nQuestion 6")
tests = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."
]

for text in tests:
    print(re.findall(r"\b\w*z\w*\b", text))


# Question 7: Remove leading zeros from an IP address
print("\nQuestion 7")
ip = "216.08.094.196"

new_ip = re.sub(r"\b0+(\d)", r"\1", ip)
print(new_ip)


# Question 8: Search for literal strings within a string
print("\nQuestion 8")
text = "The quick brown fox jumps over the lazy dog."
words = ["fox", "dog", "horse"]

for word in words:
    if re.search(re.escape(word), text):
        print(word, "- Found")
    else:
        print(word, "- Not found")


# Question 9: Search for a literal string and find its position
print("\nQuestion 9")
text = "The quick brown fox jumps over the lazy dog."
word = "fox"

result = re.search(re.escape(word), text)

if result:
    print("Found:", word)
    print("Position:", result.start())
else:
    print("Not found")


# Question 10: Replace whitespaces with underscores
# and underscores with whitespaces
print("\nQuestion 10")

text1 = "Regular Expressions"
text2 = "Code_Examples"

print(re.sub(r"\s", "_", text1))
print(re.sub(r"_", " ", text2))


# Question 11: Extract year, month, and date from a URL
print("\nQuestion 11")
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

result = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)

if result:
    print("Year:", result.group(1))
    print("Month:", result.group(2))
    print("Date:", result.group(3))


# Question 12: Find all words starting with a or e
print("\nQuestion 12")
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

print(re.findall(r"\b[ae]\w*", text, re.IGNORECASE))


# Question 13: Replace spaces, commas, and dots with colons
print("\nQuestion 13")
text = "Python Exercises, PHP exercises."

new_text = re.sub(r"[ ,.]", ":", text)
print(new_text)


# Question 14: Find all words starting with a or e
print("\nQuestion 14")
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

print(re.findall(r"\b[ae]\w*", text, re.IGNORECASE))


# Question 15: Remove multiple spaces from a string
print("\nQuestion 15")
text = "Python    Exercises"

new_text = re.sub(r"\s+", " ", text)
print(new_text)
