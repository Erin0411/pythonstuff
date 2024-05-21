from os import system

username = system('whoami')
hostname = system('hostname')
path = system('pwd')
command = 'ls'
header = system('whoami'),'@',system('hostname'), system('path'), '$ '
method = '?'
while method != 'exit':
    print('(type exit to exit)')
    method = input('Try to emulate bash using system() or type in truebash to get the real bash\n\n')
    print('type emulate or truebash')
    if method == 'emulate':
        print('basic bash terminal to try to epic hack this thing')
        while command.lower() != 'exit':
            command = input(header)
            system(command)
    if method == 'truebash':
        system('bash')
        print('True bash failed! falling back to bash emulator.')
        print('(if you exited this is normal)')
