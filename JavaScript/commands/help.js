const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('help')
		.setDescription('コマンドの詳細表示'),
	execute: async function(interaction) {
		await interaction.reply({
			embeds: [{
				color: 0x9C59B6,
				fields: [
					{
						name: "",
						value: "`/help：`コマンド詳細を表示。",
						// inline: False
					},
					{
						name: "",
						value: "`/おみくじ：`運勢を占ってくれるよ。"
					},
					{
						name: "",
						value: "`/チーム分け @mention：`ランダムでチーム分け"
					},
					{
						name: "",
						value: "`/ヒーロー：`ランダムでヒーローを表示",
					},
					{
						name: "",
						value: "`/ステージ：`ランダムでステージを表示",
					},
					{
						name: "",
						value: "`/ロール削除：`ロール削除",
					},
					{
						name: "",
						value: "`/ロール：`残りロール回数確認",
					},
					{
						name: "",
						value: "`/使用 アタッカー, ガンナー, スプリンター, タンク：`指定したロールの回数を減らせる",
					},
					{
						name: "",
						value: "`/回数リセット：`ロール回数をリセットすることができます。",
					}
				]
			}]
		});
	},
};