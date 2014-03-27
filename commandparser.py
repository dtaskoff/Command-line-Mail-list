class CommandParser():
    def __init__(self, commands):
        self.commands_hash = commands

    def parse(self, command, arguments):
        if command in self.commands_hash:
            try:
                return self.commands_hash[command](*arguments)
            except TypeError:
                return self.commands_hash['error']()
        else:
            return self.commands_hash['error']()