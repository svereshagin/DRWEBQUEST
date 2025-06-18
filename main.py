import typer
from rich import print
from src.utils.db import TransactionalDB
from src.utils.interactor import InterActor



def main():
    print("[green]This is a DataBase sample[/green]\n",
                    "[pink]Write 'HELP' to get a help message[/pink]\n",
                    "[white]Write any possible command for test reason[/white]\n",)
    
    actor = InterActor(database = TransactionalDB())
    while True:
        raw_string = input("> ")
        actor.get_raw_input(raw_string)
        actor.action()

if __name__ == "__main__":
    typer.run(main)