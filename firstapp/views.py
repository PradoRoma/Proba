from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseGone, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseNotModified, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm
from firstapp import forms

#def  index(request):
#        return render(request, "firstapp/home.html")


def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            progname = userform.cleaned_data["header"]
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            email = userform.cleaned_data["email"]
            weight = userform.cleaned_data["weight"]
            comment = userform.cleaned_data["comment"]
            #comment = request.POST.get("comment")
            return HttpResponse(f"<h2> <p>Тема: {progname}</p> <p>Ваше имя: {name}</p> <p>Ваш возраст: {age}</p>  <p>Масса вашего тела: {weight}</p> <p>Ваша почта: {email}</p> <p>Твой комментарий: {comment}</p> </h2>")
        #else:
        #    return HttpResponse("Invalid data")
    return render(request, "index.html", {"form":userform})
    #else:
    #    userform = UserForm()
    #    header = "Personal Data"  # обычная переменная
    #    langs = ["English", "German", "French", "Spanish", "Chinese"]    # массиd
    #    user ={"name" : "Tom", "age" : 23}          # словарь
    #    addr = ("Абрикосовая", 23, 45)              # кортеж
    #
    #    data = {"header": header, "langs": langs, "user": user, "address": addr, "n":5}
    #
    #    return render(request, "index.html", {"form":userform})
        #return render(request, "index.html", context=data)
        #return TemplateResponse(request,  "index.html", data)

def about(request):
    return HttpResponse('<h2>О Сайте</h2>')

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect("/")

#def product(request, productid = 21):
#    output = f"<h2>Product № {productid}</h2>"
#    return HttpResponse(output)

#def users(request, id = 21, name = "Roma"):
#    output = f"<h2>User</h2><h3>id: {id} name: {name}</h3>"
#    return HttpResponse(output)

def products(request, productid):
    category = request.GET.get("cat", " ")
    output = f"<h2>Product № {productid} Category: {category}</h2>"
    return HttpResponse(output)

def users(request):
    id = request.GET.get('id', 21)
    name = request.GET.get('name', 'Roma')
    output = f"<h2>User</h2><h3>id: {id}, name: {name}</h3>"
    return HttpResponse(output)

def m304(request):
    return HttpResponseNotModified()

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2> Content is not longer here</h2>")

def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")


# Create your views here.
