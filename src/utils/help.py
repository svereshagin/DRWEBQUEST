from rich.table import Table
from rich.console import Console


def help_instructions():
    console = Console()
    table = Table("Command", "Description")
    table.add_row("SET", "сохраняет аргумент в базе данных")
    table.add_row("GET", "возвращает, ранее сохраненную переменную. Если такой переменной не было сохранено, возвращает NULL")
    table.add_row("UNSET", "удаляет, ранее установленную переменную. Если значение не было установлено, не делает ничего.")
    table.add_row("COUNTS", "показывает сколько раз данные значение встречается в базе данных.")
    table.add_row("FIND", "выводит найденные установленные переменные для данного значения.")
    table.add_row("END", "закрывает приложение")
    return table