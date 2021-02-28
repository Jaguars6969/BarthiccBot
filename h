			
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
				elif 50 <= rand <= 60:
					gain = random.randint(10, 15)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
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
				elif 30 <= rand <= 40:
					gain = random.randint(20, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 40 <= rand <= 90:

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
				elif 25 <= rand <= 30:
					gain = random.randint(40, 55)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					uryard += gain
				elif 30 <= rand <= 90:

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
			till -= gain

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
				elif 25 <= rand <= 50:
					gain = random.randint(10, 15)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a short pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 50 <= rand <= 90:

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
				elif 30 <= rand <= 40:
					gain = random.randint(20, 25)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a medium pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 40 <= rand <= 90:

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
				elif 25 <= rand <= 30:
					gain = random.randint(40, 55)
					await ctx.send(embed=discord.Embed(title="Football! :football:", description=f"You stepped back in the pocket\n you threw a long pass for your receiver and got {gain} yards", color = random.choice(color)))
					theyard += gain
				elif 30 <= rand <= 90:

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
