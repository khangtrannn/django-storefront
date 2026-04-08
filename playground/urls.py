from playground import views
from django.urls import include, path


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('celery', views.celery)
]
