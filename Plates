def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Tiene un max de 6 y min de 2
    if len(s) < 2 or len(s) > 6:
        return False

    # Must be 2 characters letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Number cannot be used in the middle of the plate
    # AAA222 is good while AAA22A is not
    # First number cannot be 0
    p = 0
    while p < len(s):
        if not s[p].isalpha():
            if s[p] == '0':
                return False
            else:
                break
        p += 1

    while p < len(s):
        if s[p].isalpha():
            return False
        p += 1

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # If all pass
    return True

if __name__ == "__main__":
    main()
