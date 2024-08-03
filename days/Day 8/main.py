from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_to_number = {letter: number for number, letter in enumerate(alphabet)}

def caesar(start_text, shift_amount, cipher_direction):
    alphabet_length = len(alphabet)
    shift_amount = shift_amount % len(alphabet)
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            if cipher_direction == "encode":
                new_letter_index = (letter_to_number[letter] + shift_amount) % alphabet_length
            else:
                new_letter_index = (letter_to_number[letter] - shift_amount) % alphabet_length
            end_text += alphabet[new_letter_index]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")
        
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode' or direction == 'decode':
        caesar(text, shift, direction)
    else:
        print(f"{direction} is not a valid function. Please run it again and make sure to choose a valid option.")
        
    like_to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if like_to_continue != 'yes':
        should_continue = False