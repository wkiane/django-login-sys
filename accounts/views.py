from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    creators = ['Willa Kiane', 'Max Goodridge']
    title = 'Social Network'

    data = {
        'title' : title,
        'creators' : creators,
    }
    return render(request, 'accounts/home.html', data)
