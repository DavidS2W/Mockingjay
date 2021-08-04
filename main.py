import discord
import random
from discord.ext import commands
import asyncio
import json
import time
from disputils import BotEmbedPaginator

def prefix(client, message):
  with open('prefixes.json', 'r') as f:
    pref = json.load(f)
    
    prefix = pref[str(message.guild.id)]

  return prefix 

client = commands.Bot(command_prefix=prefix)

colors = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694]

products = [{"name": "Golden ring", "price": 10000, "district": 1, "description": "A gold ring that does nothing really apart from looking good", "icon": ":ring:"}, 
{"name": "Septsilk gown", "price": 5500, "district": 1, "description": "A gorgeous lavender gown. Made by the esteemed seamstresses of District 1 from high-grade silk produced by the hardworking labor of District 8", "icon": ":dress:"}, 
{"name": "Toolbox", "price": 10000, "district": 2, "description": "An assortment of vital tools perfect for the hardworking industrial worker. With this toolbox, you can contribute more with your labor to the beautiful nation of Panem.", "icon": ":tools:"}, 
{"name": "Shield", "price": 4000, "district": 2, "description": "Caught in a bad situation while hunting? Faced with Peacekeepers who intend to execute you for unruly activity? Protect yourself with this shield! Decreases chances of dying while hunting by 30% and Peacekeeper encounters by 40% ", "icon": ":shield:"}, {"name": "Computer", "price": 20000, "district": 3, "description": "Get district travel passes more easily with a computer! Use the Capitol's efficient TransPlan system instead of getting a pass from the Hob or the District Office.", "icon": ":computer:"}, 
{"name": "Tilapia", "price": 200, "district": 4, "description": "A tasty fish caught from the shores of District 4!", "icon": ":tropical_fish:"}, 
{"name": "Panfish", "price": "Cannot be bought", "district": "All", "description": "A tasty fish you can get anywhere while fishing!", "icon": ":fish:"}, 
{"name": "Fishing rod", "price": 15000, "district": 4, "description": "Catch your own fish with this handy rod!", "icon": ":fishing_pole_and_fish:"}, 
{"name": "Battery", "price": 500, "district": 5, "description": "Use this battery to power your computer!", "icon": ":battery:"}, 
{"name": "Axe", "price": 5000, "district": 7, "description": "Just an axe. Use it to obtain wood or kill large animals when hunting.", "icon": ":axe:"}, 
{"name": "Jacket", "price": 5000, "district": 8, "description": "A drab, durable utility jacket meant only to last and keep you warm. As far as aesthetics go, it scores a zero.", "icon": ":coat:"}, 
{"name": "Armour", "price": 10000, "district": 8, "description": "A durable set of Kevlar armour made by the esteemed industrial workers of District 8. Usually factory rejects from the stockpile created for the use of Peacekeepers. Reduces the chances of dying when hunting by 40% and Peacekeeper encounters by 50%", "icon": "<:armour:865145803126865961> "}, 
{"name": "Bread", "price": 50, "district": 9, "description": "A sawdust filled loaf of bread that restores 10HP. It's just too bad that all the good stuff goes to the Capitol.", "icon": ":bread:"}, 
{"name": "Beef", "price": 100, "district": 10, "description": "A slab of frozen beef. Can be cooked to restore 30HP", "icon": ":meat_on_bone:"}, 
{"name": "Milk", "price": 50, "district": 10, "description": "Get your milk here! Restores 10HP of health.", "icon": ":milk:"}, 
{"name": "Apple", "price": 40, "district": 11, "description": "Just an ordinary apple. Restores 20HP.", "icon": ":apple:"}, 
{"name": "Bow", "price": 10000, "district": 12, "description": "You met Katniss in district 12 and bought a bow from her! Unfortunately, if this one breaks there are none left...", "icon": ":bow_and_arrow:"}, 
{"name": "Travel pass", "price": 2000, "district": "All", "description": "Get this in any district! A travel pass allows you to hop on a train to any district in the great nation of Panem. Except the Capitol...", "icon": ":page_facing_up:"}, 
{"name": "Elk", "price": "Cannot be bought", "district": "All", "description": "If you're lucky, you may find this when hunting...", "icon": ":deer:"}, 
{"name": "Groosling", "price": 20000, "district": "All", "description": "Fresh groosling from the Glades! Expensive when bought but can be hunted free of charge.", "icon": ":poultry_leg:"}, 
{"name": "Magpie", "price": 2000, "district": "All", "description": "Fresh magpie from the Glades! Expensive when bought but can be hunted free of charge.", "icon": ":bird:"}, 
{"name": "Katniss", "price": 'Cannot be bought', "district": "All", "description": "A potato-like plant you can forage from the Glades.", "icon": ":sweet_potato:"}, 
{"name": "Wild fruit", "price": "Can't be bought", "district": "All", "description": "Sweet, rounded fruit that can be found sometimes when foraging. Tastes great and replenishes 20 HP", "icon": ":mango:"}, 
{"name": "Groosling nest", "price": "Can't be bought", "district": "All", "description": "An abandoned nest that once belonged to a groosling. Any uses? I'm not sure, use your creativity...", "icon": "<:nest:865148588500713482>"}, 
{"name": "Reward box", "price": "Can't be bought", "district": "All", "description": "A reward box given by the Capitol if you win the Hunger Games. Use it to get a random selection of goodies...", "icon": ":gift:"}]

shop_id = ['golden ring', 'armour', 'jacket', 'fishing rod', 'travel pass', 'computer', 'battery', 'milk', 'travel pass', 'groosling', 'magpie', 'bread', 'bow', 'toolbox', 'shield', 'septsilk gown', 'apple', 'beef', 'axe']

usables = ['computer', 'reward box']

edibles = ['milk', 'elk', 'groosling', 'apple', 'beef', 'tilapia', 'bread', 'wild fruit', 'katniss', 'panfish']

hp_food = {"milk": 20, "elk": 50, "groosling": 50, "apple": 20, "beef": 60, "bread": 20, "wild fruit": 20, "katniss": 20, "tilapia": 20, "panfish": 50}

forage_stuff = ['katniss', 'wild fruit', 'apple', 'groosling nest']

@client.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = 'h.'

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes.pop(str(guild.id))

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

client.remove_command('help')

