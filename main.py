import discord
import random
from discord.ext import commands
import asyncio
import json

def prefix(client, message):
  with open('prefixes.json', 'r') as f:
    pref = json.load(f)
    
    prefix = pref[str(message.guild.id)]
  
  return prefix 

client = commands.Bot(command_prefix=prefix)

colors = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694]

products = [{"name": "Golden ring", "price": 10000, "district": 1, "description": "A gold ring that does nothing really apart from looking good"}, {"name": "Septsilk gown", "price": 5500, "district": 1, "description": "A gorgeous lavender gown. Made by the esteemed seamstresses of District 1 from high-grade silk produced by the hardworking labor of District 8"}, {"name": "Toolbox", "price": 10000, "district": 2, "description": "An assortment of vital tools perfect for the hardworking industrial worker. With this toolbox, you can contribute more with your labor to the beautiful nation of Panem."}, {"name": "Shield", "price": 4000, "district": 2, "description": "Caught in a bad situation while hunting? Faced with Peacekeepers who intend to execute you for unruly activity? Protect yourself with this shield! Decreases chances of dying while hunting by 30% and Peacekeeper encounters by 40% "}, {"name": "Computer", "price": 20000, "district": 3, "description": "Get district travel passes more easily with a computer! Use the Capitol's efficient TransPlan system instead of getting a pass from the Hob or the District Office."}, {"name": "Tilapia", "price": 200, "district": 4, "description": "A tasty fish caught from the shores of District 4!"}, {"name": "panfish", "price": "Cannot be bought", "district": "All", "description": "A tasty fish you can get anywhere while fishing!"}, {"name": "Fishing rod", "price": 15000, "district": 4, "description": "Catch your own fish with this handy rod!"}, {"name": "battery", "price": 500, "district": 5, "description": "Use this battery to power your computer!"}, {"name": "Charge", "price": 100, "district": 5, "description": "Umm, just some electrons to fill up your battery."}, {"name": "Axe", "price": 5000, "district": 7, "description": "Just an axe. Use it to obtain wood or kill large animals when hunting."}, {"name": "Jacket", "price": 5000, "district": 8, "description": "A drab, durable utility jacket meant only to last and keep you warm. As far as aesthetics go, it scores a zero."}, {"name": "Armour", "price": 10000, "district": 8, "description": "A durable set of Kevlar armour made by the esteemed industrial workers of District 8. Usually factory rejects from the stockpile created for the use of Peacekeepers. Reduces the chances of dying when hunting by 40% and Peacekeeper encounters by 50%"}, {"name": "bread", "price": 50, "district": 9, "description": "A sawdust filled loaf of bread that restores 10HP. It's just too bad that all the good stuff goes to the Capitol."}, {"name": "beef", "price": 100, "district": 10, "description": "A slab of frozen beef. Can be cooked to restore 30HP"}, {"name": "Milk", "price": 50, "district": 10, "description": "Get your milk here! Restores 10HP of health."}, {"name": "Apple", "price": 40, "district": 11, "description": "Just an ordinary apple. Restores 20HP."}, {"name": "Bow", "price": 10000, "district": 12, "description": "You met Katniss in district 12 and bought a bow from her! Unfortunately, if this one breaks there are none left..."}, {"name": "Travel pass", "price": 2000, "district": 0, "description": "Get this in any district! A travel pass allows you to hop on a train to any district in the great nation of Panem. Except the Capitol..."}, {"name": "Elk", "price": "Cannot be bought", "district": 0, "description": "If you're lucky, you may find this when hunting..."}, {"name": "Groosling", "price": 20000, "district": 0, "description": "Fresh groosling from the Glades! Expensive when bought but can be hunted free of charge."}, {"name": "Magpie", "price": 2000, "district": 0, "description": "Fresh magpie from the Glades! Expensive when bought but can be hunted free of charge."}, {"name": "Katniss", "price": 'Cannot be bought', "district": 0, "description": "A potato-like plant you can forage from the Glades."}, {"name": "Wild fruit", "price": "Can't be bought", "district": 0, "description": "Sweet, rounded fruit that can be found sometimes when foraging. Tastes great and replenishes 20 HP"}, {"name": "Groosling nest", "price": "Can't be bought", "district": 0, "description": "An abandoned nest that once belonged to a groosling. Any uses? I'm not sure, use your creativity..."}]

