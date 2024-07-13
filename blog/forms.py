from allauth.account.forms import SignupForm
from django import forms
from .models import Post, Comment

# Signup form using allauth


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first name']
        user.last_name = self.cleaned_data['last name']
        user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        