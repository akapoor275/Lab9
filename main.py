def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)  # Shift each digit down by 3 numbers
        decoded_password += decoded_digit
    return decoded_password
def encode(password):
    encoded_list = []
    for char in password:
        encoded_char = chr(ord(char) + 3)
        encoded_list.append(encoded_char)
    return ''.join(encoded_list)


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    user_input = input("Please enter an option: ")
    if user_input == "1":
        password = input("Please enter you password to encode: ")
        encoded_password = encode(password)
        # print("Encoded password:", encoded_password)
        print("Your password has been encoded and stored")
    elif user_input == "2":
                 encoded_password = input("Please enter your password to decode: ")
                 decoded_password = decode(encoded_password)
                 print("Your password has been decoded!")
                 print("Decoded password:", decoded_password)
    elif user_input == "3":
                 print("Exiting the program.")
                 break
    else:
                 print("Invalid option. Please enter a valid option (1, 2, or 3).")


