#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  TOOLS IS BASED IN
  CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
  Copyright (C) 2020  

  DISCLAIMER: This file is for informational and educational purposes only. 
  We are not responsible for any misuse applied to it. All responsibility falls on the user

  ||================================================================================||
  || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
  ||================================================================================||

  Adapted BY lanniscaf ALL RIGHTS RESERVED
  """
from generator_with_license2 import Tools, Log
from extrapola import *
from binlookup import bincheck
from datetime import datetime, timedelta

import logging
import os
import json

from telegram import ParseMode, ChatPermissions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

clavesecreta = 'token'


TOKEN = clavesecreta
PORT = int(os.environ.get('PORT', '8443'))
def start(update, context):
    userName = '{}'.format(update.message.from_user.first_name)
    update.message.reply_text('`Hola {}! Gracias por la preferencia, para visualizar los comandos del BOT, por favor mande el comando` */help*\n\n\n`Si quieres incluir este BOT a tu grupo sientete libre de hacerlo y/o si quieres ver el codigo fuente o aportar contacta a mi dueño (INFO EN MI BIO)`'.format(userName), parse_mode=ParseMode.MARKDOWN)
# //  utils:
def getFutureDate(days):
    double = days / 1
    return (datetime.now() + timedelta(days= double))
def help(update, context):
    message = '\t`匚ㄖ爪卂几ᗪㄖ丂`\n\n*-* /gen <bin> <more bins> _- Genera tarjetas basado en 1 o mas bins_ \n\n*-* /extra <cc> <cc2> _- Extrapola tarjetas basado en 1 o 2 ccs_ \n\n*-* /bin <bin> _- Busca informacion de un bin_'
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
def generator(update, context):
    params = context.args
    if(params == []):
        update.message.reply_text('*[X]* Pase un bin valido: /gen <bin> <optional bins>', parse_mode=ParseMode.MARKDOWN)
        return False
    __genUtils = Tools()
    __response = __genUtils.ccgenFromList(params)
    message = '*< --- + 𝔗𝔞𝔯𝔧𝔢𝔱𝔞𝔰 𝔊𝔢𝔫 + --- >*\n'
    for c in __response:
        message += '`{}`\n'.format(c)
    reply = update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    
def extras(update, context):
    extrautils = Extrapola()
    params = context.args
    try:
        bin1 = params[0]
    except:
        update.message.reply_text('*[X]* *Uso incorrecto:* /extra <cc> <cc>', parse_mode=ParseMode.MARKDOWN)
    try:
        bin2 = params[1]
    except:
        pass
    extrautils.bin1 = bin1
    try:
        extrautils.bin2 = bin2
    except:
        pass
    result = extrautils.extrapolarTodo()
    if(result == False):
        update.message.reply_text('Error', parse_mode=ParseMode.MARKDOWN)
        return False
    
    message = '*<--- [+] 𝔈𝔵𝔱𝔯𝔞𝔭𝔬𝔩𝔞𝔡𝔞𝔰 [+] --->*\n\n'
    for key, value in result.items():
        if(key == 'similitud'):
            message += '*Similitud* `-->{}`\n'.format(value)
            continue
        elif(key == 'bank'):
            message += '*Sofia*     `-->{}`\n'.format(value)
            continue
        elif(key == 'advance'):
            message += '*Avanzado*  `-->{}`\n'.format(value)
            continue
        message += '*{0}*       `-->{1}`\n'.format(key,value)
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    return False
def lookup(update, context):
    try:
        arg = context.args
        res = bincheck(arg[0])
        message = ''
        for k,v in res.items():
            message += '*{}:* `{}`\n'.format(k,v)
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    except:
        update.message.reply_text('*[X]* `Error`', parse_mode=ParseMode.MARKDOWN)
def textCommands(update, context):
    message = update.message.text
    if(message[:4] in ['!bin']):
        mensajes = message.split()
        res = bincheck(mensajes[1])
        message = ''
        for k,v in res.items():
            message += '*{}:* `{}`\n'.format(k,v)
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
        return False
    elif(message[:4] in ['!gen']):
        mensajes = message.split()
        __genUtils = Tools()
        res = __genUtils.ccgenFromList([mensajes[1]])
        message = '*< --- + 𝔗𝔞𝔯𝔧𝔢𝔱𝔞𝔰 𝔊𝔢𝔫 + --- >*\n'
        for c in res:
            message += '`{}`\n'.format(c)
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
        return False
def isAdmin(update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.from_user.id
    chat_member = context.bot.getChatMember(chat_id, user_id)
    level = chat_member.status # // member | creator | admin
    if level in ('creator','admin'):
        return  True
    elif level in ('member'):
        return False
    else:
        return True  
def ban(update, context):
    chat_id = update.effective_chat.id
    try:
        user = update.message.reply_to_message.from_user
    except:
        update.message.reply_text('Para banear a un usuario debes primero responderle. /ban <motivo>')
        return False
    try:
        motivo = update.message.text[5:]
    except:
        motivo = 'Motivo no especificado'
    if(isAdmin(update, context) == False):
        return False
    try:
        context.bot.kickChatMember(chat_id, user.id)
        update.message.reply_text('`Se ha baneado a` *{}*.\n\n`Motivo:` _{}_'.format(user.first_name, motivo), parse_mode=ParseMode.MARKDOWN)
    except:
        update.message.reply_text('`No he podido banear a` *{}*. :('.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
def mute(update, context):
    chat_id = update.effective_chat.id
    permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_polls=False, can_send_other_messages=False, can_add_web_page_previews=False, can_change_info=False, can_invite_users=False, can_pin_messages=False)
    infinito = False
    try:
        user = update.message.reply_to_message.from_user
        if( context.args[0] == None):
            date= 390
            infinito = True
        else:
            date = int(context.args[0])
    except:
        update.message.reply_text('`Para mutear a un usuario debes primero responderle.` /mute <dias>', parse_mode= ParseMode.MARKDOWN)
        return False
    if(isAdmin(update, context) == False):
        return False
    try:
        fecha = getFutureDate(date)
        context.bot.restrictChatMember(chat_id, user.id, permisos, until_date= fecha)
        #context.bot.deleteMessage(chat_id, update.message.reply_to_message.message_id)
        if infinito:
            update.message.reply_text('`Se ha muteado a` *{}* `para siempre!`'.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text('`Se ha muteado a` *{}* `por` *{}* `dias`'.format(user.first_name, date), parse_mode=ParseMode.MARKDOWN)
    except:
        update.message.reply_text('`No he podido mutear a` *{}.* `:(`'.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
def unmute(update, context):
    chat_id = update.effective_chat.id
    permisos = ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=False, can_invite_users=False, can_pin_messages=False)
    try:
        user = update.message.reply_to_message.from_user
    except:
        update.message.reply_text('`Para desmutear a un usuario debes primero responderle.` /unmute', parse_mode=ParseMode.MARKDOWN)
        return False
    if(isAdmin(update, context) == False):
        return False
    try:
        context.bot.restrictChatMember(chat_id, user.id, permisos, until_date= 86400)
        update.message.reply_text('`Se ha desmuteado a` *{}*'.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
    except:
        update.message.reply_text('`No he podido desmutear a` *{}.* `:(`'.format(user.first_name), parse_mode=ParseMode.MARKDOWN)
def set_welcome(update, context):
    if(isAdmin(update, context) == False):
        return False
    welcome = update.message.text[9:]
    chat_id = update.message.chat.id
    with open('welcome.txt', 'r') as pepe:
        message = json.load(pepe)
        pepe.close()
    message[str(chat_id)] = {'welcome': welcome}
    with open('welcome.txt', 'w') as pepe:
        json.dump(message, pepe)
        pepe.close()

    update.message.reply_text('_Mensaje de Bienvenida Actualizado._', parse_mode=ParseMode.MARKDOWN)
def welcome(update, context):
    chat_id = update.message.chat.id
    with open('welcome.txt', 'r') as pepe:
        saludoS = json.load(pepe)
        pepe.close()
    if update.message.new_chat_members:
        message = 'Welcome $USERNAME'
        for groups in saludoS:
            if str(chat_id) == str(groups):
                message = saludoS[str(groups)]
                message = str(message['welcome'])
                break
        for new_member in update.message.new_chat_members:
            #if(new_member.username == 'BOTNAME'):
                # // presentacion del bot
            # // retrieve welcome message
            saludo = message.replace('$USERNAME', new_member.username)
            update.message.reply_text(saludo, parse_mode=ParseMode.MARKDOWN)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def main():
    updater = Updater(
        TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('gen', generator))
    dp.add_handler(CommandHandler('extra', extras))
    dp.add_handler(CommandHandler('bin', lookup))
    #dp.add_handler(CommandHandler('ban', ban))
    dp.add_handler(CommandHandler('mute', mute))
    dp.add_handler(CommandHandler('unmute', unmute))
    #dp.add_handler(CommandHandler('welcome', set_welcome))
    dp.add_handler(MessageHandler(Filters.text, textCommands))
    #dp.add_handler(MessageHandler(Filters.status_update, welcome))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("herokuhost" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()





