from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','phone',)
    
class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email','phone',)

class StaffEditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','phone','email','banned','balance',)
#        fields = ('username','phone','email','address_home','address_work','occupation','referral_source','balance','banned','regular_customer',)