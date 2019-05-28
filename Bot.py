import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import nekos
import time
import colorsys
import sys
import subprocess
from pymongo import MongoClient
import os
import pymongo
import json
import traceback
import requests
import datetime
import random

from random import choice





url = os.environ.get('URL')
mongo = MongoClient(url)

prefix = ['s!', 'S!', 'st!', 'ss!']

bot = commands.Bot(prefix, owner_id=497518244165320734)
print (discord.__version__)
bot.remove_command("help")
start = time.time()

bot.launch_time = datetime.datetime.utcnow()
COLOUR = 0xFFFF00
COR = 0x00ff00
amounts = {}
n = "O Motivo Não Foi Definido."


@bot.event
async def on_ready():
	while True:
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(set(bot.get_all_members())))} Seres Humanos!"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(set(bot.guilds)))} Servidores!"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Teste Meu Sistema De Economia!"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="s!invite - Me Adicione Em Seu Servidor s!vote - me ajude dando um upvote"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(name="Minha versão: 3.0"))
		await asyncio.sleep(20)



		



    
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.content.lower().startswith('<@539468157291855903>'):
		await message.channel.send('Olá {} Meu prefixo é ``s!`` para ver meus comandos digite ``s!ajuda`` ou ``s!help``!'.format(message.author.mention))



		





    
@bot.command(pass_context=True, aliases=['latency', 'pong'])
async def ping(ctx):
    '''Find the response time in milliseconds.\n`latency` `pong`'''
    ptime = time.time()
    embed = discord.Embed(Title='Ping', color=0x00FF00)
    embed.add_field(name='Pong!', value='Calculando...')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    ping3 = await ctx.send(embed=embed)
    ping2 = time.time() - ptime
    ping1 = discord.Embed(Title='Ping', color=0x00FF00)
    ping1.add_field(name='Pong!', value='{} ms.'.format(int((round(ping2 * 1000)))))
    ping1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ping3.edit(embed=ping1)
    
    
semdesc= "Este usuário não possui descrição. para adicionar uma descrição digite `s!sobre <descrição>`"
nobadg = "Este usuário não possui badges"
novp = "Este usuário não é vip"
nott = "Nenhuma frase adicionada. Use `s!frase <frase>` para adicionar"
nosp = "Solteiro(a)"   
@bot.command(pass_context=True)
async def registro(ctx):
       try:

         tutorial = mongo["tutorial"]
         rpg = tutorial["rpg"]
         rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
         if rpg is None:
            usuario = {"_id":str(ctx.author.id),"usuario":str(ctx.author.name), "coins":0,"reps":0,"donator":False,"CaixaB":0,"sobre":semdesc, "CaixaM":0, "CaixaE":0, "CaixaL":0, "badges":nobadg, "vip":novp, "titulo":nott, "ship":nosp}
            tutorial.rpg.insert_one(usuario).inserted_id
            await ctx.send(f"<:Registro:581790276163600424> | {ctx.author.mention}, você foi registrado no banco de dados com sucesso!")
         else:
           await ctx.send(f"<:erro:581791491467378699> | {ctx.author.mention}, você já está registrado no banco de dados!")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")
@bot.command(name="eval")
async def _eval(ctx, *, code: str):
        try:
            if ctx.message.author.id == 497518244165320734:
                m = ctx.message.content.split(' ')
                if len(m) == 1:
                    await ctx.send('Digite algo!')
                else:
                    if not 'await' in ctx.message.content:
                        await ctx.send(eval(code))
                    else:
                        res = eval(str(code).replace('await', ''))
                    
                        print(await res)
            else:
                await ctx.send(f'{ctx.author.mention} Apenas Meu Glorioso Criador Pode Usar Esse Comando!')
        except Exception as e:
            error = discord.Embed(color=0x36393f)
            error.add_field(name='Erro', value=f'{e}')
            await ctx.send(embed=error)           


                                 
@bot.command(pass_context=True,aliases=['lb','ryucoinstop','topryucoins'])
async def learderboard(ctx):
	try:
		
		tutorial = mongo["tutorial"]
		rpg = tutorial["rpg"]
		sort = rpg.find().limit(10).sort('coins', -1)
		users = []
		rank = ""
		for d in sort:
			users.append(f'{rpg["usuario"]} - `{rpg["coins"]}`')
			for i in range(len(users)):
				rank += f'{i+1}º {users[i]} \n'
				await ctx.send(rank)
 
	except Exception as e:
			await ctx.send(f"[Erro] {e}")
						     

@bot.command(pass_context=True, aliases=['coins', 'vercoins', 'versaldo'])
async def saldo(ctx, user: discord.User=None):
	if user is None:
		user = ctx.author
		try:
			
			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(user.id)})
			if rpg is None:
				await ctx.send(f"<:erro:581791491467378699> | {ctx.author.mention}, você não está registrado no sistema de coins, use s!registro para se registrar!")
			else:
				moedas = rpg["coins"]
				await ctx.send(f"<a:momeym:581669926809370626> | {user.mention}, Você tem {moedas} ryuCoins.")
		except Exception as e:
			await ctx.send(f"[Erro] {e}")
			

@bot.command(pass_context=True, aliases=['reputações', 'reputação'])
async def reps(ctx, user: discord.Member=None):
	if user is None:
		user = ctx.author
	else:
		try:

			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(user.id)})
			if rpg is None:
				await ctx.send(f"Olá {ctx.author.mention}, você não está registrado em meu sistema, use s!registro para se registrar!")
			else:
				reps = rpg["reps"]
				await ctx.send(f"<a:rep100:581676089491980301> | {user.mention},  tem {reps} reputações.")
		except Exception as e:
			await ctx.send(f"[Erro] {e}")                 
    

		
@bot.command(pass_context=True)
async def servers(ctx):
	servers = list(bot.guilds)
	await ctx.send("Estou conectado em " + str(len(bot.guilds)) + " servers:")
	for x in range(len(servers)):
		await ctx.send(" "+servers[x-1].name)
		
