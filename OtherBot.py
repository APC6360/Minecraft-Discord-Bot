import discord
import requests
import json
import base64

client = discord.Client(intents=discord.Intents.all())




def grab_info(uuid,key):
    data=requests.get(
        url="https://api.hypixel.net/player",
        params={
            'key': key,
            'uuid': uuid
        }
    )
    return data.json()

class UserInformation():
    def __init__(self,username):
        self.username=username
        self.uuid=self.get_uuid(username)
        self.skin=self.get_skin(self.uuid)
        self.head=self.get_head(self.uuid)
        self.skin3d=self.get_skin3d(self.uuid)
    def get_username(self):
        return self.username
    def get_uuid(self,username):
        url = requests.get("https://api.mojang.com/users/profiles/minecraft/{username}".format(username=username))
        userID=url.json()['id']
        return userID
    def get_skin(self,uuid):
        skinURL = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{userID}".format(userID=uuid))    
        skinURL=skinURL.json()['properties'][0]['value']
        skinURL=base64.b64decode(skinURL)
        skinURL=json.loads(skinURL)
        skinURL=skinURL['textures']['SKIN']['url']
        return skinURL
    def get_head(self,uuid):
        renderURL = requests.get("https://visage.surgeplay.com/head/512/{userID}".format(userID=uuid))
        return renderURL.url

    def get_skin3d(self,uuid):
        renderURL = requests.get("https://visage.surgeplay.com/full/512/{userID}".format(userID=uuid))
        renderURL=renderURL.url
        return renderURL
        
    
