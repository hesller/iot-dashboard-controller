from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from crm import forms
from crm import models


# Create your views here.
from crm.repositories.AirConditioningRepository import getAcWithEnvID
from crm.repositories.environment_equipament_repository import get_all_equipament_environment


@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html', context={})


class LoginView(View):
    """
        This class defines the login methods allowed
    """

    html_template = 'pages/auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, self.html_template, context={'page_title': 'Painel'})

    def post(self, request, *args, **kwargs):

        form = forms.UserAuthenticationForm(request=request,data=request.POST)

        if form.is_valid():
            try:
                user = form.user_cache
                login(request, user)
                return redirect('dashboard')
            except:
                return render(request, self.html_template, context={'old_email': request.POST['email'], 'form': form})

        return render(request, self.html_template, context={'old_email': request.POST['email'], 'form': form})


class LogoutView(View):
    """
        This class removes the user from sessions
    """
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(View):
    """
        This class defines the register methods
    """
    template_name = 'pages/auth/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, self.template_name, context={'page_title': 'Cadastrar'})

    def post(self, request, *args, **kwargs):
        """
        Register new users to the system
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('dashboard')

        return redirect('register', {'form': form})


class EnvironmentListView(View):
    """
        List all environments on database
    """
    html_template = 'pages/environments.html'

    def get(self, request):
        return render(request, self.html_template, context={'page_title': 'Ambientes', })


class EnvironmentCreateView(View):
    """
        View to manage Environment CRUD
    """
    html_template = 'pages/environments_create.html'

    def get(self, request):
        return render(request, self.html_template, context={'page_title': 'Ambientes'})

    def post(self, request, *args, **kwargs):
        '''
            Handles how environment is created.
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        form = forms.EnvironmentCreateForm(request.POST)

        if form.is_valid():
            environment = form.save()
            messages.add_message(request, messages.SUCCESS, f'Ambiente {environment.name} criado com sucesso!')
            return redirect('list-environments')


class EnvironmentDetails(UpdateView):
    template_name = 'pages/environments_edit.html'
    model = models.Environment
    slug_url_kwarg = 'pk'
    fields = ['name', 'local', 't_t']

    success_url = '/ambientes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_all_equipament_environment(context, self.object)
        return context


class EnvironmentDelete(DeleteView):
    template_name = 'pages/environments_delete.html'
    model = models.Environment
    slug_url_kwarg = 'pk'

    success_url = reverse_lazy('list-environments')


class AirconditioningCreate(CreateView):
    model = models.AirConditioning
    template_name = 'pages/environments_ac_create.html'
    fields = '__all__'

    def get_success_url(self):
        '''Redirect user is object is created successfully'''
        env_id = self.object.environment.id
        return reverse('edit-environment', kwargs={'pk': env_id})


class LampCreate(CreateView):
    model = models.Lamp
    http_method_names = ['post']
    fields = '__all__'

    def get_success_url(self):
        '''Redirect user is object is created successfully'''
        env_id = self.object.environment.id
        return reverse('edit-environment', kwargs={'pk': env_id})







class AirConditionUpdate(UpdateView):
    template_name = 'pages/environments_ac_edit.html'
    model = models.AirConditioning
    slug_url_kwarg = 'pk'
    fields = ['brand', 'model', 'power', 'on_off']

    def get_context_data(self, **kwargs):
        '''
            Pass the environment id to the context data
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(**kwargs)
        context['env_id'] = self.object.environment.id
        context['page_title'] = 'Aparelhos de ar'

        return context

    def get_success_url(self):
        '''
            If successfull redirect to url where the ac is located
        :return:
        '''
        env_id = self.object.environment.id

        return f"/ambientes/editar/{env_id}/"


class AirConditioningDelete(DeleteView):
    template_name = 'pages/environments_ac_delete.html'
    model = models.AirConditioning
    slug_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('edit-environment', kwargs={'pk': self.object.environment.id})

    def get_context_data(self, **kwargs):
        context = super(AirConditioningDelete, self).get_context_data(**kwargs)
        return context



class LampUpdate(UpdateView):
    template_name = 'pages/environments_lamp_edit.html'
    model = models.Lamp
    slug_url_kwarg = 'pk'
    fields = ['brand', 'model', 'power', 'on_off']

    def get_context_data(self, **kwargs):
        '''
            Pass the environment id to the context data
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(**kwargs)
        context['env_id'] = self.object.environment.id
        context['page_title'] = 'Iluminação'
        return context

    def get_success_url(self):
        '''
            If successfull redirect to url where the ac is located
        :return:
        '''
        env_id = self.object.environment.id

        return f"/ambientes/editar/{env_id}/"


class LampDelete(DeleteView):
    template_name = 'pages/environments_lamp_delete.html'
    model = models.Lamp
    slug_url_kwarg = 'pk'
    fields = ['brand', 'model', 'power', 'on_off']

    def get_success_url(self):
        '''If successfull return to the environment selected'''
        return reverse('edit-environment', kwargs={'pk': self.object.environment.id})


