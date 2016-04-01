import click
from scrawl.cli import pass_context


@click.command()
# @click.argument('filename', default='import.json', type=click.File('r'))
@click.argument('path', default='import.json', type=click.Path(exists=True, file_okay=True, dir_okay=True, writable=True, readable=True, resolve_path=True))
@click.option('--format', default='json', help="data format of the import file")
@pass_context
def cli(ctx,path, format):
    """
    Command import notes from a path
    """
    # click.echo(path)
    # click.pause()
    file = click.open_file(path, 'r')

    # if not file:
    #     click.echo('file doestnt exist')
    #     return

    new_data = ""
    # click.echo((file.readlines.__doc__))
    while True:
        string_from_file = file.readline()
        new_data += string_from_file
        # click.echo(type(string_from_file))
        if not string_from_file:
            break

    # new_data = file.read()

    if new_data:
        defaults = {
            'title': None,
            'content': " ",
            'date_created': datetime.now(),
            'date_modified': datetime.now()
        }
        # notes = json.loads(new_data, object_pairs_hook=namedtuple)
        # notes = json.loads(new_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        # notes = json.loads(new_data, object_hook=lambda d: tuple(d.values()))

        notes = json.loads(new_data)
        notes = [{k: note.get(k, defaults[k])
                  for k in defaults} for note in notes]
        # click.echo(notes)
        # click.pause()
        db = ctx.database()
        cursor = db.cursor()

        # books = [(title4, author4, price4, year4),(title5, author5, price5, year5)]
        cursor.executemany(
            # '''INSERT INTO notes(title, content, date_created, date_modified) VALUES(?,?,?,?)''', [notes])
            '''INSERT INTO notes(title, content, date_created, date_modified) VALUES(:title, :content, :date_created, :date_modified)''',
            notes)
        db.commit()
        click.echo(
                click.style("Imported ",fg="green") + \
                click.style("{}".format(len(notes)),fg="cyan") + \
                click.style(" notes from to the file ",fg="green") + \
                click.style("{}".format(file),fg="cyan")
                )
    else:
        click.secho('No data to import',fg="white",bg="red")

