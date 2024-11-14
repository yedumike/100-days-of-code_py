alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("""
 .o88b. d88888b  .d8b.  .d8888. d88888b d8888b.     
d8P  Y8 88'     d8' `8b 88'  YP 88'     88  `8D   
8P      88ooooo 88ooo88 `8bo.   88ooooo 88oobY'    
8b      88ooooo 88ooo88   `Y8b. 88ooooo 88`8b      
Y8b  d8 88.     88   88 db   8D 88.     88 `88.    
 `Y88P' Y88888P YP   YP `8888Y' Y88888P 88   YD    

 .o88b. d888888b d8888b. db   db d88888b d8888b.
d8P  Y8   `88'   88  `8D 88   88 88'     88  `8D
8P         88    88oodD' 8888888 88ooooo 88oobY'
8b         88    88~~~   8888888 88ooooo 88`8b
Y8b  d8   .88.   88      88   88 88.     88 `88.
 `Y88P' Y888888P 88      YP   YP Y88888P 88   YD
                                                                                                   """)
direction = input("Type'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text =  input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original, shift_amount):
#     cipher_text = ""
#     for i in original:
#         shifted_position = (alphabet.index(i) + shift_amount) % 25
#         cipher_text += alphabet[shifted_position]
    
#     print(cipher_text)

# def decrypt(ciphertext, shift_amount):
#     decoded = ""
#     for i in ciphertext:
#         shifted_position = alphabet.index(i) - shift_amount 
#         decoded += alphabet[shifted_position]
    
#     print(decoded)


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Enter correct input!!!")



############ <<<<<<< OR >>>>>>> ###################

def ceaser(text, shift_amount, encode_or_decode):
    output_text =""
    if encode_or_decode != "encode" or encode_or_decode != "decode":
         print("Enter a valid option!")
         return
    if encode_or_decode == "decode":
            shift_amount *= -1
    
    for letter in text:
        if letter not in alphabet:
             output_text += letter 
        else:
            print(shift_amount)
            shifted_position = (alphabet.index(letter) + shift_amount) % 25
            output_text += alphabet[shifted_position]
    print("Here is your encoded result" if encode_or_decode == "encode" else "Here is your decoded result",output_text)
        

ceaser(text,shift,direction)