import discord, json, keep_alive, asyncio, random, os, sys, datetime, time, traceback
from discord.ext import commands
from datetime import datetime
now = datetime.now

with open('config.json') as f:
  config = json.load(f)
token = config.get('token')
prefix = config.get("prefix")
gen_only_channel = (config.get("gen_only_channel"))
owner = (config.get("owner"))

intents = discord.Intents().all()
genbot = commands.Bot(command_prefix=f'{prefix}', intents=intents)
genbot.remove_command('help')


@genbot.event
async def on_ready():
  await eysxia.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.competing, name="github/vqea"))
  print(f"connected to {genbot.user}")


@genbot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.message.delete()
  

@genbot.command()
async def shutdown(ctx):
  id = str(ctx.author.id)
  if id == owner:
    await ctx.reply("shutting down bot..", mention_author=False)
    await ctx.genbot.close()
  else:
    e = discord.Embed(description=f">>> {ctx.author.mention} you must be <@{owner}> to access this command")
    msg = await ctx.reply(embed=e, mention_author=False)
    await asyncio.sleep(60)
    await msg.delete()
    await ctx.message.delete()


def restart_genbot():
  os.execv(sys.executable, ['python'] + sys.argv)


@genbot.command()
async def restart(ctx):
  id = str(ctx.author.id)
  if id == owner:
    await ctx.reply("Restarting bot..")
    restart_eysxia()
  else:
    er = discord.Embed(description=f">>> {ctx.author.mention} you must be <@{owner}> to access this command")
    msg = await ctx.reply(embed=er, mention_author=False)
    await asyncio.sleep(60)
    await msg.delete()
    await ctx.message.delete()


@genbot.command()
async def stock(ctx):
  tiktok = len(open('stock/tiktok.txt').readlines())
  spotify = len(open('stock/spotify.txt').readlines())
  nitro = len(open('stock/nitro.txt').readlines())
  cc = len(open('stock/cc.txt').readlines())
  embed = discord.Embed()
  embed.set_author(name = f"{ctx.guild.name} <3", icon_url = genbot.user.avatar.url)
  embed.set_thumbnail(
    url = eysxia.user.avatar.url)
  embed.add_field(name="tiktok", value=f"```{str(tiktok)}```", inline=False)
  embed.add_field(name="spotify", value=f"```{str(spotify)}```", inline=False)
  embed.add_field(name="nitro", value=f"```{str(nitro)}```", inline=False)
  embed.add_field(name="cc", value=f"```{str(cc)}```", inline=False)
  embed.set_footer(text=f'requested by {ctx.author}')
  await ctx.reply(embed=embed, mention_author=False)


@genbot.command()
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gen(ctx, acc: str = None):
  acc = acc.lower()
  if not str(ctx.channel.id) in gen_only_channel: return
  if acc == "tiktok":
    with open("stock/tiktok.txt") as file:
      lines = file.readlines()
      if len(lines) == 0:
        no_stock_embed = discord.Embed(description=f">>> {ctx.author.mention} `we are currently out of stock`")
        msg = await ctx.reply(embed=no_stock_embed, mention_author=False)
        await asyncio.sleep(60)
        await msg.delete()
        await ctx.message.delete()   
      else:
        with open("stock/tiktok.txt") as file:
          account = random.choice(lines)
          check_dm_embed = discord.Embed(description=f">>> {ctx.author.mention} `account has been sent to dms!`")
          account_dm_embed = discord.Embed()
          account_dm_embed.add_field(name=f"account: {acc}", value=f"```{str(account)}```", inline=False)
          account_dm_embed.set_footer(icon_url=genbot.user.avatar.url, text=f'sent from {ctx.guild.name} <3 | deleting in 5 minutes')
          await ctx.author.send(embed=account_dm_embed, delete_after=300)
          await ctx.author.send(f"your copy+paste:\n`{str(account)}`", delete_after=300)
          msg = await ctx.reply(embed=check_dm_embed, mention_author=False)
          await asyncio.sleep(60)
          await msg.delete()
          await ctx.message.delete()
          return
  if acc == "spotify":
    with open("stock/spotify.txt") as file:
      lines = file.readlines()
      if len(lines) == 0:
        no_stock_embed = discord.Embed(description=f">>> {ctx.author.mention} `we are currently out of stock`")
        msg = await ctx.reply(embed=no_stock_embed, mention_author=False)
        await asyncio.sleep(60)
        await msg.delete()
        await ctx.message.delete()
      else:
        with open("stock/spotify.txt") as file:
          account = random.choice(lines)
          check_dm_embed = discord.Embed(description=f">>> {ctx.author.mention} `account has been sent to dms!`", )
          account_dm_embed = discord.Embed()
          account_dm_embed.add_field(name=f"account: {acc}", value=f"```{str(account)}```", inline=False)
          account_dm_embed.set_footer(icon_url=genbot.user.avatar.url, text=f'sent from {ctx.guild.name} <3 | deleting in 5 minutes')
          await ctx.author.send(embed=account_dm_embed, delete_after=300)
          await ctx.author.send(f"your copy+paste:\n`{str(account)}`", delete_after=300)
          msg = await ctx.reply(embed=check_dm_embed, mention_author=False)
          await asyncio.sleep(60)
          await msg.delete()
          await ctx.message.delete()
          return
  if acc == "nitro":
    with open("stock/nitro.txt") as file:
      lines = file.readlines()
      if len(lines) == 0:
        no_stock_embed = discord.Embed(description=f">>> {ctx.author.mention} `we are currently out of stock`")
        msg = await ctx.reply(embed=no_stock_embed, mention_author=False)
        await asyncio.sleep(60)
        await msg.delete()
        await ctx.message.delete()
      else:
        with open("stock/nitro.txt") as file:
          account = random.choice(lines)
          check_dm_embed = discord.Embed(description=f">>> {ctx.author.mention} `gift has been sent to dms!`", )
          await ctx.author.send(f"{str(account)}", delete_after=300)
          msg = await ctx.reply(embed=check_dm_embed, mention_author=False)
          await asyncio.sleep(60)
          await msg.delete()
          await ctx.message.delete()
          return
  if acc == "cc":
    with open("stock/cc.txt") as file:
      lines = file.readlines()
      if len(lines) == 0:
        no_stock_embed = discord.Embed(description=f">>> {ctx.author.mention} `we are currently out of stock`")
        msg = await ctx.reply(embed=no_stock_embed, mention_author=False)
        await asyncio.sleep(60)
        await msg.delete()
        await ctx.message.delete()
      else:
        with open("stock/cc.txt") as file:
          account = random.choice(lines)
          check_dm_embed = discord.Embed(description=f">>> {ctx.author.mention} `code has been sent to dms!`", )
          await ctx.author.send(f"your copy+paste:\n`{str(account)}`", delete_after=300)
          msg = await ctx.reply(embed=check_dm_embed, mention_author=False)
          await asyncio.sleep(60)
          await msg.delete()
          await ctx.message.delete()
          return
  else: return await ctx.message.delete()


keep_alive.keep_alive()
genbot.run(token)
