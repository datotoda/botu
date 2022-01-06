import discord
import random

from discord import player

with open('token.txt', 'r') as f:
    TOKEN = f.read()

client = discord.Client()


@client.event
async def on_ready():
    print(f'მე დავლოგინდი როგორც {client.user}')


@client.event
async def on_message(message):
    
    await message.add_reaction('❤️')

    if message.author == client.user:
        return

    if message.content.startswith('!botu'):
        await message.channel.send('სალამი, მე ვარ BOTU, მიხარია შენი დანახვა!')

    if message.content.startswith('!hello'):
        await message.channel.send('გამარჯობა ❤')

    if message.content.startswith('!roll'):
        await message.channel.send(f'შენ გააგორე {random.randint(1, 6)}')


if __name__ == '__main__':
    client.run(TOKEN)
