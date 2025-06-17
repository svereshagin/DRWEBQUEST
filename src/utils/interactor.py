from src.enums.enums import Command
from rich import print
from src.utils.help import help_instructions


class InterActor:
    def __init__(self, database):
        """
        :param database: 
        """
        self.database = database

        self.command = ''
        self.params = []

        self.handlers = {
            Command.SET: (2, self.database.set, False),
            Command.GET: (1, self.database.get, True),
            Command.UNSET: (1, self.database.unset, False),
            Command.FIND: (1, self.database.find, True),
            Command.COUNT: (1, self.database.count, True),
            Command.END: (0, self.database.end, False),
            Command.HELP: (0, help_instructions, True)
        }

    def get_raw_input(self, raw_string: str) -> None:
        parts = list(map(str, raw_string.split()))
        if not parts:
            return
        try:
            self.command = Command(parts[0])
            self.params = parts[1:]
        except ValueError:
            print(f"Неизвестная команда: {parts[0]}")
            self.command = None


    def action(self):
        if not self.command:
            return
        arg_count, handler, should_print = self.handlers[self.command]

        if len(self.params) != arg_count:
            print(f"Ошибка: команда {self.command.value} требует {arg_count} аргументов")
            return
        result = handler(*self.params)

        if should_print:
            print(result)