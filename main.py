#770371351579852880
import discord
from discord.ext import commands
from webbot import Browser
import asyncio 
import datetime
servers = {}
server_name = {}
intents = discord.Intents.default()
intents.members = True
challenges = {}
respons = {}
forbidden_words = [ 'nigga', 'nigger', 'ass', 'headass', 'dickhead', 'fucker', 'faggot', 'fag']
import random
color = [discord.Color.red(), discord.Color.green(), discord.Color.blue(), discord.Color.purple(), discord.Color.orange()]
people = {}
import time
repeat = ""
repeatCounting = ""
hell = ["Hi", "Hello", "Hey", "HIHIHIHIHIHIHIHIHIHI", "Namaste", "Hola", "YOOOOOOOOOOOOO", "Wassup", "Wassup Cuh", "Wassup Bluh", "Imma make sure they remember cuz I walk around with a lot of enimies", "sup", "sup dog"]
prefix =["!8", "!"]
client = commands.Bot(command_prefix = prefix, intents=intents)
client.remove_command("help")
will = ["yes", "no"]
by = ["cya", "bye", "see ya", "Leave", "Adios", "Sayonara", "Buh Bye"]
much = ['A lot', 'Not a lot', 'A little', 'None', 'As much as you can imagine']
replies = ['As I see it, yes.',
 'Ask again later.',
 'Better not tell you now.',
 'Cannot predict now.',
 'Concentrate and ask again.',
 'Don’t count on it.',
 'It is certain.',
 'It is decidedly so.',
 'Most likely.',
 'My reply is no.',
 'My sources say no.',
 'Outlook not so good.',
 'Outlook good.',
 'Reply hazy, try again.',
 'Signs point to yes.',
 'Very doubtful.',
 'Without a doubt.',
 'Yes.',
 'Yes – definitely.',
 'You may rely on it.']
trollz = []
trollVictim = []
response = []
league = {}
alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, " ":0}
players = {}
fareWellMessage = {}
GreetingMessage = {}
antiSpam = []
mutes = {}
@client.event
async def on_guild_join(guild):
	woo = discord.Embed( description = f"**Thank you, {guild.name} for inviting BarthiccBot to your server\n\nBarthiccBot is a A multiple purpose bots that include playing games like blackjack with your friends, fun utilities, and easy to access moderation commands\n\nType !help to have access to over 61 different commands and make sure to try it all\n\n> :ballot_box: PLEASE UPVOTE FOR MY BOT [HERE](https://top.gg/bot/770371351579852880/vote)\n\n> :email: MAKE SURE YOU INVITE THE BOT TO OTHER SERVERS USING THE [INVITATION LINK](https://discord.com/api/oauth2/authorize?client_id=770371351579852880&permissions=137526352&scope=bot)\n\n> :computer: JOIN OUR [BARTHICCBOT SUPPORT SERVER](https://discord.gg/ePhUPNJaVN)\n\nMake sure to add the creator ``Barthicc#8624`` as a friend if you have any suggestions or we can chat**", color = random.choice(color))
	woo.set_author(name = "SAY HELLO TO BARTHICCBOT :D", icon_url= "https://www.sohh.com/wp-content/uploads/2020/12/3b3baf71a0251cf5f7adce147c219ee5.jpg")
	woo.set_thumbnail(url=guild.icon_url)
	try:
		await guild.text_channels[0].send(embed=woo)
	except:

		pass

			


"""footballStandings = {}
			
async def football(ctx, member:discord.Member=""):
	if not ctx.author.guild.id in footballStandings:
		footballStandings[ctx.author.guild.id] = {"BarthiccBot":[0, 0]}
	if not ctx.author.name in footballStandings[ctx.author.guild.id]:
		footballStandings[ctx.author.guild.id][ctx.author.name] = [0, 0]	
	if not member == "":
		if member.name == ctx.author.name:
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"https://tenor.com/view/idiot-congratulations-you-played-your-self-gif-10536951"))
			
			return
		
			
		if not member.name in footballStandings[ctx.author.guild.id]:
			footballStandings[ctx.author.guild.id][member.name] = [0, 0]
	home = footballStandings[ctx.author.guild.id][ctx.author.name]
	if member == "":
		away = footballStandings[ctx.author.guild.id]["BarthiccBot"]
	else:
		away = footballStandings[ctx.author.guild.id][member.name]
	ur = 0
	their = 0
	uryard = 0
	theyard = 0
	urtouchdowns = 0
	thetouchdowns = 0
	brea = False
	
	urpicks = 0
	thepicks = 0
	down = 1
	till = 10
	yard = random.randint(15, 30)
	
	name = ctx.author.name
	if member == "":
		opp = "Bot"
	else:
		opp = member.name

	string = ""
	start = random.randint(1, 100)

	acc = 0
	pick6 = False
	pick7 = False

	for i in range(10):
		print(f"drive {i}")
		if i == 0:
			woo ="First Quarter\n"
		elif i == 2:
			woo = "Second Quarter\n"
		elif i == 4:
			woo = "Two Minute Warning\n"
		elif i == 5:
			woo ="Third Quarter\n"
		elif i == 7:
			woo ="Fourth Quarter\n"
		
		elif i == 9:
			woo = "Two Minute Warning\n"
		if yard > 100:
			yard = random.randint(10, 40)
		passin_yards = 0
		Off = ["run", "short pass", "medium pass", "long pass", "field goal", "punt"]
		Def = ["blitz", "man", "zone"]

		down = 0
		till = 10
		while True:
			string = woo +"\n"
			if yard <= 0 or yard >=100:
				yard = random.randint(15, 30)
			gain = 0
			if till <= 0:
				if till + yard >= 100:
					till =  "goal"
				else:
					till =10
				down = 0

			
			if down == 4:
				await ctx.send(embed=discord.Embed(title="Football! :football:", description="Turn over on downs", color = random.choice(color)))
				uryard += passin_yards
				break
			down += 1

			
			string += f"{down} & {till}\n"
			if yard < 50:
				string += f"On {name[0:3].upper()} {yard}"
			elif yard > 50:
				string += f"On {opp[0:3].upper()} {100-yard} "
			else:
				string += "You are on the 50 yard line"
			string += f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{name}'s stats\n{uryard} yards\n{urtouchdowns} touchdowns\n{urpicks} picks\n"
			
			if opp != "Bot":
				string += "\nDefense, choose your play:\n\n :football: Man\n :football: Zone\n :football: Blitz"

				await ctx.send(embed=discord.Embed(title="Football! :football:", description=string, color = random.choice(color)))
				response = await client.wait_for("message")
				while response.author.name != opp.name or not response.content.lower() in Def:
					if not response.content.lower() in Def:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description="That is not one of the options\n\nDefense, choose your play:\n\n :football: Man\n :football: Zone\n :football: Blitz", color = random.choice(color)))
					response = await client.wait_for("message")
				
			
			await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"{string}\n\nOffense it is your turn, choose your play:\n\n :football: Run\n :football: Short pass\n :football: Medium Pass\n :football: Long Pass\n :football: Field Goal\n :football: Punt", color = random.choice(color)))
			offresponse = await client.wait_for("message")
			while offresponse.author.name != name or not offresponse.content.lower() in Off:
				if offresponse.author.name == name and not offresponse.content.lower() in Off:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description="That is not one of the options Offense it is your turn, choose your play:\n\n :football: Run\n :football: Short pass\n :football: Medium Pass\n :football: Long Pass\n :football: Field Goal\n :football: Punt", color = random.choice(color)))
				offresponse = await client.wait_for("message")
			rand = random.randint(0, 100)

			if offresponse.content.lower() == "run":
				if 0 <= rand <= 50:
					gain = random.randint(0, 10)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"Your runner ran {gain} yards", color = random.choice(color)))
				elif 50 <= rand <= 80:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"Your runner lost {gain * -1} yards", color = random.choice(color)))
				elif 80 <= rand <= 90:
					gain = random.randint(10, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"Your runner ran {gain} yards ", color = random.choice(color)))
				elif 90 <= rand <= 95:
					
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOUR RUNNER RAN INTO THE ENDZONE!!! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 100
					

				elif 95 <= rand <= 100:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"Your rumnner fumbled the ball", color = random.choice(color)))
					break

			
			elif offresponse.content.lower() == "short pass":
				if 0 <= rand <= 50:
					gain = random.randint(1, 10)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 50 <= rand <= 55:
					gain = random.randint(10, 15)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 55 <= rand <=60:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 60 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 94:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					uryard += 100-yard
					yard = 100
					
				elif 94 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					urpicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick6 = True

					thepicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))
						break
				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					pick6 = True

			elif offresponse.content.lower() == "medium pass":
				if 0 <= rand <= 30:
					gain = random.randint(10, 20)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 30 <= rand <= 35:
					gain = random.randint(20, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 35 <= rand <=45:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 45 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 93:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 100
					uryard += (100-gain)


				elif 93 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					urpicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick6 = True
					urpicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))

				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					

					pick6 = True
					
			elif offresponse.content.lower() == "long pass":
				if 0 <= rand <= 25:
					gain = random.randint(30, 40)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 25 <= rand <= 27:
					gain = random.randint(40, 55)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 27 <= rand <=40:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 40 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 93:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 100
					uryard += (100-gain)
					
				elif 93 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					urpicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick6 = True
					urpicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))
						break
				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					pick6 = True
			elif offresponse.content.lower() == "punt":
				
				gain = random.randint(40, 60)
				if gain + yard >= 100:
					yard = 80
				else:
					yard += gain
				await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The ball is punted {gain} yards", color = random.choice(color)))
				break
			elif offresponse.content.lower() == "field goal":
				chan = random.randint(0, 110)
				if(chan>=0 and chan <= yard):
					await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
					ur+=3
					break
				else:
					await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
					
			print(f"yard {yard}")
			yard += gain
			try:
				till -= gain
			except: 
				pass

			if pick6 == True:
				their += 6
				await asyncio.sleep(1)
				await ctx.send(embed=discord.Embed(title=f"TOUCHDOWN TEAM {name.upper()}! Field Goal or Two Point Conversion", color = random.choice(color)))

				if opp == "Bot":
					if ur-their == 2 or ur-their==5:
						if random.randint(0, 100) < 50:
							await ctx.send(embed=discord.Embed(title="Two point conversion is good", color = random.choice(color)))
							their+=2
						else:
							await ctx.send(embed=discord.Embed(title="Two point conversion is no good", color = random.choice(color)))
					else:
						if random.randint(0, 100) < 96:
							await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
							their+=1
						else:
							await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
					
				else:

					await ctx.send(embed=discord.Embed(title="Field Goal or Two Point Conversion", color = random.choice(color)))
					response = await client.wait_for('message')
					while response.author.name != name or (response.content.lower() != "field goal" and response.content.lower() != "two point conversion"):
						await ctx.send(embed=discord.Embed(title="THATS NOT AN OPTION, Field Goal or Two Point Conversion", color = random.choice(color)))
						response = await client.wait_for('message')
					if response.content.lower() =="two point conversion":
						if random.randint(0, 100) < 50:
							await ctx.send(embed=discord.Embed(title="Two point conversion is good", color = random.choice(color)))
							their+=2
						else:
							await ctx.send(embed=discord.Embed(title="Two point conversion is no good", color = random.choice(color)))
					else:
						if random.randint(0, 100) < 96:
							await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
							their+=1
						else:
							await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
				yard = random.randint(15, 30)
				till = 10
				down = 0
				pick6 = False
			if yard >= 100:
				if offresponse.content.lower() != "run":
					urtouchdowns += 1

				ur += 6
				await asyncio.sleep(1)
				await ctx.send(embed=discord.Embed(title=f"TOUCHDOWN TEAM {name.upper()}! Field Goal or Two Point Conversion", color = random.choice(color)))

				response = await client.wait_for('message')

				while response.author.name != name and (response.content.lower() != "field goal" and response.content.lower() != "two point conversion"):
					await ctx.send(embed=discord.Embed(title="THATS NOT AN OPTION, Field Goal or Two Point Conversion", color = random.choice(color)))
					response = await client.wait_for('message')
				if random.randint(0, 100) < 96:
					await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
					ur+=1
				else:
					await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))

				break


		down = 0
		till = 10

		while True:
			gain = 0
			if yard <= 0 or yard >=100:
				yard = random.randint(60, 85)
			
			if till <= 0:
				till =10
				down = 0
			if down == 4:
				await ctx.send(embed=discord.Embed(title="Football! :football:", description="Turn over on downs", color = random.choice(color)))

				break
			down += 1
			string = woo
			
			string += f"{down} & {till}\n"
			if yard < 50:
				string += f"On {name[0:3].upper()} {yard}"
			elif yard > 50:
				string += f"On {opp[0:3].upper()} {100-yard} "
			else:
				string += "You are on the 50 yard line"
			string += f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{opp}'s stats\n{theyard} yards\n{thetouchdowns} touchdowns\n{thepicks} picks\n"
			
			string += "\nDefense, choose your play:\n\n :football: Man\n :football: Zone\n :football: Blitz"

			await ctx.send(embed=discord.Embed(title="Football! :football:", description=string, color = random.choice(color)))
			response = await client.wait_for("message")
			while response.author.name != name or not response.content.lower() in Def:
				if response.author.name == name and not response.content.lower() in Def:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description="That is not one of the options\n\nDefense, choose your play:\n\n :football: Man\n :football: Zone\n :football: Blitz", color = random.choice(color)))
				response = await client.wait_for("message")
			
			if opp != "Bot":
				await ctx.send(embed=discord.Embed(title="Football! :football:", description="Offense it is your turn, choose your play:\n\n :football: Run\n :football: Short pass\n :football: Medium Pass\n :football: Long Pass\n :football: Field Goal\n :football: Punt", color = random.choice(color)))
				offresponse = await client.wait_for("message")
				while offresponse.author.name != opp or not offresponse.content.lower() in Off:
					if offresponse.author.name == opp and not offresponse.content.lower() in Off:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description="That is not one of the options Offense it is your turn, choose your play:\n\n :football: Run\n :football: Short pass\n :football: Medium Pass\n :football: Long Pass\n :football: Field Goal\n :football: Punt", color = random.choice(color)))
					offresponse = await client.wait_for("message")
			else:
				wo = ["run", "short pass", "medium pass", "long pass"]
				if down == 4 and 1< yard < 35:
					offresponse = "field goal"
				
				elif down == 4 and till > 2:
					offresponse = "punt"
				else:
					offresponse = random.choice(wo)
			rand = random.randint(0, 100)
			rand = random.randint(0, 100)

			if offresponse == "run":
				if 0 <= rand <= 40:
					gain = random.randint(0, 10)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The runner ran {gain} yards", color = random.choice(color)))
				elif 40 <= rand <= 70:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The runner lost {gain * -1} yards", color = random.choice(color)))
				elif 70 <= rand <= 90:
					gain = random.randint(10, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The runner ran {gain} yards ", color = random.choice(color)))
				elif 90 <= rand <= 95:
					
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"THE RUNNER RAN INTO THE ENDZONE!!! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 0
					

				elif 95 <= rand <= 100:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The runner fumbled the ball", color = random.choice(color)))
					break

			
			elif offresponse == "short pass" :
				if 0 <= rand <= 25:
					gain = random.randint(1, 10)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 50 <= rand <= 55:
					gain = random.randint(10, 15)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 55 <= rand <=58:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 58 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 94:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 0
					theyard += 100-yard
					
				elif 94 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					thepicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick7 = True

					thepicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))
						break
				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					pick7 = True

			elif offresponse == "medium pass" :
				if 0 <= rand <= 30:
					gain = random.randint(10, 20)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 30 <= rand <= 35:
					gain = random.randint(20, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))

					theyard += gain
				elif 35 <= rand <=45:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 45 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 93:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 0
					theyard += (100-gain)


				elif 93 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					thepicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick6 = True
					thepicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))

				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					

					pick6 = True
					
			elif offresponse == "long pass" :
				if 0 <= rand <= 25:
					gain = random.randint(30, 40)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 25 <= rand <= 18:
					gain = random.randint(40, 55)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 28 <= rand <=40:
					gain = random.randint(-5, 0)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"YOU GOT SACKED {gain * -1} YARDS", color = random.choice(color)))
				elif 40 <= rand <= 90:

					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but it is incomplete", color = random.choice(color)))

				elif 90 <= rand <= 93:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but AND THE RECEIVER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {name.upper()}", color = random.choice(color)))
					yard = 0
					theyard += (100-gain)
					
				elif 93 <= rand <= 96:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but IT IS PICKED OFF", color = random.choice(color)))
					
					thepicks +=1
					break
				elif 96 <= rand <=97:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but IT IS PICKED OFF AND THE DEFENDER IS RUNNING TO THE ENDZONE! TOUCHDOWN TEAM {opp.upper()}", color = random.choice(color)))
					pick7 = True
					thepicks +=1
				elif 97 <= rand <=98:
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP!", color = random.choice(color)))
						break
					else:
						await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE OFFENSE PICKED IT UP!", color = random.choice(color)))
						break
				elif 99 <= rand <= 100:
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass, but THE RECEIVER FUMBLED THE BALL\nAND THE DEFENDER PICKED IT UP! HE IS RUNNING TO THE ENDZONE", color = random.choice(color)))
					pick7 = True
			elif offresponse == "punt":
				
				gain = random.randint(40, 60)
				if gain + yard <= 0:
					yard = 20
				else:
					yard -= gain
				await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"The ball is punted {gain} yards", color = random.choice(color)))
				break
			elif offresponse == "field goal":
				chan = random.randint(0, 110)
				if(chan>=0 and chan <= 100-yard):
					await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
					their+=3
					break
				else:
					await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
					
			print(f"theyard, {yard}")
			yard -= gain
			till -= gain

			if pick7 == True:

				ur += 6
				await asyncio.sleep(1)
				await ctx.send(embed=discord.Embed(title=f"TOUCHDOWN TEAM {name.upper()}! Field Goal or Two Point Conversion", color = random.choice(color)))

				

				await ctx.send(embed=discord.Embed(title="Field Goal or Two Point Conversion", color = random.choice(color)))
				response = await client.wait_for('message')
				while response.author.name != name or (response.content.lower() != "field goal" and response.content.lower() != "two point conversion"):
					await ctx.send(embed=discord.Embed(title="THATS NOT AN OPTION, Field Goal or Two Point Conversion", color = random.choice(color)))
					response = await client.wait_for('message')
				if response.content.lower() =="two point conversion":
					if random.randint(0, 100) < 50:
						await ctx.send(embed=discord.Embed(title="Two point conversion is good", color = random.choice(color)))
						ur+=2
					else:
						await ctx.send(embed=discord.Embed(title="Two point conversion is no good", color = random.choice(color)))
				else:
					if random.randint(0, 100) < 96:
						await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
						ur+=1
					else:
						await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
				yard = random.randint(15, 30)
				till = 10
				down = 0
				pick7 = False
			if yard <= 0:
				if offresponse != "run":
					thetouchdowns += 1
				their += 6
				await asyncio.sleep(1)
				await ctx.send(embed=discord.Embed(title=f"TOUCHDOWN TEAM {opp.upper()}! Field Goal or Two Point Conversion", color = random.choice(color)))
				if opp == "Bot":
					if ur-their == 2 or ur-their==5:
						if random.randint(0, 100) < 50:
							await ctx.send(embed=discord.Embed(title="Two point conversion is good", color = random.choice(color)))
							their+=2
						else:
							await ctx.send(embed=discord.Embed(title="Two point conversion is no good", color = random.choice(color)))
					else:
						if random.randint(0, 100) < 96:
							await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
							their+=1
						else:
							await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))
					yard = random.randint(15, 30)
					till = 10
					down = 0
				else:

					response = await client.wait_for('message')

					while response.author.name != name and (response.content.lower() != "field goal" and response.content.lower() != "two point conversion"):
						await ctx.send(embed=discord.Embed(title="THATS NOT AN OPTION, Field Goal or Two Point Conversion", color = random.choice(color)))
						response = await client.wait_for('message')
					if random.randint(0, 100) < 96:
						await ctx.send(embed=discord.Embed(title="The field goal is good", color = random.choice(color)))
						ur+=1
					else:
						await ctx.send(embed=discord.Embed(title="The field goal is no good", color = random.choice(color)))

				break
		
		
	if ur > their:
		if member == "":
			stateEmbed = discord.Embed(description = f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{name}'s stats\n{uryard} yards\n{urtouchdowns} touchdowns\n{urpicks} picks\n\n{opp}'s stats\n{theyard} yards\n{thetouchdowns} touchdowns\n{thepicks} picks", color =random.choice(color))
			stateEmbed.set_author(name=f'{ctx.author.name} Won the blackjack game', icon_url = ctx.author.avatar_url)
			
		else:
			stateEmbed = discord.Embed(description = f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{name}'s stats\n{uryard} yards\n{urtouchdowns} touchdowns\n{urpicks} picks\n\n{opp}'s stats\n{theyard} yards\n{thetouchdowns} touchdowns\n{thepicks} picks", color =random.choice(color))
			stateEmbed.set_author(name=f'{ctx.author.name} Won the blackjack game', icon_url = ctx.author.avatar_url)
		await ctx.send(embed=stateEmbed)
		home[0] += 1
		away[1] +=1

	if their > ur:
		if member == "":
			stateEmbed = discord.Embed(description = f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{name}'s stats\n{uryard} yards\n{urtouchdowns} touchdowns\n{urpicks} picks\n\n{opp}'s stats\n{theyard} yards\n{thetouchdowns} touchdowns\n{thepicks} picks", color =random.choice(color))
			stateEmbed.set_author(name='BarthiccBot Won the blackjack game', icon_url = "https://www.sohh.com/wp-content/uploads/2020/12/3b3baf71a0251cf5f7adce147c219ee5.jpg")
		else:
			stateEmbed = discord.Embed(description = f"\n{name[0:3].upper()} {ur} - {their} {opp[0:3].upper()}\n{name}'s stats\n{uryard} yards\n{urtouchdowns} touchdowns\n{urpicks} picks\n\n{opp}'s stats\n{theyard} yards\n{thetouchdowns} touchdowns\n{thepicks} picks", color =random.choice(color))
			stateEmbed.set_author(name=f'{member.name} Won the blackjack game', icon_url = member.avatar_url)
		await ctx.send(embed=stateEmbed)
		home[1] += 1
		away[0] +=1

@client.command()
async def football_game(ctx, member:discord.Member=""):
	if member == "":
		await football(ctx)
	else:
		await football(ctx, member)

@client.command()
async def football_standings(ctx):
	
	if not ctx.author.guild.id in footballStandings:
		
		await ctx.send(embed=discord.Embed(title = ":hearts: :diamonds:blackjack:spades: :clubs:", description = "Your server has not played rock paper scissors before"))
		return
	football_pct = {}
	for i in footballStandings[ctx.author.guild.id]:
		
		win = footballStandings[ctx.author.guild.id][i][0]
		loss = footballStandings[ctx.author.guild.id][i][1]
		
		try:
			win_percentage = round((win/(win+loss))*100, 3)
			football_pct[i] = win_percentage
		except:
			football_pct[i] = "-"
		
	standingsText = "> **NAME - WIN - LOSS - WIN %**\n\n"
	standings = sorted(football_pct.items(), key = lambda x : x[1], reverse = True)
	
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			
			standingsText += f">  {rank}  **{standings[i+woo][0]} - ``{footballStandings[ctx.author.guild.id][standings[i+woo][0]][0]}`` - ``{footballStandings[ctx.author.guild.id][standings[i+woo][0]][1]}`` - ``{standings[i+woo][1]}``**\n\n"
	except:
		pass
	
	

	await ctx.send(embed=discord.Embed(title = f"Standings :trophy: For :trophy: {ctx.message.author.guild.name}", description = f"{standingsText}", color = random.choice(color)))


"""

