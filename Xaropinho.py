import discord
from discord.ext import commands
import os

TOKEN = os.environ.get("TOKEN")
AUDIO_FOLDER = "audios"   # pasta onde estão os MP3

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Comando para listar todos os áudios disponíveis
@bot.command()
async def audios(ctx):
    try:
        arquivos = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(".mp3")]
        if not arquivos:
            await ctx.send("❌ Nenhum áudio encontrado na pasta!")
            return
        nomes = [os.path.splitext(f)[0] for f in arquivos]
        await ctx.send("🎵 Áudios disponíveis:\n" + "\n".join(nomes))
    except Exception as e:
        await ctx.send(f"❌ Erro ao listar áudios: {e}")

# Evento para tocar o áudio quando alguém digita !nome_do_audio
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # ignora mensagens de bots

    content = message.content.strip()

    # só processa mensagens que começam com "!"
    if not content.startswith("!"):
        return

    # ignora o comando !audios para não conflitar
    if content.lower() == "!audios":
        await bot.process_commands(message)
        return

    # pega o nome do áudio (sem o "!")
    nome_arquivo = content[1:]

    # caminho do arquivo de áudio
    file_path = os.path.join(AUDIO_FOLDER, f"{nome_arquivo}.mp3")

    if not os.path.exists(file_path):
        await message.channel.send("❌ Áudio não encontrado!")
        return

    # verifica se o autor está em um canal de voz
    if message.author.voice is None:
        await message.channel.send("❌ Você precisa estar em um canal de voz!")
        return

    # deleta a mensagem com o !
    try:
        await message.delete()
    except discord.errors.Forbidden:
        # se o bot não tiver permissão para deletar, ignora
        pass

    # conecta no canal de voz
    channel = message.author.voice.channel
    voice_client = await channel.connect()

    # toca o áudio
    source = discord.FFmpegPCMAudio(file_path)
    voice_client.play(source)

    # espera terminar e desconecta
    while voice_client.is_playing():
        await discord.utils.sleep_until(discord.utils.utcnow())

    await voice_client.disconnect()

    # processa outros comandos caso existam
    await bot.process_commands(message)

bot.run(TOKEN)

