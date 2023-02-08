def main_menu():
    commands = ['Show all contacts',
                'Open file',
                'Save file',
                'New contact',
                'Change contact',
                'Delete contact',
                'Find contact',
                'Exit']
    print('\n   Select menu: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\n   Enter menu: '))
    return user_input


def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(
                f'{phone_book.index(item)+1}) {item[0]} {item[1]} ({item[2]} )')
    else:
        print('The phone book is empty or not loaded')


def load_success():
    print('The phone book is loaded success!')


def save_success():
    print('The phone book is saved success!')


def delete_contact(phone_book):
    show_contacts(phone_book)
    line = int(input("Who do you want to delete? Enter number: "))
    return line


def change_contact(phone_book):
    show_contacts(phone_book)
    line = int(input("Who do you want to change? Enter number: "))
    section = int(input("Enter digit for what: name(1), number(2), comment(3) ?: "))
    value = input("Enter a new value: ")
    return line, section, value


def new_contact():
    name = input('Enter first and last name of contact: ')
    phone = input('Enter the phone number: ')
    comment = input('Enter a comment to the contact: ')
    print('The data is entered, but not saved')
    return name, phone, comment


def find_contact():
    search = input('Enter the desired value: ')
    return search
