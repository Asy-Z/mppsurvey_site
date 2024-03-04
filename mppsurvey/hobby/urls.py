from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("newmentor/", views.NewMentor, name = "newmentor"),
    path("update/<str:MentorID>", views.update, name='update'),
    path("update/updatedata/<str:MentorID>", views.updatedata, name='updatedata'),
    path("delete/<str:MentorID", views.delete, name='viewsdelete'),
    path("delete/deletedata/<str:MentorID>", views.delete, name='delete'),
    path("searchpage", views.searchpage, name = "searchpage"),
    
    
]

