from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
def index_view(request):
    return render(request, 'index-one-page.html')
