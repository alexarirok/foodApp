from django.shortcuts import render

def home(request):
    template = 'vendor/index.html'
    return render(request, template, { })

def base(request):
    template='vendor/base.html'
    return render(request, template, { })

