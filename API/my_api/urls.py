from django.urls import path, include
from . import views

urlpatterns = [
    path('heroes/', views.heroes.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]