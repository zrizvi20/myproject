from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.utils.encoding import force_text
from django.db import transaction

import logging
log = logging.getLogger(__name__)

from .models import Client, Contractor, Supervisor

# -----------------------------------
# CLIENT SIGNUP FORM

class ClientSignUp(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True)

    
    class Meta(UserCreationForm):
        model = Client
        fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                  'po_box_no', 'landline_no', 'username', 'mobile_no_1', 'mobile_no_2',
                  'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
class ClientChangeForm(UserChangeForm):

    class Meta:
        model = Client
        fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                  'po_box_no', 'landline_no', 'username', 'mobile_no_1', 'mobile_no_2',
                  'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )
        
# -----------------------------------
# CONTRACTOR SIGNUP FORM

class ContractorSignUp(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True)


    class Meta(UserCreationForm):
            model = Contractor
            fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                  'po_box_no', 'landline_no', 'username', 'mobile_no_1', 'mobile_no_2', 
                  'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_contractor = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
class ContractorChangeForm(UserChangeForm):

    class Meta:
        model = Contractor
        fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                  'po_box_no', 'landline_no', 'username','mobile_no_1', 'mobile_no_2',
                  'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )
        
# -----------------------------------
# SUPERVISOR SIGNUP FORM

class SupervisorSignUp(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True)


    class Meta(UserCreationForm):
            model = Supervisor
            fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                      'po_box_no', 'landline_no', 'username', 'mobile_no_1', 'mobile_no_2', 
                      'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_supervisor = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
class SupervisorChangeForm(UserChangeForm):

    class Meta:
        model = Supervisor
        fields = ('email', 'name', 'address_1', 'address_2', 'country', 'city', 'region', 'postal_code',
                  'po_box_no', 'landline_no', 'username','mobile_no_1', 'mobile_no_2',
                  'bank_name_1', 'bank_account_no_1', 'bank_name_2', 'bank_account_no_2', 'national_id', 'zip_code',
                  )

