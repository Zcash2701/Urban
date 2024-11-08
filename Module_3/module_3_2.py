def check_mail_address(address):
    domains = ['.ru', '.com', '.net']
    if "@" in address:
        for domain_i in domains:
            if domain_i in address:
                return True
        else:
            return False
    else:
        return False

def send_email(text_message, recipient, sender="university.help@gmail.com"):

    if check_mail_address(recipient) and check_mail_address(sender):
        if sender == recipient:
            return print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
