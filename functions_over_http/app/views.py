from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.forms import HeyYouForm, HowOldForm, OrderForm
# Create your views here.


def hey_view(request: HttpRequest) -> HttpResponse:
    form = HeyYouForm(request.GET)
    if form.is_valid():
        input = form.cleaned_data["input_name"]
        return render(request, "hey_you.html", {"input": input})
    else:
        return render(request, "hey_you.html")


def old_view(request: HttpRequest) -> HttpResponse:
    form = HowOldForm(request.GET)
    if form.is_valid():
        this_year = int(form.cleaned_data["this_year"])
        birth_year = int(form.cleaned_data["birth_year"])
        age = this_year - birth_year
        return render(request, "how_old.html", {"age": age})
    else:
        return render(request, "how_old.html")


def order_view(request: HttpRequest) -> HttpResponse:
    form = OrderForm(request.GET)
    if form.is_valid():
        burgers = int(form.cleaned_data["burgers"])
        fries = int(form.cleaned_data["fries"])
        drinks = int(form.cleaned_data["drinks"])
        total = (burgers * 4.5) + (fries * 1.5) + (drinks)
        return render(request, "order.html", {"total": total})
    else:
        return render(request, "order.html")
