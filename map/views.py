from io import BytesIO
from PIL import Image

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import TravelRecord, TravelImage
from .forms import TravelRecordForm


def resize_image(image_data):
    """Helper function to resize an image"""
    img = Image.open(image_data)
    img.thumbnail([1200, 1200], Image.ANTIALIAS)
    buffer = BytesIO()
    img_format = image_data.content_type.split('/')[1]
    if img_format == 'apng':
        img_format = 'png'
    img.save(fp=buffer, format=img_format)
    img_file = ContentFile(buffer.getvalue())
    return InMemoryUploadedFile(img_file, None, image_data.name,
                                image_data.content_type, img_file.tell, None)


def map_view(request):
    form = TravelRecordForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        travel_record = form.save()
        for photo in request.FILES.getlist('photos'):
            photo = resize_image(photo)
            TravelImage.objects.create(photo=photo, travel=travel_record)
        return HttpResponseRedirect('')

    records = TravelRecord.objects.all().order_by('start_date')
    records_dict = {}
    for record in records:
        if record.place_name not in records_dict:
            records_dict[record.place_name] = []
        records_dict[record.place_name].append(record)
    context = {
        "form": form,
        "records_dict": records_dict,
        "records": records,
    }
    return render(request, "map/map.html", context)
