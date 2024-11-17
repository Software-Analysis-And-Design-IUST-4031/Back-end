from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("A user email is needed.")
        
        if not password:
            raise ValueError("A user password is needed.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if not email:
            raise ValueError("A user email is needed.")
        
        if not password:
            raise ValueError("A user password is needed.")
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200, blank=False, null=False)  
    lastname = models.CharField(max_length=200, blank=False, null=False)   
    username = models.CharField(max_length=200, blank=False, null=False, unique=True)   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
<<<<<<< HEAD
    nickname = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    national_id = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)



=======
    
>>>>>>> dev
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  

    objects = CustomUserManager()

    def __str__(self):
        return self.username
<<<<<<< HEAD



        
=======
>>>>>>> dev
