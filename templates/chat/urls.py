from django.urls import path
from .views import chat_room, send_message

urlpatterns = [
    path('<int:shop_id>/', chat_room, name='chat-room'),
    path('send/', send_message, name='send-message'),
]
