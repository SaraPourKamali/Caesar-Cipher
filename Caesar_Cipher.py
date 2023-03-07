alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(txt, shft):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    cipher_position = position + shift
    if cipher_position > 26:
      cipher_position -= 26
    cipher_letter = alphabet[cipher_position]
    cipher_text += cipher_letter
  
  print(f"The encoded text is {cipher_text}")
if direction == "encode":
    encrypt(txt = text, shft = shift)