@client.event
async def on_ready():
    print('We are now logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'h.help | In  {len(client.guilds)} servers!'))

def icon(product):
  for item in products:
    if product.lower() == item["name"].lower():
      return item["icon"]
    else:
      pass

def timecon(n):
  if n>60:
    ty_res = time.gmtime(n)
    res = time.strftime("%H:%M:%S",ty_res)
    return(res)
  else:
    return f'{n}s'

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    pass
  elif isinstance(error, commands.CommandInvokeError):
    if ctx.message.content.startswith(f'{prefix(client, ctx.message)}give') or ctx.message.content.startswith(f'{prefix(client, ctx.message)}profile') or ctx.message.content.startswith(f'{prefix(client, ctx.message)}hgame') or ctx.message.content.startswith(f'{prefix(client, ctx.message)}buy'):
      pass
    else:
      with open('bank.json', 'r') as f:
        b = json.load(f)
      if str(ctx.author.id) in b:
        await ctx.send(':warning: Something went wrong.\nYou may have specified invalid arguments.')
        raise error
      else:
        await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create`!')
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f':snowflake: You are on cooldown, please try again in {timecon(round(error.retry_after))}')
  else:
    pass

def check_item_price(product):
  for item in products:
    if item["name"].lower() == product.lower():
      return(item["price"])
    else:
      pass

def afford(author, price, walbank):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  networth = val[str(author.id)][walbank] 

  if networth < price:
    return(0)
  else:
    return(1)

def author_info(author, category):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  info = val[str(author.id)][category]

  return(info)

def check_item_value(author, name):
  with open('inventory.json', 'r') as f:
    val = json.load(f)

  inv = val[str(author.id)]

  for item in inv:
    if item["name"].lower() == name.lower():
      return(item["value"])
    else:
      pass

def check_item_district(author, name):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  dnum = val[str(author.id)]["district"]

  for item in products:
    if item["name"].lower() == name.lower() and item["district"] == dnum:
      return(1)
    elif item["name"].lower() == name.lower() and item["district"] == "All":
      return(1)
    else:
      pass

def productlist_info(arg1):
  for item in products:
    if item["name"].lower() == arg1.lower():
      return(item)

async def create_account(author):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  dnum = random.randint(1, 12)

  val[str(author.id)] = {"bank": 1000, "wallet": 2000, "district": dnum, "residence": dnum, "HP": 100, "job": "Nil", "successor": "Nil"}

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)

  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  inv[str(author.id)] = []
  y = inv[str(author.id)]
  for item in products:
    temp = {"name": item["name"], "value": 0}
    y.append(temp)
  with open('inventory.json', 'w') as f:
    json.dump(inv, f, indent=4)

async def hp_change(author, value):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)]["HP"] =  val[str(author.id)]["HP"] + value

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)

async def district_change(author, value):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)]["district"] =  value

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)

async def job_change(author, value):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)]["job"] =  value

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)

async def money_change(author, value, walbank):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)][walbank] = val[str(author.id)][walbank] + value

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)

async def sello(author, price, itema):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)]["wallet"] = val[str(author.id)]["wallet"] + price

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)
    
  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  initinv = inv[str(author.id)]

  for item in initinv:
    if itema.lower() == item["name"].lower():
      item["value"] = item["value"] - 1
    else:
      pass

  with open('inventory.json', 'w') as f:
    json.dump(inv, f, indent=4)

async def useo(author, itema):
  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  initinv = inv[str(author.id)]

  for item in initinv:
    if itema.lower() == item["name"].lower():
      item["value"] = item["value"] - 1
    else:
      pass

  with open('inventory.json', 'w') as f:
    json.dump(inv, f, indent=4)

async def buyo(author, price, itema):
  with open('bank.json', 'r') as f:
    val = json.load(f)

  val[str(author.id)]["wallet"] = val[str(author.id)]["wallet"] - price

  with open('bank.json', 'w') as f:
    json.dump(val, f, indent=4)
    
  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  initinv = inv[str(author.id)]

  for item in initinv:
    if itema.lower() == item["name"].lower():
      item["value"] = item["value"] + 1
    else:
      pass

  with open('inventory.json', 'w') as f:
    json.dump(inv, f, indent=4)

async def dying(author, message):
  hp = author_info(author, "HP")
  cash = author_info(author, "wallet")
  bank = author_info(author, "bank")

  bankdata = round(0.7*(cash+bank))
  sidone = author_info(author, "successor")
  if hp <= 0:
    if sidone != 'Nil':
      sid = author_info(author, "successor")["id"]
      user = await client.fetch_user(sid)
      await money_change(user, bankdata, "bank")
      await money_change(author, -1*bankdata, "bank")
      await message.channel.send(f'{user.mention} you have received ${bankdata} from {author.mention} because he/she died. Spend it well.')
      await hp_change(author, abs(hp)+200)
    else:
      await money_change(author, -1*(cash+bank), "bank")
      await message.channel.send(f'{author.mention} you have lost ${bankdata} from your account because you died. Oof.')
      await hp_change(author, abs(hp)+200)
  else:
    pass

async def dyinga(author, message):
  hp = author_info(author, "HP")
  cash = author_info(author, "wallet")
  bank = author_info(author, "bank")

  bankdata = round(0.7*(cash+bank))
  sidone = author_info(author, "successor")
  if hp <= 0:
    if sidone != 'Nil':
      sid = author_info(author, "successor")["id"]
      user = await client.fetch_user(sid)
      await money_change(user, bankdata, "bank")
      await money_change(author, -1*bankdata, "bank")
      await message.channel.send(f'{user.mention} you have received ${bankdata} from {author.mention} because he/she died. Spend it well.')
      return
      await message.channel.send('You have died and lost the hunger games.')
    else:
      await money_change(author, -1*(cash+bank), "bank")
      await message.channel.send(f'{author.mention} you have lost ${bankdata} from your account because you died. Oof.')
      return
      await message.channel.send('You have died and lost the hunger games.')
  else:
    pass

@client.command(aliases=['prefix'])
async def prefixo(ctx, prefixa):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(ctx.guild.id)] = prefixa

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

  await ctx.send(f'The prefix for this server has been changed to `{prefixa}.`')

@prefixo.error
async def prefixo_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please enter the new prefix.\nExample: {prefix(client, ctx.message)}prefix *')

@client.command()
async def credits(ctx):
  em = discord.Embed()
  em.title = 'Credits and ownership of Mockingjay'
  dav = await client.fetch_user(746646972483502140)
  gav = await client.fetch_user(599216781659471912)
  nico = await client.fetch_user(647372398886125569)
  ivan = await client.fetch_user(762190577893638184)
  em.description=f"This project was coded and initiated by **{dav}** in python with help from\n\nKey Beta Testers:\n{gav}\n{nico}\n\nA special thank you to {ivan} for his help and advice in earlier projects, namely GenshinWikiBot which was integral in the process of creating this bot."
  em.set_thumbnail(url=client.user.avatar_url)
  em.color=random.choice(colors)
  await ctx.send(embed=em)

@client.command()
async def lolol(ctx):
  await ctx.send('PRIME DIFFERENCE BETWEEN ELEMENTS RESPONSIBLE FOR HIROSHIMA AND NAGASAKI')
  
@client.command(aliases = ['Shop'])
async def shop(ctx, *, arg1):
  if arg1.lower() not in shop_id and arg1.lower() not in forage_stuff and arg1.lower() not in edibles and arg1.lower() not in usables:
    await ctx.send('The item you are trying to obtain info for does not exist!')
  else:
    owned = check_item_value(ctx.author, arg1.lower())
    product = productlist_info(arg1)
    em= discord.Embed(title=f'{product["icon"]} {product["name"]}', description=product["description"], color=random.choice(colors))
    em.add_field(name='District', value=product["district"], inline=True)
    em.add_field(name='Price', value=product["price"], inline=True)
    em.add_field(name='Owned', value=owned, inline=True)
    await ctx.send(embed=em)
    
@shop.error
async def shop_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    em = discord.Embed(title='A list of items you can buy!', description='In order to buy an item, you must travel to the district it comes from to do so.\nNote: Selling an item only returns half of its initial value.', color=random.choice(colors))
    for item in products:
      em.add_field(name=f'{item["icon"]} {item["name"]}', value=f'Price: {item["price"]} | District: {item["district"]}')
    await ctx.send(embed=em)

@client.command(aliases = ['Create'])
async def create(ctx):
  with open('bank.json', 'r') as f:
    b = json.load(f)

  if str(ctx.author.id) not in b:
    pref = prefix(client, ctx.message)
    await create_account(ctx.author)
    await ctx.send('Account created! Please check your DMS for a quick guide to this bot!')
    em = discord.Embed(title='A quick guide to the Mockingjay Discord bot', description='[Click this link to join the support server and get some rewards](https://discord.gg/SptuDpcvrX)', color=random.choice(colors))
    em.add_field(name='1. Get to know yourself.', value=f'Type {pref}profile to view your stats, including your district of residence.', inline=False)
    em.add_field(name='2. Try getting a job in your district. You can work every 30 minutes. If you are lucky, your boss will give you a travel pass.', value=f'Type {pref}joblist to view jobs available in your district and type {pref}job <number> to choose a job. For example, if I were to choose the job Jeweller, I would type {pref}job 1', inline=False)
    em.add_field(name='3. Earn some money, get travel passes and travel to other districts to get tools such as fishing rods and bows. Tools like these allow you to hunt, fish, etc.', value=f'Type {pref}travel <district number> to travel to a district and use the {pref}buy command to buy stuff.', inline=False)
    em.add_field(name='4. Collect tesserae.', value=f'Bread and beef can be collected every one hour. Type {pref}tesserae to collect it.', inline=False)
    em.add_field(name=f'5. Use the {pref}services command from time to time to earn extra cash.', value='You can contribute your services to the nation of Panem by volunteering for dangerous jobs. But hey, if you succeed, you get paid well...', inline=False)
    em.add_field(name=f'6. Use the {pref}hgame command, if you want to risk it.', value='You can join interactive Hunger Games sessions once in a while. Make sure your knowledge of the Hunger Games books and films are stitched up tight!', inline=False)
    em.set_footer(text='Bot created by AnakinSkywaler#3739', icon_url=client.user.avatar_url)
    await ctx.author.send(embed=em)
  else:
    await ctx.send('You already have an account!')

@client.command(aliases=['Invite'])
async def invite(ctx):
  em = discord.Embed(title='Hit this link to invite me to your server!', description = 'https://discord.com/api/oauth2/authorize?client_id=855240212800339978&permissions=2148005952&scope=bot', color=random.choice(colors))
  em.set_thumbnail(url=client.user.avatar_url)
  await ctx.send(embed=em)

@client.command(aliases = ['Buy'])
async def buy(ctx, arg1, *, product):
  if int(arg1) <= 0:
    await ctx.send('Please specify a positive value!')
    return
  if product.lower() not in shop_id:
    await ctx.send("You can't buy this item!")
  else:
    price = check_item_price(product)
    if afford(ctx.author, price, "wallet") == 1 and check_item_district(ctx.author, product.lower()) != None:
      for item in range(int(arg1)):
        await buyo(ctx.author, price, product.lower())
      await ctx.send(f'You have bought {arg1} {product} {icon(product.lower())}.')
    elif afford(ctx.author, price, "wallet") == 1 and check_item_district(ctx.author, product.lower()) == None:
      await ctx.send('You are in the wrong district!')
    elif afford(ctx.author, price, "wallet") == 0 and check_item_district(ctx.author, product.lower()) != None:
      await ctx.send("You can't afford this!")
    elif afford(ctx.author, price, "wallet") == 0 and check_item_district(ctx.author, product.lower()) == None:
      await ctx.send('You could not be in a worse position right now. You do not have enough money to buy this product and you are in the wrong district.')

@buy.error
async def buy_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the item you want to buy after the buy command.\nExample: {prefix(client, ctx.message)}buy 3 bow')
  else:
    with open('bank.json', 'r') as f:
        b = json.load(f)
    if str(ctx.author.id) in b:
      await ctx.send(f'Please specify the all of the required arguments after the command.\nExample: {prefix(client, ctx.message)}buy 3 bow')
    else:
      await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create`!')

@client.command(aliases = ['Hunt'])
@commands.cooldown(1, 10, commands.BucketType.user) 
async def hunt(ctx):
  valaxe = check_item_value(ctx.author, "axe")
  valbow = check_item_value(ctx.author, "bow")
  valarm = check_item_value(ctx.author, "armour")
  valshield = check_item_value(ctx.author, "shield")

  hunt_words = ["elk", "magpie", "groosling"]
  if valaxe >= 1 or valbow >= 1:
    rate = random.randint(1, 100)
    if rate <= 85:
      animal = random.choice(hunt_words)
      await buyo(ctx.author, 0, animal)
      hunters = ["You went out hunting and found one", "You chased down and killed one", "You finally managed to get one"]
      await ctx.send(f'{random.choice(hunters)} {animal} {icon(animal.lower())}!')
    else:
      if valarm >= 1 or valshield >= 1:
        ratetwo = random.randint(1, 30)
        await hp_change(ctx.author, -1*ratetwo)
        await ctx.send(f'You encountered an angry bison that charged right at you and hurt you badly! Luckily, you were protected by your shield or armour! \nYour hp has decreased by `{ratetwo}`.')
        await dying(ctx.author, ctx.message)
      else:
        ratetwo = random.randint(20, 60)
        await hp_change(ctx.author, -1*ratetwo)
        await ctx.send(f'You encountered an angry bison that charged right at you and hurt you badly!\nYour hp has decreased by `{ratetwo}`.')
        await dying(ctx.author, ctx.message)
  else:
    await ctx.send('You cannot hunt without an axe or a bow. Buy one as soon as possible.')

@client.command(aliases=['Profile', 'user', 'User'])
async def profile(ctx, user: discord.Member):
    with open('bank.json', 'r') as f:
      bank = json.load(f)
    stat = bank[str(user.id)]
    em = discord.Embed()
    em.title=f'{user.name}, here are your stats!'
    em.color = random.choice(colors)
    perc = round((stat["HP"]/200)*100)
    em.add_field(name='Current District', value=stat["district"], inline=False)
    em.add_field(name='Home District', value=stat["residence"], inline=False)
    em.add_field(name='HP', value=f'{stat["HP"]} | {perc}%', inline=False)
    em.add_field(name='Wallet', value=stat["wallet"], inline=False)
    em.add_field(name='Bank', value=stat["bank"], inline=False)
    if stat["successor"] != "Nil":
      em.add_field(name='Successor', value=stat["successor"]["name"], inline=False)
    else:
      em.add_field(name='Successor', value=stat["successor"], inline=False)
    em.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=em)

