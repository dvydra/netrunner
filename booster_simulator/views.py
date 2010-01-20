from django.http import HttpResponse
from models import Card
import random
from django.shortcuts import render_to_response


def booster(request):
    DISTRIBUTION = ['V','V','C','C','C','C','C','C','C','U','U','U','U','U','R']
    booster = []
    for rarity in DISTRIBUTION:
        card = Card.objects.filter(rarity=rarity).order_by('?')[:1].get()
        booster.append(card)
        print card.filename
    return render_to_response('booster.html', {'booster': booster})
    
    
    
    
