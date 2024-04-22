from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(args, kwargs):
        try:
            match func.__name__:
                case 'add_contact' if len(args) < 2:
                    return 'Enter name and phone for add contact'
                case 'change_contact' if len(args) < 2:
                    return 'Enter name and phone for change contact'
                case 'get_phone' if len(args) < 1:
                    return 'Enter name for the get phone'

            return func(args, kwargs)
        except (KeyError, ValueError, IndexError):
            return 'Not correct arguments for command'

    return inner


@input_error
def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


@input_error
def change_contact(args: list, contacts: dict):
    name, phone = args
    if name not in contacts.keys():
        return f'Contact "{name}" is not exist'

    contacts[name] = phone
    return f'Phone of contact "{name}" changed'


@input_error
def get_phone(args: list, contacts: dict):
    name = args[0]

    if name not in contacts.keys():
        return f'Contact "{name}" is not exist'

    return contacts[name]
