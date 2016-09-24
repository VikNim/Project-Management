from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'user/register.html'

    def get(self, request,):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email_id = form.cleaned_data['email']
            position = form.cleaned_data['position']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, template_name='home/index.html')  # return redirect('home:Home')
        return render(request, self.template_name, {'form': form})

'''
class ProfileView(View):
    template_name = '''