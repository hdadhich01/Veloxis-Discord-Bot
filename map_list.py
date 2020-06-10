import discord

def Ascent():
  
  mapName = 'Ascent'
  embed = discord.Embed(title=mapName+" (Map)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='*Suburban Area*', value='Map supposedly situated in Venice, Italy, in a market zone or a public landmark', inline=False)

  embed.set_image(url="https://i.imgur.com/MALtQgW.png")

  return embed

def Bind():
  
  mapName = 'Bind'
  embed = discord.Embed(title=mapName+" (Map)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='*Map with Teleportation*', value='This map has two portals with the insides of them reading Laboratory A, and Laboratory B)', inline=False)

  embed.set_image(url="https://i.imgur.com/MALtQgW.png")

  return embed

def Haven():
  
  mapName = 'Haven'
  embed = discord.Embed(title=mapName+" (Map)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='*Southeast/South Asian Themed Map*', value='Supposedly a Bhutanese themed map according to this [forum](https://www.reddit.com/r/VALORANT/comments/g3yk5w/haven_bhutanese_themed_map/)', inline=False)

  embed.set_image(url="https://i.imgur.com/32txSCs.jpg")

  return embed

def Split():
  
  mapName = 'Split'
  embed = discord.Embed(title=mapName+" (Map)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='*Urban Area Themed Map*', value='Environment seems to be situated in some sort of Urban populated place', inline=False)

  embed.set_image(url="https://i.imgur.com/HYTknv8.jpg")

  embed.set_image(url="https://i.imgur.com/HYTknv8.jpg")

  return embed

def Range():
  
  mapName = 'Range'
  embed = discord.Embed(title=mapName+" (Map)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='*Training Map for Diff Aspects of the Game*', value='This map is meant to test your parkour skills in Valorant. The goal is to strafe and parkour your way to the top of a tower in order to obtain a trophy, you may also practice other aspects of the game such as planting, defusing, etc.', inline=False)

  embed.set_image(url="https://i.imgur.com/u5ggujF.png")

  return embed

def invalidMessage():
  
  embed = discord.Embed(title="Invalid Command Usage", color=0xFF0000)
  
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='***Use*** **`v!help`** ***for Info on All Commands***', value='The correct usage of this command is \n**`v!map <name/listcodee>`** (alias = **`v!mp`**)\n\nTo get the names of all the maps use \n**`v!maps`** (alias = **`v!mp`**) \n\n*the names of maps are NOT CASE SENSITIVE so you can do either **`v!mp haven`** or **`v!mp Haven`***', inline=True)

  return embed