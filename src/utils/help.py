from rich.table import Table
from rich import print as richpr

def help_instructions():
    table = Table("Command", "Description")
    table.add_row("SET", "сохраняет аргумент в базе данных")
    table.add_row("GET", "возвращает, ранее сохраненную переменную. Если такой переменной не было сохранено, возвращает NULL")
    table.add_row("UNSET", "удаляет, ранее установленную переменную. Если значение не было установлено, не делает ничего.")
    table.add_row("COUNTS", "показывает сколько раз данные значение встречается в базе данных.")
    table.add_row("FIND", "выводит найденные установленные переменные для данного значения.")
    table.add_row("END", "закрывает приложение")
    table.add_row("BEGIN", "начать транзакцию")
    table.add_row("ROLLBACK", "откатить транзакцию")
    table.add_row("COMMIT", "подтвердить изменения")
    return table

def welcome_user():
    return richpr("[green]This is a DataBase sample[/green]\n",
          "[pink]Write 'HELP' to get a help message[/pink]\n",
          "[white]Write any possible command for test reason[/white]\n",)
    