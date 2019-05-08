import os
import discord
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.auth')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
TOKEN = os.environ.get("TOKEN")


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

        if message.content.startswith('!hello'):
            print('Message from {0.author}: {0.content}'.format(message))
            await message.channel.send('Hello {0.author.mention}'.format(message))

def main():
    client = MyClient()
    client.run(TOKEN)


if __name__ == '__main__':
    main()
