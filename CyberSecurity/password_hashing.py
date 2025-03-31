import argparse
import hashlib


def create_parser():
    """
    Creates and returns the argument parser for the program.

    Returns:
        argparse.ArgumentParser: The argument parser with predefined arguments.
    """
    parser = argparse.ArgumentParser(description='Hash the given password')
    parser.add_argument('password', help='Input password you want to hash')
    parser.add_argument('-t', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'],
                        help='The hashing algorithm to use. Choices: sha256, sha512, md5. Default is sha256.')
    return parser


def hash_password(password, hashtype):
    """
    Hashes the input password using the specified hash algorithm.

    Args:
        password (str): The password string to be hashed.
        hashtype (str): The hashing algorithm to use. Can be 'sha256', 'sha512', or 'md5'.

    Returns:
        str: The hashed password in hexadecimal format.
    """
    x = getattr(hashlib, hashtype)()  # Get the hash object (e.g., sha256, sha512, etc.)
    x.update(password.encode())  # Encode the password string to bytes and hash it
    return x.hexdigest()  # Return the hexadecimal representation of the hash


def main():
    """
    The main function that handles parsing the arguments,
    calling the hashing function, and printing the result.
    """
    parser = create_parser()
    args = parser.parse_args()

    # Extract password and hash type from the parsed arguments
    password = args.password
    hashtype = args.type

    # Get the hashed password and print the result
    hashed_password = hash_password(password, hashtype)

    # Print the result in a formatted manner
    print(f'< hash-type: {hashtype} >')
    print(hashed_password)


if __name__ == '__main__':
    main()
