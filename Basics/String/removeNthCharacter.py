"""
File: removeNthCharacter.py
Author: Somnath
Date: 03-05-2026
Description: 
"""


def main(str, n):
        # Create a new string 'first_part' that includes all characters from the beginning of 'str' up to the character at index 'n' (not inclusive).
        first_part = str[:n]

        # Create a new string 'last_part' that includes all characters from the character at index 'n+1' to the end of 'str'.
        last_part = str[n + 1:]

        # Return the result by concatenating 'first_part' and 'last_part', effectively removing the character at index 'n'.
        return first_part + last_part


if __name__ == '__main__':
    print(main('Python', 0))  # Output: 'ython'
    print(main('Python', 3))  # Output: 'Pyton'
    print(main('Python', 5))  # Output: 'Pytho'