@profile.error
async def profile_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    try:
      with open('bank.json', 'r') as f:
        bank = json.load(f)
      stat = bank[str(ctx.author.id)]
      em = discord.Embed()
      em.title=f'{ctx.author.name}, here are your stats!'
      em.color = random.choice(colors)
      perc = round((stat["HP"]/200)*100)
      em.add_field(name='Current District', value=stat["district"], inline=False)
      em.add_field(name='Home District', value=stat["residence"], inline=False)
      em.add_field(name='HP', value=f'{stat["HP"]} | {perc}%', inline=False)
      em.add_field(name='Wallet', value=stat["wallet"], inline=False)
      em.add_field(name='Bank', value=stat["bank"], inline=False)
      if stat["successor"] != "Nil":
        em.add_field(name='Successor', value=stat["successor"]["name"], inline=False)
      else:
        em.add_field(name='Successor', value=stat["successor"], inline=False)
      em.set_thumbnail(url=ctx.author.avatar_url)
      await ctx.send(embed=em)
    except:
      await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create` first!')
  elif isinstance(error, commands.CommandInvokeError):
    with open('bank.json', 'r') as f:
      inv = json.load(f)
    if str(ctx.author.id) not in inv:
      await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create` first!')
    elif str(ctx.author.id) in inv:
      await ctx.send(f'Please ask your friend to create an account by typing `{prefix(client, ctx.message)}create` first!')

@client.command(aliases = ['Travel'])
@commands.cooldown(1.0, 60, commands.BucketType.user) 
async def travel(ctx, arg1):
  districts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
  if arg1 not in districts:
    await ctx.send('There is no such district!')
    return
  rate = random.randint(1, 100)
  tp = check_item_value(ctx.author, "travel pass")
  if rate <= 85 and tp >= 1:
    await useo(ctx.author, "travel pass")
    arg2 = int(arg1)
    em=discord.Embed(title=f'Alright, on to District {arg1}!', description="Keep your eyes peeled and don't run into any suspicious Peacekeepers!", color=random.choice(colors))
    em.set_thumbnail(url='https://www.syfy.com/sites/syfy/files/2017/08/screen_shot_2017-08-09_at_6.11.35_pm.png')
    await ctx.send(embed=em)
    msg = await ctx.send(f'On your way to district {arg1}...')
    await asyncio.sleep(random.randint(1, 10))
    await district_change(ctx.author, arg2)
    await msg.edit(content=f'You have arrrived at District {arg1}! Use the shop command to find out what you can buy!')
    
  elif rate > 85 and tp >= 1:
    shield = check_item_value(ctx.author, "shield")
    armour = check_item_value(ctx.author, "armour")

    if shield >= 1 or armour >= 1:
      ratetwo = random.randint(1, 20)
      await hp_change(ctx.author, -1*ratetwo)
      await useo(ctx.author, "travel_pass")
      em = discord.Embed(title=f"Uh oh... You've run into some Peacekeepers by accident. You put up a good fight and managed to get away, but they've confiscated your :page_facing_up: travel pass and your HP has decreased by {ratetwo}", description='Better luck travelling next time!', color=random.choice(colors))
      em.set_thumbnail(url='https://static.wikia.nocookie.net/thehungergames/images/e/e5/2peacekeepersCF.png/revision/latest/scale-to-width-down/547?cb=20130415223924')
      await ctx.send(embed=em)
      await dying(ctx.author, ctx.message)
    else:
      ratetwo = random.randint(20, 40)
      await hp_change(ctx.author, -1*ratetwo)
      await useo(ctx.author, "travel_pass")
      em = discord.Embed(title=f"Uh oh... You've run into some Peacekeepers by accident. You put up a good fight and managed to get away, but they've confiscated your :page_facing_up: travel pass and your HP has decreased by {ratetwo}", description='Better luck travelling next time!', color=random.choice(colors))
      em.set_thumbnail(url='https://static.wikia.nocookie.net/thehungergames/images/e/e5/2peacekeepersCF.png/revision/latest/scale-to-width-down/547?cb=20130415223924')
      await ctx.send(embed=em)
      await dying(ctx.author, ctx.message)
  else:
    await ctx.send("You can't travel without a :page_facing_up: travel pass! Get a job. Maybe your employer will let you have some...")

@travel.error
async def travel_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the district you want to travel to after the travel command.\nExample: {prefix(client, ctx.message)}travel 3')

dice_pics = {'<:d6:806019379774226452>': 6, '<:d5:810328229444452363>': 5, '<:d4:806019355996979231>': 4, '<:d3:810328197484118017>': 3, '<:d2:806019324804333568>': 2, '<:d1:810328161127497778>': 1}

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def use(ctx, *, arg1):
  if arg1.lower() not in usables:
    await ctx.send("You can't use this item!")
  else:
    unboxing_words = ['Amazing! You found one', 'Wow, in the box is one', 'You found one', 'You obtained one']
    if arg1.lower() == 'reward box':
      await ctx.send('Opening reward box...')
      items = random.randint(3, 7)
      templist = []
      for item in range(items):
        gift = random.choice(shop_id)
        templist.append(gift)
        await buyo(ctx.author, 0, gift)
        await ctx.send(f'{random.choice(unboxing_words)} {gift} {icon(gift)}.')
        await asyncio.sleep(1)
      await useo(ctx.author, "reward box")
      await ctx.send(f'You have obtained {items} items from the reward box!')
    elif arg1.lower() == "computer":
      await ctx.send('Would you like to obtain a travel pass or hack?\nRespond with `1` for travel pass and `2` for hack.')
      def check(m):
        return m.author == ctx.message.author

      try:
        msg = await client.wait_for('message', check=check, timeout=20)
      except:
        await ctx.send(':clock8: Your search timed out...')
        return

      ok = ['1', '2']
      if msg.content not in ok:
        await ctx.send('Please specify a valid choice!')
        return
      else:
        if msg.content == '1':
          rate = random.randint(1, 100)
          if rate >= 70:
            await ctx.send("Whoops, your internet connection cut out when trying to go onto the Capitol's TransPlan website. Try again.")
          else:
            bank = author_info(ctx.author, "bank")
            if bank < 4000:
              await ctx.send("You can't afford a travel pass! The money you have in your bank is below $4000!")
            else:
              await buyo(ctx.author, 0, "travel pass")
              await money_change(ctx.author, -4000, "bank")
              await ctx.send("You managed to purchase 1 travel pass for a price of $4000. Yes, it's double the price of the passes sold in District 5.")
        elif msg.content == '2':
          hackem = discord.Embed(title='Which institution would you like to hack?', description='If you succeed, you are given the specified reward money. If you fail, you are flogged.', color=random.choice(colors))
          hacks = {1: {"name": "District Office", "risk": 30, "reward": 300}, 2: {"name": "The Government of Panem's main office", "risk": 70, "reward": 40000}, 3: {"name": "District 3's tech labs", "risk": 40, "reward": 3000}}

          for item in hacks:
            hackem.add_field(name=f'{item}. {hacks[item]["name"]}', value=f'Risk: {hacks[item]["risk"]}% | Reward: ${hacks[item]["reward"]}', inline=False)
          hackem.set_thumbnail(url='https://www.pngitem.com/pimgs/m/548-5488692_icon-hacker-225854374-hd-png-download.png')
          await ctx.send(embed=hackem)
          await ctx.send('Respond by typing the number of the institution you want to hack.\nExample: 1')
          def check(m):
            return m.author == ctx.message.author

          try:
            msg = await client.wait_for('message', check=check, timeout=20)
          except:
            await ctx.send(':clock8: Your search timed out...')
            return

          hax = ['1', '2', '3']
          choice = msg.content
          if choice not in hax:
            await ctx.send('Please specify an actual place you want to hack into.')
          else:
            rate = random.randint(1, 100)
            risky = hacks[int(choice)]["risk"]
            reward = hacks[int(choice)]["reward"]
            if rate <= risky:
              hp = random.randint(70, 120)
              msga = await ctx.send('Booting up...')
              await msga.edit(content='Getting past the firewall...')
              await asyncio.sleep(1)
              await msga.edit(content='Exposing passwords...')
              await asyncio.sleep(1)
              await msga.edit(content='Locating secure file...')
              await asyncio.sleep(1)
              await msga.edit(content='Retrieving pass-key...')
              await asyncio.sleep(1)
              await msga.delete()
              em = discord.Embed(title="Oh no, the Capitol's cyber-force has caught you hacking! You are publicly flogged as a punishment for mutiny and misconduct.", description=f"Your HP has decreased by `{hp}`.", color=random.choice(colors))
              em.set_thumbnail(url="https://www4.pictures.zimbio.com/mp/9aPz5Ed772Zl.jpg")
              await hp_change(ctx.author, -1*hp)
              await ctx.send(embed=em)
              await dying(ctx.author, ctx.message)
            else:
              msga = await ctx.send('Booting up...')
              await msga.edit(content='Getting past the firewall...')
              await asyncio.sleep(1)
              await msga.edit(content='Exposing passwords...')
              await asyncio.sleep(1)
              await msga.edit(content='Locating secure file...')
              await asyncio.sleep(1)
              await msga.edit(content='Retrieving pass-key...')
              await asyncio.sleep(1)
              await msga.delete()
              await money_change(ctx.author, reward, "bank")
              await ctx.send(f'You have succeeded! ${reward} has been banked into your bank account.')
    
@use.error
async def use_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the item you want to use after the command. So far, only `reward boxes` and `computers` can be used.\nExample: {prefix(client, ctx.message)}use reward box')
    
