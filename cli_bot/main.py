from operations import add_contact, change_contact, get_phone


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print('Enter command and arguments')
            continue

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        match command:
            case 'hello':
                print('How can I help you?')
            case 'add':
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(get_phone(args, contacts))
            case 'all':
                print(contacts)
            case _:
                print('Invalid command.')


if __name__ == "__main__":
    main()
