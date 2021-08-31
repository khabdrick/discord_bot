import discord
import random
from replit import db


client = discord.Client()

trigger_words = ["fitness", "fitness tip",]

starter_tips  = [
  "Make sure you drink water",
  "Make sure you're eating healthy",
  "Good posture is essetial for a great workout"
]

def add_tips(fitness_tip):
  if "tips" in db.keys():
    tips = db["tips"]
    tips.append(fitness_tip)
    db["tips"] = tips
  else:
    db["tips"] = [fitness_tip]

def delete_tip(index):
  tips = db["tips"]
  if len(tips) > index:
    del tips[index]
    db["tips"] = tips

@client.event
async def on_message(message):
  if message.author == client.user:
    return


  options = starter_tips
  if "tips" in db.keys():
    options = options + list(db["tips"])

  if any(word in message.content for word in trigger_words):
    await message.channel.send(random.choice(options))

  if message.content.startswith("#new"):
    fitness_tip = message.content.split("#new ",1)[1]
    add_tips(fitness_tip)
    await message.channel.send("New fitness tip added.")

  if message.content.startswith("#del"):
    tips = []
    if "tips" in db.keys():
      index = int(message.content.split("#del",1)[1])
      delete_tip(index)
      tips = db["tips"]
    await message.channel.send("A tip has been deleted")

  if message.content.startswith("#list"):
    tips = []
    if "tips" in db.keys():
      tips = list(db["tips"])
    await message.channel.send(tips)

client.run("paste_your_bot_token_here")