@client.command()
async def uno(ctx):
	cards = ['0 🟦', '1 🟦', '2 🟦', '3 🟦', '4 🟦', '5 🟦', '6 🟦', '7 🟦', '8 🟦', '9 🟦', '🔄 🟦', '🚫 🟦', '+2🟦', '1 🟦', '2 🟦', '3 🟦', '4 🟦', '5 🟦', '6 🟦', '7 🟦', '8 🟦', '9 🟦', '🔄 🟦', '🚫 🟦', '+2🟦', '1 🟥', '2 🟥', '3 🟥', '4 🟥', '5 🟥', '6 🟥', '7 🟥', '8 🟥', '9 🟥', '🔄 🟥', '🚫 🟥', '+2🟥', '1 🟥', '2 🟥', '3 🟥', '4 🟥', '5 🟥', '6 🟥', '7 🟥', '8 🟥', '9 🟥', '🔄 🟥', '🚫 🟥', '+2🟥', '1 🟨', '2 🟨', '3 🟨', '4 🟨', '5 🟨', '6 🟨', '7 🟨', '8 🟨', '9 🟨', '🔄 🟨', '🚫 🟨', '+2🟨', '1 🟨', '2 🟨', '3 🟨', '4 🟨', '5 🟨', '6 🟨', '7 🟨', '8 🟨', '9 🟨', '🔄 🟨' , '🚫 🟨', '+2🟨', '1 🟩', '2 🟩' , '3 🟩', '4 🟩', '5 🟩', '6 🟩', '7 🟩', '8 🟩', '9 🟩', '🔄 🟩', '🚫 🟩', '+2🟩', '1 🟩', '2 🟩', '3 🟩', '4 🟩', '5 🟩', '6 🟩', '7 🟩', '8 🟩', '9 🟩', '🔄 🟩', '🚫 🟩', '+2🟩', '🟦🟥+4🟨🟩', '🟦🟥+4🟨🟩', '🟦🟥+4🟨🟩', '🟦🟥+4🟨🟩', '🟦🟥WILD🟨🟩', '🟦🟥WILD🟨🟩', '🟦🟥WILD🟨🟩', '🟦🟥WILD🟨🟩']
	stacked = []
	players = [ctx.author]
	slapjackPlayer = {ctx.author.name: []}
	not_start = True
	await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"Everyone! {ctx.author.name} is creating a UNO! game.\nType ``join`` to join the game.\n\n{ctx.author.mention}, type ``start`` when your ready to start the game", color = random.choice(color)))
	
	response = await client.wait_for("message")
	try:
		if response.author.id == ctx.author.id and response.content.lower() == "start":
			not_start = False
		elif response.content.lower() == "join" and response.author.guild.id == ctx.author.guild.id and not response.author.name in slapjackPlayer:
			slapjackPlayer[response.author.name] = []
			players.append(response.author)
			await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"{response.author.name.upper()} HAVE JOINED THE GAME", color = random.choice(color)))
		if response.content.lower() == "end" and response.author.name == ctx.author.name:
			await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"The Host ended the game", color = random.choice(color)))
			return
	except:
		pass
	while not_start:
		response = await client.wait_for("message")
		if response.content.lower() == "end" and response.author.name == ctx.author.name:
				await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"The Host ended the game", color = random.choice(color)))
				return
		try:
			if response.author.id == ctx.author.id and response.content.lower() == "start":
				not_start = False
			elif response.content.lower() == "join" and not response.author.name in slapjackPlayer and response.author.guild.id == ctx.author.guild.id:
				slapjackPlayer[response.author.name] = []
				players.append(response.author)
				await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"{response.author.name.upper()} HAVE JOINED THE GAME", color = random.choice(color)))
		except:
			pass
	random.shuffle(cards)
	slay3r = 0
	for i in slapjackPlayer:
		for _ in range(7):
			slapjackPlayer[i].append(cards[0])
			cards.pop(0)
	stacked.append(cards[0])
	cards.pop(0)
	add = 1
	g = 0
	hurry = True
	reversed = False
	skipped = False
	await ctx.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description = f"{ctx.author.mention} We have sent you a DM", color = random.choice(color)))
	while True:

		if g >= len(players):
			
			g -= len(players)
			
		if g < 0:
			g += len(players)
		i = players[g]
	

		cardString = ""
		for d in range(len(slapjackPlayer[i.name])):
			cardString += f"``{d+1}``. {slapjackPlayer[i.name][d]}\n"
		
		st0p = discord.Embed( description=f"Top Card: {stacked[len(stacked)-1]}\n{cardString}\nTo place your card, Type the position that relates to the card.\n If you can't put any card, type ``pick`` to pick a card from the deck")
		
		if i == "BarthiccBot":
			br3athing = "https://www.sohh.com/wp-content/uploads/2020/12/3b3baf71a0251cf5f7adce147c219ee5.jpg"
		else:
			br3athing = i.avatar_url
		st0p.set_author(name="🟦🟥UNO!🟨🟩", icon_url = br3athing)
		try:
			await i.send(embed = st0p)
		except:
			await ctx.author.send(embed=discord.Embed(title="🟦🟥UNO!🟨🟩", description=f"{i.mention} Could you please turn on permissions that can let the bot dm you, so that we could keep your choices private? Type \"Ready\""))
			response = await client.wait_for("message")
			while response.content.lower() != "ready":
				response = await client.wait_for("message")
			try:
				await i.send(embed = st0p)
			except:
				continue
			

		response = await client.wait_for("message")

		while response.author.id != i.id or (not response.content.isnumeric()):
			if response.content.lower() == "pick":
				break
			response = await client.wait_for("message")
		if response.content.lower() == "pick":
			slapjackPlayer[i.name].append(cards[0])
			cards.pop(0)
			g+=1
			continue

		Feb = int(response.content)-1
		while Feb > len(slapjackPlayer[i.name])-1:
			await i.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = "You cannot choose that number", color = random.choice(color)))
			response = await client.wait_for("message")
			Feb = int(response.content)-1
			
		maybach = slapjackPlayer[i.name][Feb]

		while (maybach[0] != stacked[len(stacked)-1][0] and maybach[2] != stacked[len(stacked)-1][2]) and maybach != "🟦🟥WILD🟨🟩" and maybach != "🟦🟥+4🟨🟩" and stacked[len(stacked)-1] != "🟦🟥WILD🟨🟩" and stacked[len(stacked)-1] != "🟦🟥+4🟨🟩":
			await i.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = "You cannot place that card on the stack, Try another card", color = random.choice(color)))

			response = await client.wait_for("message")
			Feb = int(response.content)-1
			maybach = slapjackPlayer[i.name][Feb]
	
			
		stacked.append(maybach)
		slapjackPlayer[i.name].pop(Feb)


		
		Unocolor = ["red", "yellow", "blue", "green"]

		if len(slapjackPlayer[i.name]) == 0:
			break
		if maybach[0] == "🚫":
			g+= 2
			continue
			
		elif maybach[0] == "🔄":
			if add == 1:
				add = -1
			else:
				add = 1
		elif maybach[1] == "2":

			for _ in range(2):
				try:
					slapjackPlayer[players[g+1].name].append(cards[0])
					cards.pop(0)
				except:
					slapjackPlayer[players[g+1-len(players)].name].append(cards[0])
					cards.pop(0)
			g+=2
			continue

		elif maybach[2] == "+":
			for _ in range(4):
				try:
					slapjackPlayer[players[g+1].name].append(cards[0])
					cards.pop(0)
				except:
					if add == 1:
						slapjackPlayer[players[g+1-len(players)].name].append(cards[0])
					else:
						slapjackPlayer[players[g+1+len(players)].name].append(cards[0])
					cards.pop(0)
			await i.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = "Which color would you like to change the stack to?"))
			response = await client.wait_for("message") 
			while response.author.id != i.id or not response.content.lower() in Unocolor:
				response = await client.wait_for("message") 
			if response.content.lower() == "red":
				stacked.append("W 🟥")
			elif response.content.lower() == "green":
				stacked.append("W 🟩")
			elif response.content.lower() == "blue":
				stacked.append("W 🟦")
			elif response.content.lower() == "yellow":
				stacked.append("W 🟨")
			g+=2
			continue
		elif maybach == "🟦🟥WILD🟨🟩":
			await i.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = "Which color would you like to change the stack to?"))
			response = await client.wait_for("message") 
			while response.author.id != i.id or not response.content.lower() in Unocolor:
				response = await client.wait_for("message") 
			if response.content.lower() == "red":
				stacked.append("W 🟥")
			elif response.content.lower() == "green":
				stacked.append("W 🟩")
			elif response.content.lower() == "blue":
				stacked.append("W 🟦")
			elif response.content.lower() == "yellow":
				stacked.append("W 🟨")
		if len(slapjackPlayer[i.name]) == 0:

			await ctx.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = f"{i.mention} HAS WON UNO GAME :trophy:"))
			return
		if len(slapjackPlayer[i.name]) == 1:
			for g in players:
				await g.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description = f"{i.mention} HAS ONE CARD LEFT GO TO THE MAIN CHANNEL AND SAY UNO !"))
			response = await client.wait_for("message")

			
			while response.content.lower() != "uno" and not response.author.name in slapjackPlayer:
				response = await client.wait_for("message")

			if response.author.id != i.id:
				slapjackPlayer[i.name].append(cards[0])
				cards.pop(0)
		
		if len(cards) == 0:
			cards = stacked
			random.shuffle(cards)
			stacked = [cards[0]]
			cards.pop(0)
		rik = ""
		for z in slapjackPlayer:
			rik += f"{z} - {len(slapjackPlayer[z])}\n"
		await ctx.send(embed=discord.Embed(title = "🟦🟥UNO!🟨🟩", description=f"{i.mention} placed a {maybach}\n{rik}"))

		g+=add

		

			
			






