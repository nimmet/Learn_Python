from django.urls import path
from . import views

urlpatterns = [
    path('',views.example_view),
    path('form/',views.example_form),
    path('variable/',views.variable_view)
]
