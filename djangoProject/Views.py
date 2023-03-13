from django.shortcuts import render




def Homepage(request):
    return render(request, 'Home.html')


def Aboutpage(request):
    return render(request, 'About.html')

def Blogpage(request):
    return render(request, 'Blog.html')

def Contactpage(request):
    return render(request, 'Contact.html')


def Productpage(request):
    return render(request, 'Product.html')

def Servicepage(request):
    return render(request, 'Services.html')

