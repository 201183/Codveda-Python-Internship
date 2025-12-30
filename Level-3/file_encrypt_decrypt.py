import os
SHIFT = 3
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def encrypt(text):
    return ''.join(chr(ord(c) + SHIFT) if c.isalpha() else c for c in text)

def decrypt(text):
    return ''.join(chr(ord(c) - SHIFT) if c.isalpha() else c for c in text)

choice = input("Choose operation (e = encrypt, d = decrypt): ").lower()
filename = input("Enter file name: ")
file_path = os.path.join(BASE_DIR, filename)

try:
    with open(file_path, "r") as file:
        content = file.read()

    if choice == "e":
        with open(os.path.join(BASE_DIR, "encrypted.txt"), "w") as f:
            f.write(encrypt(content))
        print(" File encrypted successfully!")

    elif choice == "d":
        with open(os.path.join(BASE_DIR, "decrypted.txt"), "w") as f:
            f.write(decrypt(content))
        print("File decrypted successfully!")

    else:
        print(" Invalid choice! Use e or d.")

except FileNotFoundError:
    print("File not found! Make sure the file is in the same folder as the script.")
