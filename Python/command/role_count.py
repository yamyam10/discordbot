from imports import *
import json

data_file = "data.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

def get_attacker_value_for_user(user_id):
    data = load_data()  # 追加
    if str(user_id) in data:
        return data[user_id].get("アタッカー", 2)
    else:
        data[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        save_data(data)
        return data[user_id]["アタッカー"]

def get_gunner_value_for_user(user_id):
    data = load_data()  # 追加
    if str(user_id) in data:
        return data[user_id].get("ガンナー", 2)
    else:
        data[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        save_data(data)
        return data[user_id]["ガンナー"]

def get_sprinter_value_for_user(user_id):
    data = load_data()  # 追加
    if str(user_id) in data:
        return data[user_id].get("スプリンター", 2)
    else:
        data[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        save_data(data)
        return data[user_id]["スプリンター"]

def get_tank_value_for_user(user_id):
    data = load_data()  # 追加
    if str(user_id) in data:
        return data[user_id].get("タンク", 2)
    else:
        data[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        save_data(data)
        return data[user_id]["タンク"]

async def role_count(interaction):
    global data

    user_id = interaction.user.id

    if str(user_id) in data:
        id_data = str(user_id)
        a_value = data[id_data]["\u30a2\u30bf\u30c3\u30ab\u30fc"]
        g_value = data[id_data]["\u30ac\u30f3\u30ca\u30fc"]
        s_value = data[id_data]["\u30b9\u30d7\u30ea\u30f3\u30bf\u30fc"]
        t_value = data[id_data]["\u30bf\u30f3\u30af"]

        アタッカー = (a_value)
        ガンナー = (g_value)
        スプリンター = (s_value)
        タンク = (t_value)
    else:
        data[user_id] = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}
        save_data(data)
        アタッカー = 2
        ガンナー = 2
        スプリンター = 2
        タンク = 2

    embed = discord.Embed(title=f"<@{user_id}>さんのロール", color=discord.Colour.purple())
    embed.add_field(name="", value=f"アタッカー: {アタッカー}", inline=False)
    embed.add_field(name="", value=f"ガンナー: {ガンナー}", inline=False)
    embed.add_field(name="", value=f"スプリンター: {スプリンター}", inline=False)
    embed.add_field(name="", value=f"タンク: {タンク}", inline=False)
    return embed



async def role_use(interaction, arg):
    global data

    user_id = interaction.user.id

    if str(user_id) in data:
        rolls = data[str(user_id)]
    else:
        rolls = {"アタッカー": 2, "ガンナー": 2, "スプリンター": 2, "タンク": 2}

    roll_names = {"アタッカー": "アタッカー", "ガンナー": "ガンナー", "スプリンター": "スプリンター", "タンク": "タンク"}

    if arg in rolls:
        if rolls[arg] > 0:
            rolls[arg] -= 1
            data[user_id] = rolls
            save_data(data)
            embed = discord.Embed(title=f'残り回数 {roll_names[arg]}: {rolls[arg]}', color=discord.Colour.purple())
            return embed
        else:
            embed = discord.Embed(title=f'{roll_names[arg]} はすでに残り回数がありません。', color=discord.Colour.purple())
            return embed
    else:
        embed = discord.Embed(title='無効な選択肢です。アタッカー、ガンナー、スプリンター、タンクのどれかを入力してください。', color=discord.Colour.purple())
        return embed

async def role_reset(interaction):
    global data

    user_id = interaction.user.id
    if str(user_id) in data:
        del data[user_id]
        save_data(data)
    embed = discord.Embed(title="回数をリセットしました。", color=discord.Colour.purple())
    return embed
