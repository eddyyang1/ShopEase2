from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from users.models import User

@login_required
def chat_room(request, shop_id):
    messages = Message.objects.filter(receiver_id=shop_id, sender=request.user) | \
               Message.objects.filter(receiver=request.user, sender_id=shop_id)
    return render(request, 'chat/chat_room.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        text = request.POST['message']
        receiver_id = request.POST['receiver_id']
        Message.objects.create(sender=request.user, receiver_id=receiver_id, text=text)
        return redirect('chat-room', shop_id=receiver_id)
