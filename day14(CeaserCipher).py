alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text =  input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original, shift_amount):
    cipher_text = ""
    for i in original:
        shifted_position = (alphabet.index(i) + shift_amount) % 25
        cipher_text += alphabet[shifted_position]
    
    print(cipher_text)


encrypt(text, shift)