# contact_mail/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string # 新增
from django.utils.html import strip_tags            # 新增
from .forms import ContactForm

def send_email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            
            # 1. 渲染 HTML 版本
            html_message = render_to_string('contact_mail/email_body.html', {
                'content': content
            })
            
            # 2. 生成纯文本版本 (作为备用，提高送达率)
            plain_message = strip_tags(html_message)
            
            try:
                # 使用Django标准的send_mail，底层会自动走Mailgun API
                send_mail(
                    subject="来自网站的新消息 (HTML)",  # 邮件标题
                    message=plain_message,  # 这里放纯文本版本
                    from_email=settings.DEFAULT_FROM_EMAIL, # 发件人
                    recipient_list=[settings.ADMIN_RECEIVER_EMAIL], # 收件人（开发者指定）
                    html_message=html_message, # 这里放 HTML 版本
                    fail_silently=False,
                )
                messages.success(request, "HTML 邮件已发送成功！")
                return redirect('contact_mail:index') # 发送成功后刷新或跳转
            except Exception as e:
                # 实际生产中建议记录日志而不是直接打印
                messages.error(request, f"发送失败: {str(e)}")
    else:
        form = ContactForm()

    return render(request, 'contact_mail/index.html', {'form': form})