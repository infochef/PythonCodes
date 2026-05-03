"""
File: getString.py
Author: Somnath
Date: 03-05-2026
Description: Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
"""


def main():
    sample_string = str(input("Enter the string that you want to maniupulate using program:"))
    if len(sample_string) < 2:
        return ""

    result = sample_string[:2] + sample_string[-2:]

    print(result)

    # using for loop
    li =[]
    for i in range(2):
        li.append(sample_string[i])

    for j in range(len(sample_string) - 2, len(sample_string)):
        li.append(sample_string[j])

    result = "".join(li)
    print(result)
if __name__ == '__main__':
    main()
