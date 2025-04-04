import string

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            encrypted_char = chr(shifted)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shift = ord(key[i % key_length].lower()) - ord('a')
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            encrypted_char = chr(shifted)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shift = ord(key[i % key_length].lower()) - ord('a')
            shifted = ord(char) - shift
            if shifted < ord('a'):
                shifted += 26
            decrypted_char = chr(shifted)
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Программа для шифрования и дешифрования текста.")
    choice = input("Выберите шифр (1 - Цезарь, 2 - Виженер): ")
    if choice == '1':
        text = input("Введите текст: ")
        shift = int(input("Введите сдвиг: "))

        encrypted_text = caesar_encrypt(text, shift)
        print(f"Зашифрованный текст: {encrypted_text}")

        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print(f"Расшифрованный текст: {decrypted_text}")
    elif choice == '2':
        text = input("Введите текст: ")
        key = input("Введите ключ: ")

        encrypted_text = vigenere_encrypt(text, key)
        print(f"Зашифрованный текст: {encrypted_text}")

        decrypted_text = vigenere_decrypt(encrypted_text, key)
        print(f"Расшифрованный текст: {decrypted_text}")
    else:
        print("Неверный выбор. Выберите 1 или 2.")

if __name__ == "__main__":
    main()
