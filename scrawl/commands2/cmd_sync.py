import click
from scrawl.cli import pass_context

@click.command()
@click.option('--url', default='https://bc-6-scrawl.firebaseio.com', help="url to the firebase app. \n default = https://bc-6-scrawl.firebaseio.com")
@pass_context
def cli(ctx,url):
    """
    Command to sync notes with Firebase
    """
    firebase_instance = firebase.FirebaseApplication(url, None)
    if firebase_instance:
        db = ctx.database()
        cursor = db.cursor()

        query_all = "SELECT * from `notes`"
        cursor.execute(query_all)
        all_notes = cursor.fetchall()

        # result = firebase_instance.post('/notes', json.dumps(all_notes))
        # result = firebase_instance.post('/notes', all_notes)
        # Every time we send a POST request, the Firebase client generates a unique ID,
        # Thus use put


        # result = firebase_instance.put(url, 'notes', all_notes)

        with click.progressbar(all_notes,length=len(all_notes),
                       label='Syncing ...', color=True,width=0,item_show_func=lambda item: 'uploading id {}'.format(item)) as bar:
            for note in bar:
                result = firebase_instance.patch(url+'/notes', note)
                # if not result:
                #     click.secho('Could not sync notes',fg="white",bg="red")
                # else:
                #     click.secho('{} notes successfully synced'.format(len(all_notes)),fg="green")
    else:
        click.secho('Invalid url provided',fg="white",bg="red")
