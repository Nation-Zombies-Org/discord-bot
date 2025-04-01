from datetime import datetime, timedelta
from discord.ext import commands
import discord

class VipCommand(commands.Cog):
    """ Command to display VIP information. """

    @commands.command(name="vip")
    async def vip(self, ctx):
        embed = discord.Embed(
            title="🌟 **Be a VIP!**",
            description=(
                "Want to stand out on the server? Become a VIP and enjoy:\n\n"
                "- Early access to new maps\n"
                "- Exclusive items\n"
                "- Priority support\n\n"
                "Contact our team for more information!\n"
                "Or go to our website: [Click Here](https://nationz-server.com/vip)\n"
            ),
            color=0x3498db,
        )
        embed.set_footer(
            text=f"Server Update Time • {datetime.now().strftime('%H:%M:%S')} \nBot Version • 2.2.1",
            icon_url="https://cdn.discordapp.com/attachments/1006072849888464968/1279389095591940219/nationz.gif",
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1006072849888464968/1279389095591940219/nationz.gif"
        )

        await ctx.send(embed=embed)

# Adicionar o comando ao bot
async def setup(bot):
    await bot.add_cog(VipCommand(bot))