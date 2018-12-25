import discord
import asyncio
import youtube_dl
from discord.ext import commands

TOKEN = 'NTEyNjk1MzI1NjU2NDgxODA2.DwK9CA.O2ZCvtcdaLDwBDL8_S2FbMJcgpg'	

client = commands.Bot(command_prefix = 't!')

@client.event
async def on_ready():
    while True:
        await client.change_presence(game=discord.Game(name='Karaoke no The World Of Bad'))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name="🎉 Fui desenvolvido pelo 彡★ｲЩ乃★彡 Brahma#1111👑", type=1))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='Musica com meu criador!', type=2))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='Quer ser staff? chame o meu criador 彡★ｲЩ乃★彡 Brahma#1111 No Pv!', type=3))
        await asyncio.sleep(20)
print('Bot online')
	
@client.event
async def on_member_join(member):
  canal = client.get_channel("495700015801434122")
  regras = client.get_channel("495700015801434122")
  msg = "{} entrou no servidor! Leia nossas regras e divirta-se em nossos chats".format(member.mention, regras.mention)
  await client.send_message(canal, msg) 

@client.event
async def on_member_remove(member):
   canal = client.get_channel("495700015801434122")
   msg = "Adeus,Te vejo no paraiso! {}".format(member.mention)
   await client.send_message(canal, msg)
	
@client.command(pass_context=True)
async def clear(ctx, limit: int=100):
    async for msg in client.logs_from(ctx.message.channel, limit= 10):
 
            try:
                await client.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description=" As mensagens foram deletadas com sucesso! :smile:", color=0x00ff00)
    await client.say (embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
	await client.kick(userName)
	print ("user has kicked")
   
 
@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
	await client.ban(userName)
	print("user has banned")

@client.event
async def on_server_join(server):
	stay = False
	admin = None
	channel = bot.get_channel("495747382051602433")
	for member.id in config.client_admin:
		admin = member.mention

        
        

	


@client.event
async def on_message(message):
    if message.content.lower().startswith("t!ping"):
 
            t1 = time.perf_counter()
            async with on_message.channel.typing():
                t2 = time.perf_counter()
                ping_embed = discord.Embed(color=0xFFA500, description='**🏓Pong!**\n'
                                                                       '** Meu Tempo de resposta é `{}ms`!**'.format(round((t2 - t1) * 1000)))
    await client.process_commands(message)
    
    
    
players = {}
COR = 0xF7FE2E

@client.event
async def on_message(message):
    if message.content.startswith('t!entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal de voz e a musica parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não esta em nenhum canal de voz.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('t!play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))




    if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))


	
client.run('NTEyNjk1MzI1NjU2NDgxODA2.DwK9CA.O2ZCvtcdaLDwBDL8_S2FbMJcgpg')
