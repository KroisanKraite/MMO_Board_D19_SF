from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:foo>', AddsList.as_view(), name="adds-list"),
    path('create/', AddsCreate.as_view(), name='adds_create'),
    path('<int:pk>/update/', AddsUpdate.as_view(), name='adds_update'),
    path('<int:pk>/delete/', AddsDelete.as_view(), name='adds_delete'),
    path('reply/<int:pk>/delete/', ReplyDelete.as_view(), name='reply_delete'),
    path('reply/<int:pk>/accept/', accept_reply, name='accept_reply'),
    path('<int:pk>/reply/', ReplyCreate.as_view(), name='reply'),
]
