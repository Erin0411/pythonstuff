print('Made by Erin, sources: decoders / encoders online, and google. \n\nNo other code was used from the internet or was ai generated\n(because ai is more efficient at coding than me 😎😎)\n\nMade in Virtual Studio code which helped much better since it showed what the error was instead of saying "bad input"\n')
from dataclasses import asdict
from os import error
from time import sleep,time

print('HEXADECIMAL AND BINARY IS BEING ADDED LATER!!')

choice = ''
while choice.lower() != 'morse' or choice.lower() != 'hexadecimal' or choice.lower() != 'binary':
    choice = input('Choose what to decode (morse, hexadecimal, binary.)\nType "Help" for help\nNot case sensitive. DO NOT MISSPELL ANYTHING.\n\nEncoding type, if you dont know, type "Help" for help:')

if choice.lower == 'help':
    print('Command List:\nExample to show the example of the code working\nHelp to show help (youre here arent you)\nMorse to decode morse code AND ONLY DECODE\n(i havent added encoding to this)')


if choice == 'morse':
    encoded = input('Paste the encoded text. \nDecoding may take some time because of me being bad at coding.\nEncoded Text: ')
    decoded = encoded
    # here we go...
    
    #Special Charachters / punctuation (this would be nothing without it.) except percentages at last!
    
    decoded = decoded.replace('.-.-.-', '[dot]')
    decoded = decoded.replace('-....-', '[dash]')
    decoded = decoded.replace('--..--', ',')
    decoded = decoded.replace('-.-.--', '!')
    decoded = decoded.replace('.--.-.', '@')
    decoded = decoded.replace('.-...', '&')
    decoded = decoded.replace('-.--.-', ')')
    decoded = decoded.replace('-.--.', '(')
    decoded = decoded.replace('.-.-.', '+')
    decoded = decoded.replace('-...-', '=')
    decoded = decoded.replace('..--..', '?')
    decoded = decoded.replace('-..-.', '/')
    decoded = decoded.replace('---...', ':')
    decoded = decoded.replace('.----.', "'")


    #LETTERS AFTER PUNCTUATION / CHARAHCTERS. IT COULD BREAK MESSAGE MAYBE I DON'T KNOW.
    
    decoded = decoded.replace('-...', 'b')
    decoded = decoded.replace('-.-.', 'c')
    decoded = decoded.replace('..-.', 'f')
    decoded = decoded.replace('....', 'h')
    decoded = decoded.replace('.---', 'j')
    decoded = decoded.replace('---', 'o')
    decoded = decoded.replace('.-..', 'l')
    decoded = decoded.replace('.-.', 'r')
    decoded = decoded.replace('.--.', 'p')
    decoded = decoded.replace('--.-', 'q')
    decoded = decoded.replace('...-', 'v')
    decoded = decoded.replace('...', 's')
    decoded = decoded.replace('-..-', 'x')
    decoded = decoded.replace('-.--', 'y')
    decoded = decoded.replace('-.-', 'k')
    decoded = decoded.replace('.--', 'w')
    decoded = decoded.replace('--..', 'z')
    decoded = decoded.replace('-..', 'd')
    decoded = decoded.replace('--.', 'g')
    decoded = decoded.replace('-.', 'n')
    decoded = decoded.replace('..-', 'u')
    decoded = decoded.replace('--', 'm')
    decoded = decoded.replace('..', 'i')
    decoded = decoded.replace('.-', 'a')
    pass1 = decoded
    
    decoded = decoded.replace('-', 't')
    decoded = decoded.replace('.', 'e')
    
    #chars that break code

    #numbers :D
    
    decoded = decoded.replace('.----', "1")
    decoded = decoded.replace('..---', "2")
    decoded = decoded.replace('...--', "3")
    decoded = decoded.replace('....-', "4")
    decoded = decoded.replace('.....', "5")
    decoded = decoded.replace('-....', "6")
    decoded = decoded.replace('--...', "7")
    decoded = decoded.replace('---..', "8")
    decoded = decoded.replace('----.', "9")
    decoded = decoded.replace('----', "0")
    
    #fix the dot dash thing
    decoded = decoded.replace('[dot]', ".")
    decoded = decoded.replace('[dash]', "-")

    #remove and fix spaces

    decoded = decoded.replace('/', ' ')
    decoded = decoded.replace('  ', '/')
    decoded = decoded.replace(' ', '')
    print('\n''Decoded message:', decoded)
            

