
from sys import executable
import discord
import yt_dlp
from discord.ext import commands


#the channel where the bot is gonna talk to
channelID = <channel ID bot listens>

#sets up to be able to take in commands
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(channelID)
    await channel.send("We online fellas!!")


class Mamadas:
    
    def __init__(ctx):
        m_ctx = ctx
    
    async def isPlaying(ctx):
        voice_channel = ctx.guild.voice_client
        return voice_channel.is_playing()
        
    async def stop(ctx):
        #checks if the bot is connected to a voice chat
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            if vc.is_playing():
                await vc.stop()
        else:
           await ctx.channel.send('U tripping or some broda? Im not playing anything rn')

    async def joinVC(ctx):
        bot_voice = ctx.guild.voice_client
        if bot_voice and bot_voice.is_connected():
            await ctx.channel.send('you are already in a VC dummy!!')
        else:
            vc = await ctx.author.voice.channel.connect()


    async def plaj(ctx, theUrl):
        #gets the channel where the user is at
        print(theUrl)
        
        #if user is not conenceted to VC then tell them they're stupid
        if ctx.author.voice is None:
            await ctx.channel.send('You are not connected to a voice channel bozo')
            return
        
        voice_channel = ctx.author.voice.channel
        
        #this vc is the object voice_client object that allows to play the stuff and use voice methods (functions)
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            print('stuff')
        else:
            vc = await ctx.author.voice.channel.connect()

        #checks if bot is playing something already
        if await Mamadas.isPlaying(ctx):
            await ctx.channel.send('wait your turn! (havent implemented query yet)')
            return

        ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #theLink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            theLink = str(theUrl)
            info = ydl.extract_info(theLink, download = False)
            url = info['url']
            vc.play(discord.FFmpegPCMAudio(executable = <The Path of ffmpeg.exe>, source = url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",options="-vn"))
     
                

@bot.command()
async def play(ctx, theUrl):
    await Mamadas.plaj(ctx, theUrl)

@bot.command()
async def joinVC(ctx):
    await Mamadas.joinVC(ctx)
    
@bot.command()
async def stop(ctx):
    await Mamadas.stop(ctx)

    





bot.run(<token>)