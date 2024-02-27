from django.http import JsonResponse
from .ciphers import caesar_encode

# Create your views here.
def greetings(request):
    return JsonResponse({'message': 'Welcome to Ciphers service!'})

def encode(request, plainshift,shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher=caesar_encode(plainshift,shift)
    return JsonResponse({'cipher':cipher})