@client.command(aliases = ['Forage'])
@commands.cooldown(1, 15, commands.BucketType.user) 
async def forage(ctx):
  forage_words = ['behind a tree!', 'stuck inside a small aquifer.', 'in a pond.']
  rate = random.randint(1, 100)
  item = random.choice(forage_stuff)
  if rate <= 60:
    await buyo(ctx.author, 0, item.lower())
    await ctx.send(f'You found one {item} {icon(item.lower())} {random.choice(forage_words)}')
  elif rate > 60 and rate <= 90:
    await ctx.send('You spent hours in the woods foraging and found nothing. Sad life...')
  else:
    itema = random.choice(shop_id)
    await buyo(ctx.author, 0, itema.lower())
    await ctx.send(f"Wow! You happened to stumble upon 1 {itema} {icon(itema.lower())} when foraging for food! Let's hope whoever who left it there isn't dead or imprisoned in the Capitol...")

async def hp_check(author):
  hp = author_info(author, "HP")
  if hp > 200:
    num = hp - 200
    await hp_change(author, -1*num)
  else:
    pass

@client.command(aliases = ['Eat']) 
async def eat(ctx, *, arg1):
  food = check_item_value(ctx.author, arg1.lower())
  hpe = author_info(ctx.author, "HP")
  if hpe >= 200:
    await ctx.send("You have maxed out your health! Don't eat any more stuff!")
    return
  if arg1.lower() in edibles and food >= 1:
    await sello(ctx.author, 0, arg1.lower())
    await hp_change(ctx.author, hp_food[arg1.lower()])
    await ctx.send(f'You ate 1 yummy {arg1} {icon(arg1.lower())} and replenished `{hp_food[arg1.lower()]}` health!')
    await hp_check(ctx.author)
  elif arg1.lower()  not in edibles:
    await ctx.send("You can't eat this item!")
  elif arg1.lower() in edibles and food < 1:
    await ctx.send(f"Sorry mate. You don't have any {arg1.lower()}.")

@eat.error
async def eat_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the item you want to eat after the eat command.\nExample: {prefix(client, ctx.message)}eat katniss')

@client.command(aliases = ['dep', 'Deposit'])
async def deposit(ctx, arg1):
  try:
    if float(arg1).is_integer() == False:
      await ctx.send('Please specify a positive integer!')
      return
  except:
    await ctx.send('Please specify the amount of money you want to deposit!')
    return

  value = abs(int(arg1))
  if afford(ctx.author, value, "wallet") == 1:
    await money_change(ctx.author, -1*value, "wallet")
    await money_change(ctx.author, value, "bank")
    await ctx.send(f'You have deposited ${value}.')
  else:
    await ctx.send('You are trying to deposit more money than you have!')

@deposit.error
async def deposit_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the amount of cash you want to deposit after the command.\nExample: {prefix(client, ctx.message)}deposit 2000')

@client.command(aliases = ['with', 'Withdraw'])
async def withdraw(ctx, arg1):
  try:
    if float(arg1).is_integer() == False:
      await ctx.send('Please specify a positive integer!')
      return
  except:
    await ctx.send('Please specify the amount of money you want to deposit!')
    return

  value = abs(int(arg1))
  if afford(ctx.author, value, "bank") == 1:
    await money_change(ctx.author, value, "wallet")
    await money_change(ctx.author, -1*value, "bank")
    await ctx.send(f'You have withdrawn ${value}.')
  else:
    await ctx.send('You are trying to withdraw more money than you have!')

@withdraw.error
async def withdraw_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the amount of cash you want to withdraw after the command.\nExample: {prefix(client, ctx.message)}withdraw 2000')

@client.command(aliases = ['Sell'])
async def sell(ctx, arg1, *, itema):
  if itema in shop_id:
    price = round(check_item_price(itema.lower())/2)
    rich = check_item_value(ctx.author, itema.lower())
    if rich >= int(arg1):
      await sello(ctx.author, price, itema)
      await ctx.send(f'You have sold one {itema} and gained ${price}!')
    else:
      await ctx.send("You don't have this item!")
  else:
    try:
      a = int(arg1)
      await ctx.send("Sorry mate. You can't buy or sell this item.")
    except:
      await ctx.send(f'Please specify all of the required arguments!\nExample: {prefix(client, ctx.message)}sell 3 bow')

@sell.error
async def sell_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify all of the required arguments!\nExample: {prefix(client, ctx.message)}sell 3 bow')

worklist = {"Jeweller": {"district": 1, "trivia": ["Diamond exists 150 - 250km below ground.", "Don't mess this one up, it's for President Snow's wife.", "Aw man, the gemcutter's broken again!", "Make sure the gemstones aligned on this bracelet are symmetrical.", "Another shipment of bracelets to the Capitol."], "pay": 2000, "die": ["cut yourself by accident with a diamond cutter", "messed up a bracelet meant for President Snow's wife", "burned yourself with a soldering tool"]}, "Seamstress": {"district": 1, "trivia": ["A thimble is the best form of protection against pricked thumbs.", "The only permitted material for towels here are silk.", "Use the seam ripper to open thse seams.", "These dresses have to be fixed.", "Use an industrial sewing machine for this one - it's made from armourweave."], "pay": 2000, "die": ["pricked your carotid artery", "had a needle poke right through your finger", "got scratched by the sewing machine LOL"]}, "Blacksmith": {"district": 2, "trivia": ["You can quench your blades in water or oil.", "These blades will be littered around the Arena, hopefully not impaling the unwary challenger.", "Can you place an order for more steel?", "I'm so damn tired today.", "There's some sign of chipping on this blade."], "pay": 1000, "die": ["burned yourself when quenching your blade", "almost cut your hand off", "was burned by the furnace"]}, "Industrial worker (Metals)": {"district": 2, "trivia": ["The four basic industrial processes are machining, joining, casting and moulding.", "Get going, the foreman's here today.", "These shipments of bauxite must be processed into aluminium tomorrow.", "I might be transferred to the steel refinery near Victor's village.", "I need some pig iron from that blast furnace to produce steel."], "pay": 2000, "die": ["touched a live wire and got burned", "was burned by molten steel", "was cut by the metal-cutter"]}, "Coder": {"district": 3, "trivia": ["In the python language, there is no ;", "Hey StackOverflow, how to fix this bug?", "The cyclomatic complexity for this code is too high!", "I can't seem to figure out where the bug is!", "Ugh, this computer's so laggy, wish we have those newfangled Intiums from the Capitol."], "pay": 2000, "die": ["got locked in a freezing server farm", "touched a live wire", "had a server fall on yourself"]}, "Industrial worker (Electronics)": {"district": 3, "trivia": ["Water used in chip fabrication must be pH 7.", "They say the chips we make are used in robots of war.", "Send these new computers to the loading bay.", "I think we're getting a shipment of silicon tomorrow.", "Oi, make sure the server farm is kept cool enough!"], "pay": 2000, "die": ["cut yourself badly when installing the new laser-cutting machine", "was poisoned by hexavalent chromium", "touched a live wire"]}, "Fisherman": {"district": 4, "trivia": ["Fish commonly found in Panem are tilapia and panfish.", "Who let a cat on board?", "Get away, there's a shark!", "Can you help me fix this net please?"], "pay": 1500, "die": ["fell into the water and was stung by a jellyfish", "was bitten by a shark", "sprained your arm trying to haul in a huge tuna"]}, "Mechanic": {"district": 4, "trivia": ["This fishing trawler needs a repaint.", "Look what just rolled into the shop.", "Hey, this propeller is in really bad shape", "Let's hope Jerard's happy with this repair, resources are really strained at the moment."], "pay": 2000, "die": ["inhaled toxic paint vapor by accident", "touched a live wire", "was hurt by a spinning boat propeller"]}, "Industrial worker (Energy)": {"district": 5, "trivia": ["A step-down transformer reduces voltage.", "Electric coverage in Panem has evolved shockingly over the years.", "Go and replace solar panel 4, I think it's broken.", "Can you help me install this new control unit?", "District 3's been using too much energy lately."], "pay": 2000, "die": ["touched a live wire and got burned", "fell from a tower", "were cut by barbed wire"]}, "Electrical engineer": {"district": 5, "trivia": ["Power equals to current times voltage.", "Have you tried turning it off and on again?", "Man, these new wires are heavy", "Guess I'll have to pull overtime again, trying to figure out what's wrong with the new power plant."], "pay": 3000, "die": ["accidentally left a switch open and zapped yourself", "cut yourself with barbed wire", "touched a live wire and died"]}, "Transport officer": {"district": 6, "trivia": ["Papers, please.", "Glory to the Capitol.", "What are you going to District 7 for?", "Holup, this travel pass looks like a fake.", "That guy has morphling in his bag. Seize him."], "pay": 2000, "die": ["was shot by a Peacekeeper for accidentally letting a rebel through", "were pushed onto the tracks", "were hit by a bus"]}, "Transport Engineer": {"district": 6, "trivia": ["Magnetic levitation trains are energy efficient and fast.", "Funny how we build electric cars all day but still have to walk to work.", "Something's wrong with that hovercraft's right motor.", "This train engine is full of dust! No wonder it broke down.", "Try to salvage something from this decomissioned train."], "pay": 3000, "die": ["touched a live wire and got electrocuted", "were pushed onto the tracks", "were hit by a bus"]}, "Lumberjack": {"district": 7, "trivia": ["Alright, get your chainsaw and cut that tree over there.", "I need to get a new checkered shirt.", "Oh crap, my saw's broken.", "We've got an order for 100kg of pine wood.", "Can you help me fix this chainsaw?"], "pay": 2000, "die": ["cut a tree the wrong way which caused it to fall right onto your head", "cut yourself with a chainsaw", "fell into a hole"]}, "Saw mill worker": {"district": 7, "trivia": ["Ironwood planks are extremely durable.", "How much wood can a woodchuck chuck if a woodchuck could chuck wood?", "Never gonna give you up, never gonna let you down, never gonna run around and desert you :)", "We've got an order for 100 planks.", "Help me fix this sawmill."], "pay": 2000, "die": ["cut yourself with an electric saw by accident", "went through the sawmill", "had a log roll over you"]}, "Industrial worker (Textiles)": {"district": 8, "trivia": ["These bedsheets look so comfy.", "There's so much cotton in here... Achoo!", "I love the colour of those lime green dyes.", "Handle that vat of dye properly.", "Too bad we can't use any of the cloth we're making for our clothes."], "pay": 2000, "die": ["succumbed to dye poisoning", "ingested toxic dye", "fell into the dyeing chamber"]}, "Peacekeeper uniform seamstress": {"district": 8, "trivia": ["Peacekeeper armour is made from Kevlar.", "Don't forget to pad the insides.", "Make sure the uniforms are all spick and span", "Only armourweave, rubber and Kevlar are used for Peacekeeper uniforms.", "These helmets are really freaky."], "pay": 3000, "die": ["pricked your wrist by accident", "messed up on a batch and was beaten up by a Peacekeeper", "cut yourself with scissors"]}, "Wheat farmer": {"district": 9, "trivia": ["There are 20 types of wheat.", "I'm so hungry I could eat the dough out of the vat.", "Why isn't this tractor working?", "High grade wheat goes to the Capitol.", "Spray some of that insecticide here, I want to be rid of those hideous bugs."], "pay": 1500, "die": ["fell into a wheat processing machine LOL", "was run over by a tractor"]}, "Baker": {"district": 9, "trivia": ["Zymase is produced by yeast to make bread rise.", "Baguettes for District 1 unleavened for District 12.", "Mmmmmm, these doughnuts smell great!", "It's odd how we produce so much bread but don't eat much of them.", "We don't have enough yeast, what do we do?"], "pay": 2000, "die": ["nearly had your fingers cut off by the bread-cutting machine", "fell into a vat", "fell into the bread-cutting machine"]}, "Cattle farmer": {"district": 10, "trivia": ["If a cow isn't milked for too long, its udder will burst.", "Wait, you're telling me a cowboy doesn't herd cows?", "Male cows produce more beef; female cows produce milk", "Herd those heifers into Area 4.", "Pasteurise the milk at 72C."], "pay": 2000, "die": ["was charged at by a bull", "fell into cow dung", "was trampled under a stampede of cows"]}, "Meatpacker": {"district": 10, "trivia": ["Meat must conform to A34 standards set by the Capitol.", "I can't stand WcBonalds or PFC anymore.", "We've got an order for 100kg of beef.", "Process this load of beef into sausages.", "It's odd that we produce so much beef but still starve everyday."], "pay": 2000, "die": ["nearly cut your hand off", "fell into the meat grinder", "cut yourself with a chopper"]},"Orchard Farmer": {"district": 11, "trivia": ["Pick those apples from that tree/", "This tree needs some pruning.", "Can you help me fix this pickup truck?", "Send these oranges to loading bay 4.", "The pear orchard is estimated to begin production next year."], "pay": 2000, "die": ["fell from a ladder", "was hit by a truck", "fell from a maple tree"]}, "Fruitpacker": {"district": 11, "trivia": ["Fruit must conform to A34 standards set by the Capitol.", "Send oranges to the Capitol, apples to District 8.", "Fruit must be waxed before being packaged", "Mmmmm, these mangoes smell so fragrant, it's a shame we can't eat any of them.", "Help me fix this waxing machine."], "pay": 2000, "die": ["fell into an automatic fruit-cutting machine", "fell into the fruit-waxer", "cut yourself with a chopper"]}, "Coal miner": {"district": 12, "trivia": ["Make sure there are no stray pieces of coal on the minecart rails.", "Coal mining is a dangerous job.", "Make sure you wear your mask properly, I don't want you to die from lung cancer.", "Get this cart working.", "We're going to be mining coal from Deposit 3A today."], "pay": 1500, "die": ["died in a mineshaft cave-in", "was run over by a minecart", "contracted lung disease"]}, "Mining engineer": {"district": 12, "trivia": ["Explosives must be used sparingly.", "We gotta fix this tunneling machine.", "Get that dynamite over here.", "Send this huge load of coal to loading bay 4.", "Don't go into that shaft, the toxicity level is way too high."], "pay": 1800, "die": ["accidentally blew yourself up with dynamite", "was run over by a minecart", "had a shaft collapse on you"]}}

