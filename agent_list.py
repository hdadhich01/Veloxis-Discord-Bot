# this file is used for importing information in main.py on all the valorant agents

import discord

def Breach():
    
  agentName = 'Breach'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/xmf4TlV.png")

  embed.add_field(name='***Origin***', value=':flag_se: Sweden', inline=True)

  embed.add_field(name='***Agent Class***', value='<:initiator_emoji:714939457589215274> Initiator', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:initiator_emoji:714939457589215274> Initiators focus on gathering intel and help the team push', inline=False)

  embed.add_field(name='***Aftershock*** (Ability 1)', value='EQUIP a fusion charge. FIRE the charge to set a slow-acting burst through the wall. The burst does heavy damage to anyone caught in its area. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Flashpoint*** (Ability 2)',
  value='EQUIP a blind charge. FIRE the charge to set a fast-acting burst through the wall. The charge detonates to blind all players looking at it. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Fault Line*** (Signature Ability)',
  value='EQUIP a seismic blast. HOLD FIRE to increase the distance. RELEASE to set off the quake, dazing all players in its zone and in a line up to the zone. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Rolling Thunder*** (Ultimate Ability)',
  value='EQUIP a Seismic Charge. FIRE to send a cascading quake through all terrain in a large cone. The quake dazes and knocks up anyone caught in it. \nDefault Keybind → `X`', inline=False)

  return embed

def Brimstone():

  agentName = 'Brimstone'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")
  
  embed.set_image(url="https://i.imgur.com/yRjZ8nt.png")

  embed.add_field(name='***Origin***', value=':flag_us: United States', inline=True)

  embed.add_field(name='***Agent Class***', value='<:controller_emoji:714940194566176958> Controller', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:controller_emoji:714940194566176958> Controllers are good at blocking off sight lines and generally offer support to the team', inline=False)

  embed.add_field(name='***Stim Beacon*** (Ability 1)',
  value='EQUIP a stim beacon. FIRE to toss the stim beacon in front of Brimstone. Upon landing, the stim beacon will create a field that grants players RapidFire. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Incendiary*** (Ability 2)', value='EQUIP an incendiary grenade launcher. FIRE to launch a grenade that detonates as it comes to a rest on the floor, creating a lingering fire zone that damages players within the zone. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Sky Smoke*** (Signature Ability)', value='EQUIP a tactical map. FIRE to set locations where Brimstone\'s smoke clouds will land. ALTERNATE FIRE to confirm, launching long-lasting smoke clouds that block vision in the selected area. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Orbital Strike*** (Ultimate Ability)',
  value='EQUIP a tactical map. FIRE to launch a lingering orbital strike laster at the selected location, dealing high damage-over-time to players caught in the selected area. \nDefault Keybind → `X`', inline=False)

  return embed

def Cypher():

  agentName = 'Cypher'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/fYvdGmj.png")

  embed.add_field(name='***Origin***', value=':flag_ma: Morocco', inline=True)

  embed.add_field(name='***Agent Class***', value='<:sentinel_emoji:714940115239305327> Sentinel', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:sentinel_emoji:714940115239305327> Sentinels are defenders, usually playing the back line of a team', inline=False)

  embed.add_field(name='***Trapwire*** (Ability 1)',
  value='EQUIP a trapwire. FIRE to place a desctuctible and covert tripwire at the targeted location, creating a line that spans between the placed location and the wall opposite. Enemy players who cross a tripwire will be tethered, and dazed after a short period if they do not destroy the device in time. This ability can be picked up to be REDEPLOYED. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Cyber Cage*** (Ability 2)', value='EQUIP a cyber cage. FIRE to toss the cyber cage in front of Cypher. ACTIVATE to create a zone that blocks vision and slows enemies who pass through it. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Spycam*** (Signature Ability)', value='EQUIP a spycam. FIRE to place the spycam at the targeted location. RE-USE this ability to take control of the camera\'s view. While in control of the camera, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Neutral Theft*** (Ultimate Ability)',
  value='INSTANTLY use on a dead enemy player in your crosshairs to reveal the location of all living enemy players. \nDefault Keybind → `X`', inline=False)

  return embed

def Jett():

  agentName = 'Jett'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/WDEyOrZ.png")

  embed.add_field(name='***Origin***', value=':flag_kr: South Korea', inline=True)

  embed.add_field(name='***Agent Class***', value='<:duelist_emoji:714940079331737701> Duelist', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:duelist_emoji:714940079331737701> Duelists are the ones who push forward into conflicts with the enemy team, they match the role of an attacker', inline=False)

  embed.add_field(name='***Cloudburst*** (Ability 1)',
  value='INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surfact. HOLD the ability key to curve the smoke in the direction of your crosshair. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Updraft*** (Ability 2)', value='INSTANTLY propel Jett high into the air. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Tailwind*** (Signature Ability)', value='INSTANTLY propel Jett in the direction she is moving. If Jett is standing still she will propel forward. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Blade Storm*** (Ultimate Ability)',
  value='EQUIP a set of highly accurate throwing knives that recharge on killing an opponent. FIRE to throw a single knife at your target. ALTERNATE FIRE to throw all remaining daggers at your target. \nDefault Keybind → `X`', inline=False)

  return embed


def Omen():
  
  agentName = 'Omen'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/BEE31Fv.png")

  embed.add_field(name='***Origin***', value=':question: Unknown', inline=True)

  embed.add_field(name='***Agent Class***', value='<:controller_emoji:714940194566176958> Controller', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:controller_emoji:714940194566176958> Controllers are good at blocking off sight lines and generally offer support to the team.', inline=False)

  embed.add_field(name='***Shrouded Step*** (Ability 1)',
  value='EQUIP a shadow walk ability and see its range indicator. FIRE to begin a brief channel, then teleport to the marked location. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Paranoia*** (Ability 2)', value='INSTANTLY fire a shadow projectile forward, briefly reducing the vision range of all players it touches. This projectile can pass straight through walls. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Dark Cover*** (_ignature Ability)', value='EQUIP a shadow orb and see its range indicator. FIRE to throw the shadow orb to the marked location, creating a long-lasting shadow sphere that blocks vision. HOLD ALTERNATE FIRE while targeting to move the marker further away. HOLD the ability key while targeting to move the marker closer. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***From the Shadows*** (Ultimate Ability)',
  value='EQUIP a tactical map. FIRE to begin teleporting to the selected location. While teleporting, Omen will appear as a Shade that can be destroyed by an enemy to cancel his teleport. \nDefault Keybind → `X`', inline=False)

  return embed

def Phoenix():
  
  agentName = 'Phoenix'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/j8pQnz7.png")

  embed.add_field(name='***Origin***', value=':flag_gb: United Kingdom', inline=True)

  embed.add_field(name='***Agent Class***', value='<:duelist_emoji:714940079331737701> Duelist', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:duelist_emoji:714940079331737701> Duelists are the ones who push forward into conflicts with the enemy team, they match the role of an attacker', inline=False)

  embed.add_field(name='***Blaze*** (Ability 1)',
  value='Equip a flame wall. Fire to create a line of flames that moves forward creating a wall that blocks vision and damages players passing through it. Hold Fire to bend the wall in the direction of your crosshair. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Curveball*** (Ability 2)', value='Equip a flare orb that takes a curving path and detonates shortly after throwing. Fire to curve the flare orb to the left, detonating the blinding any player who sees the orb. Alternate fire to curve the flare orb to the right. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Hot Hands*** (Signature Ability)', value='Equip a fireball. Fire to throw a fireball that explodes after a set amount of time or upon hitting the ground, creating a lingering fire zone that damages enemies. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Run It Back*** (Ultimate Ability)',
  value='INSTANTLY place a marker at Phoenix\'s location. while this ability is active, dying or allowing the timer to expire will end this ability and bring Phoenix back to this location with full health. \nDefault Keybind → `X`', inline=False)

  return embed

def Raze():
  
  agentName = 'Raze'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/VP0RJlQ.png")

  embed.add_field(name='***Origin***', value=':flag_br: Brazil', inline=True)

  embed.add_field(name='***Agent Class***', value='<:duelist_emoji:714940079331737701> Duelist', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:duelist_emoji:714940079331737701> Duelists are the ones who push forward into conflicts with the enemy team, they match the role of an attacker', inline=False)

  embed.add_field(name='***Boom Bot*** (Ability 1)',
  value='	Equip a Boom Bot. Fire will deploy the bot, causing it to travel in a straight line on the ground, bouncing off walls. The Boom Bot will lock on to any enemies in its frontal cone and chase them, exploding for heavy damage if it reaches them. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Blast Pack*** (Ability 2)', value='Instantly throw a Blast Pack that will stick to surfaces. Re-us the ability after deployment to detonate, damaging and moving anything hit. Raze isn\'t damaged by this ability, but will still take fall damage if launched up far enough. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Paint Shells*** (Signature Ability)', value='Equip a cluster grenade. Fire to throw the grenade, which does damage and creates sub-munitions, each doing damage to anyone in their range. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Showstopper*** (Ultimate Ability)',
  value='Equip a rocket launcher. Fire shoots a rocket that does massive area damage on contact with anything. \nDefault Keybind → `X`', inline=False)

  return embed

def Reyna():
  agentName = 'Reyna'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://vignette.wikia.nocookie.net/valorant/images/4/41/Reyna_artwork.png/revision/latest/top-crop/width/360/height/450?cb=20200602020340")

  embed.add_field(name='***Origin***', value=':flag_it: Mexico', inline=True)

  embed.add_field(name='***Agent Class***', value='<:duelist_emoji:714940079331737701> Duelist', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:duelist_emoji:714940079331737701> Duelists are the ones who push forward into conflicts with the enemy team, they match the role of an attacker', inline=False)

  embed.add_field(name='***Leer*** (Ability 1)',
  value='EQUIP an ethereal destructible eye. ACTIVATE to cast the eye a short distance forward. The eye will Nearsight all enemies who look at it. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Devour*** (Ability 2)', value='Enemies killed by Reyna leave behind Soul Orbs that last 3 seconds. INSTANTLY consume a nearby soul orb, rapidly healing for a short duration. Health gained through this skill exceeding 100 will decay over time. If EMPRESS is active, this skill will automatically cast and not consume the orb. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Dismiss*** (Signature Ability)', value='INSTANTLY consume a nearby soul orb, becoming intangible for a short duration. If EMPRESS is active, also become invisible. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Empress (Ultimate Ability)***',
  value='INSTANTLY enter a frenzy, increasing firing speed, equip and reload speed dramatically. Scoring a kill renews the duration. \nDefault Keybind → `X`', inline=False)

  return embed

def Sage():
  
  agentName = 'Sage'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/8Elw4Sc.png")

  embed.add_field(name='***Origin***', value=':flag_cn: China', inline=True)

  embed.add_field(name='***Agent Class***', value='<:sentinel_emoji:714940115239305327> Sentinel', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:sentinel_emoji:714940115239305327> Sentinels are defenders, usually playing the back line of a team', inline=False)

  embed.add_field(name='***Barrier Orb*** (Ability 1)',
  value='EQUIP a barrier orb. FIRE places a solid wall. ALT FIRE rotates the targeter. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Slow Orb*** (Ability 2)', value='EQUIP a slowing orb. FIRE to throw a slowing orb forward that detonates upon landing, creating a lingering field that slows players caught inside of it. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Healing Orb*** (Signature Ability)', value='EQUIP a healing orb. FIRE with your crosshairs over a damaged ally to activate a heal-over-time on them. ALT FIRE while Sage is damaged to activate a self heal-over-time. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Resurrection*** (Ultimate Ability)',
  value='EQUIP a resurrection ability. FIRE with your crosshairs placed over a dead ally to begin resurrecting them. After a brief channel, the ally will be brought back to life with full health. \nDefault Keybind → `X`', inline=False)

  return embed

def Sova():
  
  agentName = 'Sova'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/ZzM8g5t.png")

  embed.add_field(name='***Origin***', value=':flag_ru: Russia', inline=True)

  embed.add_field(name='***Agent Class***', value='<:initiator_emoji:714939457589215274> Initiator', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:initiator_emoji:714939457589215274> Initiators focus on gathering intel and help the team push', inline=False)

  embed.add_field(name='***Owl Drone*** (Ability 1)',
  value='EQUIP an owl drone. FIRE to deploy and take control of movement of the drone. While in control of the drone, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Shock Bolt*** (Ability 2)', value='EQUIP a bow with a shock bolt. FIRE to send the explosive bolt forward, detonating upon collision and damaging players nearby. HOLD FIRE to extend the range of teh projectile. ALTERNATE FIRE to add up to two bounces to this arrow. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Recon Bolt*** (Signature Ability)', value='EQUIP a bow with recon boly. FIRE to send the recon bolt forward, activating upon collision and revealing the location of nearby enemies caught in the line of sight of the bolt. Enemies can destroy this bolt. HOLD FIRE to extend the range of the projective. ALTERNATE FIRE to add up to two bounces to this arrow. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Hunter\'s Fury*** (Ultimate Ability)',
  value='EQUIP a bow with three long-range, wall-piercing energy blasts. FIRE to release an energy blast in a line in front of Sova, dealing damage and revealing the location of enemies caught in the line. This ability can be RE-USED up to two more times while the ability timer is active. \nDefault Keybind → `X`', inline=False)

  return embed


def Viper():
  
  agentName = 'Viper'
  embed = discord.Embed(title=agentName + " (Agent)", color=0xFF004D)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/Hp9mbcU.png")

  embed.add_field(name='***Origin***', value=':flag_us: United States', inline=True)

  embed.add_field(name='***Agent Class***', value='<:controller_emoji:714940194566176958> Controller', inline=True)

  embed.add_field(name='***Agent Class Definition***', value='<:controller_emoji:714940194566176958> Controllers are good at blocking off sight lines and generally offer support to the team', inline=False)

  embed.add_field(name='***Snake Bite*** (Ability 1)',
  value='Equip a chemical launcher. Fire to launch a canister that shatters upon hitting the floor, creating a lingering chemical zone that damages and slows enemies. \nDefault Keybind → `C`', inline=False)

  embed.add_field(name='***Poison Cloud*** (Ability 2)', value='Equip a gas emitter. Fire to throw the emitter that perpetually remains throughout the round. Re-use the ability to create a toxic gas cloud at the cost of fuel. This ability can be re-used more than once and can be picked up to be redeployed. \nDefault Keybind → `Q`', inline=False)

  embed.add_field(name='***Toxic Screen*** (Signature Ability)', value='Equip a gas emitter launcher. Fire to deploy a long line of gas emitters. Re-use the ability to create a tall wall of toxic gas at the cost of fuel. This ability can be re-used more than once. \nDefault Keybind → `E`', inline=False)

  embed.add_field(name='***Viper\'s Pit (Ultimate Ability)***',
  value='Equip a chemical sprayer. Fire to spray a chemical cloud in all directions around Viper, creating a large cloud that reduces the vision range and maximum health of players inside of it. \nDefault Keybind → `X`', inline=False)

  return embed

def invalidMessage():
  
  embed = discord.Embed(title="Invalid Command Usage", color=0xFF0000)
  
  embed.set_author(name="Veloxis", url="https://Valorant-Bot.hdadhich01.repl.co", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='***Use*** **`v!help`** ***for Info on All Commands***', value='The correct usage of this command is \n**`v!agent <name/listcode>`** (aliases = **`v!ag`**) \n\nTo get the names of all the agents, use \n**`v!agents`** (aliases = **`v!ags`**) \n\n*the names of agents are NOT CASE SENSITIVE so you can do either **`v!ag sova`** or **`v!ag Sova`***', inline=True)

  return embed

