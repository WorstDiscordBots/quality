import discord
import random
import aiohttp
import traceback
import sys

from discord.ext import commands
from pyqrcode import QRCode # Used for Qualities
from PIL import Image # more Quality
from io import BytesIO # saving quality
from functools import partial # for executor quality
from datetime import timedelta # quality errors

import config # our config

bot = commands.Bot(command_prefix=[":star:", "quality ", ":star: "], case_insensitive=True, owner_id=356091260429402122) # Quality Prefix

@bot.event
async def on_ready(): # the bot has initalized and is ready for making quality
    bot.session = aiohttp.ClientSession() # used for getting quality avys
    print("Quality is ready for making the world more quality!")

@bot.event
async def on_command_error(ctx, error): # handlers for our quality errors
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"You are on cooldown. Try again in {timedelta(seconds=int(error.retry_after))}.")
    else:
        print('In {}:'.format(ctx.command.qualified_name), file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print('{0}: {1}'.format(error.original.__class__.__name__, error.original), file=sys.stderr)

@commands.cooldown(1, 60, commands.BucketType.channel) # we do not want this to be spammed too often
@bot.command()
async def ping(ctx):
    """A command to see the bot's latency, which is always quality"""
    if random.randint(1, 2) == 1:
        await ctx.send("My current latency is quality, as always!")
    else:
        await ctx.send(f"Quality is delayed by {bot.latency * 1000}ms today, sorry")

def qualitize(avy):
    url = QRCode('http://quality.com',error = 'H')
    url.png('test.png', scale=10)
    with Image.open('test.png').convert("RGBA") as im:
        box = (135, 135, 235, 235)
        im.crop(box)
        avy = Image.open(avy)
        avy = avy.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(avy, box)
        out = BytesIO()
        im.save(out, format="png")
    out.seek(0)
    return out

@bot.command()
async def quality(ctx, member: discord.Member=None):
    """Make me quality!"""
    member = member or ctx.author
    async with bot.session.get(member.avatar_url) as r: # get quality as avy
        avy = BytesIO(await r.read())
    func = partial(qualitize, avy)
    out = await bot.loop.run_in_executor(None, func)
    await ctx.send(file=discord.File(fp=out, filename="quality.png")) # quality!

@commands.is_owner()
@bot.command()
async def die(ctx):
    await ctx.send("On my way! Bye quality world...")
    await bot.session.close()
    await bot.logout()

bot.run(config.token)
