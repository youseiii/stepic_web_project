from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
        q.author_id = self._user.id
        q.save()
        return q


class AnswerForm(forms.Form):
    question = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=forms.Textarea)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if 'fuck' in text:
            raise forms.ValidationError('Dont be rude', code=12)
        return text

    def clean(self):
        pass

    def save(self):
        an = Answer(**self.cleaned_data)
        an.author_id = self._user.id
        an.save()
        return an


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # if not username:
            # raise forms.ValidationError('не указан логин')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('такой пользователь уже существует')
        except:
            pass
        return username

    def clean_password(self):
        passw  = self.cleaned_data.get('password')
        self.raw_password = passw
        return make_password(passw)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('неправильнй логин или пароль')
        if not user.check_password(password):
            raise forms.ValidationError('неправильнй логин или пароль')

