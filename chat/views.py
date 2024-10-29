from .models import Message
from django.shortcuts import render
import json
from datetime import datetime
from django.template.loader import render_to_string

def index(request):
    messages = Message.objects.order_by("-message_date")[:5]
    context = {
        "latest_messages": messages[::-1],
    }
    return render(request, "chat/chatView.html", context)


def submitMessage(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        message = Message()
        message.message_text = json_data["message"]
        message.message_date = datetime.now()
        message.save()

    messages = Message.objects.order_by("-message_date")[:5]
    context = {
        "latest_messages": messages[::-1],
    }
    return render(request, "chat/messages.html", context)
