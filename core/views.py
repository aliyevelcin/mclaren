from django.shortcuts import render
from core.models import *
# Create your views here.
def main(request):

    posts = MPost.objects.order_by('-id')[:2]
    newss = MNews.objects.order_by('-id')[:3]
    partners = Partner.objects.order_by('-id')
    context = {
        'posts': posts,
        'newss': newss,
        'partners': partners
    }
    return render(request, 'main.html', context)

def artickles(request):

    cards = ACards.objects.order_by('-id')
    partners = Partner.objects.order_by('-id')
    contex = {
        'cards': cards,
        'partners': partners
    }
    return render(request, 'artickles.html', contex)    

def sheldue(request):
    
    events = Events.objects.order_by('-id')[:3]
    races = Races.objects.order_by('-id')[:12]
    partners = Partner.objects.order_by('-id')[:1]

    contex = {
        
        'events': events,
        'races': races,
        'partners': partners
        
        }
    return render(request, 'sheldue.html', contex)

def academy(request):
    return render(request, 'academy.html')    