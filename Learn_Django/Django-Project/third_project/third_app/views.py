from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'third_app/example.html')


def example_form(request):
    return render(request, 'third_app/example_form.html')


def variable_view(request):
    
    my_var = {
    'first_name': 'Uyghur','last_name': 'Lopnur', 
    'some_list': [1,2,3], 'some_dict': {'city':'Korla'},
    'user_logged_in': True  
    }
    
    return render(request, 'third_app/variable.html',context=my_var)
