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
FAKE_TOKEN = os.environ.get("FAKE_TOKEN")

locator = Locator()
debug = True


class MyClient(discord.Client):
    def __init__(self, debug=False):
        super(MyClient, self).__init__()
        self.debug = True


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if self.debug:
            if "Greenlamp" not in message.author.name:
                return
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
    client = MyClient(debug)
    token = TOKEN if not debug else FAKE_TOKEN
    client.run(token)


if __name__ == '__main__':
    main()
