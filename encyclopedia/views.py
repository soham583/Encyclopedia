from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util
from markdown import markdown
from django.urls import reverse
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "text":"All pages"
    })

def pages(request, topic):
    if topic not in util.list_entries():
        return render(request, "encyclopedia/index.html")
    text= markdown(util.get_entry(topic))
    return render(request, "encyclopedia/page.html",{
        "text":text,"topic":topic
    })
def search(request):
    if request.method == "GET":
        inp = request.GET['q']
        result = []
        text = "Search Results"
        for entry in util.list_entries():
            if inp.lower() == entry.lower():
                return redirect("encyclopedia:pages", topic=entry)
            if inp.lower() in entry.lower():
                result.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": result,
            "text": text
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def editm(request,title):
    if request.method=="GET":
        text = util.get_entry(title)
        return render(request, "encyclopedia/editm.html",{
            "text": text, "new": False, "title":title
        })
    else:
        content = request.POST['mdm']
        util.save_entry(title, content.replace("\n", "") )
        return redirect("encyclopedia:pages", topic=title)

def newm(request):
    if request.method=="POST":
        title = request.POST['titl']
        content = request.POST['cont']
        for i in util.list_entries():
            if i.lower()==title.lower():
                return render(request,"encyclopedia/newm.html",{"contr":content,"errv":True})
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:index"))
    else:
        return render(request,"encyclopedia/newm.html",{"errv":False})

def ranm(request):
    lis = util.list_entries()
    l = len(lis)
    z = random.randint(0,l-1)
    entry = lis[z]
    return redirect("encyclopedia:pages", topic=entry)