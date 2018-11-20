from django.urls import path
from movie_rental import views


urlpatterns = [
    path('addcustomer/',views.addcustomer),
    path('addmovie/', views.addmovie),
    path('availablemovies/',views.availablemovies,name='delete'),
    path('rentedmovies/',views.rentedmovies),
    path('listcustomers/',views.listcustomers),
    path('assignmovie/',views.assignmovie),
    path('delete/<int:deleteid>',views.delete),
]