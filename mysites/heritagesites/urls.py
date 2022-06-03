from django.urls import path
from heritagesites.views import HomePageView, subcounty_datasets, historicalsite_points 

urlpatterns = [
    path('index/', HomePageView.as_view(), name = 'home'),
    path('subcounty_data/', subcounty_datasets, name = 'subcounty'),
    path('historicalsite_data/', historicalsite_points, name = 'historicalsite'),
]
