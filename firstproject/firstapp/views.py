from django.shortcuts import render
from .models import Shoes


# Create your views here.

def index(request):
    shoe1 = Shoes()
    shoe1.name = 'Slippers'
    shoe1.price = 480
    shoe1.desc = 'ready to work out'
    shoe1.img = 's7.jpg'

    shoe2 = Shoes()
    shoe2.name = 'Boots'
    shoe2.price = 560
    shoe2.desc = 'Look Classy'
    shoe2.img = 's6.jpg'

    shoe3 = Shoes()
    shoe3.name = 'snikers'
    shoe3.price = 395
    shoe3.desc = 'lets go for the chill'
    shoe3.img = 's13.jpg'

    shoes = [shoe1, shoe2, shoe3]
    return render(request, 'home.html', {'shoes': shoes})