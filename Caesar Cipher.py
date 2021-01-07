import pyperclip
print("---------------------------------------------------------------------------\n")

message = input("Enter a message you want to encrypt or decrypt: ")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'


print("---------------------------------------------------------------------------\n")

mode = input("'Encrypt' or 'Decrypt' you can only choose one: ")

print("---------------------------------------------------------------------------\n")

key = int(input("Enter an encyption key for your message: "))

translated = ""
## to loop around all the characters in the message
for symbol in message:
    ##to check if the symbol is in the set of symbols
    if symbol in SYMBOLS:
        # to keep track of the symbol's index
        translated_index = SYMBOLS.find(symbol)
        # to check what mode the user enters
        if mode == "encrypt":
            translated_index += key
        elif mode == "decrypt":
            translated_index -= key
        # to handle wrap around
        if translated_index >= len(SYMBOLS):
            translated_index -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)

        # to add the symbol to the translated message
        translated += SYMBOLS[translated_index]
        
      
    else:
        translated += symbol


print("\n\nHere is your " + str(mode) + "ed message:")
print("---------------------------------------------------------------------------\n")
print(translated)
pyperclip.copy(translated)
