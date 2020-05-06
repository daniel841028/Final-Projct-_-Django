from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
        #'kk': 7,
        #jjj': 'hhhhh'
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
def rider(request):
    
    context = {
        'kk': 7,
        'jjj': 'hhhhh'
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'rider.html', context=context)

def provider(request):
    
    context = {
        'kk': 7,
        'jjj': 'hhhhh'
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'provider.html', context=context)

def home(request):
	return render(request, "home.html", {})