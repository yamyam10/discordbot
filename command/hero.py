from imports import *

clr = [
    0xfa3d2a,
    0x2854a6,
    0xf33d8e,
    0xa2009e,
    0x92d400,
    0xae9100,
    0xa66400,
    0x323f3e,
    0x002ea2,
    0xd5281d,
    0x4d2275,
    0xf6c230,
    0x554230,
    0x33b5b2,
    0x61001f,
    0x3295b6,
    0x121212,
    0x4148d8,
    0xfca3b7,
    0xc56b4a,
    0xa60200,
    0x504040,
    0xcbc7c3,
    0xbd9bf0,
    0x7596bf,
    0xcfff00,
    0xff8b18,
    0xae78da,
    0xa887a8,
    0x9a0404,
    0x65a3de,
    0x65a3de,
    0xe35479,
    0x817a8d,
    0x132832,
    0x00956d,
    0xf75096,
    0xa239b7,
    0xA597E2
    ]

clr_crb = [
    0x990c02,
    0x3acd5c,
    0xaf4400,
    0x0086a9,
    0x8e60aa,
    0x5181c7,
    0x283e69,
    0xe2e27c,
    0xe2e27c,
    0x330a0a,
    0x000000,
    0x75c8e0,
    0xc74438,
    0xb3a379,
    0xf97d00,
    0xff9600,
    0x202130,
    0xe3b100,
    0xfbd3d3,
    0x5871bb,
    0x969da2,
    0x9d9d94,
    0x675f6d,
    0xe7c559,
    0xe02323,
    0x302e38,
    0x9e9b9a,
    0xe9e9f1,
    0xd35d86,
    0xb2af9a,
    0x5db0cf,
    0xffc155,
    0x8e95a6,
    0x5177A2,
    0xBFCAF7
    ]

hero = [
    "十文字 アタリ",
    "ジャスティス ハンコック",
    "リリカ",
    "双挽 乃保",
    "桜華 忠臣",
    "ジャンヌ ダルク",
    "マルコス'55",
    "ルチアーノ",
    "Voidoll",
    "深川 まとい",
    "グスタフ ハイドリヒ",
    "ニコラ テスラ",
    "ヴィオレッタ ノワール",
    "コクリコット ブランシュ",
    "マリア=S=レオンブルク",
    "アダム=ユーリエフ",
    "13†サーティーン†",
    "かけだし勇者",
    "メグメグ",
    "イスタカ",
    "輝龍院 きらら",
    "ヴィーナス ポロロッチョ",
    "ソーン=ユーリエフ",
    "デビルミント鬼龍 デルミン",
    "トマス",
    "零夜",
    "ルルカ",
    "ピエール 77世",
    "狐ヶ咲 甘色",
    "HM-WA100 ニーズヘッグ",
    "ゲームバズーカガール",
    "青春 アリス",
    "イグニス=ウィル=ウィスプ",
    "糸廻 輪廻",
    "Bugdoll",
    "ステリア・ララ・シルワ",
    "ラヴィ・シュシュマルシュ",
    "アル・ダハブ=アルカティア",
    "天空王 ぶれいずどらごん"
]

hero_crb = [
    "ソル=バッドガイ",
    "ディズィー",
    "リュウ",
    "春麗",
    "エミリア",
    "レム",
    "カイ=キスク",
    "鏡音 リン",
    "鏡音 レン",
    "ザック＆レイチェル",
    "モノクマ",
    "アクア",
    "めぐみん",
    "リヴァイ",
    "猫宮 ひなた",
    "岡部 倫太郎",
    "セイバーオルタ",
    "ギルガメッシュ",
    "佐藤四郎兵衛忠信",
    "アイズ・ヴァレンシュタイン",
    "ノクティス",
    "中島 敦",
    "芥川 龍之介",
    "ライザリン・シュタウト",
    "ジョーカー",
    "アインズ・ウール・ゴウン",
    "キリト",
    "アスナ",
    "ラム",
    "2B",
    "リムル=テンペスト",
    "御坂 美琴",
    "アクセラレータ",
    "ベル・クラネル",
    "ロキシー・ミグルディア"
]

file2 = random.choice(hero+hero_crb)

