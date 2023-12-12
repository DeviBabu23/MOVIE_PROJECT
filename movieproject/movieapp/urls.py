
from django.urls import path

from movieapp import views
app_name='movieapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
     path('delete/<int:movie_id>/',views.delete,name='delete'),
    path('update/<int:movie_id>/', views.update, name='update')

]