import click, sqlite3, json, csv
from datetime import datetime, date



@click.group()
def scrawl():
    """Scrawl - Python note-taking console app


    """


def dbase():
    db = sqlite3.connect('data.db')
    # prefer
    # db.row_factory = sqlite3.Row
    db.row_factory = dict_factory

    return db


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




@scrawl.command()
@click.argument('content')
def createnote(content):
    db = dbase()
    cursor = db.cursor()

    response = cursor.execute('''INSERT INTO notes
        (title, content, date_created,date_modified)
        VALUES(?,?,?,?)''',
                              (" ", content, datetime.now(), datetime.now()))

    db.commit()
    db.close()
    click.echo(response)


@scrawl.command()
@click.argument('id', type=int)
def viewnote(id):
    db = dbase()
    cursor = db.cursor()
    query = "SELECT * from `notes` where id = {}".format(id)
    cursor.execute(query)
    notes = cursor.fetchall()

    # while True:
    #     row = cursor.fetchone()
    #     if row is None:
    #         break
    if notes:
        click.echo(
            "Row id is {} and content - {}".format(notes[0]['id'], notes[0]['content']))
        return
    click.echo("No note found with id {}".format(id))


@scrawl.command()
@click.argument('id')
def deletenote(id):
    db = dbase()
    cursor = db.cursor()
    query = "SELECT * from `notes` where id = {}".format(id)
    cursor.execute(query)
    notes = cursor.fetchall()

    if notes:
        query = "DELETE from `notes` where id = {}".format(id)
        cursor.execute(query)
        db.commit()
        click.echo("Note with id {} has been deleted".format(id))
        return
    click.echo("No note found with id {}".format(id))


@scrawl.command()
@click.option('--limit', '-l', default=None, type=int)
def listnotes(limit):
    db = dbase()
    cursor = db.cursor()

    query_all = "SELECT * from `notes`"
    cursor.execute(query_all)
    all_notes = cursor.fetchall()
    all_notes_count = len(all_notes)

    if all_notes:
        if not limit:
            limit = len(all_notes)
        if all_notes_count % limit:
            page_count = all_notes_count // limit + 1
        else:
            page_count = all_notes_count // limit

        click.echo(
            "Number of notes found : '{}".format(all_notes_count))
        offset = 0
        for i in range(1, page_count + 1):
            query = "SELECT * from `notes` LIMIT {} OFFSET {}".format(limit, offset)

            offset += limit
            cursor.execute(query)
            notes = cursor.fetchall()
            for note in notes:
                click.echo("\n")
                click.echo("Note id : {} , created on {} , last modified on {}".format(
                    note['id'], note['date_created'], note['date_modified']))
                click.echo("........." * 3)
                click.echo(note['content'])
            if all_notes_count > limit and page_count != i:
                display_next = click.prompt(
                    'Type "next" to display next set of {} records. Any other key to abort'.format(all_notes_count- (limit * i)))
                click.echo(display_next)
                if display_next != 'next':
                    break

                # click.echo('Continue? [yn] ', nl=False)
                # c = click.getchar()
                # click.echo(c)
        return
    click.echo("No notes found")


@scrawl.command()
@click.argument('query_str')
@click.option('--limit', '-l', default=None, type=int)
def searchnotes(query_str, limit):
    db = dbase()
    cursor = db.cursor()

    query_all = "SELECT * from `notes` WHERE content like '%{}%'".format(
        query_str)
    cursor.execute(query_all)
    all_notes = cursor.fetchall()
    all_notes_count = len(all_notes)

    if all_notes:
        if not limit:
            limit = len(all_notes)
        if all_notes_count % limit:
            page_count = all_notes_count // limit + 1
        else:
            page_count = all_notes_count // limit

        click.echo(
            "Number of notes matching the search '{}': {}".format(query_str, all_notes_count))
        offset = 0
        for i in range(1, page_count + 1):
            query = "SELECT * from `notes` WHERE content like '%{}%' LIMIT {} OFFSET {}".format(
                query_str, limit, offset)
            offset += limit
            cursor.execute(query)
            notes = cursor.fetchall()
            for note in notes:
                click.echo("\n")
                click.echo("Note id : {} , created on {} , last modified on {}".format(
                    note['id'], note['date_created'], note['date_modified']))
                click.echo("........." * 3)
                click.echo(note['content'])
            if all_notes_count > limit and page_count != i:
                display_next = click.prompt(
                    'Type "next" to display next set of {} records. Any other key to abort'.format(all_notes_count- (limit * i)))
                click.echo(display_next)
                if display_next != 'next':
                    break

                # click.echo('Continue? [yn] ', nl=False)
                # c = click.getchar()
                # click.echo(c)
        return
    click.echo("No notes found")

@scrawl.command()
@click.option('--format', default='json')
# dont provide file ext to avoid eg .json but --format=csv
# @click.argument('filename', default='backup', type=click.File('wb'))
@click.argument('filename', default='backup', type=str)
def export(format,filename):
    export_format = format
    # click.echo(export_format)
    # click.pause()
    if export_format == 'json':
        filename += '.json'
        file = click.open_file(filename,'w')
    else:
        filename += '.csv'
        file = open(filename, 'w')


    db = dbase()
    cursor = db.cursor()

    query_all = "SELECT * from `notes`"
    cursor.execute(query_all)
    all_rows = cursor.fetchall()

    if all_rows:
        # rows_list = []
        # for row in all_rows:
        #     rows_list.append(row)
        if export_format == 'json':
            # output = json.dumps(rows_list, sort_keys=True, indent=4)
            output = json.dumps(all_rows, sort_keys=True, indent=4)
            file.write(output)
        else:
            # csv_file = open(file, 'w', newline='')
            csv_writer = csv.writer(file)
            # [lambda row: csv_writer.writerow(row.values()) for row in all_rows]
            for row in all_rows:
                # csv_writer.writerow(row.values())
                # above line sorts the keys in desc. Prefer explicit
                csv_writer.writerow([row['id'],row['title'],row['content'],row['date_created'],row['date_modified']])
            file.close()
    else:
        click.echo('No data')
