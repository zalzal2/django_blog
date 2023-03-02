from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    #path('', views.index),
    #path('<int:pk>/', views.single_post_page), 
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page, name="category"),
]
   
    