"""Palindrome"""

def palindrome(word):
    return word[::-1]

"""
if __name__ == "__main__":
    word = "this is a word"
    print(palindrome(word))
"""

# Question 3: Write a Python program to find the largest element in a list.

def find_element(list):
    list = []

    for element in list:
        if element > element:
            print(element)
        else:
            print(list)


if __name__ == "__main__":
    find_element_list = [1,2,3,4,5]
    find_element_solution = find_element(find_element_list)
    print(find_element_solution)