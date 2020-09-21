from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from django.http import HttpResponse
from django.template import loader
from app.forms import MailCreationForm
from django.views.generic import CreateView  
from app.models import Mail
from django.utils import timezone, dateformat
from datetime import datetime
import requests
import threading
import datetime
import os


API_KEY = os.environ.get('API_KEY') 
SANDBOX = os.environ.get('SANDBOX')
SCHEDULED = "запланировано"
SENT = "отправлено"


class CreateEmail(CreateView):
    model = Mail
    success_url = reverse_lazy("app:mail_list")
    form_class = MailCreationForm  
    template_name = 'index.html'   
	
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        # instance.added = datetime.datetime.now().strftime('%H:%M:%S')
        instance.added = dateformat.format(timezone.localtime(timezone.now()), 'H:i:s')
        instance.save()
        preparing_a_message_for_sending(instance)
        return super(CreateEmail, self).form_valid(form)


def mail_list(request):
    template = loader.get_template('mail_list.html')
    mail_list = Mail.objects.all().order_by('-id')[:10]
    data = {
        'mail_list': mail_list
    } 
    return HttpResponse(template.render(data, request))


def preparing_a_message_for_sending(instance):
    text = instance.text
    delay = instance.time_delay
    id = instance.id
    threading.Timer(delay, send_message, args=(text, id)).start()


def send_message(text, id):
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(SANDBOX)
    request = requests.post(request_url, auth=('api', API_KEY), data={
        'from': 'mentor@skillfactory.ru',
        'to': 'daniltarasov@yandex.ru',
        'subject': 'проверка ДЗ',
        'text': text
    })
    print('Status: {0}'.format(request.status_code))
    print('Body:   {0}'.format(request.text))
    if request.status_code == 200:
        sent_mail = Mail.objects.get(id = id)
        sent_mail.mail_status = SENT
        sent_mail.save()


def mails_clear(request):
    Mail.objects.all().delete()
    return redirect('app:mail_list')