@bot.command(pass_context=True)
async def frase(ctx, *, frase: str=None):
	if frase is None:
		await ctx.send(f'{ctx.author.mention}, Digite algo para ser a frase de seu perfil')
	else:
		try:
			
			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
			if rpg is None:
				await ctx.send(f"<:erro:581791491467378699> | {ctx.author.mention}, você não está registrado no sistema, use s!registro para se registrar!")
			else:
				
				tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"titulo":str(frase)}})
				await ctx.send(f"<:semregistro:581793891179560960> | {ctx.author.mention}, setou a frase `{frase}`")
		except Exception as e:
				await ctx.send(f"[Erro] {e}")		


@bot.command(pass_context=True, aliases=['casar'])
async def marry(ctx):
	await ctx.send(f'{ctx.author.mention} Este Comando Ainda Não Esta Ativo')

@bot.command(pass_context=True, aliases=['loja'])
async def shop(ctx):
	await ctx.send(f'{ctx.author.mention} Este Comando Ainda Não Esta Ativo')				
						
@bot.command(pass_context=True)
async def sobre(ctx, *, sobre: str=None):
	if sobre is None:
		await ctx.send(f'{ctx.author.mention}, Digite algo para ser sua descrição')
	else:
		try:

			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
			if rpg is None:
				await ctx.send(f"<:erro:581791491467378699> | {ctx.author.mention}, você não está registrado no sistema, use s!registro para se registrar!")
			else:
				
				tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"sobre":str(sobre)}})
				await ctx.send(f"<:semregistro:581793891179560960> | {ctx.author.mention}, setou a descrição `{sobre}`")
		except Exception as e:
				await ctx.send(f"[Erro] {e}")		

@bot.command(pass_context=True)
@commands.is_owner()
async def setcoins(ctx, member:discord.Member=None, coins:int=None):
       try:

         tutorial = mongo["tutorial"]
         rpg = tutorial["rpg"]
         rpg = tutorial.rpg.find_one({"_id":str(member.id)})
         if rpg is None:
            await ctx.send(f"Olá {ctx.author.mention}, você não está registrado no sistema de coins, use s!registro para se registrar!")
         else:
             moedas = int(rpg["coins"])+ int(coins)
             tutorial.rpg.update_one({"_id":str(member.id)}, {"$set":{"coins":int(moedas)}})
             await ctx.send(f"💸 {ctx.author.mention}, setou {coins} com sucesso para {member.mention}.")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def daily(ctx):
       try:   	  
 
          tutorial = mongo["tutorial"]
          rpg = tutorial["rpg"]
          rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
          if rpg is None:
            await ctx.send('Você não esta registrado digite `s!registro` para se registrar')
            ctx.command.reset_cooldown(ctx)        
          else:
          	coins = random.randint(500,1800)
          	moedas = int(rpg["coins"])+ int(coins)
          	tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas)}})
          	await ctx.send(f"<a:momeym:581669926809370626> | {ctx.author.mention}, você ganhou {coins} ryuCoins diários.")
       except Exception as e:
          		await ctx.send(f"[Erro] {e}")

@daily.error
async def daily_error(ctx,error):
     if isinstance(error, discord.ext.commands.CommandOnCooldown):
       min, sec = divmod(error.retry_after, 60)
       h, min = divmod(min, 60)
       if min == 0.0 and h == 0:
           await ctx.send('<a:time:520595409429594125> | **Espere `{0}` segundos para usar o comando novamente.**'.format(round(sec)))
       else:
           await ctx.send('**Espere `{0}` horas `{1}` minutos  e `{2}` segundos para pegar sua daily novamente.**'.format(round(h),round(min),round(sec)))						

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*2, commands.BucketType.user)
async def rep(ctx, user: discord.User=None):
	bot = user.bot
	if user is None:
		return await ctx.send(f'{ctx.author.mention} Você deve mencionar um usuário')
		ctx.command.reset_cooldown(ctx)
	if user == ctx.author:
		return await ctx.send(f'{user.mention} Você não pode dar reputações a você mesmo')
		ctx.command.reset_cooldown(ctx)
	if user == bot:
		return await ctx.send(f'{user.mention} Você não pode dar reputações a um bot')
		ctx.command.reset_cooldown(ctx)		
	else:
		try:

			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(user.id)})
			id = ctx.author.id
			if rpg is None:
				await ctx.send('Você não esta registrado digite `s!registro` para se registrar')
				ctx.command.reset_cooldown(ctx)
			else:
				reps = 1
				reput = int(rpg["reps"])+ int(reps)
				tutorial.rpg.update_one({"_id":str(user.id)}, {"$set":{"reps":int(reput)}})
				await ctx.send(f"<a:rep100:581676089491980301> | {ctx.author.mention}, você deu `1` reputações para {user.mention} Agora ele tem um total de `{reput}` reputações.")
		except Exception as e:
			await ctx.send(f"[Erro] {e}")
@rep.error
async def rep_error(ctx,error):
     if isinstance(error, discord.ext.commands.CommandOnCooldown):
       min, sec = divmod(error.retry_after, 60)
       h, min = divmod(min, 60)
       if min == 0.0 and h == 0:
           await ctx.send('<a:time:520595409429594125> | **Espere `{0}` segundos para usar o comando novamente.**'.format(round(sec)))
       else:
           await ctx.send('**Espere `{0}` horas `{1}` minutos  e `{2}` segundos para usar o comando novamente.**'.format(round(h),round(min),round(sec)))
           
