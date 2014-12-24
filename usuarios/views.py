# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


def userRegister(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        data = request.POST.copy()
        if form.is_valid:
            new_user = form.save(data)
            return redirect('/usuarios')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, "usuarios/register.html", context)

def userLogin(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					return redirect('/usuarios')
				else:
					return render(request, 'usuarios/inactive.html')
			else:
				return render(request, 'usuarios/nouser.html')
	else:
		form = AuthenticationForm()
	context = {'form': form}
	return render(request,'usuarios/login.html', context)

#@login_required(login_url='/usuarios/login')
def userLogout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')