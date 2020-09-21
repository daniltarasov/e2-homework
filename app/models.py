from django.db import models

# Create your models here.

class Mail(models.Model):
    SCHEDULED = "запланировано"
    SENT = "отправлено"
    CHOISES = (
    (SCHEDULED, 'запланировано'),
    (SENT, 'отправлено'),
    )
    added = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    time_delay = models.IntegerField()
    mail_status = models.CharField(max_length=30, choices=CHOISES, default=SCHEDULED)

