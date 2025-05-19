from django.shortcuts import render

def index(request):
    return render(request, 'startup/index.html')

def about(request):
    return render(request, 'startup/about.html')

def blog(request):
    return render(request, 'startup/blog.html')

def contact(request):
    return render(request, 'startup/contact.html')

def detail(request):
    return render(request, 'startup/detail.html')

def feature(request):
    return render(request, 'startup/feature.html')

def price(request):
    return render(request, 'startup/price.html')

def quote(request):
    return render(request, 'startup/quote.html')

def service(request):
    return render(request, 'startup/service.html')

def team(request):
    return render(request, 'startup/team.html')

def testimonial(request):
    return render(request, 'startup/testimonial.html')
