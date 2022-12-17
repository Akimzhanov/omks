from django.urls import path
from . import views

urlpatterns = [
    path('smartphones/', views.SmartphoneListAPIView.as_view()),
    path('smartphones/create/', views.SmartphoneCreateAPIView.as_view()),
    path('smartphones/<slug:slug>/', views.SmartphoneAPIView.as_view()),
    path('smartphones/<slug:slug>/update/', views.SmartphoneUpdateAPIView.as_view()),

    path('brands/', views.BrandListAPIView.as_view()),
    path('brands/<slug:slug>', views.BrandAPIView.as_view())
]
