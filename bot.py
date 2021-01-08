import discord
from discord.ext import commands
import random
import youtube_dl

client = commands.Bot(command_prefix="?")
thug = ["Brandon Barber", "The Boy In The Pic", "Holliwud", "Warren So Fine"]
jokes = ['Brandon Barber is a Holliwud Star', 'What do you call a racist white lady? Ku Klux Karen', 'Why dont racist people take photographs in old cameras?Cause they appear in black and white.', 'If I had a nickel for every time someone called me a racist...I could quit my job at the NYPD', 'So, I asked my German grandfather hoe racist he was, scale of 1 to 10, He said "NEIN!"', 'They say 30percent of Australians are casual racists,The other 70percent are full time', 'Being racist is like saying you dont like red skittles,They may be a different colour but they still taste about the same',
         'There are only two types of people worse than racists, The Blacks and Jews', 'Minecraft is Racist,Minecraft has taught me not to look tall black guys in the eye or they get aggressive. Theyre faster and stronger than you and they randomly steal things. However, you can escape by running to water--they cant swim.', 'A racist, a rapist, and a President walk into a bar......in Mar-a-Lago. The bartender says, "Good Morning Donald, all by yourself today?"', 'My black friend said he doesnt watch the tv show "Friends," because its racist.How can it be racist though when it doesnt even have black people in it?!?']
