print('Made by Erin, sources: decoders / encoders online, and google. \n\nNo other code was used from the internet or was ai generated\n(because ai is more efficient at coding than me B) )\n\nthis isnt meant to be used as a proper decoder i reccomend using online ones since they may be more accurate\nand theres like also much better decoders you can find on github so thats epic :D\n\n')

choice = ''
while choice.lower() != 'exit':
    choice = input('Choose what to decode\nType "Help" for help\n\nEncoding type, if you dont know, type "Help" for help, Type "Exit" to well, exit.: ')
    if choice.lower == 'help':
        print('Command List:\nExample to show the example of the code working\nHelp to show help (youre here arent you)\nMorse to decode morse code AND ONLY DECODE\n(i havent added encoding to this)')

    if choice.lower() == 'morse':
        encoded = input('\nPaste the encoded text. \nDecoding may take some time because of me being bad at coding.\nEncoded Text: ')
        decoded = encoded
        #Special Charachters / punctuation (this would be nothing without it)
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
        decoded = decoded.replace('-..-.', '[slash]')
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
        
        #letters
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
        #fix the dot dash thing
        decoded = decoded.replace('[dot]', ".")
        decoded = decoded.replace('[dash]', "-")

        #percentages
        decoded = decoded.replace('0/0', '%')
        #remove and fix spaces

        decoded = decoded.replace(' ', '')
        decoded = decoded.replace('[slash]', '/')
        decoded = decoded.replace('/', ' ')
        print('\n''Decoded message:', decoded, '\n\n\n\n\n\n\n\n')

    #hexadecimal
    if choice == 'hex':
        print('Work in progress.\n(in other words this does not work at all until this thingy is removed 😨)\n')
        #lucklily these cant glitch since its all speperated by spaces and unique so erm yeah
        encoded = input('\nPaste the encoded text. \nDecoding may take some time because of me being bad at coding.\nEncoded Text: ')
        decoded = encoded.upper
        #im not adding ".upper()" to every single line here sorry not sorry

        #letters
        # (letters lowercase)
        decoded = decoded.replace('61', 'a')
        decoded = decoded.replace('62', 'b')
        decoded = decoded.replace('63', 'c')
        decoded = decoded.replace('64', 'd')
        decoded = decoded.replace('65', 'e')
        decoded = decoded.replace('66', 'f')
        decoded = decoded.replace('67', 'g')
        decoded = decoded.replace('68', 'h')
        decoded = decoded.replace('69', 'i')
        decoded = decoded.replace('6A', 'j')
        decoded = decoded.replace('6B', 'k')
        decoded = decoded.replace('6C', 'l')
        decoded = decoded.replace('6D', 'm')
        decoded = decoded.replace('6E', 'n')
        decoded = decoded.replace('6F', 'o')
        decoded = decoded.replace('70', 'p')
        decoded = decoded.replace('71', 'q')
        decoded = decoded.replace('72', 'r')
        decoded = decoded.replace('73', 's')
        decoded = decoded.replace('74', 't')
        decoded = decoded.replace('75', 'u')
        decoded = decoded.replace('76', 'v')
        decoded = decoded.replace('77', 'w')
        decoded = decoded.replace('78', 'x')
        decoded = decoded.replace('79', 'y')
        decoded = decoded.replace('7A', 'z')

        #LETTERS
        # (letters uppercase)
        decoded = decoded.replace('41', 'A')
        decoded = decoded.replace('42', 'B')
        decoded = decoded.replace('43', 'C')
        decoded = decoded.replace('44', 'D')
        decoded = decoded.replace('45', 'E')
        decoded = decoded.replace('46', 'F')
        decoded = decoded.replace('47', 'G')
        decoded = decoded.replace('48', 'H')
        decoded = decoded.replace('49', 'I')
        decoded = decoded.replace('4A', 'J')
        decoded = decoded.replace('4B', 'K')
        decoded = decoded.replace('4C', 'L')
        decoded = decoded.replace('4D', 'M')
        decoded = decoded.replace('4E', 'N')
        decoded = decoded.replace('4F', 'O')
        decoded = decoded.replace('50', 'P')
        decoded = decoded.replace('51', 'Q')
        decoded = decoded.replace('52', 'R')
        decoded = decoded.replace('53', 'S')
        decoded = decoded.replace('54', 'T')
        decoded = decoded.replace('55', 'U')
        decoded = decoded.replace('56', 'V')
        decoded = decoded.replace('57', 'W')
        decoded = decoded.replace('58', 'X')
        decoded = decoded.replace('59', 'Y')
        decoded = decoded.replace('5A', 'Z')

        #symbols
        decoded = decoded.replace('21', '!')
        decoded = decoded.replace('40', '@')
        decoded = decoded.replace('23', '#')
        decoded = decoded.replace('24', '$')
        decoded = decoded.replace('25', '%')
        decoded = decoded.replace('5E', '^')
        decoded = decoded.replace('26', '%')
        decoded = decoded.replace('2A', '*')
        decoded = decoded.replace('28', '(')
        decoded = decoded.replace('29', ')')
        decoded = decoded.replace('2D', '-')
        decoded = decoded.replace('5F', '_')
        decoded = decoded.replace('3D', '=')
        decoded = decoded.replace('2B', '+')
        decoded = decoded.replace('5B', '[')
        decoded = decoded.replace('5D', ']')
        decoded = decoded.replace('7B', '{')
        decoded = decoded.replace('7D', '}')
        decoded = decoded.replace('3B', ';')
        decoded = decoded.replace('3A', ':')
        decoded = decoded.replace('27', "'")
        decoded = decoded.replace('22', '"')
        decoded = decoded.replace('5C', '\\')
        decoded = decoded.replace('7C', '|')
        decoded = decoded.replace('3C', '<')
        decoded = decoded.replace('3E', '>')
        decoded = decoded.replace('2C', ',')
        decoded = decoded.replace('2E', '.')
        decoded = decoded.replace('2F', '/')
        decoded = decoded.replace('3F', '?')
        
        #nums
        decoded = decoded.replace('30', '0')
        decoded = decoded.replace('31', '1')
        decoded = decoded.replace('32', '2')
        decoded = decoded.replace('33', '3')
        decoded = decoded.replace('34', '4')
        decoded = decoded.replace('35', '5')
        decoded = decoded.replace('36', '6')
        decoded = decoded.replace('37', '7')
        decoded = decoded.replace('38', '8')
        decoded = decoded.replace('39', '9')

        #spaces
        decoded = decoded.replace(' ', '')
        decoded = decoded.replace('20', ' ')
        
        print('Decoded!')
        print('Decoded text:', decoded)

    #example!
    if choice.lower() == 'example':
        encoded = '.-- --- .-- / - .... .. ... / .. ... / .- / .-.. --- -. --. / ... - .-. .. -. --. / .... . .-. . ... / .- -. / . -..- .- -- .--. .-.. . / --- ..-. / - .... . / .- .-.. .--. .... .- -... . - / .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. / ... -.-- -- -... --- .-.. ... / .- .-. . -. - / .- -.. -.. . -.. / -.-- . - / .- -. -.. / ..- .... / --. --- --- -.. -... -.-- .'
        decoded = encoded
        print('The example thats going to be printed', decoded)
        print("Hexadecimal and Binary will be added later.")
        
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


    #debugging!
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
        
        if encodedtype == 'hex':
            decoded = '61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 54 55 56 57 58 59 5a 21 40 23 24 25 5e 26 2a 28 29 5f 2b 5b 5d 7b 7d 3b 3a 27 22 5c 7c 2c 2e 3c 3e 2f 3f'
            decoded = decoded.upper()
            print('DECODING:', decoded)
            
            decoded = decoded.replace('61', 'a')
            decoded = decoded.replace('62', 'b')
            decoded = decoded.replace('63', 'c')
            decoded = decoded.replace('64', 'd')
            decoded = decoded.replace('65', 'e')
            decoded = decoded.replace('66', 'f')
            decoded = decoded.replace('67', 'g')
            decoded = decoded.replace('68', 'h')
            decoded = decoded.replace('69', 'i')
            decoded = decoded.replace('6A', 'j')
            decoded = decoded.replace('6B', 'k')
            decoded = decoded.replace('6C', 'l')
            decoded = decoded.replace('6D', 'm')
            decoded = decoded.replace('6E', 'n')
            decoded = decoded.replace('6F', 'o')
            decoded = decoded.replace('70', 'p')
            decoded = decoded.replace('71', 'q')
            decoded = decoded.replace('72', 'r')
            decoded = decoded.replace('73', 's')
            decoded = decoded.replace('74', 't')
            decoded = decoded.replace('75', 'u')
            decoded = decoded.replace('76', 'v')
            decoded = decoded.replace('77', 'w')
            decoded = decoded.replace('78', 'x')
            decoded = decoded.replace('79', 'y')
            decoded = decoded.replace('7A', 'z')
            print('\n', decoded, '\n\n\n\n\n\n\n\n')

            #LETTERS
            decoded = decoded.replace('41', 'A')
            decoded = decoded.replace('42', 'B')
            decoded = decoded.replace('43', 'C')
            decoded = decoded.replace('44', 'D')
            decoded = decoded.replace('45', 'E')
            decoded = decoded.replace('46', 'F')
            decoded = decoded.replace('47', 'G')
            decoded = decoded.replace('48', 'H')
            decoded = decoded.replace('49', 'I')
            decoded = decoded.replace('4A', 'J')
            decoded = decoded.replace('4B', 'K')
            decoded = decoded.replace('4C', 'L')
            decoded = decoded.replace('4D', 'M')
            decoded = decoded.replace('4E', 'N')
            decoded = decoded.replace('4F', 'O')
            decoded = decoded.replace('50', 'P')
            decoded = decoded.replace('51', 'Q')
            decoded = decoded.replace('52', 'R')
            decoded = decoded.replace('53', 'S')
            decoded = decoded.replace('54', 'T')
            decoded = decoded.replace('55', 'U')
            decoded = decoded.replace('56', 'V')
            decoded = decoded.replace('57', 'W')
            decoded = decoded.replace('58', 'X')
            decoded = decoded.replace('59', 'Y')
            decoded = decoded.replace('5A', 'Z')

            #symbols
            decoded = decoded.replace('21', '!')
            decoded = decoded.replace('40', '@')
            decoded = decoded.replace('23', '#')
            decoded = decoded.replace('24', '$')
            decoded = decoded.replace('25', '%')
            decoded = decoded.replace('5E', '^')
            decoded = decoded.replace('26', '&')
            decoded = decoded.replace('2A', '*')
            decoded = decoded.replace('28', '(')
            decoded = decoded.replace('29', ')')
            decoded = decoded.replace('2d', '-')
            decoded = decoded.replace('5F', '_')
            decoded = decoded.replace('3D', '=')
            decoded = decoded.replace('2B', '+')
            decoded = decoded.replace('5B', '[')
            decoded = decoded.replace('5D', ']')
            decoded = decoded.replace('7B', '{')
            decoded = decoded.replace('7D', '}')
            decoded = decoded.replace('3B', ';')
            decoded = decoded.replace('3A', ':')
            decoded = decoded.replace('27', "'")
            decoded = decoded.replace('22', '"')
            decoded = decoded.replace('5C', """\"""")
            decoded = decoded.replace('7C', '|')
            decoded = decoded.replace('3C', '<')
            decoded = decoded.replace('3E', '>')
            decoded = decoded.replace('2C', ',')
            decoded = decoded.replace('2E', '.')
            decoded = decoded.replace('2F', '/')
            decoded = decoded.replace('3F', '?')
            
            #THEN finally spaces.
            decoded = decoded.replace(' ', '')
            decoded = decoded.replace('20', ' ')

            print('Decoded!')
            print('Should look like:', '\n', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+[]{};:|,.<>/?')
            print('', decoded)
            print('(yes it should have the backslash and the quotes, and the decoded thing is under the should look like thing.)')

    if choice.lower() == 'help':
        print('\n\n\nType "morse" to decode morse, hex to decode hex\nEncoding and binary is work in progress!')
    if choice.lower() == 'exit':
        print('\nBye!')