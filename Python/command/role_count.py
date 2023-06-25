from imports import *

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

async def role_count(interaction):
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
    return embed

async def role_use(interaction, arg):
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
            return embed
        else:
            embed = discord.Embed(title=f'{roll_names[arg]} はすでに残り回数がありません。',color=discord.Colour.purple())
            return embed
    else:
        embed = discord.Embed(title='無効な選択肢です。アタッカー, ガンナー, スプリンター, タンクのどれかを入力してください。',color=discord.Colour.purple())
        # 回数が負の値にならないように修正
        アタッカー = max(rolls["アタッカー"], 0)
        ガンナー = max(rolls["ガンナー"], 0)
        スプリンター = max(rolls["スプリンター"], 0)
        タンク = max(rolls["タンク"], 0)
        return embed

async def role_reset(interaction):
    user_id = interaction.user.id
    user_values[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
    embed = discord.Embed(title="回数をリセットしました。",color=discord.Colour.purple())
    return embed