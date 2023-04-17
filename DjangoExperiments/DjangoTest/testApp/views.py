from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Net, User
 
# получение данных из бд
def index(request):
    return render(request, "index.html")
def users(request):
    people = User.objects.all()
    return render(request, "users.html", {"users": people})
def nets(request):
    people = Net.objects.all()
    return render(request, "nets.html", {"nets": people})
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = User()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = User.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = User.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")