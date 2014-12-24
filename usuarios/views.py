# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from articulos.models import *
from django.contrib.auth.forms import AuthenticationForm
from forms import UserCreationForm, MyUserForm, editUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def registro(request):
	subs = Subcategoria.objects.all().order_by('nombre')
    # if (request.user.is_superuser and request.user.is_staff):
	if request.method == 'POST':
        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
		form = MyUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/usuarios/login')
	else:
        # form = UserCreationForm()
		form = MyUserForm()
	context = {'form':form, 'subcategoria': subs}
	return render(request, 'usuarios/registro.html',  context)

def userLogin(request):
	subs = Subcategoria.objects.all().order_by('nombre')
	if request.method == 'POST':
		form_auth = AuthenticationForm(request.POST)
		if form_auth.is_valid:
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username = user, password = passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					request.session['carrito'] = {}
					return redirect('/')
				else:
					return render(request, 'usuarios/errorLogin.html')
			else:
				return render(request, 'usuarios/errorLogin.html')
	else:
		form_auth = AuthenticationForm()
	context = {'form_auth': form_auth, 'subcategoria': subs}
	return render(request, 'usuarios/login.html', context)

@login_required(login_url='/usuarios/login')
def userLogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/usuarios/login')
def Configuracion(request):
	subs = Subcategoria.objects.all().order_by('nombre')
	usu = User.objects.get(username=request.user.username)
	usuario = get_object_or_404(User, pk = usu.id)
	if request.method == 'POST':
		form = editUser(request.POST, request.FILES, instance = usuario)
		if form.is_valid():
			form.save()
			return redirect('/usuarios/detalles')
	else:
		form = editUser(instance = usuario)
	context = {'form':form, 'subcategoria': subs}
	return render(request, 'usuarios/detalles.html', context)