s = "mensagem não definida"           
n = "O Modulo Não Esta Ativo No Servidor"
a = "Nenhum Canal Definido"
@bot.group(aliases=['shop'])
async def loja(ctx):
	if ctx.invoked_subcommand is None:.member = ctx.message.author
	help_p = discord.Embed(title='Loja Dos Maloka', description='**Caixas** - 📦 \n**Itens** - 💎\n**Badges** -  💼')
	msg = await ctx.send(embed=help_p)
	await msg.add_reaction('📦')
	await msg.add_reaction('💎')	
	await msg.add_reaction('💼')
	try:
		while True:
			reaction, user = await bot.wait_for("reaction_add", timeout=360, check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id)
			emoji = str(reaction.emoji)
			if emoji == '📦':
				await msg.delete()
				embed_help = discord.Embed(description="📦┃Menu De Caixinhas")
				embed_help.add_field(name='Caixa Básica', value='')
				msg = await ctx.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '✨':
				await msg.delete()
				embed_help = discord.Embed(description="📕┃Menu de ajuda Ações")
				embed_help.add_field(name = 's!dance ',value ='Como usar ``s!dance`` dance com algum usuário',inline = False)
				embed_help.add_field(name = 's!kiss',value ='Como usar ``s!kiss @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
				embed_help.add_field(name = 's!hug ',value ='Como usar ``s!hug @usuário``',inline = False)
				embed_help.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
				msg = await member.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '⬅':
				await msg.delete()
				msg = await member.send(embed=help_p)
				await msg.add_reaction('👮')
				await msg.add_reaction('✨')
	except asyncio.TimeoutError:
		await msg.delete() #deletar mensagem após um tempo sem resposta dos reactions
	except Exception as e:
		await msg.delete()
		print(repr(e))		
		embed = discord.Embed(title='Shop Dos Maloka kk', description="para comprar algo digite (s!loja comprar <nomeDoItem>", color=0xFF0000)
		embed.add_field(name='caixa Normal', value='Ganhe entre 150 a 500 de ryucoins\n**Valor:**`250`')
		embed.add_field(name='st!welbye canal <canal>', value='Seleciona O Canal Onde A Mensagem Sera Enviada\nCanal Welcome Ativo: {canalWel.mention}\nCanal Adeus Ativo {canal.mention}\nExemplo: st!welbye canal #bem-vindo')
		return await ctx.send(embed=embed)

@welbye.command(pass_context=True)
async def ativar(ctx):
	if not ctx.author.guild_permissions.manage_guild:
		return await ctx.send("🚨| Para executar este comando, você precisa da permissão de gerenciar servidor")
	else:
		try:
			mongo = MongoClient(url)
			tutorial = mongo["eventos"]
			rpg = tutorial["welcome"]
			rpg = tutorial.rpg.find_one({"_id":str(ctx.guild.id)})
			if rpg is None:
				servidorModulo = {"_id":str(ctx.guild.id),"nome":str(ctx.guild.name), "canalWelcome":a,"canalBye":a,"MensagemBye":s,"mensagemWel":s, "statusWel":n, "statusBye":n}
				tutorial.rpg.insert_one(servidorModulo).inserted_id
				canalWel = bot.get_channel("{canalWelcome}")
				canal = bot.get_channel("{canalBye}")
				await ctx.send(f"Olá {ctx.author.mention}, O Modulo de Welcome/Adeus foi ativado em seu servidor!")
			else:
				return await ctx.send(f"Olá {ctx.author.mention}, O Modulo De Welcome Ja Esta Ativo No Servidor")
		except Exception as e:
			await ctx.send(f"[Erro] {e}")		
@welbye.command(pass_context=True)
async def canalW(ctx, canal: discord.TextChannel=None):
	if canal is None:
		return await ctx.send(f'{ctx.author.mention}, mencione um canal')
	else:
		try:
			mongo = MongoClient(url)
			tutorial = mongo["eventos"]
			rpg = tutorial["welcome"]
			rpg = tutorial.rpg.find_one({"_id":str(ctx.guild.id)})
			if rpg is None:
				await ctx.send(f"Olá {ctx.author.mention}, seu servidor não esta no meu sistema, use `s!welbye ativar` para adicionar seu servidor")
			else:
				
				tutorial.rpg.update_one({"_id":str(ctx.guild.id)}, {"$set":{"canalWel":str(canal.id)}})
				await ctx.send(f"{ctx.author.mention}, Canal de Bem Vindo/Adeus Definido Em {canal.mention}")
		except Exception as e:
				await ctx.send(f"[Erro] {e}") 

@welbye.command(pass_context=True)
async def welmsg(ctx, msg: str=None):
	if msg is None:
		return await ctx.send(f'{ctx.author.mention}, digite uma mensagem')
	else:
		try:
			mongo = MongoClient(url)
			tutorial = mongo["eventos"]
			rpg = tutorial["welcome"]
			rpg = tutorial.rpg.find_one({"_id":str(ctx.guild.id)})
			if rpg is None:
				await ctx.send(f"Olá {ctx.author.mention}, seu servidor não esta no meu sistema, use `s!welbye ativar` para adicionar seu servidor")
			else:
				user = member.mention
				guild = guild.name
				tutorial.rpg.update_one({"_id":str(ctx.guild.id)}, {"$set":{"mensagemWel":str(msg)}})
				await ctx.send(f"{ctx.author.mention}, setou a mensagem `{msg}`")
		except Exception as e:
				await ctx.send(f"[Erro] {e}") 
@bot.event
async def on_member_join(member):
	try:
		mongo = MongoClient(url)
		tutorial = mongo["eventos"]
		rpg = tutorial["welcome"]
		rpg = tutorial.rpg.find_one({"_id":str(guild.id)})	
		mensagem = rpg["mensagemWel"]
		id = rpg["canalWel"]
		canal = bot.get_channel(id)
		await canal.send(mensagem)
	except Exception as e:
		print(f"[Erro] {e}")       	

@bot.event
async def on_member_remove(member):
	mensagem = "mensagem teste"
	canal = bot.get_channel(581586752460816474)
	await canal.send(mensagem)	