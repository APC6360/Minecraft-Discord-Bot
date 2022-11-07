import discord
import requests
import json
import base64

client = discord.Client(intents=discord.Intents.all())


def grab_uuid(username):
    url = requests.get("https://api.mojang.com/users/profiles/minecraft/{username}".format(username=username))
    userID=url.json()['id']
    return userID

def grab_skin_file(uuid):
    skinURL = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{userID}".format(userID=uuid))    
    skinURL=skinURL.json()['properties'][0]['value']
    skinURL=base64.b64decode(skinURL)
    skinURL=json.loads(skinURL)
    skinURL=skinURL['textures']['SKIN']['url']
    return skinURL

def grab_3d_skin(uuid):
    renderURL = requests.get("https://visage.surgeplay.com/full/512/{userID}".format(userID=uuid))
    renderURL=renderURL.url
    return renderURL

def grab_3d_head(uuid):
    renderURL = requests.get("https://visage.surgeplay.com/head/512/{userID}".format(userID=uuid))
    return renderURL.url


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$skin"):
        skinName=message.content.split('$skin ',1)[1]
        try:
            uuid=grab_uuid(skinName)
        except:
            await message.channel.send("Invalid username, Try Again")
            return
        embed=discord.Embed(
            title=skinName+"'s Skin",
            description="Here is the skin of "+skinName,
            color=0x00ff00,
            url=grab_skin_file(uuid)
            )
        embed.set_thumbnail(url=grab_3d_head(uuid))
        embed.set_image(url=grab_3d_skin(uuid))
        await message.channel.send(embed=embed)

client.run(token)




