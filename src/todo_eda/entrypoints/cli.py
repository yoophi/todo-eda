import click


@click.group('cli')
def main():
    pass


@main.add_command
@click.command()
def add_todo():
    click.echo('add-todo')


if __name__ == '__main__':
    main()
