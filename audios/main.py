import discord
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.command(pass_context = True)
async def ajuda(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send("Lista de Comandos:\
        !patrao\
        !rapaz\
        !uepa\
        !biribo\
        !scatman\
        !cenoura\
        !pitipau\
        !suco\
        !cavalo\
        !cagabombom\
        !pare\
        !caminhao\
        cuzinho\
        amem")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Não estou em um canal de voz")

@client.command(pass_context = True)
async def rapaz(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('rapaz.mp3')
        player = voice.play(source)
        await asyncio.sleep(3)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def uepa(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('uepa.mp3')
        player = voice.play(source)
        await asyncio.sleep(2)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def biribo(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('biribo.mp3')
        player = voice.play(source)
        await asyncio.sleep(6)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def scatman(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('scatman.mp3')
        player = voice.play(source)
        await asyncio.sleep(2)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def cenoura(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cenoura.mp3')
        player = voice.play(source)
        await asyncio.sleep(5)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def pitipau(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('pitipau.mp3')
        player = voice.play(source)
        await asyncio.sleep(5)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def suco(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('suco.mp3')
        player = voice.play(source)
        await asyncio.sleep(8)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def cavalo(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cavalo.mp3')
        player = voice.play(source)
        await asyncio.sleep(2)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def cagabombom(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cagabombom.mp3')
        player = voice.play(source)
        await asyncio.sleep(6)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def patrao(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('patrao.mp3')
        player = voice.play(source)
        await asyncio.sleep(6)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def carente(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('rapaz.mp3')
        player = voice.play(source)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def pare(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('pare.mp3')
        player = voice.play(source)
        await asyncio.sleep(2)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def caminhao(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('caminhao.mp3')
        player = voice.play(source)
        await asyncio.sleep(3)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def cuzinho(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cuzinho.mp3')
        player = voice.play(source)
        await asyncio.sleep(4)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def amem(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('amem.mp3')
        player = voice.play(source)
        await asyncio.sleep(1)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def ratinho(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('ratinho.mp3')
        player = voice.play(source)
        await asyncio.sleep(3)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

@client.command(pass_context = True)
async def cuzin(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cuzinho.mp3')
        player = voice.play(source)
        await asyncio.sleep(4)
        await voice.disconnect(force=True)
    else:
        await ctx.send("Para utilizar o bot é necessário estar conectado a um canal de voz")

client.run('OTEyOTA2NTU1NTA5MzQyMjI4.YZ2wew.u5JqbtvRif_Ig5o2JyEWp2Nf5qs')
