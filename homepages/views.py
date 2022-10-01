from django.shortcuts import render
from .models import Entry
def index(request):
    return render(request, 'homepages/index.html')
def entries(request):
    entries = Entry.objects.order_by('date_added')
    context = {'entries': entries}
    return render(request, 'homepages/entries.html', context)
