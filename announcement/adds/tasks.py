from celery import shared_task
from .models import Reply, Advertisement
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


@shared_task
def notify_author(oid):
    reply = Reply.objects.get(pk=oid)
    author = reply.advertisement.author
    post = reply.advertisement
    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email='mytestemailDilia@yandex.ru',
        to=[author.email],
    )
    html_content = render_to_string(
        'send_reply.html',
        {
            'reply': reply,
            'title': post.title,
            'link': settings.SITE_URL,
            'username': author.username,
        }
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def notify_reply_accepted(oid):
    reply = Reply.objects.get(pk=oid)
    user = reply.user
    author = reply.advertisement.author
    post = reply.advertisement
    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email='mytestemailDilia@yandex.ru',
        to=[user.email],
    )
    html_content = render_to_string(
        'reply_accepted.html',
        {
            'email': author.email,
            'title': post.title,
            'username': user.username,
        }
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