@bot.command(pass_context=True, aliases=['perfil'])
async def profile(ctx, user: discord.Member=None):
		user = user or ctx.author
		try:

			tutorial = mongo["tutorial"]
			rpg = tutorial["rpg"]
			rpg = tutorial.rpg.find_one({"_id":str(user.id)})
			if rpg is None:
				await ctx.send(f"Olá {ctx.author.mention}, você não está registrado em meu sistema, use s!registro para se registrar!")
			else:
				reps = rpg["reps"]
				ship = rpg["ship"]
				money = rpg["coins"]
				sobremim = rpg["sobre"]
				vip = rpg["vip"]
				titulo = rpg["titulo"]
				badges = rpg['badges']
				basica = rpg['CaixaB']
				media = rpg['CaixaM']
				epica = rpg['CaixaE']
				lendaria = rpg['CaixaL']
				embed = discord.Embed(title=f'perfil de {user.name}', color=0xff00AB)
				embed.add_field(name="<a:rep100:581676089491980301> Reputação", value=f"{reps}")
				embed.add_field(name="<a:momeym:581669926809370626> RyuCoins", value=f"{money}")
				embed.add_field(name="😍 Estado Civil", value=f"{ship}")
				embed.add_field(name="<:basica:581838984351580180> Caixas", value=f"<:basica:581838984351580180> **Caixas Basicas:** `{basica}`\n<:media:581838910754127894> **Caixas Medias:** `{media}`\n<:epica:581839027687260164> **Caixas Epicas:**`{epica}`\n<:lendaria:581839194004127764> **Caixas Lendarias**`{lendaria}`")
			embed.add_field(name="📌 Frase", value=f"{titulo}")
			embed.add_field(name="<:Icon_Monthly_VIP_Badge:581844119979032596> Badges",value=f"{badges}")
			embed.add_field(name="<a:vip:581858116631658497> Vip", value=f"{vip}")
			embed.add_field(name="📖 Sobre", value=f"{sobremim}")
			embed.set_thumbnail(url=user.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f"[Erro] {e}")
			
			 		           		          
@bot.command(pass_context=True, aliases=['apostar'])
async def aposta(ctx, aposta: int=None):
       try:
    	
          tutorial = mongo["tutorial"]
          rpg = tutorial["rpg"]
          moedas = tutorial.rpg.find_one({"_id":str(ctx.author.id)})       
          if rpg is None:
             await ctx.send(f"🎲 {ctx.author.mention}, você não está registrado no sistema, use s!registro para se registrar!")
          else:
          	if int(moedas['coins']) < aposta:
          		return await ctx.send(f'<:erro:581791491467378699> | {ctx.author.mention} Você não tem ryucoins suficientes para apostar')
          	else:
          		flip = random.randint(1, 2)
          	if flip == 1:
          		moedas = int(moedas["coins"])

          		tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas) + aposta}})
          		msg = await ctx.send(f"<a:momeym:581669926809370626>| {ctx.author.mention}, Ganhou a aposta e recebeu `{aposta}` Ryucoins.")
          		await msg.add_reaction('<a:momeym:581669926809370626>')
          	if flip ==2:
          	
          		moedas = int(moedas["coins"])
         
          		tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas) - aposta}})
         
          		msg = await ctx.send(f"<a:money:581670005306032130> | {ctx.author.mention}, Perdeu a aposta e perdeu `{aposta}` Ryucoins.")
          		
          		
       except Exception as e:
           await ctx.send(f"[Erro] {e}")

            	
            	
            	
@bot.command(pass_context=True, aliases=['pagar', 'dar', 'transferir'])
async def pay(ctx, member:discord.User=None, coins:int=None):
       try:
          mongo = MongoClient(url)       	
          tutorial = mongo["tutorial"]
          rpg = tutorial["rpg"]
          rpg = tutorial.rpg.find_one({"_id":str(member.id)})
          moeda2 = tutorial.rpg.find_one({"_id":str(ctx.author.id)})       
          if rpg is None:
             await ctx.send(f"🎲 {ctx.author.mention}, você não está registrado no sistema, use s!registro para se registrar!")
          if moeda2 is None:
             await ctx.send(f"🎲 {ctx.author.mention}, O Usuário mencionado não está registrado no sistema, use s!registro para se registrar!")
          else:
          	if int(moeda2['coins']) < coins:
          		return await ctx.send(f"<:erro:581791491467378699> | {ctx.author.mention} Você não tem ryucoins suficientes!")
          	else:
          		moedas = int(rpg["coins"])
          		moedas2 = int(moeda2["coins"])
          		tutorial.rpg.update_one({"_id":str(member.id)}, {"$set":{"coins":int(moedas) + coins}})
          		tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas2) - coins}})
          		await ctx.send(f"<a:money:581670005306032130> | {ctx.author.mention}, transferiu {coins} ryucoins com sucesso para {member.mention}.")

       except Exception as e:
           await ctx.send(f"[Erro] {e}")

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*4, commands.BucketType.user)
async def trabalhar(ctx):
       try:
          mongo = MongoClient(url)    
          tutorial = mongo["tutorial"]
          rpg = tutorial["rpg"]
          rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
          if rpg is None:
            await ctx.send('Você não esta registrado digite `s!registro` para se registrar')
            ctx.command.reset_cooldown(ctx)            
          
          else:
              coins = random.randint(500, 1000)
              moedas = int(rpg["coins"])+ int(coins)
              tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas)}})
              await ctx.send(f"💸 {ctx.author.mention}, você trabalhou e ganhou {coins} ryuCoins.")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")
@trabalhar.error
async def trabalhar_error(ctx,error):
     if isinstance(error, discord.ext.commands.CommandOnCooldown):
       min, sec = divmod(error.retry_after, 60)
       h, min = divmod(min, 60)
       if min == 0.0 and h == 0:
           await ctx.send('<a:time:520595409429594125> | **Espere `{0}` segundos para usar o comando novamente.**'.format(round(sec)))
       else:
           await ctx.send('**Espere `{0}` horas `{1}` minutos  e `{2}` segundos para usar o comando novamente.**'.format(round(h),round(min),round(sec)))
@bot.command(pass_context=True)
async def dog(ctx):
    '''Check out a random cute or funny dog!'''
    r = requests.get('https://random.dog/woof.json')
    json = r.json()
    if r.status_code == 200:
        sdog = discord.Embed(title='Dogão', color=0x00FF00,timestamp = datetime.datetime.utcnow())
        sdog.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        sdog.set_image(url=json['url'])
        return await ctx.send(embed=sdog)
    else:
        rdog = discord.Embed(title='Error', description='Não pude acessar a API', color=0xFF0000)
        rdog.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await ctx.send(embed=rdog)

