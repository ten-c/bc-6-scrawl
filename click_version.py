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
