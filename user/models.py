from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from behaviors import BaseField

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, BaseField):
    email = models.EmailField('email',unique=True)
    name = models.CharField(max_length=30, blank=True)
    selfie = models.ImageField(upload_to='images/', default='default.png', blank=True, null=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'         # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name']       # 필수입력값

    class Meta:
        verbose_name = 'user'         # 어드민 페이지에서 클래스명 설정(단수)
        verbose_name_plural = 'users' # 어드민 페이지에서 클래스명 설정(복수)
        swappable = 'AUTH_USER_MODEL' # 'AUTH_USER_MODEL'에 의해 변경될 수 있음

    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)