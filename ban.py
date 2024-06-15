import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import app_commands, utils


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("I'm ready!")


@bot.tree.command(name="ban", description="Ban User.")
@app_commands.describe(member = "Ban a user.")
@app_commands.describe(reason = "Ban reason.")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: Optional[str]):
    await member.ban(reason=reason)
    await interaction.response.send_message(f"`{member.name}` was banned because `{reason}`.")

#My mail write !xronzen
bot.command()
async def xronzen(ctx):
  await ctx.send("```yaml\nxronzen@proton.me\n```")


bot.run("YOUR TOKEN")
