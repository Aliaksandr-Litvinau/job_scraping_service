from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    query_set = Vacancy.objects.all()
    return render(request, "scraping/home.html", {"object_list": query_set})

# def home(request):
#     date = datetime.now().date()
#     name = 'Dave'
#     _context = {'date': date, 'name': name}
#     return render(request, 'home.html', _context)
