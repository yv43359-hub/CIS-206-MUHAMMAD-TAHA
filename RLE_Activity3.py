def encode_rle(user_input):
    """Encode a string using run-length encoding with escape sequences."""

    result = "#00"
    i = 0

    while i < len(user_input):
        character = user_input[i]
        count = 1

        while i + count < len(user_input) and user_input[i + count] == character:
            count += 1

        # Numbers need # so they are treated as literal characters
        if character.isdigit():
            result += "#" + character

        # # needs ## to represent a literal #
        elif character == "#":
            result += "##"

        # Letters use normal RLE
        else:
            if count == 1:
                result += character
            else:
                result += character + str(count)

        # For escaped characters, handle repeated characters
        if character.isdigit() or character == "#":
            for _ in range(count - 1):
                if character.isdigit():
                    result += "#" + character
                else:
                    result += "##"

        i += count

    return result


def decode_rle(encoded):
    """Decode an RLE string containing escape sequences."""

    if not encoded.startswith("#00"):
        return None

    encoded = encoded[3:]
    result = ""
    i = 0

    while i < len(encoded):

        # Escape sequence
        if encoded[i] == "#":
            if i + 1 >= len(encoded):
                return None

            # ## means literal #
            if encoded[i + 1] == "#":
                result += "#"
                i += 2

            # #number means literal number
            elif encoded[i + 1].isdigit():
                result += encoded[i + 1]
                i += 2

            else:
                return None

        else:
            character = encoded[i]
            i += 1

            # Read repetition count if present
            if i < len(encoded) and encoded[i].isdigit():
                count = ""

                while i < len(encoded) and encoded[i].isdigit():
                    count += encoded[i]
                    i += 1

                result += character * int(count)
            else:
                result += character

    return result


def main():
    """Run the RLE encoding and decoding program."""

    user_input = input("Enter a string: ")

    if user_input.startswith("#00"):
        result = decode_rle(user_input)

        if result is None:
            print("Invalid input.")
        else:
            print("Decoded string:", result)

    else:
        result = encode_rle(user_input)
        print("Encoded string:", result)


if __name__ == "__main__":
    main()