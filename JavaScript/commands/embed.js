const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('embed2')
		.setDescription('botがembedを返事します'),
	execute: async function(interaction) {
		await interaction.reply({
			embeds: [{
				author: {
					name: "author name",
					url: "https://discordapp.com",
					icon_url: "https://cdn.discordapp.com/embed/avatars/0.png"
				},
				title: "タイトル",
				url: "https://discordapp.com",
				description: "This is description. [URLを埋め込むことも出来る](https://discordapp.com)\n" +
					"***embedの中でもMarkDownを利用できます***",
				color: 7506394,
				timestamp: new Date(),
				footer: {
					icon_url: interaction.client.user.avatarURL(),
					text: "©️ example | footer text"
				},
				thumbnail: {
					url: "https://cdn.discordapp.com/embed/avatars/0.png"
				},
				image: {
					url: "https://cdn.discordapp.com/embed/avatars/0.png"
				},
				fields: [
					{
						name: "field :one:",
						value: "*ここはfield 1の内容だよ*"
					},
					{
						name: "field :two:",
						value: "~~ここはfield 2の内容だよ~~"
					},
					{
						name: "field :three:",
						value: "__ここはfield 3の内容だよ__"
					},
					{
						name: "inline field :cat:",
						value: "`これはinlineのfieldだよ`",
						inline: true
					},
					{
						name: "inline field :dog:",
						value: "[これもinlineのfieldだよ](https://discordapp.com)",
						inline: true
					}
				]
			}]
		});
	},
};
