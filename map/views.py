from django.shortcuts import render

from .models import TravelRecord
from .forms import TravelRecordForm


def map_view(request):
    success_text = ""
    form = TravelRecordForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        record = form.save(commit=False)
        # ...
        # record.save()
        success_text = "Путешествие добавлено! :)"

    context = {
        "form": form,
        "records": TravelRecord.objects.all(),
        "success_text": success_text,
    }
    return render(request, "map/map.html", context)