if choice.lower() == 'example':
    encoded = '.-- --- .-- / - .... .. ... / .. ... / .- / .-.. --- -. --. / ... - .-. .. -. --. / .... . .-. . ... / .- -. / . -..- .- -- .--. .-.. . / --- ..-. / - .... . / .- .-.. .--. .... .- -... . - / .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. / ... -.-- -- -... --- .-.. ... / .- .-. . -. - / .- -.. -.. . -.. / -.-- . - / .- -. -.. / ..- .... / --. --- --- -.. -... -.-- .'
    decoded = encoded
    print('The example thats going to be printed', decoded)
    liveprint = input('Do you want to see the decoder decoding live?\n [if youre on the platform then choose NO because it will fill the output]\n(yes / no)')
    if liveprint.lower() == 'yes' or liveprint.lower() == 'y':
        decoded = decoded.replace('-...', 'b')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-.-.', 'c')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('..-.', 'f')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('....', 'h')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.---', 'j')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('---', 'o')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.-..', 'l')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.-.', 'r')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.--.', 'p')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('--.-', 'q')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('...-', 'v')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('...', 's')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-..-', 'x')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-.--', 'y')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-.-', 'k')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.--', 'w')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('--..', 'z')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-..', 'd')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('--.', 'g')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-.', 'n')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('..-', 'u')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('--', 'm')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('..', 'i')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.-', 'a')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('-', 't')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('.', 'e')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace(' ', '')
        print('Progress on decoding:\n', decoded)
        decoded = decoded.replace('/', ' ')
        print('Progress on decoding:\n', decoded)
    else:
        decoded = decoded.replace('-...', 'b')
        decoded = decoded.replace('-.-.', 'c')
        decoded = decoded.replace('..-.', 'f')
        decoded = decoded.replace('....', 'h')
        decoded = decoded.replace('.---', 'j')
        decoded = decoded.replace('---', 'o')
        decoded = decoded.replace('.-..', 'l')
        decoded = decoded.replace('.-.', 'r')
        decoded = decoded.replace('.--.', 'p')
        decoded = decoded.replace('--.-', 'q')
        decoded = decoded.replace('...-', 'v')
        decoded = decoded.replace('...', 's')
        decoded = decoded.replace('-..-', 'x')
        decoded = decoded.replace('-.--', 'y')
        decoded = decoded.replace('-.-', 'k')
        decoded = decoded.replace('.--', 'w')
        decoded = decoded.replace('--..', 'z')
        decoded = decoded.replace('-..', 'd')
        decoded = decoded.replace('--.', 'g')
        decoded = decoded.replace('-.', 'n')
        decoded = decoded.replace('..-', 'u')
        decoded = decoded.replace('--', 'm')
        decoded = decoded.replace('..', 'i')
        decoded = decoded.replace('.-', 'a')
        decoded = decoded.replace('-', 't')
        decoded = decoded.replace('.', 'e')
        decoded = decoded.replace(' ', '')
        decoded = decoded.replace('/', ' ')
    print('\n''Decoded message:', decoded)

if choice == 'debug':
    encodedtype= input('What type of encoding do you want to debug?\n')
    if encodedtype == 'morse':
        encoded = input('Paste the encoded text. \nDecoding may take some time because of me being bad at coding.\nEncoded Text: ')
        decoded = encoded
        decodedinput = input('Decoded text: ')
        decoded = decoded.replace('.-.-.-', '.')
        decoded = decoded.replace('-....-', '-')
        decoded = decoded.replace('--..--', ',')
        decoded = decoded.replace('-.-.--', '!')
        decoded = decoded.replace('.--.-.', '@')
        decoded = decoded.replace('.-...', '&')
        decoded = decoded.replace('-.--.-', ')')
        decoded = decoded.replace('-.--.', '(')
        decoded = decoded.replace('.-.-.', '+')
        decoded = decoded.replace('-...-', '=')
        decoded = decoded.replace('..--..', '?')
        decoded = decoded.replace('-..-.', '/')
        decoded = decoded.replace('---...', ':')
        decoded = decoded.replace('.----.', "'")
        #numbers :D
        decoded = decoded.replace('.----', "1")
        decoded = decoded.replace('..---', "2")
        decoded = decoded.replace('...--', "3")
        decoded = decoded.replace('....-', "4")
        decoded = decoded.replace('.....', "5")
        decoded = decoded.replace('-....', "6")
        decoded = decoded.replace('--...', "7")
        decoded = decoded.replace('---..', "8")
        decoded = decoded.replace('----.', "9")
        decoded = decoded.replace('----', "0")

        #LETTERS AFTER PUNCTUATION / CHARAHCTERS. IT COULD BREAK MESSAGE MAYBE I DON'T KNOW.
        decoded = decoded.replace('-...', 'b')
        decoded = decoded.replace('-.-.', 'c')
        decoded = decoded.replace('..-.', 'f')
        decoded = decoded.replace('....', 'h')
        decoded = decoded.replace('.---', 'j')
        decoded = decoded.replace('---', 'o')
        decoded = decoded.replace('.-..', 'l')
        decoded = decoded.replace('.-.', 'r')
        decoded = decoded.replace('.--.', 'p')
        decoded = decoded.replace('--.-', 'q')
        decoded = decoded.replace('...-', 'v')
        decoded = decoded.replace('...', 's')
        decoded = decoded.replace('-..-', 'x')
        decoded = decoded.replace('-.--', 'y')
        decoded = decoded.replace('-.-', 'k')
        decoded = decoded.replace('.--', 'w')
        decoded = decoded.replace('--..', 'z')
        decoded = decoded.replace('-..', 'd')
        decoded = decoded.replace('--.', 'g')
        decoded = decoded.replace('-.', 'n')
        decoded = decoded.replace('..-', 'u')
        decoded = decoded.replace('--', 'm')
        decoded = decoded.replace('..', 'i')
        decoded = decoded.replace('.-', 'a')
        decoded = decoded.replace('-', 't')
        decoded = decoded.replace('.', 'e')
        
        decoded = decoded.replace('/', ' ')
        decoded = decoded.replace('  ', '/')
        decoded = decoded.replace(' ', '')

        print('\n''Decoded message:', decoded)
        print('Real decoded text:', decodedinput)
        if decoded == decodedinput:
            print('YEAH YOU FIXED IT!! NOW GO COPY THE CODE.')
        else:
            print('you didnt fix it.')