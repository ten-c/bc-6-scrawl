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
