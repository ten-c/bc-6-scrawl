import click
import sqlite3
from datetime import datetime, date


@click.group()
def scrawl():
    """Scrawl - Python note-taking console app


    """


def dbase():
    db = sqlite3.connect('data.db')
    db.row_factory = sqlite3.Row

    return db


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

    # click.echo('Continue? [yn] ', nl=False)
    # c = click.getchar()
    # click.echo()
    # if c == 'y':
    #     click.echo('We will go on')
    # elif c == 'n':
    #     click.echo('Abort!')
    # else:
    #     click.echo('Invalid input :(')

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

