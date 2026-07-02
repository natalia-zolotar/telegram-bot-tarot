import os
from openai import OpenAI


def get_client():
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is missing")

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key
    )


def generate_card_description(card_title: str, spread_type: str) -> str:
    prompt = f"""
    Ти — досвідчений таролог із 20-річною практикою, який глибоко знає класичну систему Таро.
    
    КАРТА: {card_title}

    ЗАВДАННЯ: дати коротке передбачення на сьогодні на основі карти.

    ПРАВИЛА:
    - тільки українською
    - звернення на "ти"
    - 1–2 речення
    - не перераховуй назви карт у відповіді
    - описуй реальні події дня через символіку карти
    - не використовуй психологічні узагальнення
    - не давай порад і мотивації
    - без вступів і заголовків

    ВІДПОВІДЬ:
    """

    client = get_client()

    response = client.chat.completions.create(
        model="qwen/qwen-2.5-coder-32b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_three_cards_description(card_titles: list[str], spread_type: str) -> str:
    titles = ", ".join(card_titles)

    prompts = {
        "tarot_thoughts_male": f"""
        Ти — досвідчений таролог із 20-річною практикою, який глибоко знає класичну систему Таро.
        
        Розклад: "Його думки про тебе сьогодні"
        Карти: {titles}
        
        ЗАВДАННЯ:
        Єдина інтерпретація трьох карт як однієї системи.
        
        ПРАВИЛА:
        - не розділяй карти
        - тільки українською
        - 2–3 речення
        - без мотивації
        - без психологічних формулювань напряму
        - не перераховуй назви карт у відповіді
        - Пиши живою, ясною мовою — як людина, а не генератор містичних кліше.
        
        Відповідь:
        """,

        "tarot_thoughts_female": f"""
        Ти — досвідчений таролог із 20-річною практикою, який глибоко знає класичну систему Таро.
        
        Розклад: "Її думки про тебе сьогодні"
        Карти: {titles}
        
        ЗАВДАННЯ:
        Інтерпретація ставлення через 3 карти як систему.
        
        ПРАВИЛА:
        - 3–4 речення
        - без загальних фраз
        - не розділяй карти
        - тільки українською
        - не перераховуй назви карт у відповіді
        
        Відповідь:
        """,

        "tarot_how_to_act": f"""
        Ти — досвідчений таролог із 20-річною практикою, який глибоко знає класичну систему Таро.
        
        Розклад: "Як діяти, щоб збулось задумане"
        Карти: {titles}
        
        ЗАВДАННЯ:
        Конкретні дії на основі 3 карт.
        
        ПРАВИЛА:
        - 1–3 речення
        - тільки практичні дії
        - без мотивації
        - тільки українською
        - не перераховуй назви карт у відповіді
        
        Відповідь:
        """
    }

    prompt = prompts[spread_type]
    client = get_client()

    response = client.chat.completions.create(
        model="qwen/qwen-2.5-coder-32b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content