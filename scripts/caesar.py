import sys

def shift_letter(c, shift):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c

def shift_text(text, shift):
    return ''.join(shift_letter(c, shift) for c in text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_text> <shift>")
        sys.exit(1)

    input_text = sys.argv[1]
    try:
        shift = int(sys.argv[2])
    except ValueError:
        print("Error: Shift must be an integer.")
        sys.exit(1)

    output_text = shift_text(input_text, shift)
    print(output_text)
