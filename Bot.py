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


bot = commands.Bot('st!', owner_id=528782261315698718)
print (discord.__version__)



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
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Sendo Desenvolvido 👷"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="s!invite - Me Adicione Em Seu Servidor s!vote - me ajude dando um upvote"))
		await asyncio.sleep(20)
		await bot.change_presence(activity=discord.Activity(name="Minha versão: 2.1"))
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
    
@bot.command(pass_context=True)
async def registro(ctx):
       try:
         mongo = MongoClient(url)
         tutorial = mongo["tutorial"]
         rpg = tutorial["rpg"]
         rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
         if rpg is None:
            usuario = {"_id":str(ctx.author.id),"usuario":str(ctx.author.name), "coins":0}
            tutorial.rpg.insert_one(usuario).inserted_id
            await ctx.send(f"Olá {ctx.author.mention}, você foi registrado no banco de dados com sucesso!")
         else:
           await ctx.send(f"Olá {ctx.author.mention}, você já está registrado no banco de dados!")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")
 
 
@bot.command(pass_context=True, aliases=['coins'])
async def saldo(ctx):
       try:
         mongo = MongoClient(url)
         tutorial = mongo["tutorial"]
         rpg = tutorial["rpg"]
         rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
         if rpg is None:
           await ctx.send(f"Olá {ctx.author.mention}, você não está registrado no sistema de coins, use !registro para se registrar!")
         else:
         	moedas = rpg["coins"]
         	await ctx.send(f"Olá, {ctx.author.mention}, você tem {moedas} zcoins.")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")
    
@bot.command(pass_context=True, aliases=['topcoins'])
async def coinstop(ctx):
        mongo = MongoClient(url)
        tutorial = mongo["tutorial"]
        rpg = tutorial["rpg"]
        top = rpg.find().sort('coins', pymongo.DESCENDING).limit(1000)
        valores = {}
        users = {}
        index = 1
        texto = []
        rank = []
        for valor in top:
          count = len(rank)
          simb = "count°"
          numero = f"{count}{simb}"
          simbolo = str(numero).replace("0count°", "🥇 **1°**").replace("1count°","🥈 **2°**").replace("2count°","🥉 **3°**").replace("3count°","🏅 **4°**").replace("4count°","🏅 **5°**").replace("5count°","🏅 **6°**").replace("6count°","🏅 **7°**").replace("7count°","🏅 **8°**").replace("8count°","🏅 **9°**").replace("9count°","🏅 **10°**")
          url = f"{simbolo} : <@{valor['_id']}> - ({valor['coins']})"
          rank.append(url)
           

        url = "\n".join(rank)
        embed=discord.Embed(description=url, color=0x7BCDE8)
        embed.set_author(name="Top rank dos RyuCoins", icon_url=ctx.author.avatar_url_as())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/519287277499973632/522607596851691524/icons8-leaderboard-100.png")
        await ctx.send(embed=embed)
		
@bot.command(pass_context=True)
async def servers(ctx):
	servers = list(bot.guilds)
	await ctx.send("Estou conectado em " + str(len(bot.guilds)) + " servers:")
	for x in range(len(servers)):
		await ctx.send(" "+servers[x-1].name)

@bot.command(pass_context=True)
@commands.is_owner()
async def setcoins(ctx, member:discord.Member=None, coins:int=None):
       try:
         mongo = MongoClient(url)
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
          mongo = MongoClient(url)       
          tutorial = mongo["tutorial"]
          rpg = tutorial["rpg"]
          rpg = tutorial.rpg.find_one({"_id":str(ctx.author.id)})
          if rpg is None:
            await ctx.send('Você não esta registrado digite `s!registro` para se registrar')
        
          else:
              coins = random.randint(500, 1800)
              moedas = int(rpg["coins"])+ int(coins)
              tutorial.rpg.update_one({"_id":str(ctx.author.id)}, {"$set":{"coins":int(moedas)}})
              await ctx.send(f"💸 {ctx.author.mention}, você ganhou {coins} ryuCoins diários.")
       except Exception as e:
           await ctx.send(f"[Erro] {e}")
