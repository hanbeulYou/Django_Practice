from django.shortcuts import render

# Create your views here.
def index(request):
    pass
    return render(request, 'articles/index.html')

def throw(request):
    pass
    return render(request, 'articles/throw.html')

def catch(request):
    # throw에서 받아올 메시지
    my_message = request.GET.get('message')
    context = {
        'my_message':my_message,
    }
    return render(request, 'articles/catch.html', context)

def catchword(request, name):
    context = {
        'name':name,
    }
    return render(request, 'articles/catchword.html', context)