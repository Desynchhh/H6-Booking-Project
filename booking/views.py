from django.shortcuts import render

# Create your views here.

def temp_home(request):
    return render(request, 'booking/temp_home.html', context={"my_name": "Mikkel Larsen"})
