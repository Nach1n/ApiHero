from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from hero import views

urlpatterns = [
    path('superheroe/', views.SuperHeroeList.as_view()),
    path('superheroe/<int:pk>/', views.SuperHeroeDetail.as_view()),
    path('publisher/', views.PublisherList.as_view()),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
