from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ClientSignUp, ContractorSignUp, SupervisorSignUp
from .models import *
from decorators import *
from myproject import backends
from projects.models import Project

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse


##@method_decorator([login_required, client_required], name='dispatch')
class ClientSignUpView(CreateView):
    model = Client
    form_class = ClientSignUp
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid:
            user = form.save()
            user.save()
            user.set_password('raw_password')
            login(self.request, user)
            return redirect('/')
        


##@method_decorator([login_required, contractor_required], name='dispatch')
class ContractorSignUpView(CreateView):
    model = Contractor
    form_class = ContractorSignUp
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'contractor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid:
            user = form.save()
            user.save()
            user.set_password('raw_password')
            login(self.request, user)
            return redirect('/')
    
####@method_decorator([login_required, supervisor_required], name='dispatch')
class SupervisorSignUpView(CreateView):
    model = Supervisor
    form_class = SupervisorSignUp
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'supervisor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            user.save()
            user.set_password('raw_password')
            login(self.request, user)
            return redirect('/')

        
def projects(request):
    current_user = request.user
    if current_user.is_authenticated:
        user = User.objects.get(pk=current_user.id)
        if user.is_client:
            projects = list(Project.objects.filter(client=user))
        elif user.is_contractor:
            projects = list(Project.objects.filter(contractor=user))
        elif user.is_supervisor:
            projects = list(Project.objects.filter(supervisor=user))
    else:
        return None
    return render(request, 'projects.html', {'projects':projects})