@client.command(aliases = ['inv', 'Inventory'])
async def inventory(ctx):
  em=discord.Embed(title=f'Inventory stats for {ctx.author.name}', description=f'Type {prefix(client, ctx.message)}shop <item> to get information for a specific product.', color=random.choice(colors))
  em.set_thumbnail(url=ctx.author.avatar_url)

  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  initinv = inv[str(ctx.author.id)]

  for item in initinv:
    if item["value"] != 0:
      em.add_field(name=f'{icon(item["name"].lower())} {item["name"]}', value=item["value"], inline=True)
    else:
      pass
  await ctx.send(embed=em)

@client.command(aliases = ['Work'])
@commands.cooldown(1, 1800, commands.BucketType.user) 
async def work(ctx):
  district = author_info(ctx.author, "district")
  worka = author_info(ctx.author, "job")
  if worka != "Nil":
    if district == worklist[worka]["district"]:
      try:
        rate = random.randint(1, 100)
        task = random.choice(worklist[worka]["trivia"])
        await ctx.send(f'Type this in the chat within 30 seconds!\n`{task}`')

        def check(m):
          return m.content == task and m.author == ctx.message.author

        await client.wait_for('message', check=check, timeout=30)
        if rate >= 65:
          await ctx.send(f"Good job, {ctx.author.name}! Here are your daily wages and I've decided to reward you with a travel pass for your hard work!")
          await money_change(ctx.author, worklist[worka]["pay"], "bank")
          await buyo(ctx.author, 0, "travel pass")
        else:
          await ctx.send(f"Good job, {ctx.author.name}! Your daily wages have been banked into your account. 💰")
          await money_change(ctx.author, worklist[worka]["pay"], "bank")
      except:
        rate = random.randint(1, 100)
        if rate <= 85:
          hp = random.randint(1, 60)
          await hp_change(ctx.author, -1*hp)
          await ctx.send(f'Oof, you {random.choice(worklist[worka]["die"])}. You have lost {hp}HP.')
          await dying(ctx.author, ctx.message)
        else:
          await ctx.send(f'Oh crap, you {random.choice(worklist[worka]["die"])} and died as a result!')
          await hp_change(ctx.author, -200)
          await dying(ctx.author, ctx.message)
    elif district != worklist[worka]["district"]:
      await ctx.send('Go back to your home district! You are of no use here!')
  else:
    await ctx.send(f'Go get a job to contribute to the great nation of Panem. Type `{prefix(client, ctx.message)}job` to find one. Note: You can only obtain a job that exists in your district. Use the `{prefix(client, ctx.message)}joblist` command to get a list of jobs.')

@client.command(aliases = ['Job'])
async def job(ctx, arg1):
  try:
    worka = int(arg1) - 1
    district = author_info(ctx.author, "district")
    jobprev = author_info(ctx.author, "job")
    templist = list(worklist)
    work = templist[worka]
    if jobprev != "Nil":
      await ctx.send(f'You are already working as a {jobprev}! Sorry, the government of Panem does not allow its citizens to change jobs.')
    else:
      if district == worklist[work]["district"]:
        await job_change(ctx.author, work)
        await ctx.send(f'You are now working as a {work}.')
      else:
        await ctx.send(f'The job you are applying for ({work}) is not available in your district.')
  except ValueError:
    await ctx.send(f'Please specify the index of the job according to the joblist command.\nExample: {prefix(client, ctx.message)}job 2')
  except IndexError:
    await ctx.send('The job you are trying to apply for does not exist!')

@job.error
async def job_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the index of the job according to the joblist command.\nExample: {prefix(client, ctx.message)}job 2')

@client.command(aliases = ['Joblist'])
async def joblist(ctx):
    em = discord.Embed(title='Showing jobs available', description=f'Get a job by typing `{prefix(client, ctx.message)}job <1>`.', color=random.choice(colors))
    templist = list(worklist)
    for item in worklist:
      em.add_field(name=f'{templist.index(item)+1}. {item}', value=f'District: {str(worklist[item]["district"])} | Pay: ${str(worklist[item]["pay"])}', inline=True)
    await ctx.send(embed=em)

services = {"fix a broken train": {"risk": 20, "stuff": "toolbox"}, "slay loose mutts in the Capitol's subway system": {"risk": 50, "stuff": "bow"}, "explore ruins of former North American cities": {"risk": 30, "stuff": "jacket"}, "fix a bridge suspended 400m above ground.": {"risk": 25, "stuff": "toolbox"}, "lead a massive mining project in the caves of District 12": {"risk": 30, "stuff": "toolbox"}}

@client.command(aliases = ['Service', 'serv'])
@commands.cooldown(1.0, 3600, commands.BucketType.user) 
async def service(ctx):
  task = ['This job is really dangerous.', 'Stay away from mutt pee; it may be poisonous.', 'Budget cuts have made armour unavailable for these missions', 'Make sure your will is kept up to date.', 'Goodbye, lover.']
  em=discord.Embed(title='Thank you for contributing your labor to the great nation of Panem.', description="There are a few jobs that are in demand right now. Make sure you have a toolbox at the ready! Please wait while we contact the Capitol's labor department to find out which job we need you to do.", color=random.choice(colors))
  em.set_thumbnail(url='https://i.redd.it/vpdp2ylf4gq01.png')
  msg = await ctx.send(embed=em)
  await asyncio.sleep(3)
  l = list(services)
  a = random.choice(l)
  serv = services[a]
  er = discord.Embed(title=f'Your mission is to {a}', description=f'Risk: {serv["risk"]}%\nYou need a {serv["stuff"]}', color=random.choice(colors))
  await msg.delete()
  await ctx.send(embed=er)
  val = check_item_value(ctx.author, serv["stuff"])
  if val >= 1:
    try:
      t = random.choice(task)
      await ctx.send(f'Send this in the chat within 10 seconds!\n`{t}`')

      def check(m):
        return m.content == t and m.author == ctx.message.author

      await client.wait_for('message', check=check, timeout=10)
      rate = random.randint(1, 100)
      if rate <= serv["risk"]:
        hp = random.randint(1, 60)
        await hp_change(ctx.author, -1*hp)
        await ctx.send(f'Whoops, you got into a bad accident while trying to {a} and lost `{hp}` HP.')
        await dying(ctx.author, ctx.message)
      else:
        ratetwo = random.randint(1, 100)
        if ratetwo >= 50:
          await money_change(ctx.author, 3000, "wallet")
          await buyo(ctx.author, 0, "travel pass")
          await buyo(ctx.author, 0, "travel pass")
          await ctx.send('Good job, citizen! As a reward for your service, the government of Panem has given you 2 travel passes and 3000 coins.')
        else:
          await money_change(ctx.author, 3000, "wallet")
          await ctx.send('Good job, citizen! As a reward for your service, the government of Panem has given you 3000 coins.')
    except:
      hp = random.randint(1, 60)
      await hp_change(ctx.author, -1*hp)
      await ctx.send(f'Whoops, you got into a bad accident while trying to {a} and lost `{hp}` HP.')
      await dying(ctx.author, ctx.message)
  else:
    await ctx.send(f'Please buy a {serv["stuff"]} first!')

