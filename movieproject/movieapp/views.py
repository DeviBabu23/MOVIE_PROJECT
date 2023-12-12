from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list': movie
    }

    return render(request,'index.html',context)
def details(request,movie_id):
    obj=Movie.objects.get(id=movie_id)
    return render(request,"details.html", {'movie':obj})

def add_movie(request):
    if request.method=='POST':
        name= request.POST.get('name',)
        des = request.POST.get('des',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,des=des,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')