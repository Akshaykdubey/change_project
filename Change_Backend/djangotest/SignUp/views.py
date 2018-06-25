from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import userForms
from .models import User

def index(request):
    u = User.objects.all()
    return HttpResponse("<h1>" + str(u[0]) + "</h1>")


class userFormview(View):

    form_class = userForms
    template_name = 'templates/SignUp/Register.html'


    def get(self, request):
        form = self.form_class(None)
        return render (request, self.template_name, form)


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.setpassword(password)
            user.save()

        user = authenticate(username='username', password='password')

        if user is not None:

            if user.is_active():
                login(request, user)