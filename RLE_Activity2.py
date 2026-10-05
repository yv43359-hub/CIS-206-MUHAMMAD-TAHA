"""
RLE Activity 2
Run-Length Encoding and Decoding

This program checks whether the input string is already
in RLE format. If it is, the program decodes it.
Otherwise, it encodes the alphabetic string.
"""


def encode_rle(text):
    """
    Encode an alphabetic string using Run-Length Encoding.

    Example:
    AAABBC -> A3B2C
    """

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1]

            if count > 1:
                result += str(count)

            count = 1

    result += text[-1]

    if count > 1:
        result += str(count)

    return result


def decode_rle(text):
    """
    Decode an RLE string.

    Example:
    A3B2C -> AAABBC
    """

    result = ""
    i = 0

    while i < len(text):
        character = text[i]
        i += 1

        count = ""

        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1

        if count:
            result += character * int(count)
        else:
            result += character

    return result


def main():
    """Run the RLE encoding and decoding program."""

    user_input = input("Enter a string: ")

    if not user_input:
        print("Invalid input. Please enter a string.")
        return

    # Check if the string contains numbers.
    if any(character.isdigit() for character in user_input):
        result = decode_rle(user_input)
        print("Decoded string:", result)
    else:
        if not user_input.isalpha():
            print("Invalid input. Please enter alphabetic characters only.")
            return

        result = encode_rle(user_input)
        print("Encoded string:", result)


if __name__ == "__main__":
    main()