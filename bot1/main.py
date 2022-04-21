import logging
import telegram
import random
import configparser
import firebase_admin
from firebase_admin import credentials, db
from numpy import empty
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from search import search_serial
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


def get_random_smile():
    # function of random selection of meaning from the list
    smiles = ['🙃', '😃', '😉', '😇', '😊', '😚', '😋', '😜', '🤩']
    return random.choice(smiles)


def get_show_details(object):
    key_list = ['id', 'name', 'type', 'language']
    show_details = list(map(object.get, key_list))
    return show_details


def get_show_id(object):
    show_dict = object.get("show")
    show_id = show_dict.get("id")
    return show_id


def start(update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    buttons = [['🔎 Search']]
    keyboard = telegram.ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(user_id, 'Hi, 'f'{name}!', reply_markup=keyboard)


def help(update, context):
    update.message.reply_text('😄Welcome to our chatbot!\n'
                              '😜/help to get the instructions!\n'
                              '😼Input any characters for show you want to search!\n')


def get_own_telegram_id(update, context):
    # function that returns user id
    name = update.message.from_user.first_name
    user_id = update.message.from_user.id
    context.bot.send_message(user_id, f'Hello {get_random_smile()}')
    update.message.reply_text(f'{name}, Your id: {user_id}')


def inline_keyboard_handler(update, context):
    message_text = update.message.text
    serial_info = search_serial(message_text)
    ref.set(serial_info)
    serials_all = ref.get()
    serials = []
    for serial in serials_all:
        serials.append(serial["show"])
    show_button_list = []
    for serial in serials:
        show_details = get_show_details(serial)
        show_details_string = ' '.join([str(elem) for elem in show_details])
        show_button_list.append([InlineKeyboardButton(
            f'{serial["name"]}', callback_data=show_details_string
        )])
    reply_markup = InlineKeyboardMarkup(show_button_list)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query_data = query.data
    query_data = query_data.split()
    show_id = query_data[0]
    show_language = query_data[-1]
    show_type = query_data[len(query_data) - 2]
    show_name = query_data[1: len(query_data) - 2]
    show_name = ' '.join([str(elem) for elem in show_name])

    serials_all = ref.get()
    serials = []
    for show_searched in serials_all:
        serials.append(show_searched["show"])

    indicated_show = []
    for show in serials:
        if show["id"] == int(show_id):
            indicated_show.append(show)
    serial_description = indicated_show[0]

    genres = serial_description.get("genres")
    images = serial_description.get("image")
    display = images.get("medium")
    time = serial_description.get("premiered")
    if (genres is not empty) and (display):
        genres = ' '.join([str(elem) for elem in genres])
        query.edit_message_text(text="Show:{}\n Laguage:{}\n Type:{}\n Time:{}\n Genres:{}\n Images:{}\n".format(
            show_name, show_language, show_type, time, genres, display))

    elif genres is not empty:
        genres = ' '.join([str(elem) for elem in genres])
        query.edit_message_text(text="Show:{}\n Laguage:{}\n Type:{}\n Time:{}\n Genres:{}\n".format(
            show_name, show_language, show_type, time, genres))

    elif display:
        query.edit_message_text(text="Show:{}\n Laguage:{}\n Type:{}\n Time:{}\n Images:{}\n".format(
            show_name, show_language, show_type, time, display))

    else:
        query.edit_message_text(text="Show:{}\n Laguage:{}\n Type:{}\n Time:{}\n".format(
            show_name, show_language, show_type, time))


def share_image(update, context):
    serials_all = ref.get()
    serials = []
    for show_searched in serials_all:
        serials.append(show_searched["show"])

    indicated_show = []
    show_name = update.message.text
    show_name = show_name.replace("Sending@", "")
    for show in serials:
        if show["name"] == show_name:
            indicated_show.append(show)
    serial_description = indicated_show[0]
    actual_url = serial_description.get("image")
    image_url = actual_url.get("medium")
    user_id = update.message.from_user.id
    context.bot.send_message(user_id, f'{image_url}')


def echo(update, context):
    if 'Search' in update.message.text:
        update.message.reply_text(
            f'Input show name you want! {get_random_smile()}')
    elif 'Sending@' in update.message.text:
        share_image(update, context)
    else:
        inline_keyboard_handler(update, context)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    global ref
    config = configparser.ConfigParser()
    config.read('config.ini')
    # updater = Updater(
    #     token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    updater = Updater(
        token=(os.environ['ACCESS_TOKEN']), use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    key = os.environ["KEY_PATH"]
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(key)
    # Initialize the app with a service account, granting admin privileges
    database_url = os.environ["DATABASE_URL"]
    firebase_admin.initialize_app(cred, {"databaseURL": database_url})
    ref = db.reference("/")

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("get_my_id", get_own_telegram_id))
    dispatcher.add_handler(CommandHandler("share_image", share_image))
    # responsible for drawing buttons in the keyboard
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
