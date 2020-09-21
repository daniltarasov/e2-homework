from django.contrib import admin
from django.urls import path
from app.views import CreateEmail, mail_list, mails_clear  


app_name = 'app'  
urlpatterns = [  

    path('', CreateEmail.as_view(), name='index'),
    path('mails/', mail_list, name='mail_list'),
    path('mails/clear', mails_clear, name='mails_clear')
 
]