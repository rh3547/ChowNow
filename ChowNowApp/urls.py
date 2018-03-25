from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home_redirect),
	url(r'^home/$', views.home),
	url(r'^search/', views.searchList),
	url(r'^notifications/', views.notifications),
	url(r'^location/', views.location),
	url(r'^categoryitems/', views.categoryItems),
	url(r'^item/', views.item),
	url(r'^history/', views.history),
	url(r'^favorites/', views.favorites),
	url(r'^cart/', views.cart),
	url(r'^submitorder/', views.submitOrder),
	url(r'^account/', views.account),
	url(r'^login/', views.login),
	url(r'^register/', views.register)
]
