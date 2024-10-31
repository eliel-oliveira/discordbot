import discord
from discord import app_commands

id_do_servidor = 1198913987161624597

class client(discord.Client):
     def __init__(self):
          super().__init__(intents=discord.Intents.default())
          self.synced = False

          async def on_ready(self):
               await self.wait_until_ready()
               if not self.synced:
                    await tree.sync(guild=discord.Object(id=id_do_servidor))
                    self.synced = True
                    print(f"entramos como {self.user}.")

aclient = client()
tree = app_commands.ComandTree(aclient)
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'test', description = 'testing')
async def slash2(interaction: discord.Interaction):
     await interaction.respose.send_message(f"Working!", ephemeral = True)
     aclient.run('')