import random
import secrets
import string

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from config.settings import EMAIL_HOST_USER
from users.forms import UserLoginForm
from users.forms import UserRegisterForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)  # генерит токен
        user.token = token
        user.save()
        host = self.request.get_host()  # получение хоста
        url = f'http://{host}/users/verify/{token}'
        send_mail(
            subject=f'Подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def verify_mail(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not User.objects.filter(email=email).exists():
            return render(request, template_name='users/login.html')
        else:
            user = get_object_or_404(User, email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(new_password)
            user.save()
            send_mail(
                subject=f'Сброс пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
            )
        return redirect(reverse('users:login'))

    return render(request, template_name='users/login.html')


