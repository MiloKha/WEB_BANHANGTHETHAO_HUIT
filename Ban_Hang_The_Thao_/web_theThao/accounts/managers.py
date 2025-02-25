﻿from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError('Email là bắt buộc!')
        if not full_name:
            raise ValueError('Họ và tên là bắt buộc!')

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user
