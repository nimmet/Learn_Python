from django.urls import path
from . import views

# Register the app namespace
# URL Names

app_name = 'third_app'

urlpatterns = [
    path('',views.example_view,name='example'),
    path('form/',views.example_form, name='form'),
    path('variable/',views.variable_view,name='variable'),
]
