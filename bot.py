import os
from dotenv import load_dotenv
load_dotenv()  # ← теперь выполняется ПЕРЕД импортом ai_descriptions

import telebot
from telebot import types
from cards import cards, get_random_one_card, get_random_three_cards
from image_utils import generate_cards_image
from ai_descriptions import generate_card_description, generate_three_cards_description

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

settings = {
    'theme': 'classic'
}

# Кнопки основного меню
def get_main_menu():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('🃏 Карта дня', callback_data='tarot_daily')
    btn2 = types.InlineKeyboardButton('👨 Його думки про тебе', callback_data='tarot_thoughts_male')
    btn3 = types.InlineKeyboardButton('👩 Її думки про тебе', callback_data='tarot_thoughts_female')
    btn4 = types.InlineKeyboardButton('🔮 Як діяти, щоб збулось задумане', callback_data='tarot_how_to_act')
    btn5 = types.InlineKeyboardButton(
        'Змінити дизайн карт',
        callback_data='choose_tarot_theme'
    )

    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4)
    markup.row(btn5)

    return markup

# Кнопка 'Спробувати ще'
def get_retry_menu():
    markup = types.InlineKeyboardMarkup()

    btn = types.InlineKeyboardButton(
        '🔄 Спробувати ще',
        callback_data='start_again'
    )

    markup.row(btn)
    return markup

# Приветственное сообщение при нажатии start
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name or 'гость'
    text = f"""
    <b>♦️ Привіт, {name}!</b>

    <i>Ласкаво просимо на розклад.</i>

    Оберіть дію:
    """
    bot.send_message(
        message.chat.id,
        text,
        parse_mode='HTML',
        reply_markup=get_main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id

    if call.data == 'tarot_daily':
        card = get_random_one_card()
        image_path = f'src/{settings["theme"]}/{card}.webp'
        title = cards[card]["title"]

        # Сообщение-заглушка пока ИИ думает
        thinking_msg = bot.send_message(call.message.chat.id, "Викликаю магію, не заважай процесу…")

        # Генерируем описание
        description = generate_card_description(title, 'tarot_daily')

        # Удаляем заглушку
        bot.delete_message(call.message.chat.id, thinking_msg.message_id)

        caption = f"<b>{title}</b>\n\n{description}"

        with open(image_path, "rb") as photo:
            bot.send_photo(
                call.message.chat.id,
                photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=get_retry_menu()
            )

    elif call.data == 'tarot_thoughts_male':
        random_cards = get_random_three_cards()
        image_path = generate_cards_image(
            random_cards,
            settings["theme"]
        )

        titles = " + ".join(
            cards[card]["title"]
            for card in random_cards
        )

        thinking_msg = bot.send_message(call.message.chat.id, "Доля вантажиться, майже готово…")
        description = generate_three_cards_description(titles, 'tarot_thoughts_male')
        bot.delete_message(call.message.chat.id, thinking_msg.message_id)

        caption = f"<b>{titles}</b>\n\n{description}"

        with open(image_path, "rb") as photo:
            bot.send_photo(
                call.message.chat.id,
                photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=get_retry_menu()
            )

    elif call.data == 'tarot_thoughts_female':
        random_cards = get_random_three_cards()
        image_path = generate_cards_image(
            random_cards,
            settings["theme"]
        )

        titles = " + ".join(
            cards[card]["title"]
            for card in random_cards
        )

        thinking_msg = bot.send_message(call.message.chat.id, "Карти шепочуть щось дивне, чекай…")
        description = generate_three_cards_description(titles, 'tarot_thoughts_female')
        bot.delete_message(call.message.chat.id, thinking_msg.message_id)

        caption = f"<b>{titles}</b>\n\n{description}"

        with open(image_path, "rb") as photo:
            bot.send_photo(
                call.message.chat.id,
                photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=get_retry_menu()
            )

    elif call.data == 'tarot_how_to_act':
        random_cards = get_random_three_cards()
        image_path = generate_cards_image(
            random_cards,
            settings["theme"]
        )

        titles = " + ".join(
            cards[card]["title"]
            for card in random_cards
        )

        thinking_msg = bot.send_message(call.message.chat.id, "Перемішую всесвіт, не перемикайся…")
        description = generate_three_cards_description(titles, 'tarot_how_to_act')
        bot.delete_message(call.message.chat.id, thinking_msg.message_id)

        caption = f"<b>{titles}</b>\n\n{description}"

        with open(image_path, "rb") as photo:
            bot.send_photo(
                call.message.chat.id,
                photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=get_retry_menu()
            )

    elif call.data == 'start_again':
        bot.send_message(
            call.message.chat.id,
            'Оберіть дію:',
            reply_markup=get_main_menu()
        )

    elif call.data == 'choose_tarot_theme':
        if settings['theme'] == 'classic':
            settings['theme'] = 'dark'
        else:
            settings['theme'] = 'classic'

        bot.send_message(
            call.message.chat.id,
            f'Тема змінена на {settings["theme"]}'
        )

# Будет работать бесконечно
bot.polling(non_stop=True)