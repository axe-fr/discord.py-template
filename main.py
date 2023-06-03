
from discord import *
import json


intents = Intents.all() # intents


client = Client(intents=intents) # client
tree = app_commands.CommandTree(client) # slash cmds


from commandes.stream import stream_def  # importation d'une commande /
stream_def.commande(client, tree)


from event.ready import ready_def # importation d'un évenement 
ready_def.ready(client, tree)


with open('data/token.json', 'r') as file:
    data = json.load(file)
    token = data["token"]
    
client.run(token)