class BedwarsSoloStats():
    def __init__(self,uuid,key):
        self.uuid=uuid
        self.key=key
        self.solo_plays=self.grab_solo_plays(self.uuid,self.key)
        self.solo_broken=self.grab_solo_broken_beds(self.uuid,self.key)
        self.solo_wins=self.grab_solo_wins(self.uuid,self.key)
        self.solo_losses=self.grab_solo_losses(self.uuid,self.key)
        self.solo_kills=self.grab_solo_kills(self.uuid,self.key)
        self.solo_deaths=self.grab_solo_deaths(self.uuid,self.key)
        self.solo_final_kills=self.grab_solo_final_kills(self.uuid,self.key)
        self.solo_beds_lost=self.grab_solo_beds_lost(self.uuid,self.key)
        self.solo_final_deaths=self.grab_solo_final_deaths(self.uuid,self.key)
    def grab_solo_plays(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_plays = bedwarsInfo['eight_one_games_played_bedwars']
            return solo_plays
        except:
            return 0
    def grab_solo_broken_beds(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_broken = bedwarsInfo['eight_one_beds_broken_bedwars']
            return solo_broken
        except:
            return 0
    def grab_solo_wins(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_wins = bedwarsInfo['eight_one_wins_bedwars']
            return solo_wins
        except:
            return 0
    def grab_solo_losses(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_losses = bedwarsInfo['eight_one_losses_bedwars']
            return solo_losses
        except:
            return 0
    def grab_solo_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_kills = bedwarsInfo['eight_one_kills_bedwars']
            return solo_kills
        except:
            return 0
    def grab_solo_deaths(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_deaths = bedwarsInfo['eight_one_deaths_bedwars']
            return solo_deaths
        except:
            return 0
    def grab_solo_final_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_final_kills = bedwarsInfo['eight_one_final_kills_bedwars']
            return solo_final_kills
        except:
            return 0
    def grab_solo_beds_lost(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_beds_lost = bedwarsInfo['eight_one_beds_lost_bedwars']
            return solo_beds_lost
        except:
            return 0
    def grab_solo_final_deaths(self,uuid,key):


        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            solo_final_deaths = bedwarsInfo['eight_one_final_deaths_bedwars']
            return solo_final_deaths
        except:
            return 0
class BedwarsDuosStats():

    def __init__(self,uuid,key):
        self.uuid=uuid
        self.key=key
        self.duos_plays=self.grab_duos_plays(self.uuid,self.key)
        self.duos_broken=self.grab_duos_broken_beds(self.uuid,self.key)
        self.duos_wins=self.grab_duos_wins(self.uuid,self.key)
        self.duos_losses=self.grab_duos_losses(self.uuid,self.key)
        self.duos_kills=self.grab_duos_kills(self.uuid,self.key)
        self.duos_deaths=self.grab_duos_deaths(self.uuid,self.key)
        self.duos_final_kills=self.grab_duos_final_kills(self.uuid,self.key)
        self.duos_beds_lost=self.grab_duos_beds_lost(self.uuid,self.key)
        self.duos_final_deaths=self.grab_duos_final_deaths(self.uuid,self.key)
    def grab_duos_plays(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_plays = bedwarsInfo['eight_two_games_played_bedwars']
            return duos_plays
        except:
            return 0
    def grab_duos_broken_beds(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_broken = bedwarsInfo['eight_two_beds_broken_bedwars']
            return duos_broken
        except:
            return 0
    def grab_duos_wins(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_wins = bedwarsInfo['eight_two_wins_bedwars']
            return duos_wins
        except:
            return 0
    def grab_duos_losses(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_losses = bedwarsInfo['eight_two_losses_bedwars']
            return duos_losses
        except:
            return 0
    def grab_duos_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_kills = bedwarsInfo['eight_two_kills_bedwars']
            return duos_kills
        except:
            return 0
    def grab_duos_deaths(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_deaths = bedwarsInfo['eight_two_deaths_bedwars']
            return duos_deaths
        except:
            return 0
    def grab_duos_final_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_final_kills = bedwarsInfo['eight_two_final_kills_bedwars']
            return duos_final_kills
        except:
            return 0
    def grab_duos_beds_lost(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_beds_lost = bedwarsInfo['eight_two_beds_lost_bedwars']
            return duos_beds_lost
        except:
            return 0
    def grab_duos_final_deaths(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            duos_final_deaths = bedwarsInfo['eight_two_final_deaths_bedwars']
            return duos_final_deaths
        except:
            return 0
class BedwarsTriosStats():
    def __init__(self,uuid,key):
        self.uuid=uuid
        self.key=key
        self.trios_plays=self.grab_trios_plays(self.uuid,self.key)
        self.trios_broken=self.grab_trios_broken_beds(self.uuid,self.key)
        self.trios_wins=self.grab_trios_wins(self.uuid,self.key)
        self.trios_losses=self.grab_trios_losses(self.uuid,self.key)
        self.trios_kills=self.grab_trios_kills(self.uuid,self.key)
        self.trios_deaths=self.grab_trios_deaths(self.uuid,self.key)
        self.trios_final_kills=self.grab_trios_final_kills(self.uuid,self.key)
        self.trios_beds_lost=self.grab_trios_beds_lost(self.uuid,self.key)
        self.trios_final_deaths=self.grab_trios_final_deaths(self.uuid,self.key)
    def grab_trios_plays(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_plays = bedwarsInfo['four_three_games_played_bedwars']
            return trios_plays
        except:
            return 0
    def grab_trios_broken_beds(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_broken = bedwarsInfo['four_three_beds_broken_bedwars']
            return trios_broken
        except:
            return 0
    def grab_trios_wins(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_wins = bedwarsInfo['four_three_wins_bedwars']
            return trios_wins
        except:
            return 0
    def grab_trios_losses(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_losses = bedwarsInfo['four_three_losses_bedwars']
            return trios_losses
        except:
            return 0
    def grab_trios_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_kills = bedwarsInfo['four_three_kills_bedwars']
            return trios_kills
        except:
            return 0
    def grab_trios_deaths(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_deaths = bedwarsInfo['four_three_deaths_bedwars']
            return trios_deaths
        except:
            return 0
    def grab_trios_final_kills(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_final_kills = bedwarsInfo['four_three_final_kills_bedwars']
            return trios_final_kills
        except:
            return 0
    def grab_trios_beds_lost(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_beds_lost = bedwarsInfo['four_three_beds_lost_bedwars']
            return trios_beds_lost
        except:
            return 0
    def grab_trios_final_deaths(self,uuid,key):
        bedwarsInfo=grab_info(uuid,key)['player']['stats']['Bedwars']
        try:
            trios_final_deaths = bedwarsInfo['four_three_final_deaths_bedwars']
            return trios_final_deaths
        except:
            return 0



    

class EmbedBedwarsSolo():
    def __init__(self,uuid,key,username):
        self.uuid=uuid
        self.key=key
        self.username=username
        self.solo_stats=BedwarsSoloStats(self.uuid,self.key)
        self.solo_plays=self.solo_stats.solo_plays
        self.solo_broken=self.solo_stats.solo_broken
        self.solo_wins=self.solo_stats.solo_wins
        self.solo_losses=self.solo_stats.solo_losses
        self.solo_kills=self.solo_stats.solo_kills
        self.solo_deaths=self.solo_stats.solo_deaths
        self.solo_final_kills=self.solo_stats.solo_final_kills
        self.solo_beds_lost=self.solo_stats.solo_beds_lost
        self.solo_final_deaths=self.solo_stats.solo_final_deaths
        self.solo_win_loss=round(self.solo_wins/self.solo_losses,2)
        
    def create_embed(self,uuid):
        embed=discord.Embed(
            title="Solo Bedwars Stats",
            description="Here are the stats of the player",
            color=0x00ff00
            )
        userInfo=UserInformation(self.username)
        embed.set_thumbnail(url=userInfo.get_head(uuid))
        embed.add_field(name="Plays",value=self.solo_plays,inline=True)
        embed.add_field(name="Broken Beds",value=self.solo_broken,inline=True)
        embed.add_field(name="Beds Lost",value=self.solo_beds_lost,inline=True)

        embed.add_field(name="Wins",value=self.solo_wins,inline=True)
        embed.add_field(name="Losses",value=self.solo_losses,inline=True)
        embed.add_field(name='W/L',value=self.solo_win_loss,inline=True)

        embed.add_field(name="Kills",value=self.solo_kills,inline=True)
        embed.add_field(name="Final Kills",value=self.solo_final_kills,inline=True)
        embed.add_field(name="Deaths",value=self.solo_deaths,inline=True)
        return embed
class EmbedBedwarsDuo():
    def __init__(self,uuid,key,username):
        self.uuid=uuid
        self.key=key
        self.username=username
        self.duo_stats=BedwarsDuosStats(self.uuid,self.key)
        self.duo_plays=self.duo_stats.duos_plays
        self.duo_broken=self.duo_stats.duos_broken
        self.duo_wins=self.duo_stats.duos_wins
        self.duo_losses=self.duo_stats.duos_losses
        self.duo_kills=self.duo_stats.duos_kills
        self.duo_deaths=self.duo_stats.duos_deaths
        self.duo_final_kills=self.duo_stats.duos_final_kills
        self.duo_beds_lost=self.duo_stats.duos_beds_lost
        self.duo_final_deaths=self.duo_stats.duos_final_deaths
        self.duo_win_loss=round(self.duo_wins/self.duo_losses,2)
        
    def create_embed(self,uuid):
        embed=discord.Embed(
            title="Duo Bedwars Stats",
            description="Here are the stats of the player",
            color=0x00ff00
            )
        userInfo=UserInformation(self.username)
        embed.set_thumbnail(url=userInfo.get_head(uuid))
        embed.add_field(name="Plays",value=self.duo_plays,inline=True)
        embed.add_field(name="Broken Beds",value=self.duo_broken,inline=True)
        embed.add_field(name="Beds Lost",value=self.duo_beds_lost,inline=True)

        embed.add_field(name="Wins",value=self.duo_wins,inline=True)
        embed.add_field(name="Losses",value=self.duo_losses,inline=True)
        embed.add_field(name='W/L',value=self.duo_win_loss,inline=True)

        embed.add_field(name="Kills",value=self.duo_kills,inline=True)
        embed.add_field(name="Final Kills",value=self.duo_final_kills,inline=True)
        embed.add_field(name="Deaths",value=self.duo_deaths,inline=True)
        return embed
class EmbedBedwarsTrio():
    def __init__(self,uuid,key,username):
        self.uuid=uuid
        self.key=key
        self.username=username
        self.trio_stats=BedwarsTriosStats(self.uuid,self.key)
        self.trio_plays=self.trio_stats.trios_plays
        self.trio_broken=self.trio_stats.trios_broken
        self.trio_wins=self.trio_stats.trios_wins
        self.trio_losses=self.trio_stats.trios_losses
        self.trio_kills=self.trio_stats.trios_kills
        self.trio_deaths=self.trio_stats.trios_deaths
        self.trio_final_kills=self.trio_stats.trios_final_kills
        self.trio_beds_lost=self.trio_stats.trios_beds_lost
        self.trio_final_deaths=self.trio_stats.trios_final_deaths
        self.trio_win_loss=round(self.trio_wins/self.trio_losses,2)
        
    def create_embed(self,uuid):
        embed=discord.Embed(
            title="Trio Bedwars Stats",
            description="Here are the stats of the player",
            color=0x00ff00
            )
        userInfo=UserInformation(self.username)
        embed.set_thumbnail(url=userInfo.get_head(uuid))
        embed.add_field(name="Plays",value=self.trio_plays,inline=True)
        embed.add_field(name="Broken Beds",value=self.trio_broken,inline=True)
        embed.add_field(name="Beds Lost",value=self.trio_beds_lost,inline=True)

        embed.add_field(name="Wins",value=self.trio_wins,inline=True)
        embed.add_field(name="Losses",value=self.trio_losses,inline=True)
        embed.add_field(name='W/L',value=self.trio_win_loss,inline=True)

        embed.add_field(name="Kills",value=self.trio_kills,inline=True)
        embed.add_field(name="Final Kills",value=self.trio_final_kills,inline=True)
        embed.add_field(name="Deaths",value=self.trio_deaths,inline=True)
        return embed

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
            UserInfo=UserInformation(skinName)
        except:
            await message.channel.send("Player not found")
            return
        try:
            uuid=UserInfo.get_uuid(skinName)
        except:
            await message.channel.send("cant fetch uuid, Try Again")
            return
        embed=discord.Embed(
            title=skinName+"'s Skin",
            description="Here is the skin of "+skinName,
            color=0x00ff00,
            url=UserInfo.get_skin(uuid)
            )
        embed.set_thumbnail(url=UserInfo.get_head(uuid))
        embed.set_image(url=UserInfo.get_skin3d(uuid))
        await message.channel.send(embed=embed)
        await message.delete()

    if message.content.startswith('$solo'):
        infoName=message.content.split('$solo ',1)[1]
        UserInfo=UserInformation(infoName)
        try:
            uuid=UserInfo.get_uuid(infoName)
        except:
            await message.channel.send("Invalid username, Try Again")
            return
        embed=EmbedBedwarsSolo(uuid,api_key,infoName)
        await message.channel.send(embed=embed.create_embed(uuid))
        
    if message.content.startswith('$duo'):
        infoName=message.content.split('$duo ',1)[1]
        UserInfo=UserInformation(infoName)
        try:
            uuid=UserInfo.get_uuid(infoName)
        except:
            await message.channel.send("Invalid username, Try Again")
            return
        embed=EmbedBedwarsDuo(uuid,api_key,infoName)
        await message.channel.send(embed=embed.create_embed(uuid))
    if message.content.startswith('$trio'):
        infoName=message.content.split('$trio ',1)[1]
        UserInfo=UserInformation(infoName)
        try:
            uuid=UserInfo.get_uuid(infoName)
        except:
            await message.channel.send("Invalid username, Try Again")
            return
        embed=EmbedBedwarsTrio(uuid,api_key,infoName)
        await message.channel.send(embed=embed.create_embed(uuid))

client.run(token)