@client.command(aliases = ['Will'])
async def will(ctx, member: discord.Member):
  with open('bank.json', 'r') as f:
    val = json.load(f)
  
  if str(member.id) not in val:
    await ctx.send(f'Please ask your friend to create an account by typing `{prefix(client, ctx.message)}create` first!')
  elif str(member.id) == str(ctx.author.id):
    await ctx.send("You can't use your acccount as your successor.")
  else:

    val[str(ctx.author.id)]["successor"] =  {"name": member.name, "id": member.id}

    with open('bank.json', 'w') as f:
      json.dump(val, f, indent=4)
  
    await ctx.send(f'When you die, 70% of your wealth will be given to {member} as well as some of your items.')

@will.error
async def will_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the user you want to include in your will.\nExample: {prefix(client, ctx.message)}will @Andrea')

@client.command(aliases = ['Fish'])
@commands.cooldown(1, 15, commands.BucketType.user) 
async def fish(ctx):
  rod = check_item_value(ctx.author, "fishing rod")
  if rod >= 1:
    rate = random.randint(1, 100)
    fish_stuff = ["tilapia", "panfish"]
    if rate <= 85:
      f = random.choice(fish_stuff)
      await buyo(ctx.author, 0, f)
      await ctx.send(f'You went fishing and came back with one {f} {icon(f.lower())}!')
    else:
      ratetwo = random.randint(1, 100)
      if ratetwo <= 75:
        hp = random.randint(1, 30)
        await hp_change(ctx.author, -1*hp)
        await ctx.send(f'You encountered a crocodile while fishing and managed to get away! However, your fishing rod was almost damaged and you lost {hp}HP.')
        await dying(ctx.author, ctx.message)
      else:
        hp = random.randint(1, 30)
        await hp_change(ctx.author, -1*hp)
        await useo(ctx.author, "fishing rod")
        await ctx.send(f'You encountered a crocodile while fishing and managed to get away! However, your fishing rod was damaged beyond repair and you lost {hp}HP.')
        await dying(ctx.author, ctx.message)
  else:
    await ctx.send(f"You don't have a fishing rod! Buy one as soon as possible to fish!")

hquiz = {"Who did Katniss team up with during the 74th Hunger Games?\nA Rue\nB Thresh\nC Cato\nD Foxface": "A", "What is Peeta's surname?": "Mellark", "Which district contributes its people to the Capitol's Peacekeeper force?": "2", "What is the usual colour of a Peacekeeper's uniform?": "white", "Which district is the poorest in the entire nation of Panem?": "12", "What is the black market called in District 12?": "The Hob", "What is Katniss' sister's name?": "Prim", "Which of the following were Peacekeepers in District 12?\nA Darius\nB Delly Cartwright\nC Boggs\nD Beetee": "A", "How old was Rue when she was picked to join the Hunger Games in the reaping?": "12", "What is the opening phrase of Panem's national anthem?": "The Horn of Plenty overflows", "What is District 3's industry?": "electronics", "Which district did Beetee come from?": "3", "Who was Katniss' stylist in the Hunger Games?": "Cinna", "Who acted as Katniss in the Hunger Games film series?": "Jennifer Lawrence", "What is District 5's industry?": "transportation", "Who was Peeta's stylist during the 74th Hunger Games?": "Portia", "What is President Snow's full name?": "Coriolanus Snow", "Who did President Paylor succeed?": "President Coin", "What was mined in District 13?": "graphite", "What was mined in District 12?": "coal", "What was the rebellion called?": "Mockingjay", "Was Plutarch Heavensbee a double agent?\nA Yes\nB No": "A", "Who was known as the sex symbol of Panem?": "Finnick Odair", "Which of the following was a former tribute in the Hunger Games?\nA Primrose Everdeen \nB Delly Cartwright\nC Johanna Mason\nD Boggs": "C"}

tributes = {12: ["Andrea Mitch", "Ian Lee"], 11: ["Enora Mason", "Michael Halpert"], 10: ["Tris", "Mitch"], 9: ["Francis", "McGregor"], 8: ["Tripp", "Hunter"], 7: ["Rachel Keefe", "Kylie"],6: ["Conner Bailey", "Alex Bailey"], 5: ["Frank", "Erin"], 4: ["Rade", "Sara"], 3: ["Pris", "Bender"], 2: ["Glimmer", "Mike"], 1: ["Anselm", "Grace"]}

tribute_die = ['was slain by another tribute.', 'was hit by a fireball.', 'was shot with an arrow.', 'froze to death in the icy lake.', 'died in a duel with another player.', 'was mauled to death by mutt wolves.', 'fell into a lava pit.']

spectate = ['Terrence from District 4 has stabbed Erin from District 2!', 'Jim from District 11 was killed by Dwight from District 2 in a bloodbath at the Cornucopia', 'Michael from District 12 narrowly escaped from a snake!']

danger = ["you've run into a fierce looking tribute from District 5", "fireballs are shooting at you from all directions", "you're being chased by a ferocious mutt wolf", "bullets are zipping past you from all directions", "you're in a duel with a large tribute"]

@client.command(aliases = ['hungergame', 'Hgame'])
@commands.cooldown(1, 1800, commands.BucketType.user)
async def hgame(ctx):
  rate = random.randint(1, 100)
  embed= discord.Embed(title='Let the hunger games begin!', description='As a sign of loyalty and submission, every district must send two representatives to take part in the Hunger Games. The 24 tributes would fight to the death in an arena crafted skillfully by the engineers of the Capitol. Please wait for the reaping to finish.', color=random.choice(colors))
  embed.set_thumbnail(url="https://i.pinimg.com/originals/f4/72/14/f47214d148cfd2e87ac1a44f11754ee6.jpg")
  await ctx.send(embed=embed)
  await asyncio.sleep(1)
  if rate <= 40:
      await ctx.send('You have been chosen as a tribute! You will bring glory to your district if you win and death to yourself if you die. Let the hunger games begin!')
      for item in range(6):
        hpa = author_info(ctx.author, "HP")
        if hpa >= 1:
          l = list(hquiz)
          r = random.choice(l)
          try: 
            ans = hquiz[r]
            await ctx.send(f"Oh no, {random.choice(danger)}! Answer this question in 20 seconds to get away!\n{r}")

            def check(m):
              return m.content == hquiz[r] and m.author == ctx.message.author

            await client.wait_for('message', check=check, timeout=20)
            await ctx.send('You managed to survive!')
          except:
            hp = random.randint(30, 60)
            await hp_change(ctx.author, -1*hp)
            await ctx.send(f'You get injured and lose {hp}HP. The answer is {ans}, dummy!')
            await dyinga(ctx.author, ctx.message)
          await asyncio.sleep(2)
        else:
            await ctx.send(random.choice(spectate))
            await asyncio.sleep(2)
      hpe = author_info(ctx.author, "HP")
      if hpe >= 1: 
        await buyo(ctx.author, 0, "reward box")
        await money_change(ctx.author, 42000, "bank")
        await ctx.send(f'{ctx.author.mention} The Hunger Games are over! As a winner, you are rewarded with $42000 and a reward box!')
      else:
        await ctx.send(f'{ctx.author.mention} You have lost the Hunger Games. Better luck next time!')
        await hp_change(ctx.author, 1000)
        await hp_check(ctx.author)
  else:
    await ctx.send('You have not been chosen to participate in the Hunger Games. However, you may bet on tributes chosen. Please enter the district of the tribute you want to bet on.')
    def check(m):
      return m.author == ctx.message.author

    msg = await client.wait_for('message', check=check, timeout=20)
    dis = msg.content
    districts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    if dis not in districts:
      await ctx.send('You blew your chance to gamble! You have to enter the number of the district you want to bet on!\nExample: 12')
    else:
      await ctx.send(f'Alright, now enter the amount of money you want to bet on the District {dis} tributes.')
      def check(m):
        return m.author == ctx.message.author

      msga = await client.wait_for('message', check=check, timeout=20)

      cash = msga.content
      rich = author_info(ctx.author, "wallet")
      if int(cash) <= rich:
          wins = random.randint(1, 100)
          if wins >= 80 and wins <= 100:
            templist = []
            for item in range(1, 13):
              tname = f'{random.choice(tributes[item])}[{item}]'
              templist.append(tname)
            for item in templist:
              if item[4:] == f'[{dis}]' or item[3:] == f'[{dis}]':
                templist.remove(item)
            await ctx.send(f'You are betting on two District {dis} tributes: {tributes[int(dis)][0]} and {tributes[int(dis)][1]}')
            for item in range(6):
              num = random.choice(templist)
              await ctx.send(f'{num} {random.choice(tribute_die)}')
              templist.remove(num)
              await asyncio.sleep(2)
            await ctx.send(f'{tributes[int(dis)][0]} and {tributes[int(dis)][1]} survived and won! You have won ${int(cash)*2}!')
            await money_change(ctx.author, int(cash)*2, "wallet")
          elif wins <= 79 and wins >= 50:
            templist = []
            for item in range(1, 13):
              tname = f'{random.choice(tributes[item])}[{item}]'
              templist.append(tname)
            for item in templist:
              if item[4:] == f'[{dis}]' or item[3:] == f'[{dis}]':
                templist.remove(item)
            templist.append(f'{random.choice(tributes[int(dis)])}[{dis}]')
            await ctx.send(f'You are betting on two District {dis} tributes: {tributes[int(dis)][0]} and {tributes[int(dis)][1]}')
            for item in range(6):
              num = random.choice(templist)
              await ctx.send(f'{num} {random.choice(tribute_die)}')
              templist.remove(num)
              await asyncio.sleep(2)
            listre = []
            listre.append(tributes[int(dis)][0])
            listre.append(tributes[int(dis)][1])
            loser = random.choice(listre)
            await ctx.send(f'**{loser} {random.choice(tribute_die)}**')
            listre.remove(loser)
            await ctx.send(f'{listre[0]} survived and won! You have won ${cash}!')
            await money_change(ctx.author, int(cash), "wallet")
          else:
            templist = []
            for item in range(1, 13):
              tname = f'{random.choice(tributes[item])}[{item}]'
              templist.append(tname)
            for item in templist:
              if item[4:] == f'[{dis}]' or item[3:] == f'[{dis}]':
                templist.remove(item)
            await ctx.send(f'You are betting on two District {dis} tributes: {tributes[int(dis)][0]} and {tributes[int(dis)][1]}')
            for item in range(6):
              num = random.choice(templist)
              await ctx.send(f'{num} {random.choice(tribute_die)}')
              await asyncio.sleep(2)
            t1 = tributes[int(dis)][0]
            t2 = tributes[int(dis)][1]
            await ctx.send(f'**{t1} {random.choice(tribute_die)}**')
            await ctx.send(f'**{t2} {random.choice(tribute_die)}**')
            await ctx.send(f'{t1} and {t2} died and lost! You have lost ${cash}.')
            await money_change(ctx.author, -1*int(cash), "wallet")
      else:
          await ctx.send('You are trying to bet more money than you have in your wallet!')

