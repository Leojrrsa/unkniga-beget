from django.core.mail import send_mail

def send_notification_email(data):
    subject = 'Новое сообщение от пользователя'
    message = f'Имя: {data["contact"]}\nEmail: {data["email"]}\n'
    message += 'Issues:\n'  # Добавляем заголовок для списка номеров
    for issue in data["issues"]:  # Проходимся по каждому выбранному номеру
        message += f'- {issue.year}\n'  # Добавляем год выпуска
        for month in issue.month_set.all():  # Проходимся по каждому месяцу в номере
            message += f'  - {month}\n'  # Добавляем информацию о месяце
    message += f'Amount: {data["amount"]}'  # Добавляем количество экземпляров
    sender = 'admin@unkniga.com'  # Электронный адрес отправителя
    recipients = ['didimon@mail.ru', 'admin@unkniga.com']  # Список адресов получателей
    send_mail(subject, message, sender, recipients)