# COMMANDS = (hello, add, change, phone, show all, close, exit, good bye)
import sys
import time


def input_error_absent_contacts(func):

    def wrapper(lst):

        if len(handbook) == 0:
            try:
                next(filter(lambda d: d.get('name') == lst[0], handbook))
            except StopIteration:
                time.sleep(0.3)
                print("You haven't added any contact. Do it with command 'add'!")
            else:
                return func(lst)
        else:
            return func(lst)
    return wrapper


def input_error_absent_name(func):

    def wrapper(lst):

        try:
            next(filter(lambda d: d.get('name') == lst[0], handbook))
        except StopIteration:
            time.sleep(0.3)
            print("The name is absent in contacts. If you want to save it, use the 'add' command")
        else:
            return func(lst)
    return wrapper


def input_error_number(func):

    def wrapper(lst):

        try:
            lst[1] = int(lst[1])
        except ValueError:
            time.sleep(0.3)
            print('Phone number must contain only digits! Try again, please')
        else:
            return func(lst)
    return wrapper


def input_error_name(func):

    def wrapper(lst):

        try:
            name, *extra = lst
        except ValueError:
            time.sleep(0.3)
            print('Enter user name!')
        else:
            return func(lst)
    return wrapper


def input_error_name_phone(func):

    def wrapper(lst):
        try:
            name, phone, *extra = lst
        except ValueError:
            time.sleep(0.3)
            print('Give me name and phone, please!')
        else:
            return func(lst)
    return wrapper


def hello(lst):

    time.sleep(0.3)
    print("How can I help you?")


@input_error_name_phone
@input_error_number
def add_name_phone(lst):

    name, phone, *extra = lst
    if {'name': name, 'phone': phone} not in handbook:
        handbook.append({'name': name, 'phone': phone})
        time.sleep(0.3)
        print(f'New contact (name: {name}, phone: {phone}) has just added')


@input_error_name_phone
@input_error_absent_name
@input_error_number
def change_phone(lst):

    name, phone, *extra = lst
    for i in handbook:
        if name == i['name']:
            i['phone'] = phone
            time.sleep(0.3)
            print(f'New phone of {name} is changed')


@input_error_name
@input_error_absent_name
def phone(lst):

    name, *extra = lst
    for i in handbook:
        if name == i['name']:
            time.sleep(0.3)
            print(f"Phone of {name} is {i['phone']}")


@input_error_absent_contacts
def show_all(lst):

    for i in handbook:
        time.sleep(0.3)
        print(f"name: {i['name']}, phone: {i['phone']}")


def bye_bot(lst):

    time.sleep(0.3)
    sys.exit('Good bye!')


def main():

    while True:
        print('\n')
        print('Enter your command, I know only 8 commands: hello, add, change, phone, show all, close, exit, good bye')
        command_entered = input('>>> ').lstrip()

        for i in COMMANDS.keys():
            if command_entered.lower().startswith(i):
                command = command_entered[:len(i)].lower()
                argument_lst = command_entered[len(i)+1:].lower().capitalize().split()
                COMMANDS[command](argument_lst)
                break

if __name__ == '__main__':

    COMMANDS = {'hello': hello, 'add': add_name_phone, 'change': change_phone, 'phone': phone,
                'show all': show_all, 'close': bye_bot, 'exit': bye_bot, 'good bye': bye_bot}
    handbook = []
    main()

