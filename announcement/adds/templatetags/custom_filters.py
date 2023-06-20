from django import template
from adds.models import Advertisement, Reply
from accounts.models import CustomUser


register = template.Library()


@register.filter()
def reply_check(id_adds, id_user):
   user = CustomUser.objects.get(id=id_user)
   adds = Advertisement.objects.get(id=id_adds)
   return Reply.objects.filter(user=user, advertisement=adds).exists()


@register.filter()
def reply_visibility(id_adds, id_user):
   user = CustomUser.objects.get(id=id_user)
   adds = Advertisement.objects.get(id=id_adds)
   return Reply.objects.filter(user=user, advertisement=adds).exists()