from .views import familia
from django.urls import path

urlpatterns = [
    path('familia', familia),
]