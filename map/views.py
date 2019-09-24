from django.shortcuts import render

from .models import TravelRecord


def map_view(request):
    records = TravelRecord.objects.all()
    context = {
        "records": records,
    }
    return render(request, "map/map.html", context)
