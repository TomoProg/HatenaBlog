from django import forms
from django.contrib.auth.models import User
from .models import Topic, TopicDetail

class AccountForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.confirm_password = forms.CharField(
            label='確認',
            max_length=128,
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '再度パスワードを入力してください。'
                }
            )
        )
        self.fields['confirm_password'] = self.confirm_password

    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'ユーザー名',
            'password': 'パスワード',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ユーザー名を入力してください。',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'パスワードを入力してください。',
                }
            ),
        }
        help_texts = {
            'username': '半角英数字、@/./+/-/_ のみ使用可能です。',
        }

    def clean(self):
        """ 確認パスワードのバリデーションチェック """
        cleaned_data = self.cleaned_data
        if 'password' in cleaned_data and 'confirm_password' in cleaned_data:
            if cleaned_data['password'] != cleaned_data['confirm_password']:
                raise forms.ValidationError('パスワードが異なります。')
        return cleaned_data

class TopicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.text = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 15,
                },
            )
        )
        self.fields['text'] = self.text

    class Meta:
        model = Topic
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = TopicDetail
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 15,
                }
            )
        }

