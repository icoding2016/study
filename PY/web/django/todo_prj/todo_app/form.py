from django import forms
from datetime import datetime


class NewTodoForm(forms.Form):
    task = forms.CharField(label='Task', max_length=255)
    # handle_time = forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'type': 'datetime'})
    handle_time = forms.DateTimeField(label='handle_time')  #  format='%Y-%m-%d %H:%M',
    create_time = forms.DateTimeField(label='create_time',)  #  initial=datetime.now().strftime("%Y-%m-%d %H:%M")