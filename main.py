import os
import discord
from os.path import join, dirname
from dotenv import load_dotenv

from locator import Locator

dotenv_path = join(dirname(__file__), '.auth')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
TOKEN = os.environ.get("TOKEN")

locator = Locator()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!where'):
            name = message.content[7:]
            location = locator.get_position(name)
            if not location:
                await message.channel.send('Je ne connais pas ce pokéstop')
            else:
                await message.channel.send('%s: %s' % (location.name, location.itineraire))

def main():
    client = MyClient()
    client.run(TOKEN)


if __name__ == '__main__':
    main()
