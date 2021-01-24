from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from crm.forms import UserAuthenticationForm
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html', context={})


class LoginView(View):
    """
        This class defines the login methods allowed
    """

    html_template = 'pages/auth/login.html'

    def get(self, request):
        return render(request, self.html_template, context={'page_title': 'Painel'})


    def post(self, request, *args, **kwargs):

        form = UserAuthenticationForm(request=request,data=request.POST)

        if form.is_valid():
            print('------- form is valid')
            try:
                user = form.user_cache
                login(request, user)
                return redirect('dashboard')
            except:
                print('------- could not auth')
                return render(request, self.html_template, context={'old_email': request.POST['email'], 'form': form})
        print('----------------------form is invalid')
        print(form.errors)
        return render(request, self.html_template, context={'old_email': request.POST['email'], 'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(View):
    """
            This class defines the register methods allowed
    """
    template_name = 'pages/auth/register.html'

    def get(self, request):

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
    html_template = 'pages/environments.html'

    def get(self, request):
        return render(request, self.html_template, context={'page_title': 'Ambientes'})


class EnvironmentCreateView(View):

    html_template = 'pages/environments_create.html'

    def get(self, request):
        return render(request, self.html_template, context={'page_title': 'Ambientes'})

    # def post(self, request, *args, **kwargs):
