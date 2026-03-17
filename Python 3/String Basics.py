# Count total characters in a string
text = input("Enter a string: ")
count = 0

for ch in text:
    count += 1

print("Total characters:", count)


# Count vowels in a string
text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)


#Count consonants in a string
text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants:", count)


# Reverse a string using loop
text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

print("Reversed string:", rev)


# Check if string is palindrome
text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