@hgame.error
async def hgame_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    with open('bank.json', 'r') as f:
      inv = json.load(f)
    if str(ctx.author.id) not in inv:
      await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create`!')
    else:
      await ctx.send("Slowpoke. The ship has sailed. Try again next time.")

@client.command(aliases=['Tesserae'])
@commands.cooldown(1.0, 3600.0, commands.BucketType.user) 
async def tesserae(ctx):
  await buyo(ctx.author, 0, "bread")
  await buyo(ctx.author, 0, "bread")
  await buyo(ctx.author, 0, "bread")
  await buyo(ctx.author, 0, "bread")
  await buyo(ctx.author, 0, "bread")
  await buyo(ctx.author, 0, "beef")
  bread = productlist_info("bread")
  beef = productlist_info("beef")
  await ctx.send(f'{ctx.author.name}, you have been given 5 bread {bread["icon"]}  and 1 beef {beef["icon"]}.')

def author_rank(author):
  with open('bank.json', 'r') as f:
    b = json.load(f)
  templist = []
  for item in b:
    wal = b[item]["wallet"] + b[item]["bank"]
    templist.append(wal)
  templist.sort(reverse=True)
  walbank = b[str(author.id)]["wallet"] + b[str(author.id)]["bank"]
  for item in templist:
    if walbank == item:
      return(templist.index(item)+1)
    else:
      pass

@client.command(aliases=['lb'])
async def leaderboard(ctx):
  with open('bank.json', 'r') as f:
    b = json.load(f)
  templist = []
  for item in b:
    wal = b[item]["wallet"] + b[item]["bank"]
    templist.append(wal)
  templist.sort(reverse=True)
  em = discord.Embed(title='Showing global rankings for wealth', description=f'Your rank: `{author_rank(ctx.author)}`', color=random.choice(colors))
  for item in range(5):
    for author in b:
      try:
        worth = b[author]["wallet"] + b[author]["bank"]
        if worth == templist[item]:
          name = await client.fetch_user(int(author))
          em.add_field(name=f'{str(item + 1)}. {name}' , value=f'Total wealth: ${worth}', inline=False)
        else:
          pass
      except IndexError:
        pass
  await ctx.send(embed=em)

@client.command(aliases = ['Give'])
async def give(ctx, user: discord.Member, arg2, *, arg1):
  if int(arg1) <= 0:
    await ctx.send('Please specify a positive value!')
    return
  nes = check_item_value(ctx.author, arg1)
  if nes > int(arg2):
    for item in range(int(arg2)):
      await buyo(user, 0, arg1)
      await sello(ctx.author, 0, arg1)
    await ctx.send(f'You have given {user.name} {arg2} {arg1}.')
  else:
    await ctx.send("You don't have enough of this item!")

@give.error
async def give_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    with open('bank.json', 'r') as f:
      inv = json.load(f)
    if str(ctx.author.id) not in inv:
      await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create` first!')
      return
    elif str(ctx.author.id) in inv:
      await ctx.send(f'Please ask your friend to create an account by typing `{prefix(client, ctx.message)}create` first!')
      return
    else:
      await ctx.send(f'Please specify the user you want to give stuff to and the item you are intending to give after the command.\nExample: {prefix(client, ctx.message)}give @Andrea 3 bow')
  elif isinstance(error, commands.MissingRequiredArgument):
    try:
      arg1 = ctx.message.content.split(" ")[2]
      user = ctx.message.mentions[0]
      if int(arg1) < 0:
        await ctx.send('Please specify a positive value!')
        return
      try:
        if float(arg1).is_integer() == True:
          rich = author_info(ctx.author, "wallet")
          if int(arg1) > rich:
            await ctx.send('You are trying to give more money than you have!')
            return
          else:
            await money_change(ctx.author, -1*int(arg1), "wallet")
            await money_change(user, int(arg1), "wallet")
            await ctx.send(f'You have give ${arg1} to {user.name}.')
            return
        else:
          await ctx.send('The item you are trying to give does not exist!')
        return
      except ValueError:
        await ctx.send('The item you are trying to give does not exist!')
        return
      except IndexError:
        await ctx.send(f'Please specify the user you want to give stuff to and the item you are intending to give after the command.\nExample: {prefix(client, ctx.message)}give @Andrea 3 bow')
    except:
      await ctx.send(f'Please specify the user you want to give stuff to and the item you are intending to give after the command.\nExample: {prefix(client, ctx.message)}give @Andrea 3 bow')

@client.command(aliases=['cd'])
async def cooldown(ctx):
  command_list = {'forage': '1. Forage', 'hunt': '2. Hunt', 'fish': '3. Fish', 'travel': '4. Travel', 'tesserae': '5. Tesserae', 'work': '6. Work', 'service': '7. Service', 'hgame': '8.Hgame', 'use': '9.Use'}
  em = discord.Embed()
  em.title =f'Showing command cooldowns for {ctx.author.name}'
  em.set_thumbnail(url=ctx.author.avatar_url)
  em.color=random.choice(colors)
  for item in command_list:
    com = client.get_command(item)
    cd = round(com.get_cooldown_retry_after(ctx))
    if cd == 0:
      em.add_field(name=command_list[item], value=':green_circle:', inline=True)
    else:
      em.add_field(name=command_list[item], value=f':red_circle: {timecon(cd)}', inline=True)
  await ctx.send(embed=em)

