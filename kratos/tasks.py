import json

from django.core.mail import send_mail

from .celery import app


@app.task
def send_offer(offer):

    """ Отправка сообщения на почту о том, что поступил заказ """

    total_price = 0

    message = 'Вы заказали:\n'
    for product in offer:
        message += f'{product["name"]} - {product["price"]} ₽\n'
        total_price += product["price"]
    message += '-'*10 + '\n'
    message += f'Финальная стоимость: {total_price} ₽'

    header = 'Оформление заказа онлайн'
    send_mail(header, message, from_email=None, recipient_list=['russia.skl.yan@mail.ru'])
