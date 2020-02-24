from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    
    return render(request, 'new.html')


def new_show(request):
    return redirect(f"/shows/new.html/{show.id}")


def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], desc = request.POST["desc"])
        messages.success(request, "Show added.")
    return redirect(f"/shows/{new_show.id}")

def shows(request):
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request, 'index.html',context)

def information(request, show_id):
    new_show = Show.objects.get(id=show_id)
    context ={
        'show': new_show
    }
    return render(request, "read.html", context)


def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show': show
    }

    return render(request, "edit.html", context)



def update(request, show_id):
    this_show = Show.objects.get(id=show_id)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    else:
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.desc = request.POST['desc']
        messages.success(request, "Show Updated.")
    this_show.save()
    return redirect(f"/shows/{show_id}")


def destroy(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except:
        return redirect('/')
    show.delete()
    return redirect('/')