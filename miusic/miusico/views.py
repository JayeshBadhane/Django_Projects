from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Musician, Album

def index(request):
    # Retrieve all musicians to display in the album form dropdown
    musicians = Musician.objects.all()
    return render(request, "index.html", {'musicians': musicians})

def miusician(request):
    if request.method == 'POST':
        lname = request.POST.get('lname', '')
        fname = request.POST.get('fname', '')
        instrument = request.POST.get('instrument', '')

        if not lname or not fname or not instrument:
            messages.error(request, "All fields are required!")
            return redirect(request.META.get('HTTP_REFERER'))

        obj = Musician(first_name=fname, last_name=lname, instrument=instrument)
        obj.save()

        messages.success(request, "Musician added successfully!")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('index')

def album(request):
    if request.method == 'POST':
        artist_id = request.POST.get('artist', '')
        name = request.POST.get('name', '')
        release_date = request.POST.get('release_date', '')
        num_stars = request.POST.get('num_stars', '')

        if not artist_id or not name or not release_date or not num_stars:
            messages.error(request, "All fields are required!")
            return redirect(request.META.get('HTTP_REFERER'))

        artist = Musician.objects.get(id=artist_id)
        album = Album(artist=artist, name=name, release_date=release_date, num_stars=num_stars)
        album.save()

        messages.success(request, "Album added successfully!")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('index')
