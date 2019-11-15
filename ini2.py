from discord.ext import commands
import discord
import praw
import random

TOKEN = 'NjQxNDA5MzMwODg4ODM1MDgz.XcLHRQ.PvhkvwlbL0ZNU_cCccDxaiOnlCA'

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await client.change_presence(game=discord.Game(name="with Miku"))
    await client.change_presence(game=discord.Game(name="Annie be cute", type=3))



@client.command()
async def test():
    await client.say('Learning Python is fun uwu')


@client.command
async def cuddle():
    await client.say("*Timmy goes up to <@207505077013839883> and cuddles tightly, "
                     "trying his best to comfort her*")


reddit = praw.Reddit(client_id='ra7W9w_QZhwRaA',
                     client_secret='DFRuha1D_QLYm-AdCfQW54uiq1M',
                     user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/78.0.3904.87 Safari/537.36')

kitsune_cache = []
@client.command(pass_context=True)
async def kitsune(ctx):
    if not kitsune_cache:
        kitsune_submissions = reddit.subreddit('kitsunemimi').hot()

        for i in range(50):
            submission = next(x for x in kitsune_submissions)
            if not submission.over_18:
                kitsune_cache.append((submission.url, submission.title))

        kitsune_submissions = reddit.subreddit("kitsunemimi").top("all")

        for i in range(100):
            submission = next(x for x in kitsune_submissions)
            if not submission.over_18:
                kitsune_cache.append((submission.url, submission.title))

        await client.send_message(ctx.message.channel, 'Results found: {}'.format(len(kitsune_cache)))

    picture, name = random.choice(kitsune_cache)

    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(ctx.message.channel, embed=embed)


wholesome_cache = []
@client.command(pass_context=True)
async def wholesome(ctx):
    if not wholesome_cache:
        wholesome_submissions = reddit.subreddit('wholesomeanimemes').hot()

        for i in range(50):
            submission = next(x for x in wholesome_submissions)
            if not submission.over_18:
                wholesome_cache.append((submission.url, submission.title))

        wholesome_submissions = reddit.subreddit("wholesomeanimemes").top("all")

        for i in range(100):
            submission = next(x for x in wholesome_submissions)
            if not submission.over_18:
                wholesome_cache.append((submission.url, submission.title))

        await client.send_message(ctx.message.channel, 'Results found: {}'.format(len(wholesome_cache)))

    picture, name = random.choice(wholesome_cache)

    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(ctx.message.channel, embed=embed)


bunny_cache = []
@client.command(pass_context=True)
async def bunny(ctx):
    if not bunny_cache:
        bunny_submissions = reddit.subreddit('usagimimi').hot()

        for i in range(50):
            submission = next(x for x in bunny_submissions)
            if not submission.over_18:
                bunny_cache.append((submission.url, submission.title))

        bunny_submissions = reddit.subreddit("usagimimi").top("all")

        for i in range(100):
            submission = next(x for x in bunny_submissions)
            if not submission.over_18:
                animegirl_cache.append((submission.url, submission.title))

        await client.send_message(ctx.message.channel, 'Results found: {}'.format(len(bunny_cache)))

    picture, name = random.choice(bunny_cache)

    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(ctx.message.channel, embed=embed)

neko_cache = []
@client.command(pass_context=True)
async def neko(ctx):
    channel = client.get_channel("478572251252391957")
    if not neko_cache:
        neko_submissions = reddit.subreddit('nekomimi').hot()

        for i in range(50):
            submission = next(x for x in neko_submissions)
            if submission.over_18:
                neko_cache.append((submission.url, submission.title))

        neko_submissions = reddit.subreddit("nekomimi").top("all")

        for i in range(100):
            submission = next(x for x in neko_submissions)
            if submission.over_18:
                neko_cache.append((submission.url, submission.title))

        await client.send_message(channel, 'Results found: {}'.format(len(neko_cache)))

    picture, name = random.choice(neko_cache)
    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(channel, embed=embed)


thighs_cache = []
@client.command(pass_context=True)
async def thicc(ctx):
    channel = client.get_channel("478572251252391957")
    if not thighs_cache:
        thighs_submissions = reddit.subreddit('thighdeology').hot()

        for i in range(50):
            submission = next(x for x in thighs_submissions)
            if submission.over_18:
                thighs_cache.append((submission.url, submission.title))

        thighs_submissions = reddit.subreddit("thighdeology").top("all")

        for i in range(100):
            submission = next(x for x in thighs_submissions)
            if not submission.over_18:
                thighs_cache.append((submission.url, submission.title))

        await client.send_message(ctx.message.channel, 'Results found: {}'.format(len(thighs_cache)))

    picture, name = random.choice(thighs_cache)

    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(channel, embed=embed)


animegirl_cache = []
@client.command(pass_context=True)
async def animegirl(ctx):
    if not animegirl_cache:
        animegirl_submissions = reddit.subreddit('animegirls').hot()

        for i in range(50):
            submission = next(x for x in animegirl_submissions)
            if not submission.over_18:
                animegirl_cache.append((submission.url, submission.title))

        animegirl_submissions = reddit.subreddit("animegirls").top("all")

        for i in range(100):
            submission = next(x for x in animegirl_submissions)
            if not submission.over_18:
                animegirl_cache.append((submission.url, submission.title))

        await client.send_message(ctx.message.channel, 'Results found: {}'.format(len(animegirl_cache)))

    picture, name = random.choice(animegirl_cache)

    try:
        title, desc = name.split('[')
        desc = '[' + desc
    except ValueError:
        title = name
        desc = None

    embed = discord.Embed(title=title, description=desc, color=0xce3a9b)
    embed.set_image(url=picture)
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(name='numguess',
                brief='Guess a number between 1 and 100',
                pass_context=True)
async def numguess(ctx):
    number = random.randint(1, 100)
    turns = 5
    await client.send_message(ctx.message.channel, "Welcome! Time to guess some numbers! You have 5 tries. I'll think"
                                                   " of a number between 1 and 100.")

    def check(author):
        def inner_check(message):
            if message.author != author:
                return False
            try:
                int(message.content)
                return True
            except ValueError:
                return False

        return inner_check

    while turns != 0:
        await client.send_message(ctx.message.channel, "Go try your luck and take a guess!")
        msg = await client.wait_for_message(check=check, timeout=60)
        guess = int(msg.content)

        if guess > number and turns != 0:
            await client.send_message(ctx.message.channel,
                                      f"Woah there, this is way too high! Maybe try and guess a lower number next time."
                                      f" You still have {turns - 1} guesses left")
            turns -= 1
        elif guess < number and turns != 0:
            await client.send_message(ctx.message.channel,
                                      f"Awww, too bad! Might wanna go higher next time! You have {turns - 1} "
                                      f"guesses left!")
            turns -= 1
        if guess == number:
            await client.send_message(ctx.message.channel, f"Yes!! You guessed right! I'm so proud of you!!")
            break
        if turns == 0 and guess != number:
            await client.send_message(ctx.message.channel,
                                      f"Maybe next time! In case you wondered, my number was {number}!")


@client.command()
async def test2(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


client.run(TOKEN)