memes = [
    'https://imgur.com/CqOHoiD',
    'https://imgur.com/a/FzcdRzT',
    'https://imgur.com/vFiaLHV',
    'https://imgur.com/ongjRue',
    'https://imgur.com/STve5r9',
    'https://imgur.com/ELHYdh3',
    'https://imgur.com/Xbo5eBr',
    'https://imgur.com/yM4FyND',
    'https://imgur.com/hgDaLsI',
    'https://imgur.com/mjNGWdq',
    'https://imgur.com/CNQ5MMc',
    'https://imgur.com/NBXkcnp',
    'https://imgur.com/kmk8cyr',
    'https://imgur.com/D72pAQJ',
    'https://imgur.com/cTe17yi',
    'https://imgur.com/4rlpMl4',
    'https://imgur.com/5NUKikW',
    'https://imgur.com/8momTzp',
    'https://imgur.com/jbJPQAi',
    'https://imgur.com/ONhCTYR',
    'https://imgur.com/1IfTwqR',
    'https://imgur.com/301s2uK',
    'https://imgur.com/7R9uhN5',
    'https://imgur.com/yCjAaQo',
    'https://imgur.com/i4bmUPT',
    'https://imgur.com/s7pAd6X',
    'https://imgur.com/5LvXM2z',
    'https://imgur.com/T6c3g73',
    'https://imgur.com/a/7OHP5zV',
    'https://imgur.com/topjCg8',
    'https://imgur.com/PkWBrz6',
    'https://imgur.com/TwQEFZr',
    'https://imgur.com/63JUeBE',
    'https://i.imgur.com/5ZOth5I.jpg',
    'https://i.imgur.com/xItUmYG.jpg',
    'https://imgur.com/Kdwp3IW',
    'https://imgur.com/nvEq9L1',
    'https://imgur.com/3ooftjT',
    'https://imgur.com/MTzVTYD',
    'https://imgur.com/ul3LPVD',
    'https://imgur.com/0mCpnae',
    'https://imgur.com/RQOVAqq',
    'https://imgur.com/LErQ4xo',
    'https://imgur.com/a/HQOJVvy',
    'https://imgur.com/wThAC5w',
    'https://imgur.com/1IbWEdr'
]
# Shit code
thugmeasure = ['0.0000001%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%',
               '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '72%', '73%', '74%', '75%', '76%', '77%', '78%', '83%', '84%', '85%', '86%', '89%', '91%', '95%', '99%', '99.99%']
thugquotes = ['Yo yo yo its hump day! Aye what I need you to do is tag 3 big dick ass niggas under this tweet right here. I need some more niggas to do this bust that nut challenge with and Im also giving away another 100 free subscriptions to my onlyfans. Be looking out for that tweet later on today. Dont forget to tag them 3 niggas under there. If you one of them big dick niggas tag yourself. HUMP DAY. Fuck wit ya boy, nude barber. - Brandon Barber', 'Yo whats up yall. Happy Friday. Its the first of the month. They done open Georgia back up but I aint cuttin. I aint going my ass outside till this shit slow down - Brandon Barber', 'Aah shit, bust that nut challenge. Look at that thang swinging it back tho but Im about to beat they ass watch this - Brandon Barber',
              'yeaah boy they just got done getting they mf erotic cut. now they wanna do a mf bust that nut challenge. they aint never win against me and my nigga. big meat wee wee. you in there? Come on. bout that bust that nut challenge, me and my nigga vs him and his nigga.The Scott boys. Im a part of the Scott boys too. my middle names Scott. - Brandon Barber', '"My favorie food is spahgetti and and and and and vegan nuggets"', 'Can you twerk on live? Yea. If you want me to twerk its gonna be at least twenty-fi hundred.', 'moderators block that nigga for life', 'can your mamas pussy be built again if it was smashed up?', 'Why is your mic shaking right now? Because im beating off right now.']


@client.event
async def on_ready():
    print("Bot is doing the Thugshaker")

# Sends thughunter gay porn site


@client.command()
async def thughunter(ctx):
    await ctx.send("www.thughunter.com")

# Dispenses the socials of famous gay pornstars


@client.command()
async def socials(ctx):
    await ctx.send("Brandon Barber: https://twitter.com/xclusive002?lang=en \n Holliwud: https://twitter.com/_holliwud_king \n TheBoyInThePic: https://twitter.com/mixmonstermeat?lang=en \n WarrenSoFine: https://www.instagram.com/warrensofine216/")

# You're telling the god of thugshaking to do a thugshaker you fucking idiot


@client.command()
async def thugshaker(ctx):
    await ctx.send("Nah Nigga I already doing the Thugshaker")

# Dispenses a picture of a gay pornstar which looks like the late actor Gary Coleman


@client.command()
async def garycoleman(ctx):
    await ctx.send("https://imgur.com/oXvKh7I")

# Dispenses thugs


@client.command()
async def thugs(ctx, *, number):
    await ctx.send(thug[int(number)-1])

# It purges the chat depending on the parameters you gave


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def thugpurge(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Thug Purged {amount} messages')
    await ctx.channel.purge(amount)

# It kicks the member and sends them gay porn site


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def thugkick(ctx, member: discord.Member, *, reason=" Do the Thugshaker"):
    await member.send("www.thughunter.com " + reason)
    await ctx.send(f'{member.name} Has been Thugkicked')
    await member.kick(reason=reason)

# It bans members and sends them gay porn site


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def thugban(ctx, member: discord.Member, *, reason=" Do the Thugshaker"):
    await member.send("www.thughunter.com " + reason)
    await ctx.send(f'{member.name} Has been Thugshaked')
    await member.ban(reason=reason)

# It mutes the discord member and adds them a muted role and sends them thugsounds.com in their DMs


@client.command()
@commands.has_permissions(kick_members=True)
async def thugmute(ctx, member: discord.Member, *, reason=" Stop doing the romp shaker"):
    muted_role = ctx.guild.get_role(747646516046331984)
    await member.add_roles(muted_role)
    await member.send("https://thugsounds.com/ " + reason)
    await ctx.send(f'{member.mention} Has been Thugshaked')

# It unmutes the member and removes the muted role


@client.command()
@commands.has_permissions(kick_members=True)
async def thugunmute(ctx, member: discord.Member, *, reason=" Started doing the Thugshaker"):
    muted_role = ctx.guild.get_role(747646516046331984)
    await member.remove_roles(muted_role)
    await ctx.send(f'{member.mention} Has started doing the Thugshaker')

# It mentions the member you @ and thugshakes them


@client.command()
async def thugshake(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} has been Thugshaked by {ctx.author.mention}')

# It dispenses a random imgur link which either is a photo meme or a video meme using the choice function from the memes list


@client.command()
async def thugmeme(ctx):
    random_link = random.choice(memes)
    await ctx.send(random_link)

# It dispenses a random joke using the random function from the jokes list


@client.command()
async def thugjoke(ctx):
    random_joke = random.choice(jokes)
    await ctx.send(random_joke)

# It dispenses a random quote using the random function from the quotes list


@client.command()
async def thugquote(ctx):
    random_quote = random.choice(thugquotes)
    await ctx.send(random_quote)

# It chooses a random percentage using the choice function from the list of percentages


@client.command()
async def thugmeter(ctx):
    the_meter = random.choice(thugmeasure)
    await ctx.send(f'{ctx.author.mention} is {the_meter} Thug')
    ctx.author = the_meter

# Enter your discord bot token here
client.run()
