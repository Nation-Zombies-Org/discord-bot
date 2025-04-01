from datetime import datetime, timedelta
from discord.ext import commands, tasks
import discord
import a2s
from datetime import timedelta
from config.settings import SERVER_IP, SERVER_PORT, CHANNEL_ID

class ServerInfoCommand(commands.Cog):
    """Command to display server information automatically every 1 minute."""

    def __init__(self, bot):
        self.bot = bot
        self.last_message = None
        self.server_info_task.start()

    def cog_unload(self):
        self.server_info_task.cancel()

    @tasks.loop(minutes=3)
    async def server_info_task(self):
        """Automatic task to send server information every 1 minute."""
        await self.send_server_info()

    @server_info_task.before_loop
    async def before_server_info_task(self):
        """Wait for the bot to be ready before starting the task."""
        await self.bot.wait_until_ready()

    @commands.command(name="players")
    async def server_info_command(self, ctx):
        """Manual command to display server information."""
        await self.send_server_info(ctx.channel, ctx.message)

    async def send_server_info(self, channel=None, command_message=None):
        """Function to send server information."""
        
        try:
            # See server information
            server_address = (SERVER_IP, SERVER_PORT)
            server_info = a2s.info(server_address)
            player_list = a2s.players(server_address)

            # Server Data
            server_name = server_info.server_name
            game_map = server_info.map_name
            max_players = server_info.max_players
            player_count = len(player_list)

            # Divide players into separate fields
            player_names = []
            player_times = []

            for player in player_list:
                player_names.append(f"👥 {player.name}")
                player_times.append(f"⏰ {str(timedelta(seconds=int(player.duration)))}")

            # Divide into 1024 characters chunks to avoid discord errors
            def split_chunks(data, chunk_size=1024):
                
                chunks = []
                current_chunk = ""
                for item in data:
                    if len(current_chunk) + len(item) + 1 > chunk_size:
                        chunks.append(current_chunk)
                        current_chunk = ""
                    current_chunk += item + "\n"
                if current_chunk:
                    chunks.append(current_chunk)
                return chunks

            player_name_chunks = split_chunks(player_names)
            player_time_chunks = split_chunks(player_times)

            # Create embed with the information
            embed = discord.Embed(
                title=f"🌍 **Server Name: {server_name}**",
                description="**Detailed Server Information:**",
                color=0x2ecc71,
            )
            embed.add_field(name="🗺 Current Map", value=game_map, inline=True)
            embed.add_field(name="📌 Server Address", value=f"`{SERVER_IP}:{SERVER_PORT}`", inline=True)

            embed.add_field(name="👥 Connected Players", value=f"{player_count}/{max_players}", inline=False)            
            embed.add_field(name="─────────────────────────────────────────────────", value="\u200b", inline=False)
            # Add fields to players and times
            for i, (name_chunk, time_chunk) in enumerate(zip(player_name_chunks, player_time_chunks)):
                embed.add_field(name=f"⏰ - TIME: - {i + 1}", value=f"```{time_chunk}```", inline=True)
                embed.add_field(name=f"👥 - PLAYER NAME: - {i + 1}", value=f"```{name_chunk}```", inline=True)

            embed.set_footer(
                text=f"Server Update Time • {datetime.now().strftime('%H:%M:%S')}{f' | Server Version • {server_info.version}' if server_info.version else ''} \nBot Version • 2.2.1",
                icon_url="https://cdn.discordapp.com/attachments/1006072849888464968/1279389095591940219/nationz.gif",
            )
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/1006072849888464968/1279389095591940219/nationz.gif"
            )

            # Send or edit the message on the channel
            if channel is None:
                channel = self.bot.get_channel(CHANNEL_ID)

            if channel:
                if self.last_message:
                    try:
                        await self.last_message.delete()
                    except discord.errors.NotFound:
                        pass
                self.last_message = await channel.send(embed=embed)

            # Delete the command message, if provided
            if command_message:
                try:
                    await command_message.delete()
                except discord.errors.NotFound:
                    pass

        except Exception as e:
            print(f"Error when obtaining server information: {e}")

async def setup(bot):
    await bot.add_cog(ServerInfoCommand(bot))