const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('ヒーロー')
		.setDescription('ランダムでヒーローを表示'),
	execute: async function (interacion) {
		const clr = [
			0xfa3d2a,
			0x2854a6,
			0xf33d8e,
		];
		
		const clr_crb = [
			0x990c02,
			0x3acd5c,
			0xaf4400,
		];
		
		const hero = [
			"十文字 アタリ",
			"ジャスティス ハンコック",
			"リリカ",
		];
		
		const hero_crb = [
			"ソル=バッドガイ",
			"ディズィー",
			"リュウ",
		];
		
		const file2 = hero.concat(hero_crb)[Math.floor(Math.random() * (hero.length + hero_crb.length))];
		console.log(file2);
		
		let embed;
		if (file2 === hero[0]) {
			embed = {
			title: "",
			color: clr[0],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1079589000899215510/atari.jpg",
			},
			};
		} else if (file2 === hero[1]) {
			embed = {
			title: "",
			color: clr[1],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1079591675237765151/BA95BD5E-6BBB-4595-895D-E8899B274F8C.jpg",
			},
			};
		} else if (file2 === hero[2]) {
			embed = {
			title: "",
			color: clr[2],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1079592519316283402/976856A4-E9DB-47E8-AB0C-3577E11C8874.jpg",
			},
			};
		} else if (file2 === hero_crb[0]) {
			embed = {
			title: "",
			color: clr_crb[0],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1081092479538962483/FF21B5E4-DE3A-430D-896D-8F4D3B7CF769.jpg",
			},
			};
		} else if (file2 === hero_crb[1]) {
			embed = {
			title: "",
			color: clr_crb[1],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1081092479778029589/6EF61A45-2A9B-45D1-92DC-F5D5A4F9720A.jpg",
			},
			};
		} else if (file2 === hero_crb[2]) {
			embed = {
			title: "",
			color: clr_crb[2],
			author: {
				name: file2,
				icon_url: "https://cdn.discordapp.com/attachments/688378324342669333/1081093082172366888/6F30A250-5D32-4A08-ABE4-37129EB1A2E2.jpg",
			},
			};
		}
		
		await interacion.response.send_message({ embeds: [embed] });
		}
		
	};