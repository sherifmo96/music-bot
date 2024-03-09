import discord
from discord.ext import commands
import youtube_dl

# تحديد بادئة الأوامر للبوت
bot = commands.Bot(command_prefix='!')

# تشغيل الأغنية
@bot.command()
async def play(ctx, *, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("يرجى الانضمام إلى قناة صوتية أولاً")
    else:
        vc = await voice_channel.connect()
        ydl_opts = {'format': 'bestaudio'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            vc.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))
        await ctx.send(f'تشغيل: {url}')

# إعادة البوت
@bot.command()
async def leave(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("لا يمكنني مغادرة القناة لأنني لست فيها")
    else:
        await ctx.voice_client.disconnect()
        await ctx.send("مغادرة القناة")

# تشغيل البوت بواسطة مفتاح الوصول الخاص بالبوت
bot.run('MTIxNjA1MDAzMTMyNTQ3OTA1NA.GB4A1y.Q2jNooyUTsjJzvQejaJJqtetlEPqE2yYerf6DE')
