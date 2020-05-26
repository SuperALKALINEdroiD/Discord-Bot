const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', async message => {
if (message.content.startsWith("boot")) {
        // Easy way to get member object though mentions.
        var member= message.mentions.members.first();
        // Kick
        await member.kick().then((member) => {
            // Successmessage
            message.channel.send(":wave: " + member.displayName + " has been successfully kicked :point_right: ");
        }).catch(() => {
             // Failmessage
            message.channel.send("Access Denied");
        });
    }
  if (message.content.toLowerCase() === 'hello') {
    message.reply('Hello Buddy!!');
  }
else if(message.content.toLowerCase()==='invite'){
message.reply('https://discord.com/api/oauth2/authorize?client_id=707561126011076733&permissions=67584&scope=bot');
}
});