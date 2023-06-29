from django.shortcuts import render
from .models import club

def home(request):
    clubs = club.objects.all()
    return render(request, "home.html", {'clubs': clubs})

def create(request):
    if request.method == 'POST':
        club = club()
        club.name = request.POST['name']
        club.intro = request.POST['intro']
        club.head = request.POST['head']
        club.save()
        return redirect('detail', club.id)
    return render(request, 'create.html')


# Create your views here.
