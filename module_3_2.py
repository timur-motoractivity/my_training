def send_email(message, recipient, \
               *, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com")\
                                 or email.endswith(".ru")\
                                 or email.endswith(".net"))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} \
                на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} \
              на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕСЛЬ! письмо отправлено \
              с адреса {sender} на адрес {recipient} .')

# Пример выполнения кода (тесты):
send_email('Это сообщение для проверки связи', \
           'vasyok133@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса',\
           'urban.fan@mail.ru',\
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',\
           'urban.student@mail.ru',\
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',\
           'urban.teacher@mail.ru',\
           sender='urban.teacher@mail.ru')




