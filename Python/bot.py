from imports import *

TOKEN = config.cps_TOKEN # カスタム大会bot
# TOKEN = config.kani_TOKEN # 🦀bot

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'ログインしました {bot.user}')

    # ログインメッセージを送信するチャンネルID
    target_channel_id = 1125038838335672352

    # メッセージを送信するチャンネルを取得
    target_channel = bot.get_channel(target_channel_id)

    # メッセージを送信
    if target_channel:
        japan_timezone = pytz.timezone('Asia/Tokyo')
        now = datetime.datetime.now(japan_timezone)
        login_message = f"{now.strftime('%Y年%m月%d日')}{now.strftime('%H:%M:%S')} ログインしました"
        await target_channel.send(login_message)
    else:
        print("指定されたチャンネルが見つかりません。")

    # スラッシュコマンド同期
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期しました。")
    except Exception as e:
        print(e)

@bot.tree.command(name="help",description="コマンドの詳細表示")
async def help(interacion: discord.Interaction):
    embed = await help_embed()
    await interacion.response.send_message(embed=embed)

@bot.tree.command(name="おみくじ", description="運勢を占ってくれるよ。")
async def おみくじ(interaction: discord.Interaction):
    embed = await omikuji(interaction)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="チーム分け", description="チーム分けをしてくれるよ。")
async def チーム分け(interaction: discord.Interaction, role: discord.Role):
    await team(interaction,role)

@bot.tree.command(name="ヒーロー",description="ランダムでヒーローを表示")
async def ヒーロー(interacion: discord.Interaction):
    hero = command.hero.hero
    hero_crb = command.hero.hero_crb

    file2 = random.choice(hero+hero_crb)
    print(file2)

    embed = get_embed_hero(file2)
    await interacion.response.send_message(embed=embed)

@bot.tree.command(name="ステージ",description="ランダムでステージを表示")
async def ステージ(interacion: discord.Interaction):
    file = get_file_stage()
    await interacion.response.send_message(file=file)

@bot.tree.command(name="ロール削除", description="全てのチームロールを一括で削除")
async def ロール削除(interaction: discord.Interaction):
    embed = await role_del(interaction)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ロール",description="ロール回数を表示してくれるよ。")
async def ロール(interaction: discord.Interaction):
    embed = await role_count(interaction)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="使用", description="回数を減らすことができます")
async def 使用(interaction: discord.Interaction, arg: str):
    embed = await role_use(interaction, arg)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="回数リセット", description="回数をリセットすることができます。")
async def 回数リセット(interaction: discord.Interaction):
    embed = await role_reset(interaction)
    await interaction.response.send_message(embed=embed)#(embed=embed, ephemeral=True)

ai_messages = [
    {"role": "system", "content": "You are a helpful assistant. The AI assistant's name is #コンパスカスタム大会bot."},
    {"role": "user", "content": "こんにちは。あなたは誰ですか？"},
    {"role": "assistant", "content": "私は AI アシスタントの #コンパスカスタム大会bot です。なにかお手伝いできることはありますか？"}
]

@bot.event
async def on_message(message):
    if message.author == bot.user:

        return
    if bot.user.id in [member.id for member in message.mentions]:
        print(message.content)
        print(message.content.split('>')[1].lstrip())
        ai_messages.append({"role": "user", "content": message.content.split('>')[1].lstrip()})

        openai_api_key = config.OPENAI_API_KEY
        openai.api_key = openai_api_key

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=ai_messages
        )

        print(completion.choices[0].message.content)
        await message.channel.send(completion.choices[0].message.content)

@bot.command()
async def test(ctx):
    embed = discord.Embed(title="正常に動作しています。",color=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command(name="履歴削除", description="メッセージ履歴を全て削除します。")
async def 履歴削除(ctx):
    channel = ctx.channel
    messages = []
    async for message in channel.history(limit=None):
        messages.append(message)

    for chunk in [messages[i:i+100] for i in range(0, len(messages), 100)]:
        await channel.delete_messages(chunk)

bot.run(TOKEN)