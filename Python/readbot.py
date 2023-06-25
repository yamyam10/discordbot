import discord
from discord.ext import commands
from discord import app_commands
from enum import Enum
from gtts import gTTS
import asyncio
import config

TOKEN = config.cps_TOKEN # カスタム大会bot
# TOKEN = config.kani_TOKEN # 🦀bot

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'ログインしました {bot.user}')
    #スラッシュコマンド同期
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期しました。")
    except Exception as e:
        print(e)

@bot.tree.command(name="help",description="コマンドの詳細表示")
async def help(interacion: discord.Interaction):
    embed = discord.Embed(title="コマンド一覧",color=discord.Colour.purple())
    embed.add_field(name="",value="`/help：`コマンド詳細を表示。",inline=False)
    embed.add_field(name="",value="`!読み上げ：`テキストを読み上げ",inline=False)
    embed.add_field(name="",value="`!切断：`ボイスチャンネルから切断する",inline=False)
    await interacion.response.send_message(embed=embed)

@bot.command()
async def test(ctx):
    embed = discord.Embed(title="正常に動作しています。",color=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command(name="読み上げ", description="メッセージを読み上げ")
async def read_message(ctx):

    if not ctx.author.voice:
        await ctx.send("ボイスチャンネルに接続してください")
        return

    # メッセージを送信するためのEmbedオブジェクトを作成する
    embed = discord.Embed(title="読み上げ", url="https://twitter.com/miyavi1117?s=20", color=discord.Color.purple())
    embed.add_field(name="", value="ボイスチャットの接続に成功しました", inline=False)
    embed.add_field(name="読み上げテキストチャンネル", value=ctx.channel.mention, inline=False)
    embed.add_field(name="読み上げボイスチャンネル", value=ctx.author.voice.channel.mention, inline=False)

    # Embedメッセージを送信する
    await ctx.send(embed=embed)

    vc = await ctx.author.voice.channel.connect()
    try:
        while True:
            message = await bot.wait_for('message', check=lambda m: m.channel == ctx.channel)
            print(f"Received message: {message.content}")
            if message.author.bot:
                continue  # ボットによるメッセージは無視する
            if not message.content:
                continue  # 空のメッセージは無視する

            try:
                tts = gTTS(text=message.content, lang='ja')
                tts.save("voice.mp3")
            except Exception as e:
                print(e)
                continue

            vc.play(discord.FFmpegPCMAudio("voice.mp3"))
            while vc.is_playing():
                await asyncio.sleep(1)

            # ボイスチャンネルから切断する
            if len(vc.channel.members) == 1:
                await vc.disconnect()
                break
    finally:
        await vc.disconnect()

@bot.command(name="切断", description="ボイスチャンネルから切断")
async def disconnect(ctx):
    if not ctx.voice_client:
        embed = discord.Embed(title="ボイスチャンネルに接続していません", color=discord.Color.purple())
        await ctx.send(embed=embed)
        return

    await ctx.voice_client.disconnect()
    embed = discord.Embed(title="読み上げ", url="https://twitter.com/miyavi1117?s=20", color=discord.Color.purple())
    embed.add_field(name="", value="ボイスチャンネルから切断に成功しました", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)