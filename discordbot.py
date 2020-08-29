# インストールした discord.py を読み込む
import discord
import os
import asyncio
import time

# アクセストークン(Botの)
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#serverID
ServerID=int(739996326665912320)
server=client.get_guild(ServerID)

#ChannnelID List
ID_SELF_MEN=int(739996327336869948)
ID_SELF_WOMEN=int(739996327336869949)
ID_BUMP_ROOM=int(739996331355013130)

#RoleID List
SELF_ROLE_ID=int(739996326871171148)
M_ROLE_ID=int(739996326779158538)
F_ROLE_ID=int(739996326737084575)
FR_ROLE_ID=int(739996326779158539)
VWAU_ROLE_ID=int(739996326737084567)

@client.event
async def on_ready(): #Bot起動準備完了時
  ChannelID = int(739996326909182036) #送信するチャンネルID
  channel = client.get_channel(ChannelID)
  await channel.send("Ready")
#   Linvite=server.invites()
#   await channel.send("await invite")
#   await channel.send(Linvite)
  await channel.send("Return")

# @client.event
# async def on_member_join(member):
#   a_invite_B=0;a_invite_C=0;a_invite_D=0;
#   Linvite=await invites()
#   a_invite_B=Linvite[0].max_uses
#   a_invite_C=Linvite[1].max_uses
#   a_invite_D=Linvite[2].max_uses
#   if a_invite_B!=invite_B:
#     role = guild.get_role(ID)
#     await member.add_roles(role)
#   elif a_invite_C!=invite_C:
#     role = guild.get_role(ID)
#     await member.add_roles(role)
#   elif a_invite_D!=invite_D:
#     role = guild.get_role(ID)
#     await member.add_roles(role)
#   else:
#     role = guild.get_role(ID)
#     await member.add_roles(role)
#   invite_B=a_invite_B
#   invite_C=a_invite_C
#   invite_D=a_invite_D


@client.event
async def on_message(message): #message受信時
  #clear
  if message.author.bot: #Botだった場合は反応しない
    return

  #clear
  if message.channel.id == ID_BUMP_ROOM and message.content == "!d bump": #disboardのbumpコマンド実行時&チャンネル指定
    await asyncio.sleep(7200)
    await message.channel.send("<@&740293083089993748> remind 2hours") #remind bump用ロール
    return

  
  if message.channel.id == ID_SELF_MEN or message.channel.id == ID_SELF_WOMEN: #自己紹介(男or女)のチャンネル
    await message.channel.send("responce")
    member = client.get_user(int(message.author.id))
    role = server.get_role(SELF_ROLE_ID)
    await message.channel.send("responce")
    await member.add_roles(role) #自己紹介済みのロールID
    await message.channel.send("responce")
    if message.channel.id == ID_SELF_MEN:
      role = server.get_role(M_ROLE_ID)
      await member.add_roles(role) #m
      return member
    else:
      role = server.get_role(F_ROLE_ID)
      await member.add_roles(role) #f
      role = server.get_role(FR_ROLE_ID)
      await member.add_roles(role) #fr
      return member

@client.event
async def on_member_update(before, after):#Member情報変更時に呼び出し
  if before.member.roles == after.member.roles: #更新前と更新後のロールが同じ
    return
  
  vwau='vwau' in after.member.roles.name
  nvwau='nvwau' in after.member.roles.name
  if vwau:
    if nvwau:
      role = guild.get_role(VWAU_ROLE_ID)
      await member.remove_roles(role) #vwauのロールID
      return member
  else:
    if not nvwau:
      role = guild.get_role(VWAU_ROLE_ID)
      await member.add_roles(role) #vwauのロールID
      return member

  R18='R18NG' in after.member.roles.name
  fr='fr' in after.member.roles.name
  if fr and R18:
    role = guild.get_role(FR_ROLE_ID)
    await member.remove_roles(role)
    return member


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
