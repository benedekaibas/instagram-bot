"""Palindrome"""

def palindrome(word):
    return word[::-1]


if __name__ == "__main__":
    word = "this is a word"
    print(palindrome(word))
