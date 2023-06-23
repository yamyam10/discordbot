from imports import *

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
    embed.add_field(name="",value="`/おみくじ：`運勢を占ってくれるよ。",inline=False)
    embed.add_field(name="",value="`/チーム分け @mention：`ランダムでチーム分け",inline=False)
    embed.add_field(name="",value="`/ヒーロー：`ランダムでヒーローを表示",inline=False)
    embed.add_field(name="",value="`/ステージ：`ランダムでステージを表示",inline=False)
    embed.add_field(name="",value="`/ロール削除：`ロール削除",inline=False)
    embed.add_field(name="",value="`/ロール：`残りロール回数確認",inline=False)
    embed.add_field(name="",value="`/使用 アタッカー, ガンナー, スプリンター, タンク：`指定したロールの回数を減らせる",inline=False)
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

アタッカー = 2
ガンナー = 2
スプリンター = 2
タンク = 2

# ユーザーごとに異なる値を取得するための辞書
user_values = {}

# ユーザーごとにアタッカーの値を取得する関数
def get_attacker_value_for_user(user_id):
    if user_id in user_values:
        return user_values[user_id]["アタッカー"]
    else:
        # ユーザーが存在しない場合、辞書に新しいユーザーを追加する
        user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        return user_values[user_id]["アタッカー"]

# ユーザーごとにガンナーの値を取得する関数
def get_gunner_value_for_user(user_id):
    if user_id in user_values:
        return user_values[user_id]["ガンナー"]
    else:
        # ユーザーが存在しない場合、辞書に新しいユーザーを追加する
        user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        return user_values[user_id]["ガンナー"]

# ユーザーごとにスプリンターの値を取得する関数
def get_sprinter_value_for_user(user_id):
    if user_id in user_values:
        return user_values[user_id]["スプリンター"]
    else:
        # ユーザーが存在しない場合、辞書に新しいユーザーを追加する
        user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        return user_values[user_id]["スプリンター"]

# ユーザーごとにタンクの値を取得する関数
def get_tank_value_for_user(user_id):
    if user_id in user_values:
        return user_values[user_id]["タンク"]
    else:
        # ユーザーが存在しない場合、辞書に新しいユーザーを追加する
        user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        return user_values[user_id]["タンク"]

@bot.tree.command(name="ロール",description="ロール回数を表示してくれるよ。")
async def ロール(interaction: discord.Interaction):
    global アタッカー, ガンナー, スプリンター, タンク
    user = interaction.user
    # ユーザーごとに異なる値を取得する
    アタッカー = get_attacker_value_for_user(user.id)
    ガンナー = get_gunner_value_for_user(user.id)
    スプリンター = get_sprinter_value_for_user(user.id)
    タンク = get_tank_value_for_user(user.id)
    embed = discord.Embed(title=f"<@{interaction.user.id}>さんのロール",color=discord.Colour.purple())
    embed.add_field(name="",value=f"アタッカー: {アタッカー}",inline=False)
    embed.add_field(name="",value=f"ガンナー: {ガンナー}",inline=False)
    embed.add_field(name="",value=f"スプリンター: {スプリンター}",inline=False)
    embed.add_field(name="",value=f"タンク: {タンク}",inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name="使用", description="回数を減らすことができます")
async def 使用(interaction: discord.Interaction, arg: str):
    global アタッカー, ガンナー, スプリンター, タンク, user_values
    user_id = interaction.user.id

    # 各ロールの回数を管理する辞書
    rolls = {"アタッカー": アタッカー, "ガンナー": ガンナー, "スプリンター": スプリンター, "タンク": タンク}
    roll_names = {"アタッカー": "アタッカー", "ガンナー": "ガンナー", "スプリンター": "スプリンター", "タンク": "タンク"}

    if arg in rolls:
        if rolls[arg] > 0:
            # 回数を減らす
            rolls[arg] -= 1
            if user_id in user_values:
                user_values[user_id][arg] = rolls[arg]
            else:
                user_values[user_id] = rolls.copy()
            embed = discord.Embed(title=f'残り回数 {roll_names[arg]}: {rolls[arg]}',color=discord.Colour.purple())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title=f'{roll_names[arg]} はすでに残り回数がありません。',color=discord.Colour.purple())
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title='無効な選択肢です。アタッカー, ガンナー, スプリンター, タンクのどれかを入力してください。',color=discord.Colour.purple())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # 回数が負の値にならないように修正
    アタッカー = max(rolls["アタッカー"], 0)
    ガンナー = max(rolls["ガンナー"], 0)
    スプリンター = max(rolls["スプリンター"], 0)
    タンク = max(rolls["タンク"], 0)

@bot.tree.command(name="回数リセット", description="回数をリセットすることができます。")
async def 回数リセット(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
    embed = discord.Embed(title="回数をリセットしました。",color=discord.Colour.purple())
    await interaction.response.send_message(embed=embed, ephemeral=True)

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