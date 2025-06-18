import typer
from rich import print
from src.database.db import TransactionalDB
from src.ui.interactor import InterActor
from src.utils.help import welcome_user


def main():
    welcome_user()
    actor = InterActor(database=TransactionalDB())
    while True:
        raw_string = input("> ")
        actor.get_raw_input(raw_string)
        actor.action()


if __name__ == "__main__":
    typer.run(main)
