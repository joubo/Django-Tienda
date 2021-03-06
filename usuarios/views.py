from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from forms import MyUserCreationForm, MyUserEditForm

# Create your views here.

def userRegister(request):
	if request.method == 'POST':
		form = MyUserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('/usuarios/login')
	else:
		form = MyUserCreationForm()

	context = {'form' : form}
	return render(request, "usuarios/register.html", context)

def userLogin(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					return redirect('/')
				else:
					context = {'user': user}
					return render(request,'usuarios/inactive.html', context)
			else:
				context = {'user': user}
				return render(request,'usuarios/nouser.html', context)
	else:
		form = AuthenticationForm()

	context = {'form': form}
	return render(request,'usuarios/login.html', context)

@login_required(login_url='/usuarios/login')
def userLogout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/usuarios/login')

@user_passes_test(lambda u: u.is_superuser,login_url='/')
def listaUsuarios(request):
	listaUsuarios = User.objects.all().order_by("username")
	context = { 'listaUsuarios' : listaUsuarios}
	return render(request, 'usuarios/listaUsuarios.html', context)

@login_required(login_url='/usuarios/login')
def detalleUsuario(request, usuario_id):
	usuario = User.objects.get(pk=usuario_id)
	context = {'usuario' : usuario}
	return render(request, 'usuarios/usuario.html', context)

@login_required(login_url='/usuarios/login')
def eliminarUsuario(request, usuario_id):
	usuario = User.objects.get(pk=usuario_id)
	usuario.delete()
	return redirect('/')

@login_required(login_url='/usuarios/login')
def modificarUsuario(request, usuario_id):
	usuario = User.objects.get(pk=usuario_id)
	if request.method == 'POST':
		form = MyUserEditForm(request.POST, request.FILES, instance=usuario)
		if form.is_valid:
			form.save()
			usuario=User.objects.get(pk=usuario_id)
			context = {'usuario' : usuario}
			return render(request, 'usuarios/usuario.html', context)
	else:
		form = MyUserEditForm(instance=usuario)
	context = {'form':form, 'usuario':usuario}
	return render(request, 'usuarios/modificarUsuario.html', context)

