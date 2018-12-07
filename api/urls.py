from django.urls import path, include
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('saveMap/', views.saveMap),
    path('shorterDistance/', views.shorterDistance),
]
