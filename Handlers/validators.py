import re

"""Валидатор для email"""

def is_valid_email(email: str) -> bool:
    # Паттерн регулярного выражения для проверки email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Проверка соответствия email шаблону
    if re.match(pattern, email):
        return True
    else:
        return False