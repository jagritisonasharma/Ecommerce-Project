from django.shortcuts import render

# Create your views here.


def HelloDjango(request):
    name = "Sona"
    last_name = "Sharma"
    context = {
        'first_name': name,
        'last_name': last_name
    }

    return render(request, 'products/hello-django.html', context)
