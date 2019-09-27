from django.shortcuts import render

from .models import TravelRecord, TravelImage
from .forms import TravelRecordForm


def map_view(request):
    success_text = ""
    form = TravelRecordForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        travel_record = form.save()
        for photo in request.FILES.getlist('photos'):
            TravelImage.objects.create(photo=photo, travel=travel_record)
        success_text = "Путешествие добавлено! :)"

    records = TravelRecord.objects.all()
    records_dict = {}
    for record in records:
        if record.place_name not in records_dict:
            records_dict[record.place_name] = []
        records_dict[record.place_name].append(record)
    context = {
        "form": form,
        "records_dict": records_dict,
        "success_text": success_text,
    }
    return render(request, "map/map.html", context)
