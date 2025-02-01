#cli interface
import click
import commands

@click.group()
def cli():
    pass

cli.add_command(commands.prompt)

if __name__ == "__main__":
   cli()