#!/usr/bin/env python
# -*- coding: utf-8 -*-
    """
    TelegramCCToolsBot - Bot for educational purposes
    Copyright (C) 2020  Lanniscaf

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Contact: paolanderfederico@gmail.com
    FULL LICENSE: https://github.com/Lanniscaf/tb/blob/master/LICENSE
    """
from generator_with_license2 import Tools
from extrapola import *
from binlookup import alternateS

import logging
import os

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

clavesecreta = ''


TOKEN = clavesecreta
PORT = int(os.environ.get('PORT', '8443'))
def start(update, context):
    userName = '{}'.format(update.message.from_user.first_name)
    update.message.reply_text('`Hola {}! Gracias por la preferencia, para visualizar los comandos del BOT, por favor mande el comando` */help*\n\n\n`Si quieres incluir este BOT a tu grupo sientete libre de hacerlo y/o si quieres ver el codigo fuente o aportar contacta a mi dueño (INFO EN MI BIO)`'.format(userName), parse_mode=ParseMode.MARKDOWN)


def help(update, context):
    message = '\t`匚ㄖ爪卂几ᗪㄖ丂`\n\n*-* /gen <bin> <more bins> _- Genera tarjetas basado en 1 o mas bins_ \n\n*-* /extra <cc> <cc2> _- Extrapola tarjetas basado en 1 o 2 ccs_ \n\n*-* /bin <bin> _- Busca informacion de un bin_'
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def generator(update, context):
    params = context.args
    if(params == []):
        update.message.reply_text('*[X]* Pase un bin valido: /gen <bin> <optional bins>')
        return False
    __genUtils = Tools()
    __response = __genUtils.ccgenFromList(params)
    message = '*< --- + 𝔗𝔞𝔯𝔧𝔢𝔱𝔞𝔰 𝔊𝔢𝔫 + --- >*\n'
    for c in __response:
        message += '`{}`\n'.format(c)
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

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
    extrautils.bin2 = bin2

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
        message = alternateS(arg[0])
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    except:
        update.message.reply_text('*[X]* `Error`', parse_mode=ParseMode.MARKDOWN)

def textCommands(update, context):
    message = update.message.text
    if(message[:4] in ['!bin']):
        mensajes = message.split()
        res = alternateS(mensajes[1])
        update.message.reply_text(res, parse_mode=ParseMode.MARKDOWN)
        return False
    


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
    dp.add_handler(MessageHandler(Filters.text, textCommands))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://sheltered-wildwood-11509.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
