from django import forms
from .models import Question, Answer

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса
#
# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
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
        an.save()
        return an