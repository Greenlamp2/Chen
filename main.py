import os
import time

import discord
from os.path import join, dirname

from discord import Guild
from dotenv import load_dotenv

from locator import Locator

dotenv_path = join(dirname(__file__), '.auth')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
TOKEN = os.environ.get("TOKEN")

locator = Locator()
debug = False


class MyClient(discord.Client):
    def __init__(self, _debug=False):
        super(MyClient, self).__init__()
        self.debug = _debug

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def fun(self, message):
        content = message.content
        channel = message.channel

        def check(reaction, user):
            if reaction.message == message and user.id != message.author.id:
                return reaction, user

        reaction, user = await self.wait_for('reaction_add', check=check)
        return reaction

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

        if message.content.startswith('!pfc'):
            moves = ["🪨", "🍃", "✂️"]
            msg = await message.author.send("choose.")
            for move in moves:
                await msg.add_reaction(move)
            reaction = await self.fun(msg)
            await msg.delete()
            await message.author.send("you chose {}.".format(reaction))

def main():
    client = MyClient(debug)
    client.run(TOKEN)


if __name__ == '__main__':
    main()
