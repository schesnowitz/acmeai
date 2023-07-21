from pages.models import Profile
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('open_api_key',) 
