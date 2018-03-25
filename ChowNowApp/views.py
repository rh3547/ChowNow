from django.shortcuts import render, redirect
from django.http import HttpResponse

"""
ChowNowApp views.py
===================

These are all of the views for ChowNow.
All functionality is contained within This
django app.
"""


def home(request):
	"""
	Display the main screen of the app that shows a search bar and
	a tiled list of dining locations.  This is where the primary
	search for food will occur.  The tiled list of dining locations
	should be built from database info by pulling a list of all locations
	in the system and returning it as context.
	"""

	title = "Home"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_home.html', context)


def home_redirect(request):
    return redirect('/home') ;


def searchList(request):
	"""
	Take in a string that represents the user's search terms
	and query the database based on those terms and display a screen that
	shows a list of results.
	"""

	title = "Search List"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_searchlist.html', context)


def notifications(request):
	"""
	Check the database to see if any outstanding notifications
	are present for this account and display a screen that shows these
	notifications.
	"""

	title = "Notifications"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_notifications.html', context)

def location(request):
	"""
	Take in a pk that represents a dining location and obtain
	all of the food categories for that location from the database.  Then a
	screen will be displayed that shows those categories.
	"""

	title = "Location Categories"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_location.html', context)


def categoryItems(request):
	"""
	Take in two pks, one representing a location and one representing
	a category for that location.  Query the database for all food items
	within that category and display a creen with the results.
	"""

	title = "Category Items"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_searchlist.html', context)


def item(request):
	"""
	Take in a pk that represents an idividual food item and
	get that item from the database.  A screen will then be displayed
	showing the details of that food item.
	"""

	title = "Food Item Details"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_fooditem.html', context)


def history(request):
	"""
	Query the database for all purchase history associated with
	the session's user and display a screen with the results.
	"""

	title = "History"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_history.html', context)

def favorites(request):
	"""
	Query the database for all saved favorites associated with
	the session's user and display a screen with the results.
	"""

	title = "Favorites"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_favorites.html', context)


def cart(request):
	"""
	Provides different functionality based on operation:

	POST:
	Add the food item with the posted pk to the session's user's cart.

	GET:
	Obtain all of the food items currently in the session's
	user's cart, calcuate the tax and the total cost, and display a screen
	with the results.
	"""

	title = "Cart/Checkout"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_cart.html', context)


def submitOrder(request):
	"""
	Used only for submitting orders via POST.  Takes in an integer that
	represents the user's PIN.  Checks if that PIN matches the PIN associated
	with the account.  If it does, the order is placed.  If it doesn't,
	display an error message to the user that the PIN was invalid.
	"""

	return HttpResponse('Post page for submitting orders, not intended to have an html page associated with it.')


def account(request):
	"""
	Gather any important account information (username, payment methods, etc.)
	from the database and display a screen with the info.
	"""

	title = "Account"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_account.html', context)


def login(request):
	"""
	POST:
	Check the posted information against user info in the database to
	authenticate and log the user in.

	GET:
	Display the login screen.
	"""

	title = "Login"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_login.html', context)

def register(request):
	"""
	POST:
	Use the posted information to create a new account in the system.

	GET:
	Display the register screen.
	"""

	title = "Register"

	context = {'title':title}
	return render(request, 'ChowNowApp/template_register.html', context)
