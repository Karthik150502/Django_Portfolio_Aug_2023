from django import forms
from web_app.models import emailform



    

class Email_form(forms.ModelForm):

    class Meta:
        model = emailform
        fields = ["username", "email"]

