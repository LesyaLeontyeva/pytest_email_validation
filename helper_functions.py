import random
import faker


def generate_valid_email(count: int) -> str:
    """Генератор валидного email"""
    fake = faker.Faker()
    for i in range(count):
        valid_email = fake.email()
        yield valid_email


def invalid_email_generator(quantity) -> str:
    """Генерируем email."""
    domain = ['yandex.ru', 'hotmail.com', 'mail.ru', 'google.com']
    name = ['test', 'mail', 'testtest']
    for i in range(quantity):
        yield random.choice(name) + "@" + random.choice(domain)


def valid_email(email) -> bool:
    """Проверяем email на регулярное выражение."""
    import re
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text) -> None:
    """Пишем в лог файл."""
    with open(file_name, 'a') as f_obj:
        f_obj.write(text)
