import random

cards = {
    # Старші Аркани
    "the_fool": {"title": "Блазень"},
    "the_magician": {"title": "Маг"},
    "the_high_priestess": {"title": "Верховна Жриця"},
    "the_empress": {"title": "Імператриця"},
    "the_emperor": {"title": "Імператор"},
    "the_hierophant": {"title": "Верховний Жрець"},
    "the_lovers": {"title": "Закохані"},
    "the_chariot": {"title": "Колісниця"},
    "strength": {"title": "Сила"},
    "the_hermit": {"title": "Відлюдник"},
    "wheel_of_fortune": {"title": "Колесо Фортуни"},
    "justice": {"title": "Справедливість"},
    "the_hanged_man": {"title": "Повішений"},

    #"death": {"title": "Смерть"},
    "temperance": {"title": "Помірність"},
    #"the_devil": {"title": "Диявол"},
    "the_tower": {"title": "Вежа"},
    "the_star": {"title": "Зірка"},
    "the_moon": {"title": "Місяць"},
    "the_sun": {"title": "Сонце"},
    "judgement": {"title": "Суд"},
    "the_world": {"title": "Світ"},

    # Кубки
    "ace_of_cups": {"title": "Туз Кубків"},
    "two_of_cups": {"title": "Двійка Кубків"},
    "three_of_cups": {"title": "Трійка Кубків"},
    "four_of_cups": {"title": "Четвірка Кубків"},
    #"five_of_cups": {"title": "П'ятірка Кубків"},
    #"six_of_cups": {"title": "Шістка Кубків"},
    #"seven_of_cups": {"title": "Сімка Кубків"},
    #"eight_of_cups": {"title": "Вісімка Кубків"},
    # "nine_of_cups": {"title": "Дев'ятка Кубків"},
    # "ten_of_cups": {"title": "Десятка Кубків"},
    # "page_of_cups": {"title": "Паж Кубків"},
    "knight_of_cups": {"title": "Лицар Кубків"},
    # "queen_of_cups": {"title": "Королева Кубків"},
    # "king_of_cups": {"title": "Король Кубків"},

    # Жезли
    "ace_of_wands": {"title": "Туз Жезлів"},
    # "two_of_wands": {"title": "Двійка Жезлів"},
    # "three_of_wands": {"title": "Трійка Жезлів"},
    # "four_of_wands": {"title": "Четвірка Жезлів"},
    "five_of_wands": {"title": "П'ятірка Жезлів"},
    # "six_of_wands": {"title": "Шістка Жезлів"},
    # "seven_of_wands": {"title": "Сімка Жезлів"},
    # "eight_of_wands": {"title": "Вісімка Жезлів"},
    # "nine_of_wands": {"title": "Дев'ятка Жезлів"},
    "ten_of_wands": {"title": "Десятка Жезлів"},
    # "page_of_wands": {"title": "Паж Жезлів"},
    # "knight_of_wands": {"title": "Лицар Жезлів"},
    # "queen_of_wands": {"title": "Королева Жезлів"},
    # "king_of_wands": {"title": "Король Жезлів"},

    # Мечі
    # "ace_of_swords": {"title": "Туз Мечів"},
    # "two_of_swords": {"title": "Двійка Мечів"},
    # "three_of_swords": {"title": "Трійка Мечів"},
    # "four_of_swords": {"title": "Четвірка Мечів"},
    # "five_of_swords": {"title": "П'ятірка Мечів"},
    # "six_of_swords": {"title": "Шістка Мечів"},
    # "seven_of_swords": {"title": "Сімка Мечів"},
    # "eight_of_swords": {"title": "Вісімка Мечів"},
    # "nine_of_swords": {"title": "Дев'ятка Мечів"},
    # "ten_of_swords": {"title": "Десятка Мечів"},
    # "page_of_swords": {"title": "Паж Мечів"},
    # "knight_of_swords": {"title": "Лицар Мечів"},
    # "queen_of_swords": {"title": "Королева Мечів"},
    # "king_of_swords": {"title": "Король Мечів"},

    # Пентаклі
    # "ace_of_pentacles": {"title": "Туз Пентаклів"},
    # "two_of_pentacles": {"title": "Двійка Пентаклів"},
    # "three_of_pentacles": {"title": "Трійка Пентаклів"},
    # "four_of_pentacles": {"title": "Четвірка Пентаклів"},
    # "five_of_pentacles": {"title": "П'ятірка Пентаклів"},
    # "six_of_pentacles": {"title": "Шістка Пентаклів"},
    # "seven_of_pentacles": {"title": "Сімка Пентаклів"},
    # "eight_of_pentacles": {"title": "Вісімка Пентаклів"},
    # "nine_of_pentacles": {"title": "Дев'ятка Пентаклів"},
    "ten_of_pentacles": {"title": "Десятка Пентаклів"},
    # "page_of_pentacles": {"title": "Паж Пентаклів"},
    # "knight_of_pentacles": {"title": "Лицар Пентаклів"},
    # "queen_of_pentacles": {"title": "Королева Пентаклів"},
    # "king_of_pentacles": {"title": "Король Пентаклів"},
}

def get_random_one_card():
    return random.choice(list(cards.keys()))

def get_random_three_cards():
    return random.sample(list(cards.keys()), 3)