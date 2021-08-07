
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.shortcuts import redirect, render
from .models import *
from django import views


class ContactForm(ModelForm):
    class Meta:
        model = contactForm
        fields = '__all__'


class Indexheadform(forms.ModelForm):
    class Meta:
        model = indexHead
        fields = "__all__"


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

        # def clean_email(self):

        #     # Get the email
        #     email = self.cleaned_data.get('email')

        #     if Subscriber.objects.filter(email=email).exists():

        #         raise forms.ValidationError("you have been already subscribed")

        #     else:
        #         return email

        #     messages.WARNING(
        #         r, "Email is already exists or you are already subscribed")
        #     return redirect(marketingindex)
        # else:
        #     S.save()
        #     messages.success(r, 'You Have been Subscribed successfully ')
        #     return redirect(marketingindex)

    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = Subscriber.objects.get(email=email)
    #     except Subscriber.DoesNotExist:
    #         raise forms.ValidationError('This email address is already in use.')

        # Unable to find a user, this is fine

        # A user was found with this as a username, raise an error.
