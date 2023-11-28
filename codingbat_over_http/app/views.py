from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.forms import FrontForm, TeenForm, XYZForm, AvgForm
# Create your views here.

def front_view(request:HttpRequest) -> HttpResponse:
    form = FrontForm(request.GET)
    if form.is_valid():
        input_text = form.cleaned_data["input_text"]
        num_r = form.cleaned_data["num_r"]
        work = ""
        for i in range(0,num_r,1):
            work = work + input_text[0:3]
        return render(request, "front.html", {"form":form, "work": work})
    else:
        return render(request, "front.html", {"form":form})

def teen_view(request:HttpRequest) -> HttpResponse:
    form = TeenForm(request.GET)
    def fix_teen(n):
        return 0 if n not in (15, 16) and 13 <= n <= 19 else n
    if form.is_valid():
        n1 = int(form.cleaned_data["n1"])
        n2 = int(form.cleaned_data["n2"])
        n3 = int(form.cleaned_data["n3"])
        nums = (n1, n2, n3)
        work = sum(fix_teen(n) for n in nums)
        return render(request, "teen.html", {"form":form, "work": work})
    else:
        return render(request, "teen.html", {"form":form})
    
def xyz_view(request:HttpRequest) -> HttpResponse:
    form = XYZForm(request.GET)
    if form.is_valid():
        bool = "False"
        str = form.cleaned_data["str"]
        if str[:3] == "xyz":
            bool = "True"
                    
        for i in range(1, len(str) - 2):
            if str[i-1] != "." and str[i:i+3] == "xyz":
                bool =  "True"
    
        return render(request, "xyz.html", {"form":form, "work":bool})
    else:
        return render(request, "xyz.html", {"form":form})
    
def avg_view(request:HttpRequest) -> HttpResponse:
    form = AvgForm(request.GET)
    if form.is_valid():
        n1 = form.cleaned_data["n1"]
        n2 = form.cleaned_data["n2"]
        n3 = form.cleaned_data["n3"]
        n4 = form.cleaned_data["n4"]
        n5 = form.cleaned_data["n5"]
        nums = [n1, n2, n3, n4, n5]
        small = min(nums)
        big = max(nums)
        work = (sum(nums) - small - big) / (len(nums) - 2)
        return render(request, "avg.html", {"form":form, "work":work})
    else:
        return render(request, "avg.html", {"form":form})