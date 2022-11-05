from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    prog_lang = request.GET.get('prog_lang')
    query_set = []
    if city or prog_lang:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if prog_lang:
            _filter['prog_lang__slug'] = prog_lang
        query_set = Vacancy.objects.filter(**_filter)
    return render(request, "scraping/home.html", {"object_list": query_set, "form": form})
