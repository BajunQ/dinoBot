import config
import telebot
import answer
import csv
import sys
from telebot import types
from itertools import groupby

bot = telebot.TeleBot(config.token)

launched = False
started = False

@bot.message_handler(commands=['start'])
def start(mes):
    global started
    if started == False:
        started = True
        bot.send_message(mes.chat.id, 'Расписание ДИНО для телеграмма распарсил Александр Шашков, 2017')

@bot.message_handler(commands=['stop'])
def stop(mes):
    global started
    if started == True:
        started = False
        bot.send_message(mes.chat.id, 'Жаль, что вы покидаете нас.')

@bot.message_handler(commands=['show'])
def showList(mes):
    global launched
    if not launched:
                group = answer.showAll()
                keyboard = types.InlineKeyboardMarkup()
                btns = []
                found = 0
                for  i in range(len(group)):
                            groupCheck = answer.csvSearch(group[i])
                            if groupCheck:
                                button = types.InlineKeyboardButton(text=group[i], callback_data=group[i])
                                btns.append(button)
                                found+=1
                            else:
                                pass
                keyboard.add(*btns)
                bot.send_message(mes.chat.id, "Вот список групп:", reply_markup=keyboard)
                launched = True
                

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
            search = call.data
            groupList = answer.csvSearch(search)
            message = search + ':\n'
            for i in range(len(groupList)):
                message += str(i+1)
                message += '. ' + ': '.join(groupList[i]) + '\n'
            bot.send_message(call.message.chat.id, message)


@bot.message_handler(content_types=["text"])
def callback(message):
    if message:
        search = message.text
        groupList = answer.csvSearch(search)
        if not groupList:
                bot.send_message(message.chat.id, 'Ничего не найдено! Может, стоит посмотреть весь список групп?')
        else:
            textAnswer = search + ':\n'
            for i in range(len(groupList)):
                    textAnswer += str(i+1)
                    textAnswer += '. ' + ': '.join(groupList[i]) + '\n'
            bot.send_message(message.chat.id, textAnswer)
        
    
bot.polling()


#bot.register_next_step_handler(botsMsg, findFunc)
