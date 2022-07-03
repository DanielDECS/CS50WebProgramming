from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from markdown2 import Markdown
from random import choice

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit(request):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html")

    if request.method == "POST":
        if request.POST["action"] == "edit":
            return render(request, "encyclopedia/edit.html", {
                "name" : request.POST["name"],
                "entry" : util.get_entry(request.POST["name"])
            })

        elif request.POST["action"] == "save":
            util.save_entry(request.POST["name"], request.POST["entry"])
            url = reverse('entry', kwargs={'name': request.POST["name"]})
            return HttpResponseRedirect(url)

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        entry = util.get_entry(query)

        if entry:
            url = reverse('entry', kwargs={'name': query})
            return HttpResponseRedirect(url)

        else:
            entries = util.list_entries()
            matches = []

            for entry in entries:
                if query.upper() in entry.upper():
                    matches.append(entry)

            return render(request, "encyclopedia/search.html", {
                "entries" : matches
            })

def random(request):
    entries = util.list_entries()
    entry = choice(entries)
    url = reverse('entry', kwargs={'name': entry})
    return HttpResponseRedirect(url)

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    
    if request.method == "POST":
        if util.get_entry(request.POST["name"]):
            return render(request, "encyclopedia/error.html", {
                "message" : "It`s not possible to create a new entry for {name} because it already exists.".format(
                    name=request.POST["name"]
                )
            })
        
        util.save_entry(request.POST["name"], request.POST["entry"])
        url = reverse('entry', kwargs={'name': request.POST['name']})
        return HttpResponseRedirect(url)



def entry(request, name):
    entry = util.get_entry(name)
    if entry == None:
        return render(request, "encyclopedia/error.html", {
            "message" : "There is no entry for {name} found. You need to create one?".format(name=name)
        })

    name = util.format_entry(name)
    markdownConverter = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "name" : name,
        "entry" : markdownConverter.convert(entry)
    })





