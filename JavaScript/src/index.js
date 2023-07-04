const heyFile = require('../commands/hey.js');
const helpFile = require('../commands/help.js');
const embedFile = require('../commands/embed.js');
const heroFile = require('../commands/hero.js');

const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('../config.json');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once('ready', async () => {
    console.log(`ログインしました ${client.user.tag}`);
  
    // ログインメッセージを送信するチャンネルID
    const targetChannelId = '1125252464501862440';
  
    // メッセージを送信するチャンネルを取得
    const targetChannel = client.channels.cache.get(targetChannelId);
  
    // メッセージを送信
    if (targetChannel) {
      const japanTimezone = 'Asia/Tokyo';
      const now = new Date().toLocaleString('ja-JP', { timeZone: japanTimezone });
      const loginMessage = `${now} ログインしました`;
      targetChannel.send(loginMessage);
    } else {
      console.log("指定されたチャンネルが見つかりません。");
    }
  });
  

client.on(Events.InteractionCreate, async interaction => {

    if (!interaction.isChatInputCommand()) return;

    if (interaction.commandName === heyFile.data.name) {
        try {
            await heyFile.execute(interaction);
        } catch (error) {
            console.error(error);
            if (interaction.replied || interaction.deferred) {
                await interaction.followUp({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            } else {
                await interaction.reply({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            }
        }
    } else {
        console.error(`${interaction.commandName}というコマンドには対応していません。`);
    }

    if (interaction.commandName === embedFile.data.name) {
        try {
            await embedFile.execute(interaction);
        } catch (error) {
            console.error(error);
            if (interaction.replied || interaction.deferred) {
                await interaction.followUp({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            } else {
                await interaction.reply({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            }
        }
    } else {
        console.error(`${interaction.commandName}というコマンドには対応していません。`);
    }

    if (interaction.commandName === heroFile.data.name) {
        try {
            await heroFile.execute(interaction);
        } catch (error) {
            console.error(error);
            if (interaction.replied || interaction.deferred) {
                await interaction.followUp({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            } else {
                await interaction.reply({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            }
        }
    } else {
        console.error(`${interaction.commandName}というコマンドには対応していません。`);
    }

    if (interaction.commandName === helpFile.data.name) {
        try {
            await helpFile.execute(interaction);
        } catch (error) {
            console.error(error);
            if (interaction.replied || interaction.deferred) {
                await interaction.followUp({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            } else {
                await interaction.reply({ content: 'コマンド実行時にエラーになりました。', ephemeral: true });
            }
        }
    } else {
        console.error(`${interaction.commandName}というコマンドには対応していません。`);
    }
});

// ログインします
client.login(token);