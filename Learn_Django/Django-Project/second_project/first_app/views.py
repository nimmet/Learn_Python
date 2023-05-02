from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request,topic):
    return HttpResponse(articles[topic])

def add_view(request,num1,num2):
    add_result = num1+num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))


# def finance_view(request):
#     return HttpResponse(articles['finance'])

# def politics_view(request):
#     return HttpResponse(articles['politics'])

# for k,v in articles.items():
#     f = k+"_view"
    
#     def f(request):
#         return HttpResponse(v)



