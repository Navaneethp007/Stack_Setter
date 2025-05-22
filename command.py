import click
from installer import install_stack
from suggestion import give_suggestion
from addtostacks import more_stacks

@click.group()
def cli():
    """Stacker: Command Line Interface for Stack Installer."""
    pass

@cli.command()
@click.argument("stack_name")
def install(stack_name):
    install_stack(stack_name)

@cli.command()
@click.argument("prompt")
def suggest(prompt):
    suggestion = give_suggestion(prompt)
    click.echo(suggestion)

@cli.command()
@click.argument("prompt")
def add(prompt):
    more_stacks(prompt)

if __name__ == '__main__':
    cli()
