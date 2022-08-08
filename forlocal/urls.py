from django.urls import path
from .import views

urlpatterns = [
	
	path('', views.home, name = 'Home'),
	path('homein/', views.homein, name = 'Homein'),
	path('signup/', views.signup, name = 'Signup'),
	path('signin/', views.signin, name = 'Login'),
	path('logout/', views.logoutpage, name = 'Logout'),
	path('shophome/', views.shopHome, name = 'Shophome'),
	path('dashboard/', views.dashboard, name = 'Dashboard'),
	# path('dashboard/<int:pk>/', views.dashboard, name = 'Dashboard'),
	path('addphone/<int:pk>/', views.createPhone, name = 'Addphone'),
	path('updatephone/<int:pk>/', views.updatePhone, name = 'Updatephone'),
	path('deletephone/<int:pk>/', views.deletePhone, name = 'Deletephone'),
	path('profile/', views.profile, name = 'Profile'),
	path('profilesetting/', views.profileSetting, name = 'Profilesetting'),
	path('shopprofile/', views.shopProfile, name = 'Shopprofile'),
	path('shopprofilesetting/', views.shopProfileSetting, name = 'Shopprofilesetting'),
	path('phoneshopdetails/<int:pk>/', views.phoneShopDetails, name = 'Phoneshopdetails'),
	path('phoneshopdetails2/<int:pk>/', views.phoneShopDetails2, name = 'Phoneshopdetails2'),
	path('select/', views.select, name = 'Select'),
	path('laptopdetails/<int:pk>/', views.laptopDetails, name = 'Laptopdetails'),
	path('laptopshopdetails2/<int:pk>/', views.laptopShopDetails2, name = 'Laptopshopdetails2'),
	path('addlaptop/<int:pk>/', views.createLaptop, name = 'Addlaptop'),
	path('updatelaptop/<int:pk>/', views.updateLaptop, name = 'Updatelaptop'),
	path('deletelaptop/<int:pk>/', views.deleteLaptop, name = 'Deletelaptop'),
	path('addfeatures/<int:pk>/', views.createFeatures, name = 'Addfeatures'),

]