from telegram.ext import Updater, CommandHandler

TOKEN = '7196821866:AAF2YhLMzxnXLwn6Nhsvp-9a2q6O14ya4iU'

def start(update, context):
    message = ('Я Бахтиёр Шаропов. Рад видеть вас в моём боте.'
               '\n\n /contact - Отправить вам мои контакты.'
                '\n /talk - Поговори со мной')

    with open('photo.jpg', 'rb') as file:
        update.message.reply_photo(file, message)

def contact(update, context):
    message = '+992 93 903 7008'
    update.message.reply_text(message)

def talk(update, context):
    message = 'Простите, но в данный момент я занят( .'
    update.message.reply_text(message)            

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()