from django.urls import path
from post import views

app_name = 'post'
urlpatterns = [
    path('', views.feeds, name='home'),
    path('create-new-post/', views.create_post, name='create_post'),
]
