
import string
def remove_punctuations(word):
    return "".join(i.lower() for i in word if i not in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = remove_punctuations(text)
    return text == reverse(text)

something = input("Enter the text which may be a palindrome: ")

if (is_palindrome(something)):
    print("Woah, u found a palindrome!")
else:
    print("not a palindrome")
