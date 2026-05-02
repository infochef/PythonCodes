"""
File: fetchData.py
Author: Somnath
Date: 02-05-2026
Description: Python program to create a tuple of numbers and print one item.
"""


def main():
    n = int(input("Enter the index for which the value has to be fetched:"))
    numbers = (10, 20, 30, 40, 50)

    print("Tuple:", numbers)
    print("Fetch the value from the tuple for a specified index:", numbers[n])

if __name__ == '__main__':
    main()
