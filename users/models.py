from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django_countries.fields import CountryField
from django.contrib.auth.base_user import BaseUserManager

from myproject import settings

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=self.normalize_email(email),
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=150, unique=True)
    is_client = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150, verbose_name='Name', null=True)
    address_1 = models.CharField(max_length=150, verbose_name='Address', null=True)
    address_2 = models.CharField(max_length=150, blank=True, verbose_name='Address (#2)', null=True)
    country = CountryField(null=True)
    region = models.CharField(max_length=150, blank=True, verbose_name='Region', null=True)
    city = models.CharField(max_length=150, verbose_name='City', null=True)
    postal_code = models.CharField(max_length=150, verbose_name='Postal code', null=True)
    po_box_no = models.IntegerField(blank=True, verbose_name='P.O. Box no', null=True, default=None)
    mobile_no_1 = models.IntegerField(verbose_name='Mobile number', default=None, null=True)
    mobile_no_2 = models.IntegerField(blank=True, verbose_name='Mobile number (#2)', null=True, default=None)
    landline_no = models.IntegerField(verbose_name='Landline number', default=None, null=True)
    bank_name_1 = models.CharField(max_length=150, verbose_name="Bank name", null=True)
    bank_account_no_1 = models.CharField(max_length=150, verbose_name='Bank account number', default=None, null=True)
    bank_name_2 = models.CharField(max_length=150, blank=True, verbose_name="Bank name (#2)", null=True)
    bank_account_no_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Bank account number (#2)', null=True, default=None)
    national_id = models.IntegerField(verbose_name='National I.D', default=None, null=True)
    zip_code = models.IntegerField(verbose_name='ZIP Code', blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    is_superuser = True
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, users):
        return self.is_superuser

    def __str__(self):
        return self.email

    
class Client(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, parent_link=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name', 'address_1', 'country', 'city', 'postal_code', 'landline_no', 'username',
        'mobile_no_1', 'bank_name_1', 'bank_account_no_1', 'national_id', 'zip_code',
        ]

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

        
class Contractor(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, parent_link=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name', 'address_1', 'country', 'city', 'postal_code', 'landline_no', 'username',
        'mobile_no_1', 'bank_name_1', 'bank_account_no_1', 'national_id', 'zip_code',
        ]
    
    class Meta:
        verbose_name = 'contractor'
        verbose_name_plural = 'contractors'


class Supervisor(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, parent_link=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name', 'address_1', 'country', 'city', 'postal_code', 'landline_no', 'username',
        'mobile_no_1', 'bank_name_1', 'bank_account_no_1', 'national_id', 'zip_code',
        ]

    class Meta:
        verbose_name = 'supervisor'
        verbose_name_plural = 'supervisors'
