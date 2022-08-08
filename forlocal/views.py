from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory  
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import *
from .forms import PhoneForm, CreateUserForm, OwnerForm, ShopForm, LaptopForm, FeaturesForm
from .filters import PhoneFilter, HomePhoneFilter, HomeLaptopFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.db.models import Q

# Create your views here.

def home(request):
	# phone = Smartphone.objects.all()
	owner = Owner.objects.all()

	search_phone = request.GET.get('search')

	if search_phone:
		phone =Smartphone.objects.filter(Q(model = search_phone) | Q(brand = search_phone))
		laptop =Laptop.objects.filter(Q(model = search_phone) | Q(brand = search_phone))
	else:
		phone = Smartphone.objects.all()
		laptop = Laptop.objects.all()


	context = {'phone': phone, 'owner': owner, 'laptop': laptop}
	return render(request, 'home2.html', context)

@unauthenticated_user
def homein(request):
	
	return render(request, 'home.html', context)

@unauthenticated_user
def signup(request):
	form =  CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			username = form.cleaned_data.get('username')
			group = Group.objects.get(name = 'owner')
			user.groups.add(group)
			Owner.objects.create(
				user=user,
				)

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Login')

	context = {'form': form}
	return render(request, 'signup2.html', context)
	
@unauthenticated_user
def signin(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')

    	user = authenticate(request, username = username, password = password)
    	if user is not None:
    		login(request, user) 
    		return redirect('Shophome')
    	else:
    		messages.info(request, 'Username or Password is incorrect ')
    context = {}
    return render(request, 'login2.html', context)
 
def logoutpage(request):
	logout(request)
	return redirect('Home')


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner', 'admin'])
def shopHome(request):
	phone = Smartphone.objects.all()
	laptop = Laptop.objects.all()
	
	context = {'phone': phone, 'laptop': laptop}
	return render(request, 'shop_home.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def dashboard(request):
	owner  = request.user.owner
	products = owner.smartphone_set.all()
	laptop = owner.laptop_set.all()

	total_order = products.count()
	total_order2 = laptop.count()
	# total = orders.filter(status = 'delivered').count()
	available = products.filter(status = 'available').count()
	available2 = laptop.filter(status = 'available').count()


	myFilter = PhoneFilter(request.GET, queryset = products)
	products = myFilter.qs

	context = {'products': products, 'laptop': laptop, 'owner': owner, 'total_order': total_order, 'total_order2': total_order2, 'available': available, 'available2': available2, 'myfilter': myFilter}
	return render(request, 'dashboard.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def profile(request):
	owner = request.user.owner

	context = {'owner': owner}
	return render(request, 'profile2.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def profileSetting(request):
	owner = request.user.owner
	form = OwnerForm(instance = owner)

	if request.method == 'POST':
		form = OwnerForm(request.POST, request.FILES, instance = owner)
		if form.is_valid():
			form.save()
			return redirect('Profile')

	context = {'form': form}
	return render(request, 'profile_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def shopProfile(request):
	owner = request.user.owner

	context = {'owner': owner}
	return render(request, 'shop_profile2.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def shopProfileSetting(request):
	owner = request.user.owner
	form = ShopForm(instance = owner.shop)
	if request.method == 'POST':
		form = ShopForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.owner_name = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Shopprofile')

	context = {'form': form}
	return render(request, 'shop_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def createPhone(request, pk):
	owne = Owner.objects.get(id = pk)
	form = PhoneForm()

	if request.method == 'POST':

		form = PhoneForm(request.POST, request.FILES)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			form.owner = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Dashboard')

	context = {'form': form}
	return render(request, 'phone_form.html', context)



@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def updatePhone(request, pk):

	phone = Smartphone.objects.get(id = pk)
	form = PhoneForm(instance = phone)

	if request.method == 'POST':
		form = PhoneForm(request.POST, request.FILES, instance = phone)
		if form.is_valid():
			form.save()
			return redirect('Dashboard')

	context = {'form': form}

	return render(request, 'phone_form.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def deletePhone(request, pk):

	phone = Smartphone.objects.get(id = pk)
	if request.method == 'POST':
		phone.delete()
		return redirect('Dashboard')

	context = {'item': phone}
	return render(request, 'delete.html', context)


def phoneShopDetails(request, pk):
	phone = Smartphone.objects.get(id=pk)
	context = {'phone': phone}
	# return render(request, 'phone_shop_view2.html', context)
	return render(request, 'phone_shop_view2.html', context)

def laptopDetails(request, pk):
	laptop = Laptop.objects.get(id=pk)
	context = {'laptop': laptop}
	# return render(request, 'phone_shop_view2.html', context)
	return render(request, 'laptopdetails.html', context)

def phoneShopDetails2(request, pk):
	phone = Smartphone.objects.get(id=pk)
	context = {'phone': phone}
	# return render(request, 'phone_shop_view2.html', context)
	return render(request, 'shop_details2.html', context)

def laptopShopDetails2(request, pk):
	laptop = Laptop.objects.get(id=pk)
	context = {'phone': laptop}
	# return render(request, 'phone_shop_view2.html', context)
	return render(request, 'shop_details2.html', context)

	
def select(request):
	context = {}
	return render(request, 'select_page.html', context)



@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def createLaptop(request, pk):
	owne = Owner.objects.get(id = pk)
	form = LaptopForm()

	if request.method == 'POST':

		form = LaptopForm(request.POST, request.FILES)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			form.owner = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Dashboard')

	context = {'form': form}
	return render(request, 'laptop_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def updateLaptop(request, pk):

	laptop = Laptop.objects.get(id = pk)
	form = LaptopForm(instance = laptop)

	if request.method == 'POST':
		form = LaptopForm(request.POST, request.FILES, instance = laptop)
		if form.is_valid():
			form.save()
			return redirect('Dashboard')

	context = {'form': form}

	return render(request, 'laptop_form.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def deleteLaptop(request, pk):

	laptop = Laptop.objects.get(id = pk)
	if request.method == 'POST':
		laptop.delete()
		return redirect('Dashboard')

	context = {'item': laptop}
	return render(request, 'deletelaptop.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def createFeatures(request, pk):
	owne = Owner.objects.get(id = pk)
	form = FeaturesForm()

	if request.method == 'POST':

		form = FeaturesForm(request.POST, request.FILES)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			form.owner = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Dashboard')

	context = {'form': form}
	return render(request, 'features_form.html', context)
