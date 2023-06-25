from imports import *

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def role_del(interaction):
    # 管理者ロールがない場合は無視
    if not discord.utils.get(interaction.user.roles, name="管理者"):
        embed = discord.Embed(title='このコマンドは管理者のみが実行できます。', color=discord.Colour.purple())
        return embed

    guild = interaction.guild  # 直接interactionオブジェクトからguildを取得
    team_roles = ['チームA', 'チームB', 'チームC', 'チームD', 'チームE', 'チームF']

    for member in guild.members:
        for role in member.roles:
            if role.name in team_roles:
                await member.remove_roles(role)

    embed = discord.Embed(title='全てのチームロールを一括で削除しました。', color=discord.Colour.purple())
    return embed
