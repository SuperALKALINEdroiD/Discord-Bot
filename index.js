const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.toLowerCase() === 'hello') {
    msg.reply('Hello Buddy!!');
  }
else if(msg.content.toLowerCase()==='invite'){
msg.reply('https://discord.com/api/oauth2/authorize?client_id=707561126011076733&permissions=67584&scope=bot');
}
});