@daily.error
async def daily_error(ctx,error):
     if isinstance(error, discord.ext.commands.CommandOnCooldown):
       min, sec = divmod(error.retry_after, 60)
       h, min = divmod(min, 60)
       if min == 0.0 and h == 0:
           await ctx.send('**Espere `{0}` segundos para usar o comando novamente.**'.format(round(sec)))
       else:
           await ctx.send('**Espere `{0}` horas `{1}` minutos  e `{2}` segundos para usar o comando novamente.**'.format(round(h),round(min),round(sec)))						

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
           await ctx.send('**Espere `{0}` segundos para usar o comando novamente.**'.format(round(sec)))
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
		
@bot.command()
async def vote():
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
	
			
					
import datetime	
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.User=None):
    user = user or ctx.message.author
    embed = discord.Embed(title="informações de {}".format(user.name), color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="👨 Nome", value=user.name, inline=True)
    embed.add_field(name="🎭 Apelido", value=user.nick)
    embed.add_field(name="💻 ID", value=user.id, inline=True)
    embed.add_field(name="📱 Status", value=user.status, inline=True)
    embed.add_field(name="🎮 Jogando", value=user.game)
    embed.add_field(name="🔝 Melhor cargo", value=user.top_role)
    embed.add_field(name="📆 Entrou aqui em", value=user.joined_at.strftime("%d %b %Y ás %H:%M"))
    embed.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print('comando attlogs digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def invite(ctx):
    e = discord.Embed(description='{} **Olá Para Me Adicionar Em Seu Servidor Clique [aqui](https://discordapp.com/oauth2/authorize?client_id=539468157291855903&permissions=8&scope=bot) | Poderia Me Ajudar Dando Um Upvote? Clique [aqui](https://discordbots.org/bot/539468157291855903/vote)**'.format(ctx.message.author.mention), color=0xff0f00)
    await ctx.send(embed=e)
    print('comando invite digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' Serverinfo".format(ctx.message.guild.name), color=0x00fA00)
	embed.add_field(name="📄 Nome do Servidor", value=ctx.message.guild.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.guild.owner));
	embed.add_field(name="💻 ID do servidor", value=ctx.message.guild.id, inline=True)
	embed.add_field(name="🎓 Total de roles", value=len(ctx.message.guild.roles), inline=True)
	embed.add_field(name="👥 Total de Membros", value=len(ctx.message.guild.members))
	embed.add_field(name='🌎 Região', value=ctx.message.guild.region)
	embed.set_thumbnail(url=ctx.message.guild.icon_url)
	await ctx.send(embed=embed)


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
    	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
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
    embed.add_field(name='👥 Usuário', value=ember)
    embed.add_field(name='💻 Id', value=ember.id)
    
    await ctx.send(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
  	


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
	
			


@bot.command(pass_context=True, aliases=['clear','limpar'])
async def purge(ctx, amount:int=None):
	if not ctx.author.guild_permissions.manage_messages:
		rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
		rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
		return await ctx.send(embed=rcat)
	if amount == None:
		apurge = discord.Embed(title='Erro', description='Você Deve Adicionar Uma Quantidade De Mensagens Para serem deletadas', color=0xFF0000)
		apurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
		return await ctx.send(embed=apurge)
		await ctx.channel.purge(limit=amount+1)
		spurge = discord.Embed(title='Purge', description=f'{ctx.message.author.mention} has purged {amount} messages!', color=0x00FF00)
		spurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
		await ctx.send(embed=spurge)
    

   

    
@bot.command(pass_context = True)
async def modajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 's!kick ',value ='como usar ``s!kick @usuário <motivo>`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = 's!ban ',value ='Como usar ``s!ban @usuário <motivo>`` bane o usuário marcado',inline = False)
    embed.add_field(name = 's!addrole ',value ='Como usar ``s!setcargo @cargo @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 's!removerole',value ='Como usar ``s!removercargo @cargo @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 's!clear',value ='Como usar ``s!clear <quantidade>`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 's!avisar',value ='Como usar ``s!avisar @usuário <mensagem>`` avisa um usuário no PV ',inline = False)


    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando modajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
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
    
    
   
   
@bot.command(pass_context=True)
async def diversaoajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 's!dance ',value ='Como usar ``s!dance`` dance com algum usuário',inline = False)
    embed.add_field(name = 's!beijar ',value ='Como usar ``s!beijar @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = 's!abraçar ',value ='Como usar ``s!abraçar @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = 's!flipcoin ',value ='Como usar ``s!flipcoin`` Cara ou coroa?',inline = False)
    embed.add_field(name = 's!deathnote ',value ='Como usar ``s!deathnote @usuário <causa da morte>`` Escreva o nome de determinado usuário em seu Death Note ',inline = False)
    embed.add_field(name = 's!avatar ',value ='Como usar ``s!avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="s!meme", value="como usar ``s!meme`` que tal ver alguns memes?!", inline=False)
    embed.add_field(name="s!ping", value="como usar ``s!ping`` Veja meu tempo de resposta!", inline=False)
    embed.add_field(name="s!userinfo", value="como usar ``s!userinfo @usuário`` Veja o perfil de um determinado usuário!", inline=True)
    embed.add_field(name="s!voadora", value="como usar ``s!voadora @usuário`` de uma voadora em alguem!", inline=True)
    embed.add_field(name="s!brigar", value="como usar ``s!brigar @usuário`` Use esse comando se alguem estiver merecendo apanhar!", inline=True)  	
    embed.add_field(name="s!matar", value="como usar ``s!matar @usuário`` Use esse comando se alguem estiver merecendo!", inline=True)
    embed.add_field(name="s!tapa", value="como usar ``s!tapa @usuário`` Use esse comando se alguem estiver merecendo levar uns tapa cabuloso", inline=True)
    embed.add_field(name="s!falar", value="como usar ``s!falar <mensagem>`` Faça eu falae alguma coisa!", inline=True)
    embed.add_field(name="s!suicidio", value="como usar ``s!suicidio`` Se Suicida", inline=True)
    embed.add_field(name="s!kepiada", value="como usar ``s!kepiada`` Que tal uma piada?!", inline=True)
    embed.add_field(name="s!atacar", value="como usar ``s!atack @usuário`` use este comando para atacar alguem!", inline=True)
    embed.add_field(name="s!chorar", value="como usar ``s!chorar`` Chorar faz bem para os olhos...", inline=True)
    embed.add_field(name="s!votar", value="como usar ``s!votar`` Faça uma votação em seu servidor", inline=True)
    embed.add_field(name="s!pergunta", value="como usar ``s!pergunta`` me faça uma pergunta!", inline=True)
    
        
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando diversaoajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))  
      
@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Ação | Chorar',  description='😭|**{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await ctx.send(embed=hugemb)
	print('comando chorar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))    
	
@bot.command(name="h", aliases=['ajuda'])
async def help(ctx):
	member = ctx.message.author
	help_p = discord.Embed(description='Menu de ajuda\n\nModeração = 👮\nAções = ✨')
	msg = await member.send(embed=help_p)
	await msg.add_reaction('👮')
	await msg.add_reaction('✨')
	await ctx.send(f'{member.mention} Verifique Suas Mensagens Privadas.')
	try:
		while True:
			reaction, user = await bot.wait_for("reaction_add", timeout=360, check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id)
			emoji = str(reaction.emoji)
			if emoji == '👮':
				await msg.delete()
				embed_help = discord.Embed(description="📙┃Menu de ajuda Moderação")
				msg = await member.send(embed=embed_help)
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

bot.run(str(os.environ.get('BOT_TOKEN')))
