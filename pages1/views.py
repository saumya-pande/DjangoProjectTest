from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def contact_page(*args, **kwargs):
    return HttpResponse("Hello, world. You're at the contact page.")
