from imports import *

async def help_embed():
    embed = discord.Embed(title="コマンド一覧",color=discord.Colour.purple())
    embed.add_field(name="",value="`/help：`コマンド詳細を表示。",inline=False)
    embed.add_field(name="",value="`/おみくじ：`運勢を占ってくれるよ。",inline=False)
    embed.add_field(name="",value="`/チーム分け @mention：`ランダムでチーム分け",inline=False)
    embed.add_field(name="",value="`/ヒーロー：`ランダムでヒーローを表示",inline=False)
    embed.add_field(name="",value="`/ステージ：`ランダムでステージを表示",inline=False)
    embed.add_field(name="",value="`/ロール削除：`ロール削除",inline=False)
    embed.add_field(name="",value="`/ロール：`残りロール回数確認",inline=False)
    embed.add_field(name="",value="`/使用 アタッカー, ガンナー, スプリンター, タンク：`指定したロールの回数を減らせる",inline=False)
    embed.add_field(name="",value="`/回数リセット：`ロール回数をリセットすることができます。",inline=False)
    return embed