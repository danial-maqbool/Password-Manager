from cryptography.fernet import Fernet


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split('|')
            decrypted_pwd = fer_key.decrypt(pwd.encode()).decode()
            print('User: ', user, ', Password: ', decrypted_pwd)


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    encrypted_pwd = fer_key.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + encrypted_pwd + '\n')


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
        return key


master_pwd = input('Enter the Master Password: ')

# activate for first run only.
# write_key()

fer_key = Fernet(load_key() + master_pwd.encode())

while True:
    mode = input('Would you to add a new password or view existing ones (view, add, quit): ').lower()

    if mode in 'quit':
        quit()

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode!')
        continue
