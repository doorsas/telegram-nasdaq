import telebot
import os

API_KEY = '5151438780:AAHcatDx7byekbr7UagP-o-lqO5h-aasMZ4'
bot = telebot.TeleBot(API_KEY)
botname = 'pugos_bot'

@bot.message_handler(commands= ['greet'])
def greet(message):
    bot.reply_to(message,'Labas Puga')


@bot.message_handler(commands= ['labas'])
def labas(message):
    bot.send_message(message.chat.id ,'Pats tu "Labusas"')


@bot.message_handler(commands= ['foto'])
def foto(message):
    bot.send_photo(message.chat.id , photo='https://erkiulio.fronto.lt/storage/erkiulio/products/1639388621_tv-lowboardmontreuxfurtvsbiszu88-1.jpg')

@bot.message_handler(commands= ['agota'])
def agota(message):
    bot.send_photo(message.chat.id , photo=open('D:/foto_redaguotos/2021/DSC_5610.jpg', 'rb'))

@bot.message_handler(commands= ['elena'])
def elena(message):
    bot.send_photo(message.chat.id , photo=open('D:/foto_redaguotos/2021/DSC_5753.jpg', 'rb'))

@bot.message_handler(commands= ['adele'])
def adele(message):
    bot.send_photo(message.chat.id , photo=open('D:/foto_redaguotos/2021/IMG_7745.jpg', 'rb'))

@bot.message_handler(commands= ['bum'])
def bum(message):
    bot.send_message(message.chat.id , 'Tralialia')

@bot.message_handler(commands= ['bamm'])
def bamm(message):
    bot.send_message(message.chat.id , 'Tralialia')

@bot.message_handler(commands= ['bumm'])
def bumm(message):
    bot.download_file('C:/Users/PC/Desktop/NT/Akcijos.xlsx')





bot.polling()

# a = 1_2_3
# b= [3,6,-5]
# del b[-2]
# print (a)
# print (b)
# print (a*sum(b))
#
# c = 3_2
# d = 2
# print (d+c)