def get_embed_hero(file2):
    if file2==hero[0]:
        embed = discord.Embed(title="",color=clr[0])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079589000899215510/atari.jpg"
        )
    elif file2==hero[1] :
        embed = discord.Embed(title="",color=clr[1])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079591675237765151/BA95BD5E-6BBB-4595-895D-E8899B274F8C.jpg"
        )
    elif file2==hero[2] :
        embed = discord.Embed(title="",color=clr[2])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079592519316283402/976856A4-E9DB-47E8-AB0C-3577E11C8874.jpg"
        )
    elif file2==hero[3] :
        embed = discord.Embed(title="",color=clr[3])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079592519794442240/A12A575D-6ED1-48D5-ACFA-D73CF3777673.jpg"
        )
    elif file2==hero[4] :
        embed = discord.Embed(title="",color=clr[4])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079592520176107540/BBC71FFC-3B20-42A6-984C-E6A0A7B29B61.jpg"
        )
    elif file2==hero[5] :
        embed = discord.Embed(title="",color=clr[5])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079592520503271484/38456329-3174-4B6A-92F4-4224617E701F.jpg"
        )
    elif file2==hero[6] :
        embed = discord.Embed(title="",color=clr[6])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079595693527805983/FACDB93C-0161-47C9-BE73-A2B2A6385F16.jpg"
        )
    elif file2==hero[7] :
        embed = discord.Embed(title="",color=clr[7])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079595755431538708/3D8ECCD0-BACB-4FB7-A25A-94ED406181CC.jpg"
        )
    elif file2==hero[8] :
        embed = discord.Embed(title="",color=clr[8])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079595767561470093/102C116C-532D-487A-8713-13D695E296E1.jpg"
        )
    elif file2==hero[9] :
        embed = discord.Embed(title="",color=clr[9])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079595777791369296/34143245-6B32-4CE8-8CFE-EC94C519BFC9.jpg"
        )
    elif file2==hero[10] :
        embed = discord.Embed(title="",color=clr[10])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079596135842324500/14571E65-24EF-4794-8C21-680F7BC4E65B.jpg"
        )
    elif file2==hero[11] :
        embed = discord.Embed(title="",color=clr[11])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079596200996655214/A7A96801-215D-492A-9CDF-99D6C21EFC29.jpg"
        )
    elif file2==hero[12] :
        embed = discord.Embed(title="",color=clr[12])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079596490978246706/07D8826E-C841-42A8-9DA1-588E499F4247.jpg"
        )
    elif file2==hero[13] :
        embed = discord.Embed(title="",color=clr[13])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079596685136777247/3686F67D-5A3A-4BC2-8B25-CD344C6A17D5.jpg"
        )
    elif file2==hero[14] :
        embed = discord.Embed(title="",color=clr[14])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079597242719154246/53F87257-5954-4158-B45D-29244216DBF4.jpg"
        )
    elif file2==hero[15] :
        embed = discord.Embed(title="",color=clr[15])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079597086842028044/038D0708-B29D-4FE4-9B8F-CBC3FA4B419B.jpg"
        )
    elif file2==hero[16] :
        embed = discord.Embed(title="",color=clr[16])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079598471520206958/41295EA9-09D7-4C51-A200-B93E3961BB71.jpg"
        )
    elif file2==hero[17] :
        embed = discord.Embed(title="",color=clr[17])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079598665141866537/B05EA783-5599-4C0E-BB4E-8FD721868490.jpg"
        )
    elif file2==hero[18] :
        embed = discord.Embed(title="",color=clr[18])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079598919882899526/56D4234A-3539-45A2-BE82-21C416E38E22.jpg"
        )
    elif file2==hero[19] :
        embed = discord.Embed(title="",color=clr[19])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079599439955628153/AD67E48A-B185-46F6-8B5D-59F27D9EB9F9.jpg"
        )
    elif file2==hero[20] :
        embed = discord.Embed(title="",color=clr[20])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079599695522967552/77F10B37-107E-4E5A-9771-BE7B898F73F3.jpg"
        )
    elif file2==hero[21] :
        embed = discord.Embed(title="",color=clr[21])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079600163171074139/57F081B3-96A5-4754-B855-53B27A759426.jpg"
        )
    elif file2==hero[22] :
        embed = discord.Embed(title="",color=clr[22])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079600174587969606/7A9EF4DF-8868-42E7-8D3E-C0CDC80BD789.jpg"
        )
    elif file2==hero[23] :
        embed = discord.Embed(title="",color=clr[23])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079600185958731836/5DC7B221-9E48-4827-96C0-65E7B9BC9516.jpg"
        )
    elif file2==hero[24] :
        embed = discord.Embed(title="",color=clr[24])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079600198021550120/FAE82E6F-EBC7-43A2-A696-5EB25F87F1FC.jpg"
        )
    elif file2==hero[25] :
        embed = discord.Embed(title="",color=clr[25])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601008646295562/170A967F-906B-4627-B183-1F391F225E3C.jpg"
        )
    elif file2==hero[26] :
        embed = discord.Embed(title="",color=clr[26])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601022823051274/92E07745-0A38-4C41-91F5-9BEA36AE3F10.jpg"
        )
    elif file2==hero[27] :
        embed = discord.Embed(title="",color=clr[27])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601037830258699/59B863FF-AC8F-4CC0-9A8D-5B04A2D1772E.jpg"
        )
    elif file2==hero[28] :
        embed = discord.Embed(title="",color=clr[28])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601051902148618/E5FE6584-B68F-4E09-A7ED-B114C5ED9BEF.jpg"
        )
    elif file2==hero[29] :
        embed = discord.Embed(title="",color=clr[29])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601064875134996/34375C22-971D-41D0-A684-A34A548EFE4E.jpg"
        )
    elif file2==hero[30] :
        embed = discord.Embed(title="",color=clr[30])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601912149708881/74304C6F-F6CA-41FB-9965-D74ED35B6313.jpg"
        )
    elif file2==hero[31] :
        embed = discord.Embed(title="",color=clr[31])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601960979792002/435D51B5-2C5C-4BC7-8671-A16B4A4A5C84.jpg"
        )
    elif file2==hero[32] :
        embed = discord.Embed(title="",color=clr[32])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079602285946093578/AD86981E-94B1-4774-AAE7-5416E12875C1.jpg"
        )
    elif file2==hero[33] :
        embed = discord.Embed(title="",color=clr[33])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079601997046632548/5167C0AA-6D15-4BB9-80D4-EC0C9EE6C0D2.jpg"
        )
    elif file2==hero[34] :
        embed = discord.Embed(title="",color=clr[34])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079602677048156242/38D6EF6C-8DE4-4A44-9E4B-87423F860554.jpg"
        )
    elif file2==hero[35] :
        embed = discord.Embed(title="",color=clr[35])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079602677362737152/D72FBFEB-CE47-4072-B596-2A09C1280354.jpg"
        )
    elif file2==hero[36] :
        embed = discord.Embed(title="",color=clr[36])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079602677677314098/932678DD-F687-40CD-8441-4C033EB378C5.jpg"
        )
    elif file2==hero[37] :
        embed = discord.Embed(title="",color=clr[37])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1079602677928960010/D6E27199-0E19-4637-A1D7-90B9A95FA24D.jpg"
        )
    elif file2==hero[38] :
        embed = discord.Embed(title="",color=clr[38])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1121659070395461703/0C97927B-6B91-41A8-AAB5-2810CE7DA9B2.jpg"
        )
    elif file2==hero_crb[0] :
        embed = discord.Embed(title="",color=clr_crb[0])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081092479538962483/FF21B5E4-DE3A-430D-896D-8F4D3B7CF769.jpg"
        )
    elif file2==hero_crb[1] :
        embed = discord.Embed(title="",color=clr_crb[1])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081092479778029589/6EF61A45-2A9B-45D1-92DC-F5D5A4F9720A.jpg"
        )
    elif file2==hero_crb[2] :
        embed = discord.Embed(title="",color=clr_crb[2])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081093082172366888/6F30A250-5D32-4A08-ABE4-37129EB1A2E2.jpg"
        )
    elif file2==hero_crb[3] :
        embed = discord.Embed(title="",color=clr_crb[3])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081093082382090301/E1F5305C-974F-42E1-B917-408060CE5A23.jpg"
        )
    elif file2==hero_crb[4] :
        embed = discord.Embed(title="",color=clr_crb[4])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081094398319792138/6E39E36C-5077-4922-A4CC-6908930B74ED.jpg"
        )
    elif file2==hero_crb[5] :
        embed = discord.Embed(title="",color=clr_crb[5])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081094398500151337/3DBF1716-A368-444D-8999-B5504760986D.jpg"
        )
    elif file2==hero_crb[6] :
        embed = discord.Embed(title="",color=clr_crb[6])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095042615234660/7163B2DF-A787-4F4F-8D00-E044B3D1958E.jpg"
        )
    elif file2==hero_crb[7] :
        embed = discord.Embed(title="",color=clr_crb[7])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095136865431602/02D98176-0F1E-40D9-B160-988E8846F71C.jpg"
        )
    elif file2==hero_crb[8] :
        embed = discord.Embed(title="",color=clr_crb[8])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095137096110100/2568DC7F-CDCB-4988-BDD7-1A69C0558788.jpg"
        )
    elif file2==hero_crb[9] :
        embed = discord.Embed(title="",color=clr_crb[9])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095284475576390/B9CC908C-9CD2-48EC-9EA8-71CED671BA60.jpg"
        )
    elif file2==hero_crb[10] :
        embed = discord.Embed(title="",color=clr_crb[10])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095284760784906/782A56F7-F2EF-430E-B390-EC290CC594C9.jpg"
        )
    elif file2==hero_crb[11] :
        embed = discord.Embed(title="",color=clr_crb[11])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095938963156992/79785A83-792A-45DC-866F-1163244A5904.jpg"
        )
    elif file2==hero_crb[12] :
        embed = discord.Embed(title="",color=clr_crb[12])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081095939164471366/5625D206-69F3-493C-BA9B-915CBA01B497.jpg"
        )
    elif file2==hero_crb[13] :
        embed = discord.Embed(title="",color=clr_crb[13])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096059671035904/7A829830-C950-4266-B1EF-E9F7996A3B18.jpg"
        )
    elif file2==hero_crb[14] :
        embed = discord.Embed(title="",color=clr_crb[14])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096059926884373/DDDB002F-ED28-4A91-AFA9-581B8599AB81.jpg"
        )
    elif file2==hero_crb[15] :
        embed = discord.Embed(title="",color=clr_crb[15])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096076817346611/8113B66F-F1BC-4554-9E8E-57ECE0AF622A.jpg"
        )
    elif file2==hero_crb[16] :
        embed = discord.Embed(title="",color=clr_crb[16])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096784446763128/16A1F7A9-A1D9-4B42-8A14-F19416A2A727.jpg"
        )
    elif file2==hero_crb[17] :
        embed = discord.Embed(title="",color=clr_crb[17])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096784673243177/9692E191-C827-4265-815E-268CB318A71C.jpg"
        )
    elif file2==hero_crb[18] :
        embed = discord.Embed(title="",color=clr_crb[18])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096945709359104/18EB4604-EB18-475B-BA0A-0D1E1EB2E6C0.jpg"
        )
    elif file2==hero_crb[19] :
        embed = discord.Embed(title="",color=clr_crb[19])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096945952636968/F80B078B-751A-49EE-B766-28B674DF14DC.jpg"
        )
    elif file2==hero_crb[20] :
        embed = discord.Embed(title="",color=clr_crb[20])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081096946162339870/BAAD2116-C89E-40E0-92B3-3A4CDACD4082.jpg"
        )
    elif file2==hero_crb[21] :
        embed = discord.Embed(title="",color=clr_crb[21])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081097631780053094/541800CF-E82B-4558-ABC5-AC2653269988.jpg"
        )
    elif file2==hero_crb[22] :
        embed = discord.Embed(title="",color=clr_crb[22])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081097631993954355/D85C2F03-8BC6-445A-83A0-7EA934AB4423.jpg"
        )
    elif file2==hero_crb[23] :
        embed = discord.Embed(title="",color=clr_crb[23])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081097771899166780/F2A0CC43-5007-4EE9-A15F-794499654D16.jpg"
        )
    elif file2==hero_crb[24] :
        embed = discord.Embed(title="",color=clr_crb[24])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081097772163403886/07B5032A-66A4-4DD0-8E79-2368F41E2DE2.jpg"
        )
    elif file2==hero_crb[25] :
        embed = discord.Embed(title="",color=clr_crb[25])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098716737458236/832C33BD-3880-48AB-B407-5EA0166C867F.jpg"
        )
    elif file2==hero_crb[26] :
        embed = discord.Embed(title="",color=clr_crb[26])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098716976517121/2532B52B-3495-4B3A-9AB5-4B239147EF83.jpg"
        )
    elif file2==hero_crb[27] :
        embed = discord.Embed(title="",color=clr_crb[27])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098851496243310/83B3BD0C-7064-40BD-AA60-7F4F71CC4CE3.jpg"
        )
    elif file2==hero_crb[28] :
        embed = discord.Embed(title="",color=clr_crb[28])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098851710160986/B9120F36-8131-4444-B4E6-82DC0A170A35.jpg"
        )
    elif file2==hero_crb[29] :
        embed = discord.Embed(title="",color=clr_crb[29])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098974649393172/434F0391-7A64-45CA-AAF3-3DC4CD8E6BE5.jpg"
        )
    elif file2==hero_crb[30] :
        embed = discord.Embed(title="",color=clr_crb[30])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081098974871699476/C9AB6B72-EEAA-40F2-AB97-72FA4959C40A.jpg"
        )
    elif file2==hero_crb[31] :
        embed = discord.Embed(title="",color=clr_crb[31])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081099102395310172/463C6689-A955-4112-AC17-A5913C1D9346.jpg"
        )
    elif file2==hero_crb[32] :
        embed = discord.Embed(title="",color=clr_crb[32])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1081099102613418004/3762CDA0-E252-4726-BC79-90903CCEB20E.jpg"
        )
    elif file2==hero_crb[33] :
        embed = discord.Embed(title="",color=clr_crb[33])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1121661538831446066/F10806AC-75BA-4B47-B4B7-B1B76B4075C7.jpg"
        )
    elif file2==hero_crb[34] :
        embed = discord.Embed(title="",color=clr_crb[34])
        embed.set_author(
        name=file2,
        icon_url="https://cdn.discordapp.com/attachments/688378324342669333/1121661547157139467/D6E33CE6-FF8C-4BA7-9B48-95B93EACBC4D.jpg"
        )
    # await interacion.response.send_message(embed=embed)
    return embed