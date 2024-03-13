from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import song,ContactUs

class SignupForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={
    'class':'form-control '
    }) )
    
    password2=forms.CharField(label='Password confirmation',widget=forms.PasswordInput(attrs={
       'class':'form-control '
    }))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        labels ={'email':'Email'}
        
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  }
        
class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
class UserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'date_joined':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                  'last_login':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                  }

class AdminProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = '__all__'
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'})
                  }
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CrudForm(forms.ModelForm):
    class Meta:
        model = song
        fields = ['song_id','name','singer','tags','image','Song','movie','categories']
        widgets = {
            'song_id': forms.NumberInput(attrs={'class': 'form-control song_id'}),
            'name': forms.TextInput(attrs={'class': 'form-control name'}),
            'singer': forms.TextInput(attrs={'class': 'form-control singer'}),
            'tags': forms.TextInput(attrs={'class': 'form-control tags'}),
            'image': forms.FileInput(attrs={'class': 'form-control image'}),
            'Song': forms.FileInput(attrs={'class': 'form-control song'}),
            'movie': forms.TextInput(attrs={'class': 'form-control movie'}),
            'categories': forms.Select(attrs={'class': 'form-control categories'}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'subject': forms.TextInput(attrs={'class': 'form-control '}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
         }