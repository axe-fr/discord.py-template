from discord import *
import json

with open('settings.json', 'r') as file:
    data = json.load(file)
    statut = data["statut"]

class ready_def:
    def ready(client, tree):
        @client.event
        async def on_ready():
            print(f'{client.user} est connecté !')
            await client.change_presence(activity=Game(name=f'{statut}'))
            await tree.sync()