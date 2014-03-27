class CommandParser():
    def __init__(self, commands):
        self.commands_hash = commands

    def parse(self, command, arguments):
        if command in self.commands_hash:
            return self.commands_hash[command](*arguments)