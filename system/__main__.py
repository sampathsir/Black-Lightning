# Copyright (C) 2021 KeinShin@Github.
import subprocess

import os.path
import sys

from setup.importer import Start
import pickle as yum
import logging 
import sys, traceback

import schedule
from pyrogram.handlers import MessageHandler
import system
from pyrogram import idle
from pyrogram.errors import *
from system.Config.utils import Variable
from pyrogram.raw.types import BotCommand
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
import holidays
from datetime import date, datetime
if Variable.COUNTRY:
    
   hol  = holidays.CountryHoliday(Variable.COUNTRY)
else:
   hol = holidays.CountryHoliday("IN", prov="AS")
a = date.today()
p  =hol.get(a)



plugin =  logging.getLogger("PLUG-ERROR")
bot_lod =  logging.getLogger("BOT-ERROR")


from system.__init__ import app, bot



chet = Variable.LOGS_CHAT_ID


USER = str(Variable.OWNER_NAME)

async def easter():
    # if Variable./
    est=yum.load("easters.dat", "rb") # for easters!
    if len(est)==7:
        await bot.send_message(chet, "**Congo**, **You have unlocked all the easters of this userbot gib party sir** 🎉🎆")

async def holydays():
    if p:
        await bot.send_message(chet, f"Happy {p} Master ✨🎉☺")
    else:
        return None


schedule.every().day.at("12:00").do(holydays)



async def add_bot_to_logg_grup(client, message):
    try: 

        await bot.join_chat(chet)
        text = f"BLACK USERBOT is deployed."

        await bot.send_message(chet, text)
    except BaseException:

        logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
        pass
        


# import glob
# import importlib



import logging
import os
import importlib
import pyrogram
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)


from  system import bot, app

def o():
    try:
        a = Start("system/plugins/")
        for  i in a.x:
             a.pat = i.replace(".py", "")   
             a.boot()
             logging.info("IMPORTED PLUGINS- {}".format(i))
        a = Start("system/user_bot_assistant/")
        for  i in a.x:
             a.pat = i.replace(".py", "")   
             a.boot()
             logging.info("IMPORTED ASISSTANT MODULE- {}".format(i))
    except ImportError:
    
     s=sys.exc_info()
     logging.error(f"ERROR - {s}")
     pass
    except ModuleNotFoundError:
     s=sys.exc_info()
     logging.error(f"ERROR - {s}")
     pass
    except BaseException:
       yo=traceback.TracebackException(*sys.exc_info())#type(e).__class__, e, e.__traceback__)
       name=yo.filename
       no = yo.lineno
       line = yo.lineno
       type_=yo.exc_type
       print(name, " ", no)
       logging.info(f"There is an error - {type_} in file {name} line {no} - {line}, In order to prevent crash it has been renamed and plugins based on this file wont work!")
       logging.info("Contact @lightning_support_group When to update!")
       filename_ = name.replace(".py", ".txt")
       os.rename(name, filename_)
       os.remove(name)
       pass

def call():
    o()
    
    try:
        try:   
       
          bot.start()
          bot.join_chat(chet)
          text = f"BLACK USERBOT has benn deployed."
          bot.send_message(chet, text)
        except BaseException:
           logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
           pass
        except SessionExpired:
            logging.info("Your String Session is not valid create a new one for more contact @lightning_support_group, till bot stopped")
            exit()
            
        except SessionRevoked:
             logging.info("Bot Father Api Token Revoked replace old with new one till bot stopped")
             exit()
        except AuthKeyDuplicated:
             logging.error("You can not use same token in two or more apps/client, stop one token!")
             exit()
        except AccessTokenInvalid:
            logging.error("Bot token expired or not valid create new one.")
            exit()
        except AccessTokenInvalid:
            logging.error("Bot token not valid")
            exit()
        try:
         app.run() 
        except SessionRevoked:
           logging.error("String Session Revoked or Terminated! Create a new one")
           exit()
        except SessionExpired:
            logging.info("Your String Session is not valid create a new one for more contact @lightning_support_group, till bot stopped")
            exit()
        except AuthKeyDuplicated:
             logging.error("You can not use same strings in two or more apps/client, terminate one of create another")
             exit()
    
    except ApiIdInvalid:
        logging.error("The Given Api Id is invalid,  grab ur Id from my.telegram.org Now!")
        exit()
    logging.info(f"© Black-Lightning - KeinShin, All  rights Reserved.")
    logging.info(f"Plugins and Whole System Loaded!, do {system.HNDLR}alive to check!")
    logging.info(f"Also add assistant to log channel to access more features!")
    idle()
 

app.loop.run_until_complete(call())

