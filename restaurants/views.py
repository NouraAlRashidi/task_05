from django.shortcuts import render
from .models import Restaurant
#we imported the models here, basically getting all the data in class Restauraunt -

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "restaurants": Restaurant.objects.all()
    }
    return render(request, 'list.html', context)
    '''IN HTML FILE 
	<li><a href= "{% url 'restaurant-detail' restaurant.id%}"><h1>{{restaurant.name}}</h1></a></li>
	we took the name " restaurant-detail " from the urls.py, it as another way of saying the long url name.
	We are creating a new url for each object or RESTAURAUNt in the list

	Then restauraunt.id means that there is an attribute already defined called id that gives the object we have asked for

    '''



def restaurant_detail(request, restaurant_id):
	#the parameter restauruant_id has already been specified.
    context = {
        "restaurant": Restaurant.objects.get(id = restaurant_id)
    }
    return render(request, 'detail.html', context)



