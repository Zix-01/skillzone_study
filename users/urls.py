from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserLoginView, UserRegisterView, verify_mail, reset_password

app_name = UsersConfig.name

urlpatterns = [
                  path('', UserLoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('user_form/', UserRegisterView.as_view(), name='register'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
