"""from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
"""

from django import forms

from Matching_Offer_CV_App.models import Offer
from Matching_Offer_CV_App.models import Cv

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title_offer', 'description_offer']

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['name','description_cv']

