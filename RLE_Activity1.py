"""
RLE Activity 1
Run-Length Encoding

This program asks the user for an alphabetic string and
converts it into Run-Length Encoding (RLE).

Example:
AAABBC -> A3B2C
"""

def encode_rle(text):
    """
    Convert an alphabetic string into Run-Length Encoding.

    A character that appears only once is displayed without
    a count.

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

    # Add the final character
    result += text[-1]

    if count > 1:
        result += str(count)

    return result


def main():
    """Run the RLE encoding program."""

    user_input = input("Enter an alphabetic string: ")

    # Validate the input
    if not user_input.isalpha():
        print("Invalid input. Please enter alphabetic characters only.")
        return

    encoded = encode_rle(user_input)

    print("Encoded string:", encoded)


if __name__ == "__main__":
    main()