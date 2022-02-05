from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    if request.method == 'GET':
        content = request.GET.get('content')
        print(content)
        return HttpResponse({'content': content})
