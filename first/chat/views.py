from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from chat.models import Message
from datetime import timedelta
from django.utils import timezone
from django.utils.html import escape
from django.http import JsonResponse, HttpResponse
import time


def jsonfun(request):
    time.sleep(2)
    stuff = {
            'first': 'first thing',
            'second': 'second thing',
            }
    return JsonResponse(stuff)


class TalkMain(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'chat/talk.html')

    def post(self, request):
        message = Message(text=request.POST['message'], owner=request.user)
        message.save()
        return redirect(reverse('chat:talk'))


class TalkMessages(LoginRequiredMixin, View):
    def get(self, request):
        Message.objects.filter(created_at__lt=timezone.now()-timedelta(minutes=20)).delete()
        messages = Message.objects.all().order_by('-created_at')[:10]
        results = []
        for message in messages:
            result = [escape(message.text), naturaltime(message.created_at)]
            results.append(result)
        return JsonResponse(results, safe=False)

