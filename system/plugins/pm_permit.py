 # Copyright (C) 2021 KeinShin@Github. All rights reserved
from system.plugins.inline import Friends, USER
import pandas as pd
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from system.Config.utils import hd_no, language
import re
from pyrogram import filters

from system import  *
from system.decorators import owner
from collections import Counter
from system.plugins import light

from system.datas_sqlite.pm_sqlite import (
    approve,
    approved,
    disapprove,
    approved_ as users,
    disapprove ,
    his_turn,
    update_turns,
    turn,
    insert_user,
    remove_user

)
SPAMMERS = []
LIMIT = []
SPAM_LIMIT = []


""""""



def counter(func):
      def wrapper():
       wrapper.count += 1
    # Call the function being decorated and return the result
       return func()
      wrapper.count = 0
  # Return the new decorated function
      return wrapper

DEVS = "1311769691" # more to be added
()



"""
Datas

"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

blocked =[]
def blocked_user(name):
    blocked.append(name)
@bot.on_callback_query(filters.regex(pattern="lightning_is_here_cant_spam"))
@owner
async def lightning_is_better(client, message):

    user = await app.get_users(int(message.chat.id))
    text1 = f"**Byy👋**!\n**You've been blocked have fun\n\n**If you think this is a mistake contact master via {g}**"
    app.block_user(user.id)
    blocked_user(user.first_name)
    await app.send_message(message.chat.id, text1)




urgent = []


Friends = {}

def add_friend(name, id):
    Friends.update({name: id})
def add_urgent(name):
    urgent.append(name)



@bot.on_callback_query(filters.regex(pattern="urgent"))
async def lightning_is_better(client, message):
    a = await app.get_me()
    user = await app.get_users(int(message.chat.id))

    if user.is_self :
        await message.answer("This command if for stranger not for the owner!", cache_time=0, show_alert=True)
        return
    USER = OWNER

    name = user.first_name
    bhat = user.status  
    text1 = "**Hello User {},  master was last online on {}**\n**Kindly wait for him to be online :)** ".format(name, bhat)
    await app.send_message(message.chat.id, text1)
    await app.send_message(
        Variable.LOGS_CHAT_ID,
        f"**Hello {USER}, [{name}]({user.id}) wants to dicuss something important!.**",
    )
    if user.is_deleted:
     return
    add_urgent(name)






@bot.on_callback_query(filters.regex(pattern="he_sucks"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    o = await app.get_me()
    owner = await app.get_users(int(o.id

    ))
    user_id = user.id
    await message.edit(f"**Hello {user.first_name} if u are friend kindly contact him via {g}**\n\n__{USER}:- was last online on__ {owner.last_online_date}")

    
    
    
    
    
    




@bot.on_callback_query(filters.regex(pattern="fck_ask"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    bot_id = await bot.get_me()
    bot_id = bot_id.id
    await message.edit
    btn =InlineKeyboardMarkup([[InlineKeyboardButton("Contact Him", url=f"tg://user?id={bot_id}")]])

    await app.send_message(
        user.id,
        f"Master is busy for some reason contact him via bot link given below",
        reply_markup=btn,
    )
print(users)

          


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Decorate foo() with the counter() decorator
@counter
@app.on_message(filters.private & ~filters.edited & ~filters.me)
async def pm(client, message: Message):
    sed = ""

    mister = await app.get_users(int(message.chat.id))
    insert_user(message.chat.id)
    update_turns(message.chat.id)
    if DELETE_MSG == "on":
    
     await app.delete_messages(message.chat.id, message.message_id, revoke=True)
     return
    sed_user = users

    if mister.id in sed_user:
        return
        

    if mister.is_bot:
        return
    if mister.is_contact:
        return
    if mister.is_mutual_contact:

    
        return
    if str(mister.id) in  DEVS and not  str(mister.id) in users:
        await app.send_message(message.chat.id, "**Dev Detected in pm, approved**")
        approve(mister.id)
        return
    if mister.is_scam:
        alt = language('ALERT')
        scm = language('SCAMMER')
        await bot.send_message(chet, f"__{alt}__!\n**{scm} [{mister.first_name}]({mister.id}) IN PM**")
        await app.send_message(message.chat.id, f"{language('Scammer Alert! Therefore blocked and informed master!')}")
        await app.block_user(message.chat.id)
        return
    # if message.chat.is_fake:
    #     await app.send_message(message.chat.id, f"**{language('FAKE ID ALERT')}!--")

    #     return
    try:
     turns = turns = turn(message.chat.id)[str(PM_LIMIT)]

    except KeyError:
     turns = None
    if f'{message.chat.id}' in turns and not f'{message.chat.id}' in users:

 
      await app.send_message(message.chat.id, f"__I warned you {PM_LIMIT} times now its time for action byy__\n\n**BLOCKED**")
 
      await app.block_user(message.chat.id)
      return

    if user_abused(message.text) and not mister.id in users :
    
      await app.send_message(message.chat.id, f"**ABUSE DETECTED! SO BLOCKED FROM PM :)**\n\n__If you think it's mistake use__ {g}")
      await app.block_user(mister.id)
      return

    if f'{message.chat.id}' in users:
        return
      
    mkp = [
          [
              InlineKeyboardButton(
                  text="Query", callback_data=f"fck_ask"
              )
          ],
          [
           InlineKeyboardButton(
                  text="Urgent", callback_data=f"urgent"
              )
          ],
          [
           InlineKeyboardButton(
                  text="Friend", callback_data=f"he_sucks"
              )
          ],
      ]
       
    if PM_PERMIT.endswith(".mp4"):
        await app.send_video(message.chat.id, PM_PERMIT, caption=Variable.PM_SECURITY_MSG, reply_markup=InlineKeyboardMarkup(mkp))
    elif PM_PERMIT.endswith(".png") or PM_PERMIT.endswith(".jpg"):
        await app.send_photo(message.chat.id, PM_PERMIT,  caption=Variable.PM_SECURITY_MSG, reply_markup=InlineKeyboardMarkup(mkp) )



@light.on(["a","ap", "approve"])
async def ap(client, message: Message):

       try:

        #   await message.edit(f"**{language('APPROVED! USER')} USER** - {id}")
        #   approve(id)
          if  message.reply_to_message:
            await message.edit(f"**{language('APPROVED! USER')} USER** - {message.reply_to_message.from_user.id}")
            approve(message.reply_to_message.from_user.id)
            try:
               turns = turn(message.chat.id)[str(PM_LIMIT)]
            except KeyError:
              turns = False
          elif " " not in  message.text:
            await message.edit(f"**{language('APPROVED! USER')} USER** - {message.chat.id}")
            approve(message.chat.id)
          else:
            name = message.text.split()[1]
            await message.edit(f"**{language('APPROVED! USER')}** - NAME {name}")
       
            approve(name)
       except BaseException as e:
            await message.edit(e)



def user_abused(txt):
    # sed=predict_prob([txt])
    # if sed > 0.5:
    #     return True
    # else:
    #     return False

    # return None
    pass

@light.on(["da", "disap", "disapprove"])
async def dis(client, message: Message):
    turns = turns = turn(message.chat.id)[str(PM_LIMIT)]
    if " " not in message.text:


      await message.edit(f"{language('DISAPPROVED USER - ')} {message.chat.id}")
      disapprove(message.chat.id)
      users.remove(f'{message.chat.id}')

    elif      message.reply_to_message:
      await message.edit(f"**{language('DISAPPROVED USER - ')}** - {message.reply_to_message.from_user.first_name}")

      disapprove(message.reply_to_message.from_user.id)
      users.remove(f'{message.chat.id}')
    elif " " in message.text:
      name = message.text.split()[1]
      await message.edit(f"**{language('DISAPPROVED USER - ')}** - {name}")
      users.remove(f'{message.chat.id}')

      disapprove(message.chat.id)
@light.on(["listapprovd"])
async def list(client, message):
    
    noice=users
    await app.send_message(message.chat.id, f"**{language('USERS - APPROVED')}**\n\n__{noice}__")


 
# def approve(id, turn):

COMMAND_HELP.update({
    "pm_permit": f"`{HNDLR}approve or a `\
    \n`{HNDLR}da or disapprove`\
    \n`{HNDLR}listapprovd`",
    "pm_permit's help": f"`{HNDLR}approve or a `\
    \n**USE**: __Approves user to your pm means he or she can pm you!__\
    \n\n`{HNDLR}da or dispprove\
    \n**USE**: __Disapproves user from your pm!__ `\
    \n\n{HNDLR}listapprovd\
    \n**USE**: __approves user to your pm__"
})
