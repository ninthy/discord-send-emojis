import os
from PIL import Image, ImageSequence
import discord
import gifmaker
from imgpy import Img
from config import TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    if message.author != client.user:
        return
    
    for filename in os.listdir("emojis"):
        file, ext = filename.split(".")
        if message.content == f":{file}:":
            filename = file + '.' + ext
            
            im = Image.open(os.path.join("emojis", filename))
            im = im.resize((48,48))
            if (ext == "gif"):
                im.save(os.path.join("emojis", filename), save_all=True)
            else:
                im.save(os.path.join("emojis", filename))
            await message.delete()
            await message.channel.send(file=discord.File(os.path.join('emojis', filename)))



client.run(TOKEN, bot=False)


