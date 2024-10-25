import string
from random import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
import secrets


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты для входа в SkillZone',
            message=f'Перейдите по ссылке для подтверждения почты - {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    return redirect(reverse('users:login'))

from django.contrib import messages

from django.contrib import messages

def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            user = User.objects.filter(email=email).first()
            if user:
                user.password = make_password(new_password)
                user.save()
                send_mail(
                    'Восстановление пароля',
                    f'Ваш новый пароль: {new_password}',
                    'koteika.koteevitch@yandex.ru',
                    [email],
                    fail_silently=False
                )
                messages.success(request, 'Новый пароль отправлен на ваш email.')
            else:
                messages.info(request, 'Пользователь с таким email не найден. Если вы считаете, что это ошибка, свяжитесь с поддержкой.')
        else:
            messages.error(request, 'Введите корректный email.')

    return redirect(reverse('login'))

