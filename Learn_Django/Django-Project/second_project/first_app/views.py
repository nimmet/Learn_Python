from django.shortcuts import render
from django.http.response import HttpResponse,Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def simple_view(request):
    return render(request,'first_app/example.html') # .html file















# articles = {
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }


# def news_view(request,topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         # result = 'No page for that topic!'
#         # return HttpResponseNotFound(result)
#         raise Http404("404 Generic error")
    

# def num_page_view(request,num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]
    
#     webpage = reverse('topic-page',args=[topic])
    
#     return HttpResponseRedirect(webpage)
    
           

# def add_view(request,num1,num2):
#     add_result = num1+num2
#     result = f"{num1} + {num2} = {add_result}"
#     return HttpResponse(str(result))


# def finance_view(request):
#     return HttpResponse(articles['finance'])

# def politics_view(request):
#     return HttpResponse(articles['politics'])

# for k,v in articles.items():
#     f = k+"_view"
    
#     def f(request):
#         return HttpResponse(v)



