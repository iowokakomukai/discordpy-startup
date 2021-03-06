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

#ChannnelID List
ID_SELF_MEN=int(739996327336869948)
ID_SELF_WOMEN=int(739996327336869949)
ID_BUMP_ROOM=int(739996331355013130)
ID_IN_ROOM=int(742916745337110578)
ID_START_ROOM=int(742916745337110578)

#RoleID List
SELF_ROLE_ID=int(739996326871171148)
M_ROLE_ID=int(739996326779158538)
F_ROLE_ID=int(739996326737084575)
FR_ROLE_ID=int(739996326779158539)
VWAU_ROLE_ID=int(739996326737084567)
NVWAU_ROLE_ID=int(739996326737084566)
B_ROLE_ID=int(751477448503328898)
C_ROLE_ID=int(751477451556913253)
D_ROLE_ID=int(751477456640409625)
I_ROLE_ID=int(751477458724978818)

#global
# invite_B=4;invite_C=15;invite_D=2

#clear
@client.event
async def on_ready(): #Bot起動準備完了時
  channel = client.get_channel(ID_START_ROOM)
  await channel.send("Ready")

#clear
@client.event
async def on_member_join(member):
#   global invite_B
#   global invite_C
#   global invite_D
  user = client.get_user(member.id)
  server=client.get_guild(ServerID)
  channel = client.get_channel(ID_IN_ROOM)
  B_invite_B=0;C_invite_C=0;D_invite_D=0
  Linvite=await server.invites()
  for item in Linvite :
    if "2z8DQQQ" in str(item) :
        C_invite_C=item.uses
    elif "96EqWqK" in str(item) :
        B_invite_B=item.uses
    elif "dnGcKws" in str(item) :
        D_invite_D=item.uses
#   if B_invite_B!=invite_B:
#     role = server.get_role(B_ROLE_ID)
#     await member.add_roles(role)
#   elif C_invite_C!=invite_C:
#     role = server.get_role(C_ROLE_ID)
#     await member.add_roles(role)
#   elif D_invite_D!=invite_D:
#     role = server.get_role(D_ROLE_ID)
#     await member.add_roles(role)
#   else:
#     role = server.get_role(I_ROLE_ID)
#     await member.add_roles(role)
#   invite_B=B_invite_B
#   invite_C=C_invite_C
#   invite_D=D_invite_D
  txt1=str(user.name)+"#"+str(user.discriminator)
  txt2=str(B_invite_B)+"."+str(C_invite_C)+"."+str(D_invite_D)
  await channel.send(txt1)
  await channel.send(txt2)

#clear
@client.event
async def on_message(message): #message受信時
  if message.author.bot: #Botだった場合は反応しない
    return

  if message.channel.id == ID_BUMP_ROOM and message.content == "!d bump": #disboardのbumpコマンド実行時&チャンネル指定
    await asyncio.sleep(7200)   #2時間待つ
    await message.channel.send("<@&740293083089993748> remind 2hours") #remind bump用ロール
    return

  if message.channel.id == ID_SELF_MEN or message.channel.id == ID_SELF_WOMEN: #自己紹介(男or女)のチャンネル
    member = message.channel.guild.get_member(message.author.id)
    role = message.guild.get_role(SELF_ROLE_ID)
    await member.add_roles(role) #自己紹介済みのロールID
    if message.channel.id == ID_SELF_MEN:
      role = message.guild.get_role(M_ROLE_ID)
      await member.add_roles(role) #m
      return member
    else:
      role = message.guild.get_role(F_ROLE_ID)
      await member.add_roles(role) #f
      return member

#clear
@client.event
async def on_member_update(before, after):#Member情報変更時に呼び出し
  if before.roles == after.roles: #更新前と更新後のロールが同じ
    return
  
  vwau=False;nvwau=False
  
  for item in after.roles :
    if str(item)=='vwau' :
        vwau = True
        #該当する要素が見つかった時点でブレイク。
        break
  for item in after.roles :
    if str(item)=='nvwau' :
        nvwau = True
        #該当する要素が見つかった時点でブレイク。
        break
  
  role = after.guild.get_role(NVWAU_ROLE_ID)
  if vwau:
    if nvwau:
      await after.remove_roles(role) #vwauのロールID
      return after
  else:
    if not nvwau:
      await after.add_roles(role) #vwauのロールID
      return after

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
