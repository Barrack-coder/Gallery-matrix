from django.shortcuts import render

# Create your views here.

def gallery(request):
        return render(request, 'matrix/gallery.html')

def viewPhotos(request,pk):
        return render(request, 'matrix/photos.html')

def addPhoto(request):
        return render(request, 'matrix/add.html')