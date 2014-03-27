import interface
import commandparser
import sqlite3


def main():
    conn = sqlite3.connect("lists.db")
    cursor = conn.cursor()
    main_interface = interface.Interface(cursor)

    commands = {
        'help': main_interface.help,
        'show_lists': main_interface.show_lists,
        'exit': main_interface.exit,
        'delete': main_interface.delete,
        'show_list': main_interface.show_list,
        'add': main_interface.add,
        'create': main_interface.create,
        'delete': main_interface.delete,
        'search_email': main_interface.search_email,
        'export': main_interface.export,
        'import':main_interface.import_,
        'update': main_interface.update,
        'update_subscriber': main_interface.update_subscriber,
        'remove_subscriber': main_interface.remove_subscriber,
        'merge_lists': main_interface.merge_lists,
        'error': main_interface.error
        }
    command_parser = commandparser.CommandParser(commands)

    while True:
        commands = input(">")

        if len(commands) == 0:
            continue

        command = commands.split()[0]
        arguments = commands.split()[1:]

        print(command_parser.parse(command, arguments))
        conn.commit()


if __name__ == '__main__':
    main()