import getpass

# Put your User/Pass in here!

username='YourUsername'
password='YourPassword'

if username == 'YourUsername' and password == 'YourPassword':
    username = raw_input('Github Username: ')
    password = getpass.getpass('Github Password: ')
