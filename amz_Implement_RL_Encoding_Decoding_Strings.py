#This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.
# Solution:
def rlencode_string(words):
    encoded_chars = list()

    count = 0
    prev_char = None
    for character in words:
        if character == prev_char or not prev_char:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(prev_char)
            count = 1
        prev_char = character

    if count:
        encoded_chars.append(str(count))
        encoded_chars.append(prev_char)

    return "".join(encoded_chars)


def rldecode_string(words):

    decoded_chars = list()
    index = 0

    while index < len(words):
        decoded_chars.append(int(words[index]) * words[index + 1])
        index += 2

    return "".join(decoded_chars)


assert rlencode_string("") == ""
assert rlencode_string("AAA") == "3A"
assert rlencode_string("AAAABBBCCDAA") == "4A3B2C1D2A"

assert rldecode_string("") == ""
assert rldecode_string("3A") == "AAA"
assert rldecode_string("4A3B2C1D2A") == "AAAABBBCCDAA"