disinfo = {1: {"text": "District 1's industry is manufacturing luxury items for the Capitol. Due to the nature of its industry, District 1 considered the wealthiest district, the only other wealthier place being the Capitol itself. It is a Career District, where prospective tributes often train for years to compete in the Hunger Games, but little else is known about the district. At the end of Mockingjay, memorials were made for the fallen tributes and victors from District 1, meaning District 1 has 148 of Panem's memorials in their district, notable ones being Cashmere, Gloss, Glimmer and Marvel.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/e/e7/District_1_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606164256"}, 2: {"text":"District 2's industry is masonry, but also manufactures weaponry, makes trains, and supplies the nation's Peacekeepers. The main military complex in the district is known as the Nut. Citizens of District 2 are sometimes called the pets of the Capitol. They are the biggest supporters of the Capitol and therefore are pampered and given many extra conveniences. Some notable tributes are Clove, Cato, Enobaria and Brutus.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/1/10/District_2_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606165316"}, 3: {"text": "District 3's primary industry is general electronics of many types, though it is known for also making various mechanical products such as automobiles and firearms. Their tributes are skilled with electronics. Some notable tributes are Wiress and Beetee.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/b/b4/District_3_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606165811"}, 4: {"text": "District 4's industry is fishing, thus most residents have experience using nets and tridents, making fishhooks from scratch, swimming, and identifying edible sea life. It is considered a Career district, and notable victors from this district are Finnick Odair, Mags, and Annie Cresta. Finnick was an important ally of Katniss Everdeen in the Quarter Quell. According to the Mockingjay podiums, District 4 had 6 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/2/28/District_4_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606170607"}, 5: {"text": "District 5's industry is power. Foxface, a clever tribute nicknamed by Katniss in the 74th Hunger Games, was from District 5. In the 75th Hunger Games the man from District 5 was the first person to die, while he attacked Katniss.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/1/1f/District_5_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606170855"}, 6: {"text": "District 6's industry is transportation. In the 75th Hunger Games, two of the past winners ended up becoming morphling addicts. Another known tribute from District 6 was Titus. Little else is known about District 6. According to the Mockingjay podiums, District 6 had 4 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/9/9f/District_6_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606171443"}, 7: {"text": "District 7's industry is lumber and many of its residents have experience with hatchets, axes, saws, and other tree cutting tools. Also, Katniss notes that this district's children begin work at an early age. Katniss and Peeta had to travel through District 7 to get to the Capitol. Johanna Mason and Blight came from this District. According to the Mockingjay podiums, District 7 had 7 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/4/42/District_7_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606171529"}, 8: {"text": "District 8's industry is the production of textiles, and they have at least one factory that is primarily used for making Peacekeeper uniforms. It was the first district to rebel after Katniss Everdeen spurred the revolution. The rebellion worsened conditions for residents and some, including Bonnie and Twill, escaped. However, Bonnie and Twill never made it to safety in District 13. Cecelia and Woof were victors from District 8. According to the Mockingjay podiums, District 8 had 4 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/c/c8/District_8_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606171816"}, 9: {"text": "District 9's industry is grain. Little is known about this district, just that there are lots of farmland for grain. In the 74th Hunger Games, the boy from District 9 was the first person to be killed in the book. According to the Mockingjay podiums, District 9 has 5 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/6/6c/District_9_Seal.png/revision/latest?cb=20140606171929"}, 10: {"text": "District 10's industry is livestock. Not much is known about this district, but some known information is that its marriage rituals are similar to that of District 4's. In the 74th Hunger Games, Katniss names the boy from District 10 the boy with the bad leg as he was crippled. Katniss and Peeta had to travel through District 10 also to get to the Capitol.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/7/70/District_10_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606172053"}, 11: {"text": "District 11's industry is agriculture - orchards and fields of grain and cotton surround the district. Almost everything grown is shipped directly to the Capitol. It is one of the poorest districts in Panem, second only to District 12. In addition, it is also one of the districts where the Peacekeepers are the strictest. Ironically, this directly results in its residents generally being malnourished and underfed despite its focus on agriculture. In Catching Fire, Katniss said on her and Peeta's Victory Tour, that District 11 is south of District 12. District 11 is located somewhere near Atlanta and is quite large. Rue and Thresh were notable tributes. Seeder and Chaff were victors from District 11. According to the Mockingjay podiums, District 11 has 5 victors.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/c/cd/District_11_Seal.png/revision/latest/scale-to-width-down/100?cb=20191125075205"}, 12: {"text": "District 12's industry is coal and is located somewhere near what was the Appalachian mountains. The district has the distinction of being one of the poorest districts, if not the outright poorest, in all of Panem. Before Katniss Everdeen and Peeta Mellark won the 74th Hunger Games, the district has not had a winner of the Hunger Games emerge from the ranks of its residents for twenty-four years since Haymitch Abernathy, a raging alcoholic and an embarrassment to the district, won the 50th Hunger Games. Before Haymitch, there was only one other victor (Lucy Gray Baird) from District 12 from 64 years before the Peeta and Katniss won the 74th Hunger Games. \n District 12 is the laughing stock of Panem. Shortly after the abrupt end of the 75th Hunger Games and during the opening hours of the second rebellion, District 12 was destroyed by the Capitol, using firebombs. Less than 900 people escaped, mostly thanks to the foresight of Gale Hawthorne. At the end of the second rebellion, District 12 starts to rebuild. According to the Mockingjay podiums, District 12 had 3 victors; however in the book it was revealed District 12 had a total of 4.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/e/ea/District_12_Seal.png/revision/latest/scale-to-width-down/100?cb=20140606172846"}, 13: {"text": "District 13 was one of the thirteen districts of Panem. Its main industry was nuclear weaponry. It was supposedly obliterated during the Dark Days as a warning to the other twelve districts of the Capitol's might. The district is now said to be uninhabitable with the ruins supposedly still smoldering from the toxic bombs dropped upon it. \n After the Dark Days, the Capitol lead Panem's population to widely believe that the main industry of District 13 was graphite mining. However, this was a cover for the truth: nuclear technology research and development, including weapons. \n  It is revealed in Mockingjay that the district is in actuality still operational, though it has seceded from the nation of Panem and operates covertly. While the surface of District 13 remains scarred and supposedly uninhabitable, its residents live deep underground, hidden away from the world and the eyes of the Capitol. It is used as a base for the Second Rebellion. The Capitol leaves District 13 alone due to a non-aggression pact, and none of its citizens participate in The Hunger Games due to this.", "icon": "https://static.wikia.nocookie.net/thehungergames/images/e/ea/D_13_holograph.png/revision/latest/scale-to-width-down/100?cb=20140831213219"}}

@client.command()
async def district(ctx, arg1):
  dis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
  if arg1 in dis:
    em = discord.Embed(title=f'Information for District {arg1}', description=disinfo[int(arg1)]["text"], color=random.choice(colors))
    em.set_thumbnail(url=disinfo[int(arg1)]["icon"])
    await ctx.send(embed=em)
  else:
    await ctx.send('There is no such district!')

@client.command(aliases=['facts'])
async def fact(ctx):
  ff = ["Effie's actor needed help going potty when The Hunger Games was being filmed due to her costume's long nails.", "There used to be 13 Districts, before the Capitol destroyed District 13 during the Dark Days.", "The name 'Panem' was derived from the term 'Panem et circenses' which meant 'bread and circuses'.", "The prequel to the book series is called A Ballad of Songbirds and Snakes", "President Coriolanus Snow has incessant mouth ulcers due to the failure of antidotes to counteract the poison he must have taken once.", "Katniss shot dead President Alma Coin as she was as savage as Former President Snow.", "Rue was the oldest among her siblings.", "Katniss' stylist was called Cinna and he was indirectly involved in the plan to overthrow the Capitol.", "District 8 is the most polluted district in the entirety of Panem", "There were about 450 wigs used when filming The Hunger Games.", "A Quarter Quell is organised in Panem every 25 years.", "Plutarch Heavensbee was a double agent. He was secretly fighting against the Capitol while working for it as the Head Gamemaker.", "Seneca Crane was likely executed for his oversight during the last moments of the 74th Hunger Games.", "Cato was shot on the back of his hand by Katniss.", "The territory of Panem consists of much of the US (excluding coastal states) and southern Canada."]
  em = discord.Embed(title='Did you know?', description=random.choice(ff), color=random.choice(colors))
  await ctx.send(embed=em)

@district.error
async def district_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'Please specify the district you want information for.\nExample: {prefix(client, ctx.message)}district 12')

@client.command(aliases = ['latency', 'Ping'])
async def ping(ctx):
  await ctx.send(f'The latency is {round(client.latency*1000)}ms.')

@client.command(aliases = ['Map'])
async def map(ctx):
  await ctx.send('https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/map-of-panem-quill-and-pearl-co.jpg')

@client.command()
async def help(ctx):
  em = discord.Embed(title='Showing a list of commands for Mockingjay', description='[Hit this link to join the Mockingjay Support Server!](https://discord.gg/CtAT7sDqxH)', color=random.choice(colors)).add_field(name="Hunt for food. You're risking your life though...", value='`hunt`', inline=False).add_field(name='Forage for food. Sometimes you might find something else...', value="`forage`", inline=False).add_field(name="Work and earn some money.", value="`work`", inline=False).add_field(name="Get a job", value="`job <index of job>`", inline=False).add_field(name="Show a list of jobs available", value="`joblist`", inline=False).set_thumbnail(url=client.user.avatar_url)

  em1 = discord.Embed(title='Showing a list of commands for Mockingjay', description='[If you join the official support server, you will be rewarded with some goodies!](https://discord.gg/CtAT7sDqxH)', color=random.choice(colors)).add_field(name="Withdraw cash", value="`withdraw <amt>` or `with <amt>`", inline=False).add_field(name="Deposit cash from you wallet", value="`deposit <amt>` or `dep <amt>`", inline=False).add_field(name="Show items in your inventory", value="`inventory` or `inv`", inline=False).add_field(name="Buy stuff", value="`buy <amt> <item name>`", inline=False).add_field(name="Sell stuff. Note: You can only sell items for half the price they're obtained for.", value="`sell <amt> <item name>`", inline=False).set_thumbnail(url=client.user.avatar_url)

  em2 = discord.Embed(title='Showing a list of commands for Mockingjay', description='[Found a bug while playing? Join the official support server and report it!](https://discord.gg/CtAT7sDqxH)', color=random.choice(colors)).add_field(name="Travel to another district. If you have a travel pass, that is...", value="`travel <district number>`", inline=False).add_field(name="Eat items to restore your HP", value="`eat <item name>`", inline=False).add_field(name="Shows a list of stuff you can buy.", value="`shop`", inline=False).add_field(name="View stats for your account.", value="`profile`", inline=False).add_field(name="Create an account", value="`create`", inline=False).add_field(name="View command cooldowns", value="`cooldown` or `cd`", inline=False).add_field(name="Change the server prefix", value="`prefix`", inline=False).set_thumbnail(url=client.user.avatar_url)

  em3 = discord.Embed(title='Showing a list of commands for Mockingjay', description='The feature that took the longest for the devs to create was hgame...', color=random.choice(colors)).add_field(name="Go for a nice fishing trip. Get some tasty fish and watch out for crocodiles!", value="`fish`", inline=False).add_field(name="Give some items to your friends.", value="`give <amt> <item>` or `give <cash_amt>`", inline=False).add_field(name="Start an interactive Hunger Games session", value="`hgame`", inline=False).add_field(name="Shows a map of Panem", value="`map`", inline=False).add_field(name="Get the latency of the bot.", value="`ping`", inline=False).add_field(name="Get some fun facs about the Hunger Games universe.", value="`facts`", inline=False).add_field(name="Get the latency of the bot.", value="`ping`", inline=False).set_thumbnail(url=client.user.avatar_url)

  em4 = discord.Embed(title='Showing a list of commands for Mockingjay', description='This bot was initially created using Repl.it and hosted on Heroku upon completion.', color=random.choice(colors)).add_field(name="Contribute your labor to Panem! You will be assigned to conduct a dangerous mission. If you survive, you get paid a handsome amount of cash and maybe a travel pass or two", value="`service`", inline=False).add_field(name="Add someone as your successor. When you die, 70% of your wealth will be given to them.", value="`will <@someone>`", inline=False).add_field(name="Use an item.", value="`use <item name>`", inline=False).add_field(name="View your global ranking for wealth.", value="`leaderboard` or `lb`", inline=False).add_field(name="Get information for a certain district", value="`district <district number>`", inline=False).add_field(name="Get the invite link for this bot", value="`invite`", inline=False).set_thumbnail(url=client.user.avatar_url)
  
  embeds = [em, em1, em2, em3, em4]

  paginator = BotEmbedPaginator(ctx, embeds)
  await paginator.run()

client.run('ODU1MjQwMjEyODAwMzM5OTc4.YMvmhA.s4QZJvm4c2xTzQmS4OOLNedMCN4')