shop_id = ['golden ring', 'armour', 'jacket', 'fishing rod', 'travel pass', 'computer', 'battery', 'charge', 'milk', 'travel pass', 'groosling', 'elk', 'katniss', 'magpie', 'bread', 'bow', 'toolbox', 'shield', 'septsilk gown', 'apple', 'beef', 'axe']

edibles = ['milk', 'elk', 'groosling', 'apple', 'beef', 'tilapia', 'bread', 'wild fruit', 'katniss', 'panfish']

hp_food = {"milk": 20, "elk": 50, "groosling": 50, "apple": 20, "beef": 60, "bread": 20, "wild fruit": 20, "katniss": 20, "tilapia": 20, "panfish": 50}

forage_stuff = ['Katniss', 'Wild fruit', 'apple', 'groosling nest']

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


@client.event
async def on_ready():
    print('We are now logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'hun help | In  {len(client.guilds)} servers!'))

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    pass
  elif isinstance(error, commands.CommandInvokeError):
    await ctx.send(f'Please create an account by typing `{prefix(client, ctx.message)}create`!')
    raise error
  else:
    raise error

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

  val[str(author.id)] = {"bank": 1000, "wallet": 2000, "district": dnum, "HP": 100, "job": "None"}

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

client.remove_command('help')

@client.command()
async def shop(ctx, *, arg1):
  if arg1.lower() not in shop_id and arg1.lower() not in forage_stuff and arg1.lower() not in edibles:
    await ctx.send('The item you are trying to obtain info for does not exist!')
  else:
    owned = check_item_value(ctx.author, arg1.lower())
    product = productlist_info(arg1)
    em= discord.Embed(title=product["name"], description=product["description"], color=random.choice(colors))
    em.add_field(name='District', value=product["district"], inline=True)
    em.add_field(name='Price', value=product["price"], inline=True)
    em.add_field(name='Owned', value=owned, inline=True)
    await ctx.send(embed=em)
    

@shop.error
async def shop_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    em = discord.Embed(title='A list of items you can buy!', description='In order to buy an item, you must travel to the district it comes from to do so.\nNote: Selling an item only returns half of its initial value.', color=random.choice(colors))
    for item in products:
      em.add_field(name=item["name"], value=f'Price: ${item["price"]} | District: {item["district"]}')
    await ctx.send(embed=em)

@client.command()
async def create(ctx):
  await create_account(ctx.author)
  await ctx.send('Account created!')

@client.command()
async def buy(ctx, *, product):
  if product.lower() not in shop_id:
    await ctx.send("The product you are trying to buy doesn't exist!")
  else:
    price = check_item_price(product)
    if afford(ctx.author, price, "wallet") == 1 and check_item_district(ctx.author, product.lower()) != None:
      await buyo(ctx.author, price, product.lower())
      await ctx.send(f'You have bought 1 {product}')
    elif afford(ctx.author, price, "wallet") == 1 and check_item_district(ctx.author, product.lower()) == None:
      await ctx.send('You are in the wrong district!')
    elif afford(ctx.author, price, "wallet") == 0 and check_item_district(ctx.author, product.lower()) != None:
      await ctx.send("You can't afford this!")
    elif afford(ctx.author, price, "wallet") == 0 and check_item_district(ctx.author, product.lower()) == None:
      await ctx.send('You could not be in a worse position right now. You do not have enough money to buy this product and you are in the wrong district.')

@client.command()
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
      await ctx.send(f'You went out hunting and found 1 {animal}! You killed it by decapitating its head and are currently walking home with a fresh {animal} stuffed neatly in your hunting bag!')
    else:
      if valarm >= 1 or valshield >= 1:
        ratetwo = random.randint(1, 30)
        await hp_change(ctx.author, -1*ratetwo)
        await ctx.send(f'You encountered an angry bison that charged right at you and hurt you badly! Luckily, you were protected by your shield or armour! \nYour hp has decreased by `{ratetwo}`.')
      else:
        ratetwo = random.randint(20, 60)
        await hp_change(ctx.author, -1*ratetwo)
        await ctx.send(f'You encountered an angry bison that charged right at you and hurt you badly!\nYour hp has decreased by `{ratetwo}`.')
  else:
    await ctx.send('You cannot hunt without an axe or a bow. Buy one as soon as possible.')

@client.command()
async def profile(ctx):
  with open('bank.json', 'r') as f:
    bank = json.load(f)
  stat = bank[str(ctx.author.id)]
  em = discord.Embed()
  em.title=f'{ctx.author.name}, here are your stats!'
  em.color = random.choice(colors)
  perc = round((stat["HP"]/200)*100)
  em.add_field(name='District of Residence', value=stat["district"], inline=False)
  em.add_field(name='HP', value=f'{stat["HP"]} | {perc}%', inline=False)
  em.add_field(name='Wallet', value=stat["wallet"], inline=False)
  em.add_field(name='Bank', value=stat["bank"], inline=False)
  await ctx.send(embed=em)

@client.command()
async def travel(ctx, arg1):
  rate = random.randint(1, 100)
  tp = check_item_value(ctx.author, "travel pass")
  if rate <= 85 and tp >= 1:
    await useo(ctx.author, "travel pass")
    arg2 = int(arg1)
    await district_change(ctx.author, arg2)
    em=discord.Embed(title=f'Alright, on to District {arg1}!', description="Keep your eyes peeled and don't run into any suspicious Peacekeepers!", color=random.choice(colors))
    em.set_thumbnail(url='https://www.syfy.com/sites/syfy/files/2017/08/screen_shot_2017-08-09_at_6.11.35_pm.png')
    await ctx.send(embed=em)
    await asyncio.sleep(random.randint(1, 10))
    await ctx.send(f'You have arrrived at District {arg1}! Use the shop command to find out what you can buy!')
  elif rate > 85 and tp >= 1:
    shield = check_item_value(ctx.author, "shield")
    armour = check_item_value(ctx.author, "armour")

    if shield >= 1 or armour >= 1:
      ratetwo = random.randint(1, 20)
      await hp_change(ctx.author, -1*ratetwo)
      await useo(ctx.author, "travel_pass")
      em = discord.Embed(title=f"Uh oh... You've run into some Peacekeepers by accident. You put up a good fight and managed to get away, but they've confiscated your travel pass and your HP has decreased by {ratetwo}", description='Better luck travelling next time!', color=random.choice(colors))
      em.set_thumbnail(url='https://static.wikia.nocookie.net/thehungergames/images/e/e5/2peacekeepersCF.png/revision/latest/scale-to-width-down/547?cb=20130415223924')
      await ctx.send(embed=em)
    else:
      ratetwo = random.randint(20, 40)
      await hp_change(ctx.author, -1*ratetwo)
      await useo(ctx.author, "travel_pass")
      em = discord.Embed(title=f"Uh oh... You've run into some Peacekeepers by accident. You put up a good fight and managed to get away, but they've confiscated your travel pass and your HP has decreased by {ratetwo}", description='Better luck travelling next time!', color=random.choice(colors))
      em.set_thumbnail(url='https://static.wikia.nocookie.net/thehungergames/images/e/e5/2peacekeepersCF.png/revision/latest/scale-to-width-down/547?cb=20130415223924')
      await ctx.send(embed=em)
  else:
    await ctx.send("You can't travel without a travel pass! Get a job. Maybe your employer will let you have some...")

@client.command()
async def forage(ctx):
  forage_words = ['behind a tree!', 'stuck inside a small aquifer.', 'in a pond.']
  rate = random.randint(1, 100)
  item = random.choice(forage_stuff)
  if rate <= 50:
    await buyo(ctx.author, 0, item.lower())
    await ctx.send(f'You found one {item} {random.choice(forage_words)}')
  elif rate > 50 and rate <= 90:
    await ctx.send('You spent hours in the woods foraging and found nothing. Sad life...')
  else:
    item = random.choice(shop_id)
    await buyo(ctx.author, 0, item.lower())
    await ctx.send(f"Wow! You happened to stumble upon 1 {item} when foraging for food! Let's hope whoever who left it there isn't dead or imprisoned in the Capitol...")

@client.command()
async def eat(ctx, *, arg1):
  food = check_item_value(ctx.author, arg1.lower())
  if arg1.lower() in edibles and food >= 1:
    await sello(ctx.author, 0, arg1.lower())
    await hp_change(ctx.author, hp_food[arg1.lower()])
    await ctx.send(f'You ate 1 yummy {arg1} and replenished `{hp_food[arg1.lower()]}` health!')
  elif arg1.lower()  not in edibles:
    await ctx.send("You can't eat this item!")
  elif arg1.lower() in edibles and food < 1:
    await ctx.send(f"Sorry bro. You don't have any {arg1.lower()}.")

@client.command()
async def deposit(ctx, arg1):
  value = abs(int(arg1))
  if afford(ctx.author, value, "wallet") == 1:
    await money_change(ctx.author, -1*value, "wallet")
    await money_change(ctx.author, value, "bank")
    await ctx.send(f'You have deposited ${value}.')
  else:
    await ctx.send('You are trying to deposit more money than you have!')

@client.command()
async def withdraw(ctx, arg1):
  value = abs(int(arg1))
  if afford(ctx.author, value, "bank") == 1:
    await money_change(ctx.author, value, "wallet")
    await money_change(ctx.author, -1*value, "bank")
    await ctx.send(f'You have withdrawn ${value}.')
  else:
    await ctx.send('You are trying to withdraw more money than you have!')

@client.command()
async def sell(ctx, *, itema):
  if itema in shop_id:
    price = round(check_item_price(itema.lower())/2)
    rich = check_item_value(ctx.author, itema.lower())
    if rich >= 1:
      await sello(ctx.author, price, itema)
      await ctx.send(f'You have sold one {itema} and gained ${price}!')
    else:
      await ctx.send("You don't have this item!")
  else:
    await ctx.send("Sorry mate. You can't buy or sell this item.")

worklist = {"Jeweller": {"district": 1, "trivia": ["Diamond exists 150 - 250km below ground."], "pay": 2000, "die": ["cut yourself by accident with a diamond cutter"]}, "Seamstress": {"district": 1, "trivia": ["A thimble is the best form of protection against pricked thumbs."], "pay": 2000, "die": ["pricked your carotid artery"]}, "Blacksmith": {"district": 2, "trivia": ["You can quench your blades in water or oil."], "pay": 1000, "die": ["burned yourself when quenching your blade"]}, "Industrial worker (Textiles)": {"district": 2, "trivia": ["The four basic industrial processes are machining, joining, casting and moulding."], "pay": 2000, "die": ["touched a live wire and got burned"]}}

@client.command()
async def inventory(ctx):
  em=discord.Embed(title=f'Inventory stats for {ctx.author.name}', description=f'Type {prefix(client, ctx.message)}shop <item> to get information for a specific product.')

  with open('inventory.json', 'r') as f:
    inv = json.load(f)

  initinv = inv[str(ctx.author.id)]

  for item in initinv:
    if item["value"] != 0:
      em.add_field(name=item["name"], value=item["value"], inline=False)
    else:
      pass
  await ctx.send(embed=em)

@client.command()
async def work(ctx):
  district = author_info(ctx.author, "district")
  work = author_info(ctx.author, "job")
  if district == worklist[work]["district"]:
    try:
      rate = random.randint(1, 100)
      task = random.choice(worklist[work]["trivia"])
      await ctx.send(f'Type this in the chat within 30 seconds!\n`{task}`')

      def check(m):
        return m.content == task and m.author == ctx.message.author

      await client.wait_for('message', check=check, timeout=30)
      if rate >= 75:
        await ctx.send(f"Good job, {ctx.author.name}! Here are your daily wages and I've decided to reward you with a travel pass for your hard work!")
        await money_change(ctx.author, worklist[work]["pay"], "bank")
        await buyo(ctx.author, 0, "travel pass")
      else:
        await ctx.send(f"Good job, {ctx.author.name}! Your daily wages have been banked into your account. 💰")
        await money_change(ctx.author, worklist[work]["pay"], "bank")
    except:
      rate = random.randint(1, 100)
      if rate <= 85:
        hp = random.randint(1, 60)
        await hp_change(ctx.author, -1*hp)
        await ctx.send(f'Oof, you {random.choice(worklist[work]["die"])}. You have lost {hp}HP.')
      else:
        await ctx.send(f'Oh crap, you {random.choice(worklist[work]["die"])} and died as a result!')
  elif district != worklist[work]["district"]:
    await ctx.send('Go back to your home district! You are of no use here!')
  elif work == "None":
    await ctx.send(f'Go get a job to contribute to the great nation of Panem. Type {prefix(client, ctx.message)}job to find one. Note: You can only obtain a job that exists in your district.')

@client.command()
async def job(ctx, arg1):
  try:
    worka = int(arg1) - 1
    district = author_info(ctx.author, "district")
    jobprev = author_info(ctx.author, "job")
    templist = list(worklist)
    work = templist[worka]
    if jobprev != "None":
      await ctx.send(f'You are already working as a {jobprev}! Sorry, the government of Panem does not allow its citizens to change jobs.')
    else:
      if district == worklist[work]["district"]:
        await job_change(ctx.author, work)
        await ctx.send(f'You are now working as a {work}. ')
      else:
        await ctx.send(f'The job you are applying for ({work}) is not available in your district.')
  except ValueError:
    await ctx.send(f'Please specify the index of the job according to the joblist command.\nExample: {prefix(client, ctx.message)}job 2')
  except IndexError:
    await ctx.send('The job you are trying to apply for does not exist!')

@client.command()
async def joblist(ctx):
    em = discord.Embed(title='Showing jobs available', description=f'Get a job by typing `{prefix(client, ctx.message)}job <1>`.', color=random.choice(colors))
    templist = list(worklist)
    for item in worklist:
      em.add_field(name=f'{templist.index(item)+1}. {item}', value=f'District: {str(worklist[item]["district"])} | Pay: ${str(worklist[item]["pay"])}', inline=False)
    await ctx.send(embed=em)

@client.command()
async def fish(ctx):
  rod = check_item_value(ctx.author, "fishing rod")
  if rod >= 1:
    rate = random.randint(1, 100)
    fish_stuff = ["tilapia", "panfish"]
    if rate <= 85:
      await buyo(ctx.author, 0, fish_stuff)
      await ctx.send(f'You went fishing and came back with one {fish_stuff}!')
    else:
      ratetwo = random.randint(1, 100)
      if ratetwo <= 75:
        hp = random.randint(1, 30)
        await useo(ctx.author, "fishing rod")
        await hp_change(ctx.author, -1*hp)
        await ctx.send(f'You encountered a crocodile while fishing and managed to get away! However, you lost your fishing rod and {hp}HP.')
  else:
    await ctx.send(f"You don't have a fishing rod! Buy one as soon as possible to fish!")
      
@client.command()
async def help(ctx):
  em = discord.Embed(title='Showing a list of commands for Mockingjay', description='[Hit this link to join the Mockingjay Support Server!](https://discord.gg/CtAT7sDqxH)', color=random.choice(colors))
  em.add_field(name="Hunt for food. You're risking your life though...", value='`hunt`', inline=False)
  em.add_field(name='Forage for food. Sometimes you might find something else...', value="`forage`", inline=False)
  em.add_field(name="Work and earn some money.", value="`work`", inline=False)
  em.add_field(name="Get a job", value="`job <index of job>`", inline=False)
  em.add_field(name="Show a list of jobs available", value="`joblist`", inline=False)
  em.add_field(name="Withdraw cash", value="`withdraw`", inline=False)
  em.add_field(name="Deposit cash from you wallet", value="`deposit`", inline=False)
  em.add_field(name="Show items in your inventory", value="`inventory`", inline=False)
  em.add_field(name="Buy stuff", value="`buy <item name>`", inline=False)
  em.add_field(name="Sell stuff. Note: You can only sell items for half the price they're obtained for.", value="`sell <item name>`", inline=False)
  em.add_field(name="Travel to another district. If you have a travel pass, that is...", value="`travel <district number>`", inline=False)
  em.add_field(name="Eat items to restore your HP", value="`eat <item name>`", inline=False)
  em.add_field(name="Show a list of stuff you can buy.", value="`shop`", inline=False)
  em.add_field(name="View stats for your account.", value="`profile`", inline=False)
  em.add_field(name="Create an account", value="`create`", inline=False)
  em.set_thumbnail(url=client.user.avatar_url)
  await ctx.send(embed=em)

@client.command()
async def map(ctx):
  await ctx.send('https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/map-of-panem-quill-and-pearl-co.jpg')

client.run('ODU1MjQwMjEyODAwMzM5OTc4.YMvmhA.s4QZJvm4c2xTzQmS4OOLNedMCN4')
