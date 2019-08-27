from django.urls import path

from users import views
from django.views.generic.base import TemplateView

from users.views import *


urlpatterns=[
    path('', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('client-signup/', ClientSignUpView.as_view(), name='clientsignup'),
    path('contractor-signup/', ContractorSignUpView.as_view(), name='contractorsignup'),
    path('supervisor-signup/', SupervisorSignUpView.as_view(), name='supervisorsignup'),
    ]
