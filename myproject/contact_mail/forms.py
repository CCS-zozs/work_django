# contact_mail/forms.py
from django import forms

class ContactForm(forms.Form):
    # 只需要一个文本域供用户输入内容
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '请输入要在邮件中发送的内容...'}),
        label="邮件内容",
        required=True
    )