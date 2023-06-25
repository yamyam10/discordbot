from imports import *

OMIKUJI_RESULTS = [
    (0.0, 0.0, "大凶", 0.05),
    (1.0, 199.0, "吉", 0.2),
    (200.0, 399.0, "中吉", 0.3),
    (400.0, 499.0, "小吉", 0.15),
    (500.0, 979.0, "末吉", 0.25),
    (980.0, 999.9, "大吉", 0.1),
]

async def omikuji(interaction):
    result = random.uniform(0, 1)
    cumulative_probability = 0.0

    for omikuji_range in OMIKUJI_RESULTS:
        start, end, title, probability = omikuji_range
        cumulative_probability += probability
        if result < cumulative_probability:
            embed = discord.Embed(title=f'{interaction.user.mention} さんの運勢は「{title}」です！', color=discord.Colour.purple())
            return embed
    else:
        # 範囲外の場合はエラーメッセージを送信する
        embed = discord.Embed(title="ERROR", color=discord.Colour.purple())
        return embed