from discord import *
import json

with open('settings.json', 'r') as file:
    data = json.load(file)
    owner = data["owner-id"]


class stream_def:
    def commande(client, tree):
        @app_commands.describe(stream="stream") # ajoute une option (exemple: /stream [option])
        @app_commands.command(description="Permet de changer le statut du bot. (stream)") # description
        async def stream(interaction : Interaction, stream: str): # option configuré ici
            if  interaction.user.id == owner : # vérifie si l'utilisateur est bien celui de l'owner 
                await client.change_presence(activity=Streaming(name=f'{stream}',url="https://twitch.tv/discord"))
                await interaction.response.send_message(f"Stream modifié en {stream}")
            else:
                return
            await interaction.response.send_message(f"Tu n'as pas les permissions requises pour executer cette commande.")
        tree.add_command(stream) #ajoute la commande au slash via le main