@bot.command(pass_context=True)
async def cat(ctx):
    '''Check out a random cute or funny cat!'''
    r = requests.get(f'https://catapi.glitch.me/random/')
    json = r.json()
    
    if r.status_code == 200:
        scat = discord.Embed(title='Gato', color=0x00FF00)
        scat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        scat.set_image(url=json['url'])
        scat.set_footer(text=f' {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
        return await ctx.send(embed=scat)
    else:
        rcat = discord.Embed(title='Error', description='Não pude accessar a API', color=0xFF0000)
        rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await ctx.send(embed=rcat)		



@bot.command(pass_context=True)
async def lock(ctx):

       if not ctx.author.guild_permissions.manage_channels:
                 await ctx.send(f"? | {ctx.author.mention} Para executar este comando, você precisa da permissão de gerenciar canais!")
          
       else:
               try:
                    role = ctx.guild.default_role
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = False
                    await ctx.channel.set_permissions(overwrite=overwrite, target=role)
                    await ctx.send("📥 | Agora nenhum membro pode falar neste canal!")
               except Exception as e:
                        await ctx.send(f"[ERROR]: {repr(e)}")
@bot.command(pass_context=True)
async def unlock(ctx):
       if not ctx.author.guild_permissions.manage_channels:
                 await ctx.send("? |{ctx.author.mention} Para executar este comando, você precisa da permissão gerenciar canais!")
       else:
               try:
                     role = ctx.guild.default_role
                     overwrite = discord.PermissionOverwrite()
                     overwrite.send_messages = True
                     await ctx.channel.set_permissions(overwrite=overwrite, target=role)
                     await ctx.send("📤 | Agora todos os membros podem falar neste canal!")
               except Exception as e:
                        await ctx.send(f"[ERROR]: {repr(e)}")

@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member=None, *, motivo: str = None):
    motivo = motivo or n
    if not member:
    	return await ctx.send('{} Você não especificou o usuário. Exemplo: ``s!ban <@usuário> <motivo>``'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.ban_members:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)
    else:
        embed = discord.Embed(title='Ação | Ban', color=0xff0Ab)
        embed.add_field(name='👮 Executor', value=ctx.message.author)
        embed.add_field(name='👥 Usuário', value=member.name)
        embed.add_field(name='💻 Id', value=member.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await ctx.send(embed=embed)
        ban = discord.Embed(title='Ação | Ban', color=0xff0Ab)
        ban.add_field(name='Executor', value=ctx.message.author)
        ban.add_field(name='Servidor', value=ctx.message.guild.name)
        ban.add_field(name='Motivo', value=motivo)
        ban.set_thumbnail(url=ctx.message.guild.icon_url)
        await member.send(embed=ban)
   
							

      
        embed = discord.Embed(title='Ação | Ban', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='👮 Executor', value=ctx.message.author)
        embed.add_field(name='👥 Usuário', value=member.name)
        embed.add_field(name='💻 Id', value=member.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await ctx.send(embed=embed)
        ban = discord.Embed(title='Ação | Ban'.format(ctx.message.author.mention), color=0xff0Ab)
        ban.add_field(name='Executor', value=ctx.message.author)
        ban.add_field(name='Servidor', value=ctx.message.guild.name)
        ban.add_field(name='Motivo', value=motivo)
        ban.set_thumbnail(url=ctx.message.guild.icon_url)
        await member.send(embed=ban)
   
							
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User=None, *, motivo: str = None):
    motivo = motivo or n
    if not user:
        return await ctx.send('{} Você não especificou o usuário. Exemplo: ``s!kick <@usuário> <motivo>``'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.kick_members:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)        
    else:
        await ctx.guild.kick(user)
        embed = discord.Embed(title='Ação | Kick!', description='{} usuário expulso com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='👮 Autor', value=ctx.message.author)
        embed.add_field(name='👥 usuário', value=user)
        embed.add_field(name='💻 Id', value=user.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await ctx.send(embed=embed)
        embedpv = discord.Embed(title='Ação | Kick'.format(ctx.message.author.mention), color=0xff0Ab)
        embedpv.add_field(name='👮 Executor', value=ctx.message.author)
        embedpv.add_field(name='💻 Servidor', value=ctx.message.guild.name)
        embedpv.add_field(name='💻 id', value=ctx.message.author.id)
        embedpv.add_field(name='📝 Motivo', value=motivo)
        embedpv.set_thumbnail(url=ctx.message.guild.icon_url)
        await user.send(embed=embedpv)
        print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		
@bot.command(pass_context=True)
async def vote(ctx):
    embed = discord.Embed(description='**Olá! Poderia Me Ajudar Votando Em Mim? clique [aqui](https://discordbots.org/bot/539468157291855903/vote)**', color=0x00ffbb)
    await ctx.send(embed=embed)
	
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await ctx.send('Você precisa falar algo para votar')
	else:
			vote = await ctx.send(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
	
	
	
@bot.command()
async def attlogs():
	embed = discord.Embed(title='Atualizações do bot', color=0xB0ffA0)
	embed.add_field(name='02/02/2018', value='Bot Aprovado Na Discord Bot List')
	embed.add_field(name='01/02/2018', value='Correções de bugs')
	embed.add_field(name='01/02/2018', value='Adicionado Motivo No Ban e Kick, O Bot tambem envia uma mensagem no PV do usuário banido')
	embed.add_field(name='01/02/2018', value= 'Novo comando de diversão ``s!chorar``')
	embed.add_field(name='31/02/3018', value='Novos comandos ``s!votar`` e ``s!pergunta``')
	await ctx.send(embed=embed)
	
			
					

	


	
@bot.command(pass_context=True)
async def invite(ctx):
    e = discord.Embed(description='{} **Olá Para Me Adicionar Em Seu Servidor Clique [aqui](https://discordapp.com/oauth2/authorize?client_id=539468157291855903&permissions=8&scope=bot) | Poderia Me Ajudar Dando Um Upvote? Clique [aqui](https://discordbots.org/bot/539468157291855903/vote)**'.format(ctx.message.author.mention), color=0xff0f00)
    await ctx.send(embed=e)
    print('comando invite digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	


@bot.command(pass_context=True)
async def serverinfo(ctx):
        try:
           embed = discord.Embed(color=0xff0000, title='**Server Info**', description='Informações do Servidor **{}**'.format(ctx.message.guild.name), timestamp=datetime.datetime.utcnow())
           embed.set_thumbnail(url=ctx.message.guild.icon_url)
           embed.add_field(name='👑 | Dono:', value=ctx.message.guild.owner)
           embed.add_field(name='👥 | Membros:', value=str(len(ctx.message.guild.members)))
           embed.add_field(name='📃 | Cargos:', value=len(ctx.message.guild.roles))
           embed.add_field(name='😁 | Emojis:', value=len(ctx.message.guild.emojis))
           embed.add_field(name='🤖 | Bots:', value=str(len([a for a in ctx.message.guild.members if a.bot])))
           embed.add_field(name='🕤 | Criado em:', value=ctx.message.guild.created_at.strftime('%d %b %Y às %H:%M'))
           embed.add_field(name='🌎 | Região:', value=str(ctx.message.guild.region).title())
           embed.set_footer(text='Comando usado por {}'.format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
           await ctx.send(embed=embed)
        except:
           await ctx.channel.send('❌**ERRO**❌') 
    

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User=None):
	user = user or ctx.message.author
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await ctx.send(embed=hugemb)
	

	
	

	

	
@bot.command(pass_context=True)
async def meme(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349760/images_9.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349761/cara-mano-tatuei-o-nome-da-minha-namora-e-ela-20426746.png', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032640/images_7.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032641/images_10.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088002383883/images_11.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088455630855/3d6dcd431d328b82ac2bc8edf5f754ee--kawaii.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='SO MEME DE QUALIDADE MONSTRA', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await ctx.send(embed=hugemb)
	
	

	

    
    
@bot.command(pass_context = True)
async def avisar(ctx, member: discord.Member=None, *, motivo: str = None):
    motivo = motivo or n
    if not member:
    	return await ctx.send('{} Você Não Especificou o Usuário'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.kick_members:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)
    else:
    	embed = discord.Embed(description='{} foi avisado com sucesso por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
    	embedpv = discord.Embed(title='Aviso', color=0x00AB70)
    	embedpv.add_field(name='Aviso Do servidor', value=ctx.message.guild.name)
    	embedpv.add_field(name='Autor', value=ctx.message.author)
    	embedpv.add_field(name='Motivo', value=motivo)
    	embedpv.set_thumbnail(url=ctx.message.guild.icon_url)
    	await member.send(embed=embedpv)
    	await ctx.send(embed=embed)  
		

	
@bot.command(pass_context=True)
async def setcargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    if not member:
    	return await ctx.send('{} Você não especificou o usuário.'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.manage_roles:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)
  
    if not role:
        await ctx.send('{} Você Precisa Mencionar Um Cargo Para Adicionar'.format(ctx.message.author.mention))
    else:
        await member.add_roles(role)
    embed = discord.Embed(title='Ação | Adicionar Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
    
    await ctx.send(embed=embed)

  	


@bot.command(pass_context=True)
async def removercargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    if not member:
    	return await ctx.send('{} Você não especificou o usuário.'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.manage_roles:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)
    if not role:
        await ctx.send('{} Você Precisa Mencionar Um Cargo Para Remover'.format(ctx.message.author.mention))
    else:
        await member.remove_roles(role)
    embed = discord.Embed(title='Ação | Remover Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
      
    await ctx.send(embed=embed)
  
    
@bot.command(pass_context=True)
async def falar(ctx, *, arg: str=None):
    if not arg:
        return await ctx.send('{} Você Precisa Escrever Algo Para Eu Falar.'.format(ctx.message.author.mention))
    else:
        await ctx.send("{} Me Forçou A Falar...{}".format(ctx.message.author.mention, arg))
        

	
@bot.command(pass_context=True, aliases=['slap'])
async def tapa(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        pic = nekos.img('slap')
        hugemb = discord.Embed(title='Ação | Tapa🔥', description=':scream:| **{}** Deu Um tapa em **{}**! Que Tapa!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=pic)
        hugemb.set_footer(text ='Comando realizado por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)
        
@bot.command(pass_context=True)
async def google(ctx, *, message: str = None):
        try:
            if message is None:
                await ctx.send("Você precisa pesquisar algo! `s!google [pesquisa]`")
            else:
                words = f'https://www.google.com/search?q={message}'.replace(' ', '+')
                search = discord.Embed(title='Pesquisa realizada com sucesso!', description='**Resultado da pesquisa no Google:**', colour=0xff0000, timestamp=datetime.datetime.utcnow())
                search.add_field(name='------------------------------------------------', value=('➡ [RESULTADO](' + words) + ')\n')
                search.set_footer(text='Comando usado pelo(a) {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
                await ctx.send(embed=search)
        except Exception as e:
            await ctx.send(f"[ERROR]: {e}")
		
@bot.command(pass_context=True)
async def brigar(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516094273290240/300px-DarkCureFight.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802763/source.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Briga 👊',  description=':scream:| **{}** Brigou com **{}**!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando realizado por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)
        
	
@bot.command(pass_context=True)
async def dance(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516095900418104/fanfiction-naruto-ao-seu-lado-2635515231020140950.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550868/ed8964dd9fb2f90e5eb4b19c577bec74.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550869/Akatsuki28.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Dançar',  description=':man_dancing:| **{}** Esta dançando com **{}**! Passinho dos Maloka 😎'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)
        
		

@bot.command(pass_context=True)
async def matar(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802762/b19b70f5c546ec7c67c2f0b4e61c21f743a5acaf_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733902097645568/tumblr_m6rerquar01qd4f2uo1_500.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Matar',  description='👮| **{}** Matou **{}**! ASSASINO!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)
	

	
	
@bot.command(pass_context=True)
async def atacar(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494351030452238/tumblr_mzh5vtuEIC1rm4wgqo4_r2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352926277633/01_Rikka.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494350053310475/G4dfvA5.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733423418376194/large.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Atack!',  description='💥| **{}** Atacou **{}**! Como ousas me atacar!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)
	
@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await ctx.send(embed=hugemb)


				

	
@bot.command(pass_context=True)
async def voadora(ctx, user: discord.User=None):
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Voadora',  description='**{}** Deu uma voadora em **{}** EITA!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)

nc = "Parada Cardiaca"		
@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User=None,*, causa: str=None):
    causa = causa or nc
    if not user:
        return await ctx.send('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Death Note',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text='Bot Oficial Shiryu')
        await ctx.send(embed=hugemb)
        await asyncio.sleep(5)
        hugemb = discord.Embed(title='Faliceu',  description='**{}** morreu Apos 30 segundos\n'
        'seu nome escrito no Death Note de **{}**\n'
        'Causa Da Morte: **{}**'.format(user.name, ctx.message.author.name, causa), color=0xA7ffbb)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await ctx.send(embed=hugemb)





  
@bot.command(pass_conetxt=True, aliases=['beijar'])
async def kiss(ctx, member: discord.Member=None):
	if not member:
		await ctx.send(f'{ctx.author.mention} Mencione alguém')
	else:
		pic = nekos.img('kiss')
		embed = discord.Embed(color=0xFF00FF, description=f'**{member.mention}** recebeu um beijo de **{ctx.author.mention}** casal fofo!')
		embed.set_image(url=pic)
		await ctx.send(embed=embed)
                
   
			
@bot.command(pass_conetxt=True, aliases=['abraçar'])
async def hug(ctx, member: discord.Member=None):
	if not member:
		await ctx.send(f'{ctx.author.mention} Mencione alguém')
	else:
		pic = nekos.img('hug')
		embed = discord.Embed(color=0xFFFF00, description=f'**{member.mention}** recebeu um abraço de **{ctx.author.mention}**')
		embed.set_image(url=pic)
		await ctx.send(embed=embed) 
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await ctx.send(random.choice(list))
	
			


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int=None):
    '''Purge a number of messages!\nUsage: !purge <amount>\nAliases: None\nPermissions: Manage Messages'''
    if amount == None:
        apurge = discord.Embed(title='Erro', description='Você não especificou uma quantidade de mensagens!', color=0xFF0000)
        apurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await ctx.send(embed=apurge)
    await ctx.channel.purge(limit=amount+1)
    spurge = discord.Embed(title='Ação | Clear', description=f'{ctx.message.author.mention} apagou {amount} messages!', color=0x00FF00)
    spurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=spurge)
    

   

    

    
@bot.command(pass_context=True)
async def pergunta(ctx, *, pergunta: str = None):
    if not pergunta:
        return await ctx.send("Você precisa perguntar alguma coisa.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro'])
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await ctx.send(embed=embed)
        print('comando roleta digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
    

   

@bot.command(pass_context=True,aliases=['ui'])
async def userinfo(ctx, user: discord.Member = None):
    '''See information about a user!\n`ui`'''
  


    if user is None:
    	user = ctx.message.author
    
    
    	
    
 
    embed = discord.Embed(color=0xff00ab, description="Informações de: {} !".format(user.name))
    embed.title = "{}".format(user)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="🆔ID:",value=user.id,inline=False)
    embed.add_field(name="📶Menção:",value=user.mention,inline=False)
    embed.add_field(name="🔢Tag:",value=user.discriminator,inline=False)
    embed.add_field(name="📆Criação da Conta:",value=user.created_at.strftime("**%H:%M - %d/%m/20%y**"),inline=False)
    embed.add_field(name="☑️Entrada no Servidor:",value=user.joined_at.strftime("**ás %H:%M - Data: %d/%m/20%y**"),inline=False)
    embed.add_field(name="📱Atividade:",value=str(user.activity).replace("None", "Nada"))
    embed.add_field(name="📷Avatar Link:",value=f"[Link]({user.avatar_url})\n",inline=False)
    embed.add_field(name='💻|Status',value=str(user.status).replace("dnd", "Não pertubar").replace("idle", "Ausente"))
    try:
    	embed.add_field(name="Jogando", value=user.game.name, inline=True)
    except:
            pass
            await ctx.send(embed=embed)
				
    	
      
@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Ação | Chorar',  description='😭|**{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await ctx.send(embed=hugemb)
	print('comando chorar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True, aliases=['bi'])
async def botinfo(ctx):
	embed = discord.Embed(title="Minhas Informações", color=0x00ffba)
	embed.add_field(name="**=====Principais Informações=====**", value=f"📆 **Criado Em:** `20 Março, 2019 às 14:32`\n<:programador:582173369722601522> **Criador:** ɱคｲ૯Ʋร †#8766\n<:programando:582173138448547843> **Linguagem Usada:** Python\n<a:discordlove:582176157609492490> **Versão Discord.py:** {discord.__version__}\n❓ **Prefixo:** `s!`")
	delta_uptime = datetime.datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)	
	embed.add_field(name='**=====Outras Informações=====**', value=f"<a:diversao:582178177078788096> **Me Adicione:** [Clique aqui](https://discordapp.com/oauth2/authorize?client_id=539468157291855903&permissions=8&scope=bot)\n<a:diversao:582178177078788096> **Vote Em Mim:** [clique aqui](https://discordbots.org/bot/539468157291855903/vote)\n<:DiscordPartner:582179555209641994> **Servidor De Suporte**: [Clique Aqui](https://discord.gg/KabD5BC)\n<a:DiscordHype:582179619978084356> **Servidores**:  `{str(len(set(bot.guilds)))}`\n💬 **Canais:** `{str(len(set(bot.get_all_channels())))}`\n👥 **Usuários:** `{str(len(set(bot.get_all_members())))}`\n<:uptime:582708017049632768> **Estou Online Há: **`{days}` **Dias** `{hours}` **Horas** `{minutes}` **Minutos** `{seconds}` **Segundos**")
	await ctx.send(embed=embed)	

		 		
		 		 		
		 		 		 		
		 		 		 		 		
		 		 		 		 		 		
s = "mensagem não definida"           
n = "O Modulo Não Esta Ativo No Servidor"
a = "Nenhum Canal Definido"
@bot.group(aliases=['welcome'])
async def welbye(ctx):
	if ctx.invoked_subcommand is None:
		embed = discord.Embed(title='Painel De Configuração Welcome', color=0xFF0000)
		embed.add_field(name='st!welbye ativar', value='Ativa a função no servidor \nBem Vindo Status: {statusWel}\nAdeus Status {statusBye}')
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
			
			
				tutorial.rpg.update_one({"_id":str(ctx.guild.id)}, {"$set":{"mensagemWel":str(msg)}})
				await ctx.send(f"{ctx.author.mention}, setou a mensagem `{msg}`")
		except Exception as e:
				await ctx.send(f"[Erro] {e}") 
@bot.event
async def on_member_join(member):
	try:
		user = member.mention
		servidor = member.guild.name
		tutorial = mongo["eventos"]
		rpg = tutorial["rpg"]
		rpg = tutorial.rpg.find_one({"_id":str(member.guild.id)})	
		mensagem = rpg["mensagemWel"]
		id = rpg["canalWel"]
		canal = bot.get_channel(id)
		await canal.send(mensagem)
	except Exception as e:
		print(f"[Erro] {e}")       	
		 		 		 		 		 		 		
		 		 		 		 		 		 		 		
		 		 		 		 		 		 		 		 		
		 		 		 		 		 		 		 		 		 		
		 		 		 		 		 		 		 		 		 		 		 		
						
@bot.command(pass_context=True,aliases=['ajuda','h'])
async def help(ctx):
	member = ctx.message.author
	help_p = discord.Embed(color=0xff00AB)
	help_p.add_field(name="Reaja Para Escolher Uma Categoria", value="👮 **Moderação**\n• comandos como `ban, kick...`\n✨ **Diversão**\n• comandos como `kiss, hug...`\nℹ **Informações**\n• comandos como `ping, avatar...`\n🚀 **Outros**\n• comandos como `pergunta, deathnote...`\n💸 **Economia**\n• comandos como `pagar, saldo...`")
	help_p.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
	await member.send(f'{member.mention}Duvidas? Entre em Meu Servidor De Suporte\nhttps://discord.gg/KabD5BC')
	await member.send(f'{member.mention} Quer Me Adicionar Em Seu Servidor? Digite `s!invite`')	
	msg = await member.send(embed=help_p)
	await msg.add_reaction('👮')
	await msg.add_reaction('✨')
	await msg.add_reaction('ℹ')
	await msg.add_reaction('🚀')
	await msg.add_reaction('💸')
	
	await ctx.send(f'{member.mention} Verifique Suas Mensagens Privadas.')
	try:
		while True:
			reaction, user = await bot.wait_for("reaction_add", timeout=360, check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id)
			emoji = str(reaction.emoji)
			if emoji == '👮':
				await msg.delete()
				embed_help = discord.Embed(description="📙┃Menu de ajuda Moderação")
				embed_help.add_field(name = 'ban ',value ='Como usar ``s!ban <@usuário> [motivo]`` - bane o usuário mencionado',inline = False)
				embed_help.add_field(name = 'kick',value ='Como usar ``s!kick <@usuário> [motivo]`` - Expulsa o usuário mencionado',inline = False)
				embed_help.add_field(name = 'setcargo',value ='Como usar ``s!setcargo <@cargo> <@usuário>`` - seta um cargo algo usuário mencionado',inline = False)
				embed_help.add_field(name = 'lock',value ='Como usar ``s!lock`` - bloqueia o canal para membros',inline = False)
				embed_help.add_field(name = 'unlock',value ='Como usar ``s!unlock`` - desbloqueia o canal para membros',inline = False)
				embed_help.add_field(name = 'mute',value ='Como usar ``s!mute <@usuário> [motivo]`` - Muta o usuário mencionado **DESATIVADO**',inline = False)
				embed_help.add_field(name = 'unmute',value ='Como usar ``s!unmute <@usuário>`` - Desmuta o usuário mencionado **DESATIVADO**',inline = False)	
				embed_help.add_field(name = 'removercargo',value ='Como usar ``s!removercargo <@cargo> <@usuário>`` - remove um cargo algo usuário mencionado',inline = False)
				embed_help.add_field(name = 'clear',value ='Como usar ``s!clear <quantidade>`` - limpa o canal de texto atual',inline = False)
				embed_help.add_field(name = 'avisar',value ='Como usar ``s!avisar <@usuário> [motivo]`` - avisa uma pessoa sobre algo',inline = False)								
				embed_help.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
				embed_help.add_field(name='-----------------------', value='***<arg> obrigatorio\n[arg] opicional***')												
				msg = await member.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '✨':
				await msg.delete()
				embed_help = discord.Embed(description="📙┃Menu de ajuda Ações", color = 0xff00AA)
				embed_help.add_field(name = 'dance ',value ='Como usar ``s!dance`` - dance com algum usuário',inline = False)
				embed_help.add_field(name = 'kiss',value ='Como usar ``s!kiss <@usuário>`` - O amor esta no ar! beije determinado usuário!',inline = False)
				embed_help.add_field(name = 'hug ',value ='Como usar ``s!hug <@usuário>``',inline = False)
				embed_help.add_field(name = 'suicidio ',value ='Como usar ``s!suicidio``',inline = False)
				embed_help.add_field(name = 'matar',value ='Como usar ``s!matar <@usuário>``',inline = False)
				embed_help.add_field(name = 'slap',value ='Como usar ``s!slap <@usuário>`` -  de uns tap cabuloso em alguem que esta te pertubando',inline = False)
				embed_help.add_field(name = 'chorar ',value ='Como usar ``s!chorar``',inline = False)
				embed_help.add_field(name = 'atack',value ='Como usar ``s!atack <@usuário> - ataque o usuário mencionado``',inline = False)
				embed_help.add_field(name = 'brigar',value ='Como usar ``s!brigar <@usuário>`` - brigue com seu amiguinho (não faça isso)',inline = False)
				embed_help.add_field(name = 'voadora',value ='Como usar ``s!voadora <@usuário>`` - de uma voadora no seu amiguinho (não faça isso)',inline = False)
				embed_help.add_field(name = 'meme',value ='Como usar ``s!meme`` - Mostra Um Meme',inline = False)															
				embed_help.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
				embed_help.add_field(name='-----------------------', value='***<arg> obrigatorio\n[arg] opicional***')				
				msg = await member.send(embed=embed_help)
				
				await msg.add_reaction('⬅')
			if emoji == 'ℹ':
				await msg.delete()
				embed_help = discord.Embed(description="📙┃Menu de ajuda Informações", color=0xff00ab)
				embed_help.add_field(name = 'serverinfo',value ='Como usar ``s!serverinfo`` - veja as informações do servidor atual',inline = False)
				embed_help.add_field(name = 'ping',value ='Como usar ``s!ping`` - Veja meu tempo de resposta',inline = False)
				embed_help.add_field(name = 'avatar',value ='Como usar ``s!avatar<@usuário>`` - Veja O Avatar Do Usuário Mencionado',inline = False)
				embed_help.add_field(name = 'ajuda ',value ='Como usar ``s!ajuda`` Meus comandos',inline = False)
				embed_help.add_field(name = 'userinfo',value ='Como usar ``s!userinfo [@usuário]`` Expulsa o usuário mencionado',inline = False)

				embed_help.add_field(name = 'invite',value ='Como usar ``s!invite`` - Meu convite para caso queira me adicionar em seu servidor',inline = False)
				embed_help.add_field(name = 'vote',value ='Como usar ``s!vote`` - Me Ajude Dando Um Upvote Na Discord Bot List',inline = False)
				embed_help.add_field(name="botinfo", value="Como Usar ``s!botinfo`` Veja minhas informações")
				embed_help.add_field(name="suporte", value="Como Usar ``s!suporte`` Veja meu servidor de suporte")					
				embed_help.add_field(name = 'google',value ='Como usar ``s!google <pesquisa>`` - Faça Uma Pesquisa',inline = False)
										
				embed_help.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
				embed_help.add_field(name='-----------------------', value='***<arg> obrigatorio\n[arg] opicional***')				
							
				msg = await member.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '🚀':
				await msg.delete()
				embed_help = discord.Embed(description="📙┃Menu de ajuda", color=0xff00ab)
				embed_help.add_field(name = 'dog ',value ='Como usar ``s!dog`` - foto aleatoria de um dogão',inline = False)
				embed_help.add_field(name = 'cat',value ='Como usar ``s!cat`` - foto aleatoria de um gato',inline = False)
				embed_help.add_field(name = 'votar',value ='Como usar ``s!votar <mensagem>`` - Inicie uma votação em seu servidor',inline = False)				
				embed_help.add_field(name = 'flipcoin',value ='Como usar ``s!flipcoin`` - Cara Ou Coroa',inline = False)																					
				embed_help.add_field(name='-----------------------', value='***<arg> obrigatorio\n[arg] opicional***')				
				msg = await member.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '💸':
					await msg.delete()
					embed_help = discord.Embed(description="📙┃Menu de Economia", color=0xff00ab)
					embed_help.add_field(name = 'pagar',value ='Como usar ``s!pagar <@usuário> <valor>`` - pague o seu amigo(a) usando minha econimia :)',inline = False)
					embed_help.add_field(name = 'saldo',value ='Como usar ``s!saldo`` - Veja quantos **ryucoins** Você tem!',inline = False)
					embed_help.add_field(name = 'rep',value ='Como usar ``s!rep <@usuário>`` - De um ponto de reputação a alguem',inline = False)
					embed_help.add_field(name = 'reps',value ='Como usar ``s!reps [@usuário]`` - Veja quantos pontos de reputação você (ou seu amigo) tem!',inline = False)
					embed_help.add_field(name = 'daily',value ='Como usar ``s!daily`` - Pegue Uma Recompensa Diaria',inline = False)				
					embed_help.add_field(name = 'Trabalhar',value ='Como usar ``s!trabalhar` - Trabalhe e ganhe ryucoins!',inline = False)
					embed_help.add_field(name="perfil", value="Como Usar ``s!perfil [@usuário]`` Veja seu perfil")
					embed_help.add_field(name="registro", value="Como Usar ``s!registro`` Registre-se em meu sistema")
					embed_help.add_field(name="frase", value="Como Usar ``s!frase <frase>`` Adicione Uma Frase A Seu Perfil")
					embed_help.add_field(name="sobre", value="Como Usar ``s!sobre <desc>` Adicione Uma Descrição a seu perfil")
					embed_help.add_field(name="loja", value="Como Usar ``s!loja`` Veja Meu Shop **(Ainda Não Adicionado)**")
					embed_help.add_field(name="casar", value="Como Usar ``s!casar <@usuário>`` Case com sua webnamorada! **(Ainda Não Adicionado)**")					
					embed_help.add_field(name='-----------------------', value='***<arg> obrigatorio\n[arg] opicional***')				
					msg = await member.send(embed=embed_help)
					await msg.add_reaction('⬅')							
			if emoji == '⬅':
				await msg.delete()
				msg = await member.send(embed=help_p)
				await msg.add_reaction('👮')
				await msg.add_reaction('✨')
				await msg.add_reaction('ℹ')
				await msg.add_reaction('🚀')
				await msg.add_reaction('💸')
	except asyncio.TimeoutError:
		await msg.delete() #deletar mensagem após um tempo sem resposta dos reactions
	except Exception as e:
		await msg.delete()
		print(repr(e))


bot.run(str(os.environ.get('BOT_TOKEN')))
