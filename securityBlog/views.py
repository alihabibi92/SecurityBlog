from django.shortcuts import render, HttpResponse


def about(request):
    # return HttpResponse("Hello World!")
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse("Hello my name is ali Trump")
    return render(request, 'contact.html')
