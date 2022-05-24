from django.urls import path
from heritagesites.views import HomePageView

urlpatterns = [
    path('index/', HomePageView.as_view(), name = 'home'),
]
