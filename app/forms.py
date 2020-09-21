from django import forms  
from app.models import Mail
  
  
class MailCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = Mail  
        fields = ['text', 'time_delay',]
        labels = {'text':'Текст письма', 'time_delay':'Задержка перед отправлением, с',}