from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuList.as_view()),
    path('menu/<int:pk>/', views.MenuDetail.as_view()),
    path('booking/', views.BookingList.as_view()),
    path('booking/<int:pk>/', views.BookingDetail.as_view()),
]