blackjackStandings = {}
@client.command()
async def blackjack(ctx, member : discord.Member = ""):
	if member != "":
		await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"Hello, {member.mention}.\n {ctx.author.mention} challenges you to a rock paper scissors battle\n you have about 15 second to reply to this text to accept the challenge"))
		def is_correct(m):
			return m.author.id != 770371351579852880 and m.channel.id == ctx.message.channel.id
		try:
			guess = await client.wait_for('message', check=is_correct, timeout=15)
		except:
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"I guess you do not accept the challenge that {ctx.author.mention} gave you"))
			return
		i = 0
		while guess.author.id != member.id and i < 5:
			i+=1
			guess = await client.wait_for('message', check=is_correct, timeout=15)
		if i >= 5:
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"I guess you do not accept the challenge that {ctx.author.mention} gave you"))
			return
		
	if not ctx.author.guild.id in blackjackStandings:
		blackjackStandings[ctx.author.guild.id] = {"BarthiccBot":[0, 0]}
	if not ctx.author.name in blackjackStandings[ctx.author.guild.id]:
		blackjackStandings[ctx.author.guild.id][ctx.author.name] = [0, 0]	
	if not member == "":
		if member.name == ctx.author.name:
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"https://tenor.com/view/idiot-congratulations-you-played-your-self-gif-10536951"))
			
			return
		
			
		if not member.name in blackjackStandings[ctx.author.guild.id]:
			blackjackStandings[ctx.author.guild.id][member.name] = [0, 0]
	home = blackjackStandings[ctx.author.guild.id][ctx.author.name]
	if member == "":
		away = blackjackStandings[ctx.author.guild.id]["BarthiccBot"]
	else:
		away = blackjackStandings[ctx.author.guild.id][member.name]
	cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9,10, 'K', 'Q', 'J' ]
	suites = [":hearts:", ":spades:", ":clubs:", ":diamonds:"]
	suitesDict = {"A":[], 2:[], 3:[],4:[],5:[],6:[],7:[], 8:[], 9:[], 10:[], "K":[], "Q":[], "J":[]}

	cpu = []
	player = []
	cpuTotal = 0
	cpuText = ""
	playTotal = 0
	playText = ""
	playAce = 0
	cancun = 0
	skeletons = 0
	cpuAce = 0
	playce = 0
	cpuace = 0
	hidden = ""
	for i in range(2):
		randomCard = random.choice(cards)
		randomSuite = random.choice(suites)
		add = randomCard
		while randomSuite in suitesDict[randomCard]:
			randomSuite = random.choice(suites)
		suitesDict[randomCard]
		

		player.append(randomCard)
		if randomCard == "A":
			
			if playTotal + 11 < 21:
				add = 11
				cancun +=1
			else:
				
				add = 1
		if randomCard == "K" or randomCard == "Q" or randomCard == "J":
			add = 10
		playText += f"{randomCard} {randomSuite}\n"

		playTotal += add

		
		if playAce < cancun and playTotal > 21:
			playTotal -= 10
		
	

		
	for i in range(2):
		randomCard = random.choice(cards)
		randomSuite = random.choice(suites)
		add = randomCard
		while randomSuite in suitesDict[randomCard]:
			randomSuite = random.choice(suites)
		suitesDict[randomCard]
		

		cpu.append(randomCard)
		if randomCard == "A":
			if cpuTotal + 11 < 21:
				add = 11
				skeletons += 1
			else:
				
				add = 1
		if randomCard == "K" or randomCard == "Q" or randomCard == "J":
			add = 10
		
		if i == 1:
			hidden = f"{randomCard} {randomSuite}"
			cpuText += ":flower_playing_cards:\n"
		else:
			cpuText += f"{randomCard} {randomSuite}\n"
			belly = f"{randomCard} {randomSuite}\n"
			cpuTotal += add






	

	
	guess = ""
	def is_correct(m):
		return m.author.id == ctx.author.id 
	
	while True:
		if member == "":
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"{ctx.author.name}'s Cards are:\n{playText}\nTotal: {playTotal}\n\nThe Dealers Cards are:\n{cpuText}\nTotal:{cpuTotal}\n\nType h to hit\nType s to stay"))
		else:
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"**It is {ctx.author.name}'s turn**\n{ctx.author.name}'s Cards are:\n{playText}\nTotal: {playTotal}\n\n{member.name}'s Cards are:\n{cpuText}\nTotal:{cpuTotal}\n\nType h to hit\nType s to stay"))
	
		guess = await client.wait_for("message", check =is_correct)
		woo = guess.content.lower()

		while woo !="h" and woo != "s":
			
			guess = await client.wait_for("message", check =is_correct)
			woo = guess.content.lower()
		
		if woo == "s":
			
			break
		randomCard = random.choice(cards)
		randomSuite = random.choice(suites)
		add = randomCard
		while randomSuite in suitesDict[randomCard]:
			randomSuite = random.choice(suites)
		suitesDict[randomCard]
		if randomCard == "A":
			if playTotal + 11 < 21:
				add = 11
				cancun += 1
			else:
				
				add = 1

		player.append(randomCard)
		
		if randomCard == "K" or randomCard == "Q" or randomCard == "J":
			add = 10
		woo = playText
		playText += f"{randomCard} {randomSuite}\n"
		
		playTotal += add
		if playAce < cancun and playTotal > 21:
			playAce += 1
			playTotal -= 10
		if playTotal>=21:
			
			break
	try:

		cpuTotal += int(hidden[0])

	except:
	
		if hidden[0] == "A":
			if cpuTotal + 11 < 21:
				add = 11
				skeletons += 1
			else:
				add = 1
		if hidden[0]== "K" or hidden[0] == "Q" or hidden[0] == "J":
			add = 10
		
		cpuTotal += add

	cpu.pop()
	cpu.append(hidden[0])

	cpuText = belly + hidden + "\n"	

	while True:
		if cpuTotal >=21:
			break
		elif cpuTotal >= playTotal and cpuTotal < 21:
			break
		elif playTotal > 21:
			break
		if member != "":
			await ctx.send(embed=discord.Embed(title=":hearts: :diamonds:blackjack:spades: :clubs:", description=f"**It is {member.name}'s turn**\n{ctx.author.name}'s Cards are:\n{playText}\nTotal: {playTotal}\n\nThe Dealers Cards are:\n{cpuText}\nTotal:{cpuTotal}\n\nType h to hit\nType s to stay"))
			def is_corrects(m):
				return m.author.id == member.id 
			guess = await client.wait_for("message", check =is_corrects)
			woo = guess.content.lower()

			while woo !="h" and woo != "s":
				
				guess = await client.wait_for("message", check =is_corrects)
				woo = guess.content.lower()
			
			if woo == "s":
				
				break

		randomCard = random.choice(cards)
		randomSuite = random.choice(suites)
		add = randomCard
		while randomSuite in suitesDict[randomCard]:

			randomSuite = random.choice(suites)
		suitesDict[randomCard]
		

		player.append(randomCard)
		if randomCard == "A":
			if cpuTotal + 11 < 21:
				skeletons +=1
				add = 11
			else:
				
				add = 1
		if randomCard == "K" or randomCard == "Q" or randomCard == "J":
			add = 10
		
		
		cpuText += f"{randomCard} {randomSuite}\n"
		cpuTotal += add
		if cpuAce < skeletons and cpuTotal > 21:
			cpuAce += 1
			cpuTotal -= 10



	if playTotal == cpuTotal:
		if member == "":
			stateEmbed = discord.Embed(title = "You both tied!",description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\nThe Dealer's Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
		else:
			stateEmbed = discord.Embed(title = "You both tied!",description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\n{member.name}'s Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
		
		await ctx.send(embed=stateEmbed)
		return
	if playTotal == 21 or cpuTotal > 21 or (playTotal > cpuTotal and playTotal < 21):
		if member == "":
			stateEmbed = discord.Embed(description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\nThe Dealers Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
			stateEmbed.set_author(name=f'{ctx.author.name} Won the blackjack game', icon_url = ctx.author.avatar_url)
			
		else:
			stateEmbed = discord.Embed(description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\n{member.name}'s Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
			stateEmbed.set_author(name=f'{ctx.author.name} Won the blackjack game', icon_url = ctx.author.avatar_url)
		await ctx.send(embed=stateEmbed)
		home[0] += 1
		away[1] +=1

	if cpuTotal == 21 or playTotal > 21 or (cpuTotal > playTotal and cpuTotal < 21):
		if member == "":
			stateEmbed = discord.Embed(description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\nThe Dealers Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
			stateEmbed.set_author(name=f'BarthiccBot Won the blackjack game', icon_url = "https://www.sohh.com/wp-content/uploads/2020/12/3b3baf71a0251cf5f7adce147c219ee5.jpg")
		else:
			stateEmbed = discord.Embed(description = f"Your Cards are:\n{playText}\nTotal: {playTotal}\n\n{member.name}'s Cards are:\n{cpuText}\nTotal:{cpuTotal}\n", color =random.choice(color))
			stateEmbed.set_author(name=f'{member.name} Won the blackjack game', icon_url = member.avatar_url)
		await ctx.send(embed=stateEmbed)
		home[1] += 1
		away[0] +=1
@client.command()
async def blackjack_standings(ctx):
	
	if not ctx.author.guild.id in blackjackStandings:
		
		await ctx.send(embed=discord.Embed(title = ":hearts: :diamonds:blackjack:spades: :clubs:", description = "Your server has not played rock paper scissors before"))
		return
	blackjack_pct = {}
	for i in blackjackStandings[ctx.author.guild.id]:
		
		win = blackjackStandings[ctx.author.guild.id][i][0]
		loss = blackjackStandings[ctx.author.guild.id][i][1]
		
		try:
			win_percentage = round((win/(win+loss))*100, 3)
			blackjack_pct[i] = win_percentage
		except:
			blackjack[i] = "-"
		
	standingsText = "> **NAME - WIN - LOSS - WIN %**\n\n"
	standings = sorted(blackjack_pct.items(), key = lambda x : x[1], reverse = True)
	
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			
			standingsText += f">  {rank}  **{standings[i+woo][0]} - ``{blackjackStandings[ctx.author.guild.id][standings[i+woo][0]][0]}`` - ``{blackjackStandings[ctx.author.guild.id][standings[i+woo][0]][1]}`` - ``{standings[i+woo][1]}``**\n\n"
	except:
		pass
	
	

	await ctx.send(embed=discord.Embed(title = f"Standings :trophy: For :trophy: {ctx.message.author.guild.name}", description = f"{standingsText}", color = random.choice(color)))

@client.event
async def on_member_join(member):
	
	if member.id == 770371351579852880:
		return
	
	try:
		await member.guild.text_channels[0].send(embed=discord.Embed(title = "Greeting :wave:", description = f"{random.choice(GreetingMessage[member.guild.id])}, {member.mention}! WELCOME TO {member.guild.name.upper()}!", color = random.choice(color)))

	except:
		try:
			await member.guild.text_channels[0].send(embed=discord.Embed(title = "Greeting :wave:", description = f"{random.choice(hell)}, {member.mention}! WELCOME TO {member.guild.name.upper()}!", color = random.choice(color)))
		except:

			await member.guild.text_channels[1].send(embed=discord.Embed(title = "Greeting :wave:", description = f"{random.choice(hell)}, {member.mention}! WELCOME TO {member.guild.name.upper()}!", color = random.choice(color)))

		
	
@client.command()
async def mute(ctx, member:discord.Member):
	if not ctx.message.author.guild_permissions.administrator:
		await ctx.send(embed = discord.Embed(title = "Mute :mute:", description = "YOU BUM! Only the administrator can use this command.", color = random.choice(color)))
		return
	if not ctx.author.guild.id in mutes:
		mutes[ctx.author.guild.id] = [member.id]
		
	mutes[ctx.author.guild.id].append(member.id)
	await ctx.send(embed = discord.Embed(title = "Mute :mute:", description = f"You have muted {member.name}", color = random.choice(color)))
@client.command()
async def unmute(ctx, member:discord.Member):
	
	if not ctx.message.author.guild_permissions.administrator:
		await ctx.send(embed = discord.Embed(title = "Mute :mute:", description = "YOU BUM! Only the administrator can use this command.", color = random.choice(color)))
		return
	try:
		mutes[ctx.author.guild.id].remove(member.id)
		await ctx.send(embed = discord.Embed(title = "Mute :mute:", description = f"You have unmuted {member.name}", color = random.choice(color)))
	except:
		await ctx.send(embed = discord.Embed(title = "Mute :mute:", description = f"The person has not been muted before", color = random.choice(color)))
	
@client.command()
async def antispam(ctx):
	if not ctx.message.author.guild_permissions.administrator:
		await ctx.send(embed = discord.Embed(title = "Anti-Spam", description = "YOU BUM! Only the administrator can use this command.", color = random.choice(color)))
		return
	if ctx.author.guild.id in antiSpam:
		antiSpam.remove(ctx.author.guild.id)
		await ctx.send(embed = discord.Embed(title = "Anti-Spam", description = "Server is not using anti spam any more", color = random.choice(color)))
	else:
		antiSpam.append(ctx.author.guild.id)
		await ctx.send(embed = discord.Embed(title = "Anti-Spam", description = "Bot is activating anti spam for server", color = random.choice(color)))

	
@client.command()
async def cartiText(ctx, *text):
	texts = []
	for i in text:
		texts.append(i)
	for i in range(len(texts)):
		if texts[i].lower() == "for":
			texts.pop(i)
			texts.insert(i, "4")
	textString =  " ".join(texts)
	textsString = []
	for i in textString:
		
		if str(i.lower()) == "e":
			textsString.append("3")
			continue
		if random.randint(0, 1) == 0:
			textsString.append(i.upper())
		else:
			textsString.append(i.lower())

		if random.randint(0, 7) == 0:
			textsString.append(">")

	for i in range(random.randint(1, 6)):
		textsString.append(":kiss: ")
	await ctx.send(embed=discord.Embed(title = "CaRTi t3Xt :vampire: :broken_heart:", description = "".join(textsString), color = random.choice(color)))


@client.command()
async def competition(ctx, days = 1):
	if not ctx.author.guild.id in league:
		league[ctx.author.guild.id] = {}

	if not ctx.author in league[ctx.author.guild.id]:
		league[ctx.author.guild.id][ctx.author] = {}
	else:
		await ctx.send(title="Leauge :trophy:", description = "you cant host more than 1 leagues ", color = random.choice(color))
	await ctx.send(embed=discord.Embed(title="Leauge :trophy:", description = f"competition set for {days} days", color = random.choice(color)))
	await asyncio.sleep(86400*days)
	standingsText = ""
	try:
		
		standings = sorted(league[ctx.author.guild.id][ctx.author].items(), key = lambda x : x[1], reverse = True)
	except:
		pass
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			if standings[i][0] == "BarthiccBot":
				woo+=1
			standingsText += f"> {rank} **{standings[i+woo][0].name} - {standings[i+woo][1]}**\n\n"
	except:
		pass

	
	await ctx.send(embed=discord.Embed(title=f"Leauge :trophy:\n The winner is f{standings[i+woo][0].name}", description = f"{ctx.author.mention}'s competition is over. \nStandings:\n{standingsText}", color = random.choice(color)))

@client.command()
async def competition_stats(ctx, host:discord.Member=""):
	if host == "":
		host = ctx.author
	try:
		standings = sorted(league[ctx.author.guild.id][host].items(), key = lambda x : x[1], reverse = True)
		
		
	except:
		
			
		
		await ctx.send(embed = discord.Embed(title="Leauge :trophy:", description = f"The person you were talking about isn't hosting any competitions", color = random.choice(color)))
		return
	standingsText = ""
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			if standings[i][0] == "BarthiccBot":
				woo+=1
			standingsText += f"> {rank} **{standings[i+woo][0].name} - {standings[i+woo][1]}**\n\n"
	except:
		pass
	await ctx.send(embed=discord.Embed(title="Leauge :trophy:", description = f"{host.mention}'s competition standings:\n{standingsText}", color = random.choice(color)))




	

@client.command()
async def greeting(ctx, *message):

	if not ctx.message.author.guild_permissions.administrator:
		await ctx.send(embed = discord.Embed(title = "Greeting :wave:", description = "YOU BUM! Only the administrator can use this command.", color = random.choice(color)))
		return
	GreetingMessag = " ".join(message)
	await ctx.send(embed = discord.Embed(title = "Greeting :wave:", description = f"Greeting changed to \"``{GreetingMessag}``\"", color = random.choice(color)))
	try:
		GreetingMessage[ctx.author.guild.id].append(GreetingMessag)
	except:
		GreetingMessage[ctx.author.guild.id]=[GreetingMessag]


@client.command()
async def farewell(ctx, *message):
	if not ctx.message.author.guild_permissions.administrator:
		await ctx.send(embed = discord.Embed(title = "Farewell :pensive:", description = "YOU BUM! Only the administrator can use this command.", color = random.choice(color)))
		return
	fareWellMessag = " ".join(message)
	await ctx.send(embed = discord.Embed(title = "Farewell :pensive:", description = f"Farewell changed to \"``{fareWellMessag}``\"", color = random.choice(color)))
	try:
		fareWellMessage[ctx.author.guild.id].append(fareWellMessag)
	except:
		fareWellMessage[ctx.author.guild.id]=[fareWellMessag]

@client.event
async def on_member_remove(member):
	if member.id == 770371351579852880:
		return

	try:
    			

		await member.guild.text_channels[0].send(embed=discord.Embed(title = "PERSON LEFT :pensive:", description = f"{random.choice(fareWellMessage[member.guild.id])}, {member.mention}! SEE YOU NEXT TIME AT {member.guild.name.upper()}!", color = random.choice(color)))
	except:
		await member.guild.text_channels[0].send(embed=discord.Embed(title = "PERSON LEFT :pensive:", description = f"{random.choice(by)}, {member.mention}! SEE YOU NEXT TIME AT {member.guild.name.upper()}!", color = random.choice(color)))
	for i in member.guild.channels:
		
		if i.name == "barthiccbot-welcome-or-goodbye":
			
			
			
			return
	channel = await member.guild.create_text_channel("BarthiccBot-Welcome-or-Goodbye".lower())
	
	
	await client.get_channel(channel.id).send(embed=discord.Embed(title = "PERSON LEFT :pensive:", description = f"{random.choice(by)}, {member.mention}! SEE YOU NEXT TIME AT {member.guild.name.upper()}!", color = random.choice(color)))
	try:
    			
		await client.get_channel(channel.id).send(embed=discord.Embed(title = "PERSON LEFT :pensive:", description = f"{random.choice(fareWellMessage[member.guild.id])}, {member.mention}! SEE YOU NEXT TIME AT {member.guild.name.upper()}!", color = random.choice(color)))
	except:
		await client.get_channel(channel.id).send(embed=discord.Embed(title = "PERSON LEFT :pensive:", description = f"{random.choice(by)}, {member.mention}! SEE YOU NEXT TIME AT {member.guild.name.upper()}!", color = random.choice(color)))
	


@client.command()
async def dick(ctx, member:discord.Member= " "):
	total=0
	if member == " ":
		member = ctx.author


	for i in str(member):
		try:
			total += alphabet[i]
		except:
			pass
	random.seed(total)
	measure = random.randint(0, 12)
	size = "8"
	for i in range(measure):
		size += "=="
	size += "D"
	await ctx.send(embed=discord.Embed(title="Dick Size :eggplant:", description=f"{member.mention}'s dick is {measure} inches long :flushed:\n ```{size}```", color=random.choice(color)))

@client.command()
async def love_calculator(ctx, *message):
	
	names = " ".join(message).split(",")
	name1, name2 = names[0].lower(), names[1].lower()

	
	try:
		seed = alphabet[name1[0]] + alphabet[name1[1]] + alphabet[name1[2]] + alphabet[name1[3]] + alphabet[name2[0]] + alphabet[name2[1]] + alphabet[name2[2]] + alphabet[name2[3]] 
	except:
		seed = alphabet[name1[0]] + alphabet[name2[0]]



	random.seed(seed)
	percentage = random.randint(0, 100)

	if percentage == 100:
		heart = ":sparkling_heart:"
	elif percentage > 90:
		heart = ":heart:"
	elif percentage > 80:
		heart = ":white_heart:"
	elif percentage > 70:
		heart = ":yellow_heart:"
	elif percentage > 60:
		heart = ":orange_heart:"
	elif percentage > 50:
		heart = ":green_heart:"
	elif percentage > 40:
		heart = ":blue_heart:"
	elif percentage > 30:
		heart = ":purple_heart:"
	elif percentage > 20:
		heart = ":brown_heart:"
	elif percentage > 10:
		heart = ":black_heart:"
	else:
		heart = ":broken_heart:"


	await ctx.send(embed = discord.Embed(title = f"__**{names[0]} {heart} {names[1]}**__", description=f"```css\n{percentage}%\n```", color = random.choice(color)))
repeatNum = 0
count = {}
chinese = {"零":"0", "一":"1", "二":"2", "三":"3", "四":"4", "五":"5", "六":"6", "七":"7", "八":"8", "九":"9", "十":"10", "百":"100", "千":"1000"}
hindi = {"०":"0", "१":"1", "२":"2", "३":"3", "४":"4", "५":"5", "६":"6", "७":"7", "८":"8", "९":"9"}
@client.command()
async def barthicc(ctx, *message):
	if ctx.author.id != 662136409301188630:
		return
	
	for z in client.guilds:

		for i in z.channels:
			
			if i.name == "barthiccbot-announcements":
				
				
					
					await client.get_channel(i.id).send(embed=discord.Embed(title = "ANNOUNCEMENT FROM BARTHICCBOT", description = " ".join(message), color = random.choice(color)))
					
					
					break
	
		try:
			channel = await z.create_text_channel("barthiccbot-announcements")
		except:
			
			for i in z.channels:
				try:
					await client.get_channel(i.id).send(embed=discord.Embed(title = "ANNOUNCEMENT FROM BARTHICCBOT", description = " ".join(message), color = random.choice(color)))
				except:
					continue
			continue
		try:
			await client.get_channel(channel.id).send(embed=discord.Embed(title = "ANNOUNCEMENT FROM BARTHICCBOT", description = " ".join(message), color = random.choice(color)))
		except:
			pass


number_channel = {}
@client.event
async def on_message(message):

	for i in respons:
		if i in message.content.lower():
			await message.channel.send(embed=discord.Embed(title = "Response :thinking_face:", description = respons[i]))
		
		
	
	
	
	pop = message.content.lower().split()
	if "am" in pop or "are" in pop or "is" in pop or "has"in pop or "have" in pop and not pop[1] in ["is", "where","who","what","why", "when"]:
		if random.randint(0, 3) == 0:
			await message.add_reaction("🧢")
	try:
		woo = message.author.guild.id
		woo = message.author.dm_channel.id
		await client.process_commands(message)
		
		return
	except:
		pass
	try:
		if message.author.id in mutes[message.author.guild.id]:
			try:
				await message.channel.purge(limit=1)
				return
			except:
				await message.channel.send(titile="Anti-Spam", description = "You have to give the bot permission to \"manage channels\" by asking your admin to go to 'server settings'>'roles'>'BarthiccBot'>'manage channels' and flipping the switch!")
			
	except:
		pass
	messageSplit = message.content.split(" ")

	for i in messageSplit:
		

		if "http" in i or ".com" in i or i.count(":") > 0 or "U0" in i or "!standings" in i:

			messageSplit.remove(i)
		
	


	exp = len( "".join(messageSplit))

	global repeatNum
	global repeat
	try:


		if message.author == repeat:
			
			repeatNum += 1
			
		else:
			repeatNum = 0
		
		if exp > 20:
			exp = 20
		if not message.author.guild.id in servers:

			servers[message.author.guild.id] = {message.author: exp}
			server_name[message.author.guild.id] = message.author.guild.name
			return
		else:
			if not message.author in servers[message.author.guild.id]:
				servers[message.author.guild.id][message.author] = exp
			

			else:
				if message.author == "BarthiccBot#6858" or message.author == "BarthiccBot #6858":
					return
				before = servers[message.author.guild.id][message.author]
				if repeatNum < 5:
					before = servers[message.author.guild.id][message.author]//500
					servers[message.author.guild.id][message.author] += exp
					after = servers[message.author.guild.id][message.author]//500

					if after > before:
						await message.channel.send(embed=discord.Embed(title=":arrow_up: **__Level Up__** :arrow_up:", description = f":partying_face: {message.author.mention} is now level {int(servers[message.author.guild.id][message.author] / 500)} :partying_face:", color = random.choice(color)))
				repeat = message.author
				
					
					
	except:
		pass
	try:	
		if message.author.guild.id in antiSpam:
			if repeatNum > 5:
				try:
					await message.channel.purge(limit=1)
					await asyncio.sleep(0.25)
				except:
					await message.channel.send(embed=discord.Embed(title="Anti-Spam", description = "You have to give the bot permission to \"manage channels\" by asking your admin to go to 'server settings'>'roles'>'BarthiccBot'>'manage channels' and flipping the switch!", color = random.choice(color)))
	except:
		pass
	
	try:


		if exp > 10:
			exp = 10
		if message.author.guild.id in league:
			for i in league[message.author.guild.id]:
				if message.author in league[message.author.guild.id][i]:
					league[message.author.guild.id][i][message.author] += exp
				else:
					league[message.author.guild.id][i][message.author] = exp
			
	except:
		pass
	
	
	await client.process_commands(message)

@client.command()
async def standings(ctx):
	standingsText = ""
	standings = sorted(servers[ctx.message.author.guild.id].items(), key = lambda x : x[1], reverse = True)
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			if standings[i][0] == "BarthiccBot":
				woo+=1
			standingsText += f"> {rank} **{standings[i+woo][0].name} - {standings[i+woo][1]}**\n\n"
	except:
		pass
	

	await ctx.send(embed=discord.Embed(title = f"Standings :trophy: For :trophy: {ctx.message.author.guild.name}", description = f"{standingsText}", color = random.choice(color)))


@client.command()
async def random_order(ctx, *message):
	optionsString = " ".join(message)
	options = optionsString.split(",")
	string = ""
	random.shuffle(options)
	for i in range(len(options)):
		string+= f"```{i+1}. {options[i]}``` \n"
	await ctx.send(embed=discord.Embed(title = "Random Order List :memo:", description = f"{string}", color = random.choice(color)))
@client.command()
async def teams(ctx, numOfTeams,  *message):
	try:
		team = int(numOfTeams)
	except:
		team = 2
	peoples = " ".join(message)
	people = peoples.split(",")
	random.shuffle(people)
	if len(people) % team == 0:
		string = "These are the teams\n"
		
		for i in range(team):
			string += f"``TEAM {i+1}``\n"
			
			for a in range(i+(len(people)//team)):
				string += f"```{a+1}. {people[0]}```\n"
				people.pop(0)


		await ctx.send(embed=discord.Embed(title = ":basketball: Teams :football:", description = f"{string}", color = random.choice(color)))
	else:
		await ctx.send(embed=discord.Embed(title = ":basketball: Teams :football:", description = f"The number of people have to be divisible by the amount of teams", color = random.choice(color)))



@client.command()
async def rank(ctx, member : discord.Member = ""):
	rank = ""
	if member == "":
		person = ctx.author
	else:
		person = member
	Full_string = f"{person.mention} stats are "
	numero = 0
	memberServers = 0
	memberTotalMessages = 0
	for i in servers:
		
		
		if ctx.author.guild.id == i:
			standings = sorted(servers[i].items(), key = lambda x : x[1], reverse = True)
			
			for b in range(len(standings)):
				if person.id == standings[b][0].id:
					rank = f"Your rank in the server is ``{b+1}``"

			if rank == "":
				rank = "You are unranked in the server"
			

			numero+=1
			memberServers += 1
			try:
				memberTotalMessages += servers[i][person]
			except:
				pass
			Full_string += f"\n**{numero}.** In {server_name[i]}, you have ``{servers[i][person]} XP``\nYou are on level ``{servers[i][person]//100}``\n{rank}\nYou have ``{((1+servers[i][person]//100)*100)-servers[i][person]}`` XP left before the next level\n\n"

	Full_string += f"You are in ``{memberServers} servers`` with BarthiccBot\nYou have ``{memberTotalMessages} messages in total``\n"
	astro = discord.Embed(description = f"{Full_string}", color = random.choice(color))
	astro.set_author(name=f'{person.name} Rank Card', icon_url = person.avatar_url)
	await ctx.send(embed=astro)
	


@client.command()
async def poll(ctx, *message):
	options = ""
	emojis = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔴", "🟡", "🟠", "🟢", "🔵", "🟣","🟤", "⚫", "⚪"]

	messa = " ".join(message)
	
	messaOptions = messa.split(";")
	if len(messaOptions) >2:
		for i in range(30):
			try:
				options += f"{emojis[i]} - {messaOptions[i+1]}\n"
			except:
				continue
	if messa[len(message)-1]!= "?":
		messa += "?"
	message = await ctx.send(embed = discord.Embed(title=f":chart_with_upwards_trend: __**{messaOptions[0]} :chart_with_downwards_trend: \n\n\n{options}**__", description = f"Poll made by {ctx.author.mention}", color = random.choice(color)))
	if len(messaOptions) > 2:
		for i in range(len(messaOptions)-1):
			await message.add_reaction(emojis[i])
	else:
		await message.add_reaction("\N{THUMBS UP SIGN}")
		await message.add_reaction("\N{THUMBS DOWN SIGN}")
	reactions = message.reactions


		
	await asyncio.sleep(600)
	

	await ctx.send(embed=discord.Embed(title = f":chart_with_upwards_trend: The \"__**{messaOptions[0]}**__\" poll is finished :chart_with_downwards_trend:", description = "", color = random.choice(color)))


		
	
@client.command(aliases = ["Goat", "GOAT"])
async def goat(ctx):
	goa = ["https://s.yimg.com/uu/api/res/1.2/8lG0WsC8MNGnhFYItiAC.A--~B/aD0yNDQ1O3c9MzYyMDtzbT0xO2FwcGlkPXl0YWNoeW9u/http://media.zenfs.com/en/homerun/feed_manager_auto_publish_494/390fd040375335a6104cc9de92da291f", "https://assets.dmagstatic.com/wp-content/uploads/2019/07/dirk-nowitzki-dallas-mavericks.jpg", "https://cdn.vox-cdn.com/thumbor/wVU_ZU20imFXLOSw4mn1SiK1jOI=/0x66:1877x1340/1400x933/filters:focal(740x298:1040x598):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/67007802/1203737491.jpg.0.jpg", "https://ichef.bbci.co.uk/news/1024/cpsprodpb/C271/production/_98677794_gettyimages-486869012.jpg", "https://thumbor.forbes.com/thumbor/fit-in/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5ec593cc431fb70007482137%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D1321%26cropX2%3D3300%26cropY1%3D114%26cropY2%3D2093", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Tom_Brady_2019.jpg/220px-Tom_Brady_2019.jpg", "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F200824175931-kobe-bryant-file.jpg", "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUQEBIVFRUXFRUVFRUVFRUPFRUVFRUWFhUVFRcYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGBAQGi8lHR4uLS0tLSstLS0tLS0wLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAAEDBQYCBwj/xAA+EAABAwIEAwUGAwgCAQUAAAABAAIDBBEFEiExBkFREyJhcYEUMpGhsdFC4fAHIzNSYnKSwYLxshdEVGOi/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAECAwQF/8QAKREAAgIBBAIBBAEFAAAAAAAAAAECEQMEEiExQVEiE0KRsTIFYXGB0f/aAAwDAQACEQMRAD8A82jRcQQsYRcYXfJGMWTNT3TBMuWSN0zu6QK4unas2UENCZwXTAujGkBBZSh43H/SToTsmEJSYJnbZAdHDTqP1qp2ULn2ym46DX49PVPT0Z2uBdWlEwtNgQGj3j1sNzbkspOujSKsUVDGwXlOUAdL+dwVSYnxF+CEENGw92/mouI8VBBy3yDbq49fJZCmc+Z+VunjqbDr4lZwg59lzmocIuKnEXSD94SNdNbWtfb4p6Wqs69iemn1PNcMpmsJF82pGY7nxTl9lqsaMnNjVL5DfKSB05eKYVjwL7u5dG2280xmuuHFVsRO9gk0rr5tSTe/r9VC3EZmEZSW+Fyd9UaV3Hhs0zJHxMLxHlz5bFwz5spDdyO6dgU9qFuZqODeM3tmyzatdo6w0PIPH9QFh4jyC9LkgbM0viex4I0vZ1idibj/ALXzj2rmOBB1Bv8ABbzhHiCSCofC51mknKTs1x1sf6SVx5sDi90Dpx5b4kXWJ4bLG9z8rmk63btp05W9Oao8epxaOQANLw4OaNBdpsHAcgb3t/pb9t6hpImIOt22uRbR19bH4bLL4zROv3zmABAduNOVuS0w53N89onJj29GMcwqMsKvJaHwXHsfgt7MSjMZTdkVdmi8EvYvBMCj7ErpsBV37F4LoUfgixUU7YVMyIq1FGu20itMlorWwlGQRIttKioqZVYAghSVoKdJKxmSjCJaoWBTtXVKRikdpildJc0pGyQgFKxqZoU8YWdlksbVM1iZgREYSA5EN12ymREYRAHok2FEEdLr0UHEMmVgiabOd7x5gb/rzR0sgYMx8/18h6rF4niuZxcdeZ8bbDyWMuWax4Q1bAJXZOTW8ja7joB6Ls4QKWMOcQXvBsLHujre/ny5KXhRufPLJo1p3PN35alR43W9rKSPdGjfILWDa4RE4qrfb/RXyOULnJ3lR2WhkSArkuTEpigBi9WXDuIthmHagmGQdnM0b5CQQ9v9THBrwd+74qsXJQBreJJMOlMjg+PtBqHR5wH2Fu9niY0k2BsLkXIGgFss2UukdIN3OJ+pCFljJ5o6gaAAb3sL2Phf7LOSLi7NxguKnMx7RcvBaR/9rBe3/Jvzur6YMmb2sYtm95h5OGn+vD5rBYNNbN4ODx5tJ1+F1uMPmbmcT7tiDyGuxPS+n+K4ZLZK0dS+SKyakA+xFiofZ1cVsVnb38fDkhixdidqznaplf7Ol7Oj8ibImIB9nSECNLEwYgAUQroQorInDE0xUDCJSsjUuVdAKrFQgxJdhOiwowQClakWJlu5GaR0UmrguTtcs2UgiMIqNCRuRUagoKYiGBDxhEsCQyeMIiNt1DG1Ex3UsZRcVVRawNGl7/TdYaqebWHhp48gtfxi3vAfitoOg5n6BYyndeUX1tr5lKK5HJ8F9BdkTYxsBc6k3cdz9ELK9dvc4/l91CYv1+a1RmyJ0ibOpo4i42aC49AMx+SnGEznaCY+Uch/0htLsEm+gAvTXVo3hurO1LL6xuH1XY4VrP8A4sn+KW+PseyXopyVwXK4fwzVjemk/wAVC/AKkf8At5fSNx+gRvj7DZL0yrzp2zWvqp5sPkb78cjf7mOb9Qgpo9LhN8onpl7hFQLWJ/AR9VomYqWxGQ5TmZ3gdL6gn5D5rBUs5uP1zVqasdk1jiOZtcgm+gsQLDn9lzThbN4z4N5hOICVuXmBp5aW+Vvgji1Y/geYl9h/VoddLfmtoQiCq0EueSEhNlU1lyQtCCLKmyqWyayAOMqVlJZKyAI7JLshcFMQ90lHdJMDOzU6DfGtBPCqyphVqRNFeWJ2sU2RSwxJ2KhoYkdFEnhjRTGKGykhRxohkaZjVO0KbKExinjsFyAoq0ns3kcmn6JMaMnxDNm7SXqcjL8hbV3lbVZWmZaRp5EG3irbiuqu7INrnT6IDB3A1ELTqGu280RdKwkrdG9wTg98rWvnd2bCLhosXkcr30b8/Raem4eo4tRC1xH4n/vT597QeisqZ1mi6DxGXN3QbeX5rgllnPtndHHGHgMhr4xYWAHhYBFirjPMFYXFYog0h8+TxBF/mswTld+4qn+FwWg+RSjiT8lPI14PYAW8ipmi6wWAYhOCGvOYdfutG7FPFQ406NFK+S4njG5VfUTMaLkhZrHuIXjSPUrE1dZPK/8AeSH+1gJK2x4r7M55a4R6LLisWuX1sqHHqCCdpd2bST+IDK4HzGqo6CJjNC91/wCV4LD6aXVhTza2vvotdtPgz3X/ACR55LGWPLf5T8dV1WvsR0ubeSveKcLcH9o0EtO56KhezN6BdEZXTOOcabRrOCJBnBaRqSHN5+7oR+uS3ZK86/Z1SyPqHGPUNYS8XsbciOuq3xk6oSSbFfCJi5ckqEyrkzJiJrpwh+1XYkQBMulEHroPRQWOQo3Bdl6ikkToVnJTKIyJJ0Fkk7FWVLFbTlV06lDZWFmqJijTZdUTE1USjuNqIaFwxqkClmiJGqQFQ3TZlNjoIzqKoeS1zWjUtIt4kbLlsnhdcul5AIsKPP8AGKB4cM2+5+ibCIrVTDbYj11/NbOuowf3j7WG97AEHcLP12HmCZpB7pNwdr5hop3faWo/ceqU5zMFuiqcVpXgXbuf1sj8HmzRg9QCr2nYCF5ztM76TPMX8PVRfdoyvyuLXPs51wNA1p0bc8zqlgWE1Mj5BOZGgB3v5i2/IZX+uy9QqKFsgsVVyYI3Nq5zvC5sto5XVGMsSbuyiwjCnjvEWtof0eS0NRh0eS9tUX2AY3K0KOrdZoCwtuR0JGFrsIc9z8pta9uvks5VcMPa8Frg+9s2YtGU89zp1uF6FC7vHoSpH0jCbloK64zaMJ40+zFS4E7ushkziwztN3tzDdw/l9FY0OCP5jb1Wwp6RgtYW8EbKxmXxRLJYowSMZxPStbSub5fULE4Tg7Xgh5sLi5tc78lueNZLQeZ/NUENbFTwRCT3pLutYmzeR+arG3tM8iTb/wWlNh0VMwGmtbm/wDET0J5jwUUtWSSTuu6LFYZL5HWuLEWIVfVNyuIGo5Fb4ndo5sioJNSufaEFdJoK2oyssGzKZj0FE0oqNpSoLCWvUgeoWMUzY06Cxy5QyuUxYopGJ0KwQuSScxJOgsJlkQshXDprqeho5J5BDE3M87NG/Uk9B4lZpFMFaEVGFo4+AKsNL5SxgGp1dI7/FgJKzzHNzmNjsxBIBDSM1ugOvxCpoETNC7DVfYHwy6oF2zRtI3YcwePNpA08UPj2HCjIbK83PunIWtd5OvY+STiy00VRYuCxaCmwKWWLtoSyRtr9xwLvLL18FUWBUOJVogjhvouiyznMtrYW6HyPVTHZd1tOxzA4hwcByuLrHInXBUWr5MZj9BVPzNkOWMcxd1x6aJS1jZqHLcmWnc2/MmPYE/AKrx6oe2TsmSP1/DuBfZAU0jqYmQkF5FrbjKdwR+K/ROMW1yNySZ6lwjVh8Qty0WrgmsFieDKYtiEg0DwH5P5L62HgtYxy48ypnZifCLH2hx0XQdbdCROK5qJljZuSyTa2XFUM2VvU/C6rcSxNlM3tJvuquo40py0FlnX8Ln16K4Rb6Jckuw2so3xWJ1F7XHI+PRExO01VEzjbt3Og7PQt1dlA1toRz0sNVbRyXaHeC2kmuyYOwl0hUbqg8yoHyLhIcmUnG4LoWBu5eB5XG6zkuSpk1LmtaxkbQ3UhjAG3IO9zcm211tsSIDWucL2eGjwJBJ+QKosSwRl+3idk72wNxfmR0C2xq1SOLLJKVhGC4JCwEtIdpufsg6s3cQDcAkA2t8ka+RhhsXEPBGw97qTZAtC6cONpWzkzZE3SOGsUkcakYxTxsW1GSY8cSJjiXUUaJjjSoqzhkSmbEpWxqZrE6AEdEoJGKxexDTMToCqcxJTObqnToVmAqccLvdafNz3H5CwUMeMzMuWPyEi3cAabeY1VebDZIKCj1DgH9qjqZhhrjJKzQxvBDpG9WnMRdvMa3GvK1rTGf2xQsLvYKUFzjd0koDLnrlZq7zJXjKdVuYHo0H7XMQLu8YQOQ7K4/8AK644n49rKqLsJmQiO4cSxpubbWzE29F56i6WtsMr9W/MJbmBbcPcU1FDOJaZ9h+Jju8xzejm3/6WrxDiWGqPtMbOylP8VrDeN/8AVY6td8V5vVNs7TY6griOQjUGyQ7NXimLHdrrkbjwXeG8R5gWSucTbu3J18FkXvvtp4JgU4umRkjvVFtWgmYvGhIu2+x9VTVUhc+79ATdabDagSsyuAJGipsXpwx5B9x+o/pcN/T7rXLhqO+PRz6fUOU3inw0ep8NttTxeMTT62t9ldxP5KiwGQeyxEagNaPS1laxS6Lw5uz348FgJFC+ZrTme4ADVRdqsfj+LAHe4v5jwWUYuTo0c6RYcT44JB2cbQ7+5ocL300KxdZiB/EBrcXsAR5eCnqazMB2bXa66A9fly+Cr3YbK46xP6jSwJ3uuzHDac83KXRYYS8g6PI6Ak2Ph8FtIMSaRY6W0vyva689dQ1MJ70ThY3F7W2/NFwYu9oDCCNTuNLaG3yHzTnBsIzcTfueuu0CpaOuztuPz1R9PJdZbS5TsB4lqrezxgXzSOdz0yttf/8ASGnfyUOKP7Wrbb3YWWP97je3naylcF6GmhUbPK1eT5UQkrtiWVTMYuho5VI6jCJjamiYio41JomdRhExhcxsRDGpGiO2BSAJNaurIGcOQdQjHoOoVCK9ySdyZMDzOSBoiDtMxef8QNvihToppp81tAANGtGzQhnArN14HFNLk6TpgldIodK6SZACKQKSSAGcnBSSQAVh9T2bweR3VzjNN2kRI3AzD03+SzpV/gdVmbkO7dvJdmmkpJ4peTz9ZBxazR7XZo/2fV4kg7F27dCPAq29sMbjG7kNPEcivPsOqjR1YOzHb+TtvgbhejVlK2ojBBsd2uG68LUY/p5Gn0z38GRZsSlHtCxDFAyMvsTy0+qyFEBUP300PL4WR0lU5hMMw12HQ+SsMMjhbrG0NPPYFJRUUPdb5CB2cLb29fv0QNTxDuQNNN1cOpWSe8dPA/X1WbxfAHNOaN/U2Ouo21Sxr2aSnL7Ql+L5xY2+yDxQNLM2Xb9XQVJgz2/xLDn5eCPktltbr1C32mTyya5BcAkJJLRp4/MfVX0dT3gwOaCdrkNHxKqon3AjiAFtzyH3KoOJa1rZewc0PAAJds8POtweXLRVGKcuTGcpKFo2r8Pe25y7kkkd65OpJIQ5CxmB8Xz0rrBxez+Vx5eBXpdJPBXxCSEBklr9A48wRyK9OKTXx/B42S4P5+fJTNREbUFSVkbJxDWO7FpuBLbMwOHJ3RaYYTEReKrhe3rct+6i0zVY5AETUZExPLSdna72O/tdmUsQUstI7a1TMakxqlaFJqh2tTEKUKN5QhkMiCnRcjkHO5WTYGUyZxSQFnlATlIJFZGhFmXQXDgpWhACSSumugB0yV0kAOkmSQA6lpZzG8PHr5KJJNNp2hSipKmXWOwiSISt5f8Aid/9K+4HxvMzsnnvN+nIrN4TVCxhfsbgeu4+yraaZ8EuZu7HEf3DYg+arWQWaKku3+zPQTlgk8b6X6Z61ilAyZuo15FZWSOWB2mo6eHgtBhGJtmja5puCPh1B8QpauFrxYjyXjRk4Ome1OCkrRSQ483ZzrHodCPinqcTa6wvzvuq3FqWxyvAI5FVjKQXXTFJnM3KPBcV2LttYH7/AK0UET5H6EFo8dHfDknpImt1AF+vNGwsJN1fSFTk+QmkaGNLjoGgk+Q1XnFdUmSR8h/E4n47Bbji2t7OmyN0Lzl/47u+3qvP1eFdyIzvqPoS0nBWKuhlygm3vDzG/wAQs2rDAf48f92vlYrrwyqaOHURUsUk/R6hxPTRygOIBbK3UdHgXBHQ2+iw+F8QVeFzH2eS7Da7HjOxw6EHb0stXiFYOyibzvp5WKxmM2eSPEq9RHbkdGWik5YVZ6X/AOqTpI2vjp4GnZ9xmF/LkjsP44ZO21XSMtsXxd17fEDmPVeJ00rozptzHIrTYTW2aD15LFtnWewS4W7IJ4T2sLhdr26kD+ockGCsxw1xRNSuIifZrtcru8wnmCP9hamTiulqGOM0PYygXzx95rndCEJkuPoYuUL3qCKqa8XabhcvkWiM26FI9CTvXUkiFmerUSNxE5yShLkk9ot5gq7C3M1b3m/MeY5+YVfdbksVNimD3u+MWdzHJ3l0K2zaOuYfg5NN/UE/jk/P/TP2SBS81yVwHqj3XJKRK4cUAdsXS5jXSAHSSSQA6SZOgBXTzyZnZjubX8Ta10xTJ34FSuyxwHEzTv1uY3e8On9Q8Vv4qjM0G9wRcOGxC8vVtguOOg7h70Z5c2+LfsubNh3crs68Gfb8ZdGurmhwIOqoXw5Sjva2S6xu0+BHmOS7ZTh26yj8TaS3coHpmXKs4WhDFvZqGorcrTbc7fdN8gqiUHGNRme0cmgj7rOo3FZ8z/LT1QbW32XVBVGjiyO5NiAV9w1TXlv/ACj5nQKtghtqVf4fKIYS8+8/UD6enNdOnSc7fS5OPVyaxuMe5cImxOrvKGjZo+appXXJKftCbuO53UYUZZ75uRphxfTgoeiN7LoqB9hZRBPmWZqWMdZpvtsrakxC+6y7SiIZiCgDVU9YWPy30KvaSqzsBvcjQ+YWF9qDrX+KvcFrmtGVx1cdDyKqDpmeRWi8kkQ0kieVyEkkXVHk4pSo6L0kOXpK9pG8jDly8pnhCyy2XpNnkRjfRU8QUg/it/5+PR3+lSly0s7wRY7HQ+RWVkblJaeRsvI1cEpbl5Pe0U24bX4Hc5J65ScdVynaTRhdLli6QA6SZOgBJ010gUwHXJXSZIB4yOamETTzQ5Cnik5WCYE0Acw3B+G6vcMxMHuv0PI7An/So4Gvc5rABdzg1tzlBLjYXJ0GpGpWzqeC42mWP26ISQNa6XtI3xRAutYCUmxvrYga2UvF9TpFRyuBT4jiAvYn4Koq624Njqriu4SqQGujj7ZjwS2SmPtLDltcXbfKdRoQFQzYa4EhzXi24c0i3919vVSsajwypZnIruzaNzdOHdBZF+yeXwKje23RaGY0IuQHHS+vlzRU9RndfkNAOgQeeyRmTt1RO1XYSSrah4cq5YjPFTvfGDbMBv1yjd3oqmggdKcoNvHde+wYrHQw0tJGBI60cRaHDM0ZRdxAHVVHG2TLLGLab6PA5GuaS1zSCNCCCCPMHZRuX0rV8PUr3ySywxuLw3PmaHXy3sddjruvPONeGMKjp31Ubyw7MbFIHh7z7rQ117eiX02XZ5ax2qkDlECkHKBkj5LLmGrOYWPMfJcuF1NgdNmqGNO17lAnwjeCS7QeoH0QkzkbM1AThdOOR5+REJkSUZSXVZzUwemxVsmgBDgLkHX4FQzy3TJKsGaWTHcisuCGLK1HoF7XkqXEv4hPWx+SdJYan+J1aZVP/RACk1JJcJ3E7SnukkgBZkrp0kAMXJsydJACzJZkkkwHDkg5JJAG0/ZvTQy1PbTgOEDe0YwgnPLcCJruWUE5j5DxWgxKOOJxfO50jjMZ3bHtJHCzM1wNG7NF7BJJVFO6vsFJK7V0QTz0zG1DB2uWN/avySOiElRLazLMynKLsF9hfwug+IOMnMkZAGuMlOzsyTI4xukt3s4dd0gb7up1skktZSlHhP2RSkYDtLC1yVE5xSSWBZwU4SSQBd8Pbu8vqfyXo/CtTTUsJxCocTeTsm2aXFh1uT1J6hJJdSk1hVf3OFQUtTJvwkbbAcaFYyV7dGZyxnIluUd4jlckrA8X8FCCIyNfnYDqHANc2+xB56pJJp1KvBU4qeLe+1bR5nOzK4t6G11G1JJcslUmjpxtuKb9EoKvsEow0h/4jt4BJJQy6NI83F1X1CSS2xnHkQE4p0kl0WYUf//Z", "data:image/jpeg;base64,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"]
	goatEmbed = discord.Embed(title="**__GOAT__** :goat:", color = random.choice(color))
	goatEmbed.set_image(url=random.choice(goa))
	await ctx.send(embed = goatEmbed)

@client.command(aliases = ["DOG", "Dog"])
async def dog(ctx):
	dog = ["https://www.inquirer.com/resizer/Yk6aD-ii4lVZF_bi65giGT51dTM=/1400x932/smart/arc-anglerfish-arc2-prod-pmn.s3.amazonaws.com/public/BAUPNVV5PFHSFAW6VBZ5PI5NXE.jpg", "https://www.sciencemag.org/sites/default/files/styles/inline__450w__no_aspect/public/dogs_1280p_0.jpg?itok=4t_1_fSJ", "https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bernese-mountain-dog-royalty-free-image-1581013857.jpg?crop=0.87845xw:1xh;center,top&resize=480:*", "https://previews.123rf.com/images/themorningstudio/themorningstudio1801/themorningstudio180100037/92716656-siberian-husky-dog-in-the-garden.jpg", "https://crhscountyline.com/wp-content/uploads/2020/03/Capture.png"]
	dogEmbed = discord.Embed(title="**__DOG__** :dog:", color = random.choice(color))
	dogEmbed.set_image(url = random.choice(dog))

	await ctx.send(embed = dogEmbed)

@client.command(aliases = ["Cat", "CAT", "pussy", "Pussy", "PUSSY"])
async def cat(ctx):
	ca = ["https://cdn.cnn.com/cnnnext/dam/assets/190517103414-01-grumpy-cat-file-restricted-super-tease.jpg", "https://media.tenor.com/images/cee5cce8e00502fa18deac66886438ca/tenor.png", "https://i.ytimg.com/vi/SkKYiZfP0Ss/hqdefault.jpg", "https://upload.wikimedia.org/wikipedia/commons/1/15/White_Persian_Cat.jpg",  "https://cache.desktopnexus.com/thumbseg/1270/1270926-bigthumbnail.jpg", "https://beta.ctvnews.ca/content/dam/ctvnews/images/2019/11/18/1_4691731.png?cache_timestamp=1574134871525"]
	catEmbed = discord.Embed(title="**__CAT__** :cat:", color = random.choice(color))
	catEmbed.set_image(url = random.choice(ca))
	
	await ctx.send(embed = catEmbed)
claimer = []
claim = []
waif =["https://cdn.discordapp.com/attachments/804758426731282442/805548225200521219/d46f4e171532ef5ea17a5a41fe94a661.png","https://qph.fs.quoracdn.net/main-qimg-1b2b48639a0af3f11c3964947ca99eb6", "https://thicc.mywaifulist.moe/waifus/2644/9990491ab8ff677202a435f64bbf37a5438780e14650244062c9356faea63be4_thumb.jpeg", "https://pbs.twimg.com/media/EfoABDaXgAA_WJg.jpg", "https://thicc.mywaifulist.moe/waifus/1192/89db9db0a26f5a3ea6cf6a077fc17c8d0f3ae979b92f068cb04a07ca2b221d0c_thumb.jpeg", "https://i.pinimg.com/originals/ee/59/5c/ee595c95b669d88b9c3c841dd5d02554.jpg", "https://thicc.mywaifulist.moe/waifus/344/56b6683a1aa73ca5f0ae7ce1ba3b18de3dffe059bcd530562fbd975a54b82dc1_thumb.png", "https://pm1.narvii.com/6872/10d1cafbd98699d21f987e56ee316e95b708bdf2r1-1000-1427v2_uhq.jpg", "https://cdn.discordapp.com/attachments/662390318703837234/780879320267751434/fd6e577311c306485a2791623ff20d3c.png", "https://cdn.discordapp.com/attachments/662390318703837234/780878494468276255/South.png", "https://cdn.discordapp.com/attachments/662390318703837234/780878064569548850/5bb41ab9844ad3e6932cf81dd39d414f_7c6b7ced4ea068ba5b8b3226c508af58.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877841729847306/f2tq37capn421.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877671776256061/dkKtV5d.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877407502204958/Saber.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877244326871060/tumblr_oy4x0wDFrq1smzgcuo1_400.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877114542260264/latest.png", "https://cdn.discordapp.com/attachments/662390318703837234/780877021630300160/original.png", "https://cdn.discordapp.com/attachments/662390318703837234/780876257570979840/239835.png", "https://cdn.discordapp.com/attachments/662390318703837234/780876111441559552/6a705cdefb63285ff29869d72919a6c2.png", "https://cdn.discordapp.com/attachments/774463189181267970/796894840582701107/image0.jpg", "https://cdn.discordapp.com/attachments/774463189181267970/796894840805654575/image1.jpg", "https://cdn.discordapp.com/attachments/774463189181267970/796894841144475698/image2.jpg", "https://cdn.discordapp.com/attachments/774463189181267970/796894841434931220/image3.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/796792028801138769/54ccb70cf3f3ca5482a5bd8fa0ca196a.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/796792050707857488/9516ab8ffd06d1f18dc641239734790d887a0533r1-640-360v2_uhq.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/796793520048439386/nodoka2.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/797153662585143387/tumblr_mzitcqigKO1r6eyjlo1_1280.png", "https://cdn.discordapp.com/attachments/796792011654955048/797154489466748958/Gasai_yuno_render_by_annaeditions24-d6ruhy7.png", "https://cdn.discordapp.com/attachments/796792011654955048/797155900178563112/803657-moe_12981_sample.jpg", "https://i.pinimg.com/736x/e1/7d/51/e17d519f087135925d9036ac9d12b857.jpg", "https://img.wattpad.com/8e9411e013bbfe7aff3794215a86985e16e01ada/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f36626239686f6e347259533233673d3d2d3731333537393934302e313539313035613734656633306266663231303438313630373539312e706e67?s=fit&w=720&h=720", "https://i.ytimg.com/vi/_NkxM_uLUpw/maxresdefault.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/798212352638058516/download_1.jpg", "https://i.pinimg.com/originals/93/dd/3a/93dd3a329974c21d4b1db888d481f330.png", "https://i.pinimg.com/originals/c9/37/c2/c937c2434c5f4a50f385b630fed837c3.png", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/a/ad/Mitsuri_colored_body.png/revision/latest?cb=20191116164005", "https://cdn.discordapp.com/attachments/796792011654955048/798320124590555176/maxresdefault_2.jpg", "https://cdn.discordapp.com/attachments/804760663079256094/804760993997520936/Screenshot_20210112-132650_Video_Player.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/805505701505007666/ovb5rbbklj651.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/804794777702105098/7l9pnz01ulv51.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/804479341949616148/urr1g6uharo41.jpg", "https://cdn.discordapp.com/attachments/796792011654955048/804479321938067476/sample-bec58a60df9db9b1e2a7fc207e0a17ca.jpg", "https://cdn.discordapp.com/attachments/805500452309434408/805500730554843216/image0.png", "https://cdn.discordapp.com/attachments/805500452309434408/805500649638854696/image0.jpg", "https://cdn.discordapp.com/attachments/805500452309434408/805500620483199017/image0.jpg", "https://cdn.discordapp.com/attachments/805500452309434408/805500585859350538/image0.webp", "https://cdn.discordapp.com/attachments/805500452309434408/805500563256115240/image1.jpg", "https://cdn.discordapp.com/attachments/805500452309434408/805500562984009758/image0.webp", "https://cdn.discordapp.com/attachments/804835963117240400/805539454067539968/1612118724200.png", "https://cdn.discordapp.com/attachments/804835963117240400/805512130479521792/ndRemqC.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805512130127986738/qbyQlgh.png", "https://cdn.discordapp.com/attachments/804835963117240400/805512129910013953/ddcczh7-70f51b7e-b1d0-479c-8c3b-3b5b42b85bd0.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805512129649573948/MW-05-Office-Nyarla.png", "https://cdn.discordapp.com/attachments/804835963117240400/805512129091207209/dc977lq-84755a5e-433b-45e4-a8d6-aeffa67eed8a.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805512127997542480/tumblr_phq2i5H3PO1qzmx5io1_1280.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805512127577194506/b7b85a5e75ed9ee7d81223199f066879.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805501040966500352/PCi3BOn.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805152069979602984/EMGhh7xUUAEXKLw.jpeg", "https://cdn.discordapp.com/attachments/804835963117240400/805149636843143238/rper0qituoq11.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805149636524244992/4zfKlvbUEXLY-iRvWIK-MAZR__yNcgC3NI10NxwYpZs.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/805149635974660117/Sword_Maiden_First_Appearence.png", "https://cdn.discordapp.com/attachments/804835963117240400/804846824972091392/dcnsdrg-350106fe-7086-4e37-abc6-9b191ef9e9dd.png", "https://cdn.discordapp.com/attachments/804835963117240400/804846824547942430/EZa9KlgXgAIYzjJ.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804846824761720872/cdd6a606da89253468c41514dace4eda.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804837708715262002/sample-65d52200b1023f72518be1ba9e71e569.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804836650676256768/vrnjfeshnjt41.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804836644217028708/k7jbrqwlqzh51.png", "https://cdn.discordapp.com/attachments/804835963117240400/804836637774315620/joel-joey-lacsa-lucoabikinismall2.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804836632174919681/403.jpg", "https://cdn.discordapp.com/attachments/804835963117240400/804836635740340244/dd14yws-efea4f7e-0b9e-4363-a51f-6897314e7b18.jpg"]
@client.command(aliases = [])
async def waifu(ctx):
	
	goatEmbed  = discord.Embed(title="**__WAIFU__** :woman:", description= "Type ``propose`` to ask for her hand in marriage", color = random.choice(color))
	gorl = random.choice(waif)
	goatEmbed.set_image(url= gorl)
	notClaimed = True
	await ctx.send(embed = goatEmbed)
	try:
		response = await client.wait_for("message", timeout = 5)
	except:
		await ctx.send(embed= discord.Embed(title="**__WAIFU__** :woman:", description= "RIP, you missed you chance. Better Luck Next Time!", color = random.choice(color)))
		return
	if response.content.lower() == "!waifu":
		return
	bruh = False
	
	while (response.author.name in claimer and response.content.lower() == "propose") or response.content.lower() != "propose" or response.author.guild.id != ctx.author.guild.id:
		if response.content.lower() == "!waifu":
			return
		
		if (response.author.name in claimer and response.content.lower() == "propose"):
			woah = discord.Embed(description = f"You are already married to ")
			woah.set_image(url=claim[claimer.index(response.author.name)])
			woah.set_author(name=f'Is {response.author.name} cheating?', icon_url = response.author.avatar_url)
			await ctx.send(embed=woah)
			bruh = True
		try:
			response = await client.wait_for("message", timeout=3)
		except:
			return
		

	woah = discord.Embed(description = f"You may kiss the bride\n\n{response.author.mention} is now married!")
	woah.set_image(url=gorl)
	woah.set_author(name=f'{response.author.name}\'s Wedding', icon_url = response.author.avatar_url)
	await ctx.send(embed=woah)
	claimer.append(response.author.name)
	claim.append(gorl)
@client.command(aliases = [])
async def add_waifu(ctx, link):
	
	if not (".png" in link or  ".jpg" in link or  ".jpeg" in link):
		await ctx.send(embed=discord.Embed(title="**__WAIFU__** :woman:", description = "That is not a picture, add a link to the picture"))
		return
	woo = discord.Embed(title = "**__WAIFU__** :woman:", description = "New waifu added")
	woo.set_image(url=link)
	waif.append(link)
	await ctx.send(embed = woo)

	
	
@client.command()
async def divorce(ctx):
	if not ctx.author.name in claimer:
		woah = discord.Embed(description = "You actually need to have a wife to get divorce :clown:")
		woah.set_author(name=f'{ctx.author.name}\'s Divorce', icon_url = ctx.author.avatar_url)
		await ctx.send(embed=woah)
		return
	claim.pop(claimer.index(ctx.author.name))
	claimer.remove(ctx.author.name)
	woah = discord.Embed(description = "You have successfully filed for divorce")
	woah.set_author(name=f'{ctx.author.name}\'s Divorce', icon_url = ctx.author.avatar_url)
	await ctx.send(embed=woah)
	
	

@client.command()
async def bot_settings(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Prefix Commands :computer:**__", description = f"\n> ```{prefix[1]}add_prefix [prefix] ```\n> ```{prefix[1]}delete_prefix [prefix] ```\n> ```{prefix[1]}default_prefix [prefix] ```\n> ```{prefix[1]}prefixes```\n", color = random.choice(color)))

@client.command()
async def games(ctx):
	await ctx.send(embed=discord.Embed(title = "__** :game_die: Fun :8ball: Games :coin: **__", description = f"\n> ```{prefix[1]}rps [member (optional)] ```\n> ```{prefix[1]}uno [member (optional)] ```\n> ```{prefix[1]}blackjack [member (optional)] ```", color = random.choice(color)))
@client.command()
async def stats(ctx):
	await ctx.send(embed=discord.Embed(title = ":chart_with_upwards_trend: STATS :chart_with_downwards_trend: ", description = f"\n> ```{prefix[1]}rps_standings```\n> ```{prefix[1]}standings```\n> ```{prefix[1]}blackjack_standings```\n> ```{prefix[1]}rank [member (Optional)] ```", color = random.choice(color)))
@client.command()
async def utilities(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Utilities**__", description = f"\n> ```{prefix[1]}avatar [member (optional)] ```\n> ```{prefix[1]}8ball [Your question] ```\n> ```{prefix[1]}roll```\n> ```{prefix[1]}flip```\n> ```{prefix[1]}dm [member] [message] ```\n> ```{prefix[1]}poll [question] ```\n> ```{prefix[1]}poll [question] [options seperated by semicolons] ```\n> ```{prefix[1]}goat```\n> ```{prefix[1]}cat```\n> ```{prefix[1]}dog```", color = random.choice(color)))

@client.command()
async def chat(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Chat :wave:**__", description = f"\n> ```{prefix[1]}wassup```\n> ```{prefix[1]}hi```\n> ```{prefix[1]}owo```\n> ```{prefix[1]}pain```\n>  ```{prefix[1]}bye```\n>  ```{prefix[1]}response [trigger word] [response] ```\n", color = random.choice(color)))

@client.command()
async def time_commands(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Time :clock:**__", description = f"\n>  ```{prefix[1]}timer [hours] [minutes] [second] ```\n>  ```{prefix[1]}stopwatch```\n>  ```{prefix[1]}stop_stopwatch```", color = random.choice(color)))

@client.command()
async def love(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Love :heart:**__", description = f"\n>  ```{prefix[1]}waifu```\n>  ```{prefix[1]}waifu_stats [member (Optional)] ```\n>  ```{prefix[1]}dick [member (Optional)] ```\n>  ```{prefix[1]}love_calculator [names seperated by commas] ```", color = random.choice(color)))
@client.command()
async def descision(ctx):
	await ctx.send(embed=discord.Embed(title = "__**Choose :thinking_face: **__", description = f"\n>  ```{prefix[1]}choose [Options] ```\n>  ```{prefix[1]}random_order [Options] ```\n>  ```{prefix[1]}teams [number of teams] [players seperated by commas] ```", color = random.choice(color)))
@client.command()
async def admin_commands(ctx):
		
		await ctx.send(embed=discord.Embed(title = "__**Administrator Commands**__", description = f"\n > ```{prefix[1]}greeting [message]``` \n> ```{prefix[1]}farewell [message]``` \n> ```{prefix[1]}kick [member ping] [reason] ```\n> ```{prefix[1]}mute [member] ```\n> ```{prefix[1]}unmute [member] ```\n> ```{prefix[1]}antispam ```", color = random.choice(color)))
	
@client.command()
async def help(ctx):
	menu = f"__**Table of Contents of help menu**__\n> :ballot_box: VOTE FOR MY BOT [HERE](https://top.gg/bot/770371351579852880)\n> :email: [Invitation Link](https://discord.com/api/oauth2/authorize?client_id=770371351579852880&permissions=137526352&scope=bot)\n > :computer: [BarthiccBot Support Server](https://discord.gg/ePhUPNJaVN)\n\nAlways on Bot Commands:\n> ```Counting```\n> ```Cap```\n> ```{prefix[1]}bot_settings```\n> ```{prefix[1]}games```\n> ```{prefix[1]}chat```\n> ```{prefix[1]}time_commands```\n> ```{prefix[1]}descision ```\n> ```{prefix[1]}stats```\n> ```{prefix[1]}utilities```\n> ```{prefix[1]}stats```"


	
	
	menu += f"\n> ```{prefix[1]}admin_commands```"

	helpEmbed = discord.Embed(title="Welcome to BarthiccBot!\n This is the help manual :sunglasses:", description = menu)
	helpEmbed.color = random.choice(color)
	helpEmbed.set_image(url="https://media.tenor.com/images/6aaf1a81c0346f798ac3ceac7e8442dd/tenor.png")
	try:
		await ctx.send(embed = helpEmbed)
	except:
		await ctx.send(embed = discord.Embed(title = f"{ctx.author.mention}\n{helpEmbed}"))

@client.command()
async def prefixes(ctx):
	string = ""
	for i in prefix:
		string += i + ", "

	prefEmbed = discord.Embed(title = ':exclamation: Existing Prefixes :exclamation:', description = f"***These are your current prefixes that you can use***\n```{string}```")
	prefEmbed.color = random.choice(color)
	await ctx.send(embed=prefEmbed)
@client.command()
async def default_prefix(ctx, pref):
	prefix[1] = pref
	prefix[0] = pref + "8"
	defEmbed = discord.Embed(title = "Prefix Change", description=f"> **New prefix added:**\n> ```{pref}```")
	defEmbed.color = random.choice(color)
	await ctx.send(embed=defEmbed)


@client.command()
async def avatar(ctx, member: discord.Member=""):
	if member =="":
		what = ctx.author
	else:
		what = member
	ayo = discord.Embed(description = f"{what.mention}\'s Avatar")

	ayo.set_image(url=what.avatar_url)
	ayo.color = random.choice(color)
	await ctx.send(embed=ayo)

@client.command()
async def add_prefix(ctx, pref):
	prefix.append(pref)
	addEmbed = discord.Embed(title = "Prefix Change", description=f"> **New prefix added:**\n> ```{pref}```")
	addEmbed.color = random.choice(color)
	await ctx.send(embed=addEmbed)
@client.command()
async def delete_prefix(ctx, pref):
	if ("8" in pref and pref != "8") or pref != prefix[1]:
		prefix.remove(pref)
		delEmbed = discord.Embed(title = "Prefix Change", description=f"> **New prefix deleted:**\n> ```{pref}```")
		delEmbed.color = random.choice(color)
		await ctx.send(embed=delEmbed)
		
@client.command()
async def ball(ctx, *place):
	lowerPlace = [each_string.lower() for each_string in place]

	jo = " ".join(place)
	
	
	if lowerPlace[0] == "how":	
		if lowerPlace[1] == "many":
			if "money" in lowerPlace or "dollars" in lowerPlace:
				descrip = f"> Q: __{jo}__\n> **A: ${random.randint(0, 10000)} :sunglasses: **"
			else:
				descrip = f"> Q: __{jo}__\n> **A: {random.randint(0, 10000)}**"

		elif lowerPlace[1] == "much":
			descrip = f"> Q: __{jo}__\n> **A: {random.choice(much)}**"
		elif lowerPlace[1] == "old":
			descrip = f"> Q: __{jo}__\n> **A: {random.randint(18,100)}**"
	elif "test" in lowerPlace[len(lowerPlace)-1] or "test" in lowerPlace[len(lowerPlace)-1]:
		
	
			descrip = f"> Q: __{jo}__\n> A: **{random.randint(50, 100)}**"

	elif "sat" in lowerPlace:
		if "math" in lowerPlace or "reading" in lowerPlace:
			descrip = f"> Q: __{jo}__\n> **A: {random.randint(20, 80)*10}**"
		else:

			descrip = f"> Q: __{jo}__\n> A: **{random.randint(40, 160) * 10}**"

	elif "act" in lowerPlace:
		descrip = f"> Q: __{jo}__\n> A: **{random.randint(1, 36)}**"
	elif place[0] == "will" or "love" in place:
		descrip = f"> Q: __{jo}__\n> A: **{random.choice(will)}**"
	
	else:
		descrip = f"> Q: __{jo}__\n> A: **{random.choice(replies)}**"
	
	emb = discord.Embed(title = "8 Ball", description = f"{ctx.author.mention}\n {descrip}")
	emb.color = random.choice(color)
	await ctx.send(embed = emb)
	
@client.command()
async def roll(ctx, max:int = 6):
	diceEmbed = discord.Embed(title = "Dice Roll",description=f"> **{ctx.author.mention} rolled a** __{random.randint(1, max)}__")
	diceEmbed.color = random.choice(color)
	await ctx.send(embed = diceEmbed)


@client.command()
async def kick(ctx, member:discord.Member, *reasons):
	if ctx.message.author.guild_permissions.administrator:

		if member.guild_permissions.administrator:
			await ctx.send(embed = discord.Embed(title = "Kick :hiking_boot:", description = "You cannot kick an administrator"))
		else:
			reason = " ".join(reasons)
			await ctx.send(embed = discord.Embed(title = "Kicked :hiking_boot:", description = f"{member.mention} was kicked because:\n \"{reason}\"", color = random.choice(color)))

			await member.send(embed = discord.Embed(title = "Kicked :hiking_boot:", description = f"You were kicked because:\n \"{reason}\"", color = random.choice(color)))
			await member.kick()

	else:
		await ctx.send(embed = discord.Embed(title = "Kick :hiking_boot:", description = "YOU BUM! Only a administrator could kick people"))




@client.command()
async def flip(ctx):
	
		if random.randint(0, 1) == 1:
			result = "Heads "
		else:
			result = "Tails "
		headEnbed = discord.Embed(title = "Coin Flip", description=f">  __{ctx.author.mention} flipped a__ **{result}** ")
		headEnbed.color = random.choice(color)
		await ctx.send(embed=headEnbed)

@client.command(aliases = ["Wassup", "WASSUP"])
async def wassup(ctx):
	wassupEmbed = discord.Embed(description = f"{random.choice(hell)} {ctx.author.mention}")
	wassupEmbed.color = random.choice(color)
	await ctx.send(embed = wassupEmbed)

@client.command(aliases = ["Hi", "HI", "Hello", "hello", "HELLO"])
async def hi(ctx):
	helloEmbed = discord.Embed(description = f"{random.choice(hell)} {ctx.author.mention} :wave:")
	helloEmbed.color = random.choice(color)
	await ctx.send(embed = helloEmbed)

@client.command(aliases=["OWO", "Owo", "OwO"])
async def owo(ctx):
	helloEmbed = discord.Embed(description = f"{ctx.author.mention} What's This :flushed:")
	helloEmbed.color = random.choice(color)
	await ctx.send(embed = helloEmbed)

@client.command()
async def pain(ctx):
	helloEmbed = discord.Embed(description = f"{ctx.author.mention} Know Pain")
	helloEmbed.color = random.choice(color)
	await ctx.send(embed = helloEmbed)

@client.command(aliases=["Bye", "BYE"])
async def bye(ctx):
	helloEmbed = discord.Embed(description = f"{by} {ctx.author.mention} :wave:")
	helloEmbed.color = random.choice(color)
	await ctx.send(embed = helloEmbed)
@client.command()
async def waifu_stats(ctx, member:discord.Member=""):
	if member == "":
		wide = str(ctx.author.id)
	else:
		wide = str(member.id)
	uzi = ""
	
	
	category = ["Loving :heart:", "Personality :blue_heart:", "Attractiveness :orange_heart:", "Horny :green_heart:", "Loyalty :white_heart:", "Popularity :purple_heart:" ]
	woo = []
	avg = 0
	for i in range(0, 12, 2):
		
		widNum = wide[int(i): int(i+2)]
		random.seed(widNum)
		rating = random.randint(0, 10)
		woo.append(rating)
		avg += rating
	for i in range(len(woo)):
		uzi+= f"{category[i]}: {woo[i]}/10\n"

	uzi += f"Average Rating: {avg//6}/10"
	stateEmbed = discord.Embed(description = uzi, color =random.choice(color))
	
	await ctx.send(embed=stateEmbed)

		
	

rpstandings = {}

@client.command()

async def rps(ctx, member:discord.Member=""):
	choices = ['rock', 'paper', 'scissors']
	if not ctx.author.guild.id in rpstandings:
		rpstandings[ctx.author.guild.id] = {"BarthiccBot":[0, 0]}
	if not ctx.author.name in rpstandings[ctx.author.guild.id]:
		rpstandings[ctx.author.guild.id][ctx.author.name] = [0, 0]	
	if not member == "":
		if member.name == ctx.author.name:
			await ctx.send(embed=discord.Embed(title="Rock, Paper, Scissors", description=f"https://tenor.com/view/idiot-congratulations-you-played-your-self-gif-10536951"))
			
			return
		
			
		if not member.name in rpstandings[ctx.author.guild.id]:
			rpstandings[ctx.author.guild.id][member.name] = [0, 0]
			
		

		await ctx.send(embed=discord.Embed(title="Rock, paper, scissors", description=f"Hello, {member.mention}.\n {ctx.author.mention} challenges you to a rock paper scissors battle\n you have about 15 second to reply to this text to accept the challenge"))
		def is_correct(m):
			return m.author.id != 770371351579852880 and m.channel.id == ctx.message.channel.id
		try:
			guess = await client.wait_for('message', check=is_correct, timeout=15)
		except:
			await ctx.send(embed=discord.Embed(title="Rock, paper, scissors", description=f"I guess you do not accept the challenge that {ctx.author.mention} gave you"))
			return
		i = 0
		while guess.author.id != member.id and i < 5:
			i+=1
			guess = await client.wait_for('message', check=is_correct, timeout=15)
		if i >= 5:
			await ctx.send(embed=discord.Embed(title="Rock, paper, scissors", description=f"I guess you do not accept the challenge that {ctx.author.mention} gave you"))
			return
			
		
		await member.send(embed=discord.Embed(title="Rock, paper, scissors", description="What is your weapon:\nrock :rock:\npaper :newspaper:\nscissors :scissors:"))
		gues = ""
		def is_correct(m):
			
			
			return m.author.id != 770371351579852880 and m.author.id == member.id and m.channel.id == member.dm_channel.id
		
		
		gues = await client.wait_for('message', check=is_correct, timeout=100)
		while gues=="":

			gues = await client.wait_for('message', check=is_correct, timeout=100)
		
			
		
		

		while not gues.content.lower() in choices:
			
			await member.send(embed=discord.Embed(title="Rock, paper, scissors", description="That is not a valid weapon\nWhat is your weapon:\nrock :rock:\npaper :newspaper:\nscissors :scissors:"))
			gues = await client.wait_for('message', check=is_correct, timeout=1000000)
		
		away = gues.content
		await ctx.send(embed = discord.Embed(title = "Rock Paper Scissors", description = f"{member.mention} chose his weapon"))
		
		try:

			await ctx.author.send(embed=discord.Embed(title="Rock, paper, scissors", description="What is your weapon:\nrock :rock:\npaper :newspaper:\nscissors :scissors:"))
			def is_corrects(m):
				try:
					return m.author.id != 770371351579852880 and m.author.id ==ctx.author.id and m.channel.id == ctx.author.dm_channel.id
				except:

					pass
			
			guess = await client.wait_for('message', check=is_corrects, timeout=10000000)
		except:
			
			await ctx.author.send(embed=discord.Embed(title="Rock, paper, scissors", description=f"{member.mention} Could you please turn on permissions that can let the bot dm you, so that we could keep your choices private? "))
		while not guess.content.lower() in choices:
			await ctx.author.send(embed=discord.Embed(title="Rock, paper, scissors", description="That is not valid weapon\nWhat is your weapon:\nrock :rock:\npaper :newspaper:\nscissors :scissors:"))
			
			guess = await client.wait_for('message', check=is_correct, timeout=100000000) 

		rockEmbed = discord.Embed()
		home = guess.content
		
		if away.lower() == home.lower():
			rockEmbed.title = 'It is a tie'
			rockEmbed.description = f"{ctx.author.mention} - {member.mention}\n**{home} - {away}**"
		elif (away.lower() == "scissors" and home.lower() =="rock") or (away.lower() == "paper" and home.lower() =="scissors") or (away.lower() == "rock" and home.lower() =="paper"):
			rockEmbed.set_author(name=f'{ctx.author.name} won', icon_url = ctx.author.avatar_url)
			rockEmbed.description = f"{ctx.author.mention} - {member.mention}\n**{home} - {away}**"
			rpstandings[ctx.author.guild.id][ctx.author.name][0] += 1
			rpstandings[ctx.author.guild.id][member.name][1] += 1
		elif (home.lower() == "scissors" and away.lower() =="rock") or (home.lower() == "paper" and away.lower() =="scissors") or (home.lower() == "rock" and away.lower() =="paper"):
			rockEmbed.set_author(name=f'{member.name} won', icon_url = member.avatar_url)
			rockEmbed.description = f"{ctx.author.mention} - {member.mention}\n**{home} - {away}**"
			rpstandings[ctx.author.guild.id][ctx.author.name][1] += 1
			rpstandings[ctx.author.guild.id][member.name][0] += 1
		
		await ctx.send(embed=rockEmbed)
		return


	win = 0
	loss = 0
	
	await ctx.send(embed=discord.Embed(title="Rock, paper, scissors", description="What is your weapon:\nrock :rock:\npaper :newspaper:\nscissors :scissors:"))
	def is_correct(m):
		return m.author.id != 770371351579852880 and m.author.id == ctx.author.id
	guess = await client.wait_for('message', check=is_correct, timeout=100000000)
	weapon = guess.content
	
	if not weapon in choices:
		gamesEmbed = discord.Embed(title = f"***{prefix[1]}battle <weapon> <games>***", description = "__**The weapon has to be either rock, paper, or scissors.**__")
		gamesEmbed.color = random.choice(color)
		await ctx.send(embed=gamesEmbed)
		return
	
	

	
	if weapon.lower() in choices:
		opponent = random.choice(choices)
		rockEmbed = discord.Embed()
		if weapon.lower() == 'rock':
			if opponent.lower() == 'rock':
				rockEmbed.title = 'It is a tie'
				rockEmbed.description = f"**{weapon} - {opponent}**"
			elif opponent.lower() == 'scissors':
				rockEmbed.title = 'You Win!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
				rpstandings[ctx.author.guild.id]["BarthiccBot"][1] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][0] +=1
				
			else:
				rockEmbed.title = 'You Lost!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
				rpstandings[ctx.author.guild.id]["BarthiccBot"][0] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][1] +=1
		elif weapon.lower() == 'scissors':
			if opponent.lower() == 'scissors':
				rockEmbed.title = 'It is a tie!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
			elif opponent.lower() == 'paper' :
				rockEmbed.title = 'You Win!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
				rpstandings[ctx.author.guild.id]["BarthiccBot"][1] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][0] +=1
				
			else:
				rockEmbed.title = 'You Loss!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
				rpstandings[ctx.author.guild.id]["BarthiccBot"][0] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][1] +=1
		elif weapon.lower() == 'paper':
			if opponent.lower() == 'paper' :
				rockEmbed.title = 'It is a tie!'
				rockEmbed.description = f"**{weapon} - {opponent}**"
			elif opponent == 'rock':
				rockEmbed.title ='You Won!'
				
				rockEmbed.description = f"**{weapon} - {opponent}**"
				win+=1
				rpstandings[ctx.author.guild.id]["BarthiccBot"][1] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][0] +=1
			else:
				rockEmbed.title = 'You Loss!'
				loss+=1
				rockEmbed.description = f"**{weapon} - {opponent}**"
				rpstandings[ctx.author.guild.id]["BarthiccBot"][0] +=1
				rpstandings[ctx.author.guild.id][ctx.author.name][1] +=1
		
		await ctx.send(embed=rockEmbed)

@client.command()
async def rps_standings(ctx):
	
	if not ctx.author.guild.id in rpstandings:
		await ctx.send(embed=discord.Embed(title = "Rock Paper Scissors Standings", description = "Your server has not played rock paper scissors before"))
		return
	rps_pct = {}
	for i in rpstandings[ctx.author.guild.id]:
		
		win = rpstandings[ctx.author.guild.id][i][0]
		loss = rpstandings[ctx.author.guild.id][i][1]
		
		win_percentage = round((win/(win+loss))*100, 3)
		rps_pct[i] = win_percentage
	
	standingsText = "> **NAME - WIN - LOSS - WIN %**\n\n"
	standings = sorted(rps_pct.items(), key = lambda x : x[1], reverse = True)
	
	woo = 0 
	try:
		for i in range(10):
			
			if i == 0:
				rank = ":first_place:"
			elif i == 1:
				rank = ":second_place:"
			elif i == 2:
				rank = ":third_place:"
			else:
				rank = f"``{i+1}.``"
			
			standingsText += f">  {rank}  **{standings[i+woo][0]} - ``{rpstandings[ctx.author.guild.id][standings[i+woo][0]][0]}`` - ``{rpstandings[ctx.author.guild.id][standings[i+woo][0]][1]}`` - ``{standings[i+woo][1]}``**\n\n"
	except:
		pass
	
	

	await ctx.send(embed=discord.Embed(title = f"Standings :trophy: For :trophy: {ctx.message.author.guild.name}", description = f"{standingsText}", color = random.choice(color)))



		
@client.command()
async def dm(ctx, person:discord.Member, *message):
	
	messa = " ".join(message)
	lowerMessa = messa.lower()
	for i in forbidden_words:
		if i in lowerMessa:
			await ctx.send(embed = discord.Embed(description = f"***You cannot send that*** :rage:"))
			return
	dm = discord.Embed(title= "NEW DM",description= f"__**{ctx.author} sent:**__\n> {messa}")
	dm.color = random.choice(color)
	try:	
		await person.send(embed = dm )
	except:
		await ctx.send(title="**__DM__**", description = f"{person.mention} blocked the bot, so you can't send dms to him :pensive:", color = random.choice(color))



	await ctx.send(embed=discord.Embed(description = f"{ctx.author.mention}'s message to {person.mention} sent", color = random.choice(color)))

	time.sleep(2)
tim = 0
timeCreator = ""
@client.command()
async def timer(ctx, hours:int, minutes:int, second:int):
	

	if hours < 10 and minutes < 120 and  second < 200:
		tim = second + minutes * 60 + hours *3600
		timeCreator = ctx.author
		

	await ctx.send(embed=discord.Embed(title = "**__Timer__** :timer:", color = random.choice(color), description = f"{timeCreator.mention} set a timer for {hours} hours, {minutes} minutes, and {second} seconds"))
	await asyncio.sleep(tim)
	await ctx.send(embed=discord.Embed(title = "**__Timer__** :timer:", color = random.choice(color), description = f"{timeCreator.mention}'s timer is done"))
	
@client.command()
async def stopwatch(ctx):
	people[ctx.author] = time.time()
	await ctx.send(embed=discord.Embed(title="**__Stopwatch__** :stopwatch:", description = f"{ctx.author.mention}'s stopwatch is started", color=random.choice(color)))

@client.command()
async def stop_stopwatch(ctx):
	try:
		timeElapsed = time.time() - people[ctx.author]
	except:
		await ctx.send(embed=discord.Embed(title="**__Stopwatch__** :stopwatch:", description = "You have to start a stopwatch to stop it", color = random.choice(color)))
		return
	await ctx.send(embed=discord.Embed(title="**__Stopwatch__** :stopwatch:", description = f"{ctx.author.mention} took ***{round(timeElapsed, 1)} ***", color = random.choice(color)))

@client.command()
async def response(ctx, word, *messag):
	woo = " ".join(messag)
	await ctx.send(embed=discord.Embed(title="Response", description= f"New response created\nTrigger Word: ``{word}``\nResponse: ``{woo}``"))
	
	respons[word] = woo


@client.command()
async def choose(ctx, *messages):
	if messages == [] or messages == [" "]:
		await ctx.send(embed = discord.embed(title = "Choose :thinking_face:", description = "You have to write something first", color = random.choice(color)))
		return
	ctxString = "BarthiccBot chooses..."
	starting = 0
	times = 1
	
	stringMessages = " ".join(messages)

	SplittedList = stringMessages.split(",")

	for i in range(len(SplittedList)):

		if "or" in SplittedList[i]:
			orList = SplittedList[i].split("or")
			
			SplittedList.pop(i)
			for a in orList:
				SplittedList.append(a)
	for i in range(starting, times):
		randChoice = random.choice(SplittedList)
		while randChoice == "" or randChoice == " ":
			randChoice = random.choice(SplittedList)
		ctxString += f"\n```{i+1}. {randChoice}```\n"

	await ctx.send(embed=discord.Embed(title = "Choose :thinking_face:", description = f"{ctxString}", color = random.choice(color)))

import csv

@client.event
async def on_ready():
	global servers
	global blackjackStandings
	global rpstandings
	print(len(client.guilds))

	await client.change_presence( activity=discord.Game(name=f"{len(client.guilds)} servers 😈\n PLEASE VOTE FOR MY BOT: https://top.gg/bot/770371351579852880\n (type !help to see the help menu)"))
	while True:
		with open('standings.csv') as csv_file:
			for x in csv.reader(csv_file,delimiter=','):
				row = {}
				for i in range(1, len(x), 2):
					row[x[i]] = x[i+1]
				servers[x[0]] = row
		with open('rps.csv') as csv_file:
			for x in csv.reader(csv_file,delimiter=','):
				row = {}
				for i in range(1, len(x), 2):
					row[x[i]] = [x[i+1],x[i+2]]
				rpstandings[x[0]] = row
		with open('blackjack.csv') as csv_file:
			for x in csv.reader(csv_file,delimiter=','):
				row = {}
				for i in range(1, len(x), 2):
					row[x[i]] = [x[i+1],x[i+2]]
				blackjackStandings[x[0]] = row
		await asyncio.sleep(86300)
		with open('standings.csv', mode='w') as standings:
			employee_writer = csv.writer(standings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			
			for i in servers:
				wok = [str(i)]
				for x in servers[i]:
					wok.append(x)
					wok.append(servers[i][x])

				employee_writer.writerow(wok)
		with open('rps.csv', mode='w') as standings:
			employee_writer = csv.writer(standings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			
			for i in rpstandings:
				wok = [str(i)]
				for x in rpstandings[i]:
					wok.append(x)
					wok.append(rpstandings[i][x][0])
					wok.append(rpstandings[i][x][1])

				employee_writer.writerow(wok)
		with open('blackjack.csv', mode='w') as standings:
			employee_writer = csv.writer(standings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			
			for i in blackjackStandings:
				wok = [str(i)]
				for x in blackjackStandings[i]:
					wok.append(x)
					wok.append(blackjackStandings[i][x][0])
					wok.append(blackjackStandings[i][x][1])

				employee_writer.writerow(wok)


	
	

	

				
client.run("NzcwMzcxMzUxNTc5ODUyODgw.X5cmOw.ro1Wl0rToU8FodI2wcLo4r3RLvo")

    