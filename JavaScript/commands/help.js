const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('help')
		.setDescription('コマンドの詳細表示'),
	async execute(interaction) {
		const embed = new discord.MessageEmbed()
			.setTitle('コマンド一覧')
			.setColor(discord.Color.PURPLE)
			.addField('/help', 'コマンド詳細を表示。')
			.addField('/おみくじ', '運勢を占ってくれるよ。')
			.addField('/チーム分け @mention', 'ランダムでチーム分け')
			.addField('/ヒーロー', 'ランダムでヒーローを表示')
			.addField('/ステージ', 'ランダムでステージを表示')
			.addField('/ロール削除', 'ロール削除')
			.addField('/ロール', '残りロール回数確認')
			.addField('/使用 アタッカー, ガンナー, スプリンター, タンク', '指定したロールの回数を減らせる')
			.addField('/回数リセット', 'ロール回数をリセットすることができます。');
		await interaction.reply({ embeds: [embed] });
	},
};
