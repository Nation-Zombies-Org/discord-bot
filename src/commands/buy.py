from discord.ext import commands
import discord

class BuyCommand(commands.Cog):
    """Comando para exibir informações sobre compra de VIP."""

    @commands.command(name="buy")
    async def buy(self, ctx):
        embed = discord.Embed(
            title="💎 **Compre seu VIP agora!**",
            description=(
                "Aproveite os benefícios exclusivos de ser um jogador VIP!\n\n"
                "**Benefícios:**\n"
                "- Acesso a skins exclusivas\n"
                "- Prioridade na fila do servidor\n"
                "- Comandos especiais no jogo\n\n"
                "**Como comprar:**\n"
                "1. Acesse nosso site: [Clique aqui](https://seusite.com/vip)\n"
                "2. Escolha o plano que mais combina com você\n"
                "3. Finalize a compra e aproveite!"
            ),
            color=0xf1c40f,
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/123456789012345678/your_thumbnail.png")
        embed.set_footer(text="Obrigado por apoiar nosso servidor!", icon_url="https://cdn.discordapp.com/icons/123456789012345678/your_footer_icon.png")

        await ctx.send(embed=embed)

# Adicionar o comando ao bot
async def setup(bot):
    await bot.add_cog(BuyCommand(bot))