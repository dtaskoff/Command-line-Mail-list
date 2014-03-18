import interface


def main():
    main_interface = interface.Interface()

    while True:
        commands = input(">")
        if len(commands) == 0:
            continue
        commands = commands.split()
        command = commands[0]

        if command == 'help':
            print(main_interface.help())
        elif command == 'show_lists':
            print(main_interface.show_lists())
        elif command == 'exit':
            main_interface.exit()
        elif len(commands) < 2:
            print(main_interface.error())
        elif command == 'show_list':
            print(main_interface.show_list(commands[1]))
        elif command == 'add':
            print(main_interface.add(commands[1]))
        elif command == 'export':
            print(main_interface.export(commands[1]))
        elif command == 'search_email':
            print(main_interface.search_email(commands[1]))
        elif command == 'create':
            print(main_interface.create(commands[1]))
        elif len(commands) < 4:
            print(main_interface.error())
        elif command == 'merge_lists':
            print(main_interface.merge_lists(commands[1],
                commands[2], commands[3]))
        else:
            print(main_interface.error())


if __name__ == '__main__':
    main()