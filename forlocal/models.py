from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
	user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = True)
	phone = models.CharField(max_length = 100, null = True)
	email = models.CharField(max_length = 100, null = True)
	profile_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name




class Shop(models.Model):
	RATING  = (
		('5', '5'),
		('4', '4'),
		('3', '3'),
		('2', '2'),
		('1', '1')
		)

	MODE = (
		('PAYTM', 'PAYTM'),
		('CASH', 'CASH'),
		('GPAY', 'GPAY'),
		('PHONEPE', 'PHONEPE')
		)

	VER = (
		('VERIFIED', 'VERIFIED'),
		('NON VERIFIED', 'NON VERIFIED')
		)

	owner_name = models.OneToOneField(Owner, null = True, on_delete = models.SET_NULL)
	shop_name = models.CharField(max_length = 100, null = True)
	contact_email = models.CharField(max_length = 100, null = True)
	contact_num = models.CharField(max_length = 100, null = True)
	state = models.CharField(max_length = 100, null = True)
	district = models.CharField(max_length = 100, null = True)
	timming = models.CharField(max_length = 100, null = True)
	rating = models.CharField(max_length = 10, null = True, choices = RATING)
	pay_mode = models.CharField(max_length = 100, null = True, choices = MODE)
	established = models.CharField(max_length = 10, null = True)
	verificatoin = models.CharField(max_length = 100, null = True, choices = VER)
	discount = models.CharField(max_length = 100, null = True)
	offer = models.CharField(max_length = 100, null = True)
	shop_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)
	description = models.TextField(max_length = 100, null = True)

	def __str__(self):
		return self.shop_name


class Smartphone(models.Model):
	STATUS = (
		('available', 'In Stock'),
		('not available', 'Out Of Stock')
		)

	BRAND = (
		('realme', 'realme'),
		('redmi', 'redmi'),
		('samsung', 'samsung'),
		('apple', 'apple'),
		('one plus', 'one plus'),
		('motorola', 'motorola'),
		('nokia', 'nokia'),
		('honor', 'hobor'),
		('asus', 'asus'),
		('poco', 'poco'),
		('vivo', 'vivo'),
		)
	RAM = (
		('1GB', '1GB'),
		('2GB', '2GB'),
		('4GB', '4GB'),
		('6GB', '6GB'),
		('8GB', '8GB'),
		('12GB', '12GB'),
		)
	ROM = (
		('2GB', '2GB'),
		('32GB', '32GB'),
		('64GB', '64GB'),
		('128GB', '128GB'),
		('256GB', '256GB')
		)
	owner = models.ForeignKey(Owner, null = True, on_delete = models.SET_NULL)
	brand = models.CharField(max_length = 100, null = True, choices = BRAND)
	model = models.CharField(max_length = 100, null = True)
	color = models.CharField(max_length = 100, null = True)
	ram = models.CharField(max_length = 100, null = True, choices = RAM)
	rom = models.CharField(max_length = 100, null = True, choices = ROM)
	price = models.FloatField(max_length = 10, null = True)
	offer = models.CharField(max_length = 100, null = True)
	status = models.CharField(max_length = 100, null = True, choices = STATUS)
	phone_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)

	def __str__(self):
		return self.model or ''



class Laptop(models.Model):
	STATUS = (
		('available', 'In Stock'),
		('unavailable', 'Out Of Stock')
		)

	BRAND = (
		('dell', 'dell'),
		('hp', 'hp'),
		('lenovo', 'lenovo'),
		('asus', 'asus'),
		('avita', 'avita'),
		('msi', 'msi'),
		('toshiba', 'toshiba'),
		('acer', 'acer'),
		('apple', 'apple'),
		# ('poco', 'poco')
		)
	RAM = (
		('4GB', '4GB'),
		('8GB', '8GB'),
		('12GB', '12GB'),
		('16GB', '16GB'),
		('20GB', '20GB')
		)
	ROM = (
		('1 TB HDD', '1 TB HDD'),
		('2 GB HDD', '32 GB HDD'),
		('4 GB HDD', '64 GB HDD'),
		('128 GB SSD', '12 GB SSD'),
		('256 GB SSD', '256 GB SSD')
		)
	owner = models.ForeignKey(Owner, null = True, on_delete = models.SET_NULL)
	brand = models.CharField(max_length = 100, null = True, choices = BRAND)
	model = models.CharField(max_length = 100, null = True)
	os = models.CharField(max_length = 100, null = True)
	core = models.CharField(max_length = 100, null = True)
	generation = models.CharField(max_length = 100, null = True)
	ram = models.CharField(max_length = 100, null = True, choices = RAM)
	rom = models.CharField(max_length = 100, null = True, choices = ROM)
	display = models.CharField(max_length = 100, null = True)
	price = models.FloatField(max_length = 10, null = True)
	offer = models.CharField(max_length = 100, null = True)
	status = models.CharField(max_length = 100, null = True, choices = STATUS)
	laptop_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)

	def __str__(self):
		return self.brand or ''


class Sfeatures(models.Model):
	phn = models.OneToOneField(Smartphone, null = True, on_delete = models.CASCADE)
	screen_size = models.CharField(max_length = 100, null = True)
	camera = models.CharField(max_length = 100, null = True)
	battery = models.CharField(max_length = 100, null = True)
	processor = models.CharField(max_length = 100, null = True)
	display = models.CharField(max_length = 100, null = True)

	def __str__(self):
		return self.battery or ''



