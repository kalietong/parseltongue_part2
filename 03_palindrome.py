
word = input("Enter the text which may be a palindrome: ").lower()

rev_word = word[::-1]

if word == rev_word:
    print("Woah, u found a palindrome!")
elif word != rev_word:
    print("not a palindrome")
