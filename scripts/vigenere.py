import sys

def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts a Vigenère cipher given the ciphertext and keyword.
    """
    keyword = keyword.upper()
    decrypted_text = []
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
            keyword_index = (keyword_index + 1) % len(keyword)  # Cycle through keyword
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <ciphertext> <keyword>")
        sys.exit(1)

    ciphertext = sys.argv[1]
    keyword = sys.argv[2]

    decrypted = vigenere_decrypt(ciphertext, keyword)
    print("Decrypted Text:", decrypted)
