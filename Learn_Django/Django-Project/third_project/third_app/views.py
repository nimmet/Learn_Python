from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'third_app/example.html')


def example_form(request):
    return render(request, 'third_app/example_form.html')
