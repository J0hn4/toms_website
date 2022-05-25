from django.shortcuts import render
from .models import Announcement

# Create your views here.
def home(request):
    all_announcements = Announcement.objects.all()
    return render(request, 'announcements/home.html', {'announcements':all_announcements})


def index(request):
    all_announcements = Announcement.objects.all()
    return render(request, 'announcements/index.html', {'announcements':all_announcements})

